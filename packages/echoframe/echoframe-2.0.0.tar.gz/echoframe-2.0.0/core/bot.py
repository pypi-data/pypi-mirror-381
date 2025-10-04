"""机器人核心类"""

from typing import Dict, Any, List, Optional
import asyncio
from loguru import logger

from .event import Event, parse_event, MessageEvent
from .plugin import PluginManager, get_plugin_manager
from .heartbeat import HeartbeatManager
from .middleware import MiddlewareManager


class Bot:
    """OneBot 机器人核心类"""
    
    def __init__(self, config: Dict[str, Any]):
        """
        初始化机器人
        
        Args:
            config: 配置字典
        """
        self.config = config
        self.bot_config = config.get("bot", {})
        
        # WebSocket API 适配器（用于调用 API）
        self._ws_api_adapter = None  # 通过 WebSocket 调用 API（双向通信）
        
        # 插件管理器
        self.plugin_manager: PluginManager = get_plugin_manager()
        
        # 运行状态
        self.is_running = False
        self._tasks: List[asyncio.Task] = []
        
        # 适配器
        self.adapters: List[Any] = []
        
        # 机器人信息
        self.self_id: Optional[int] = None
        self.nickname: Optional[str] = None
        
        # 心跳管理器
        heartbeat_config = config.get("heartbeat", {"enable": False})
        self.heartbeat = HeartbeatManager(self, heartbeat_config)
        
        # 中间件管理器
        self.middleware = MiddlewareManager()
    
    async def start(self):
        """启动机器人"""
        if self.is_running:
            logger.warning("机器人已在运行中")
            return
        
        logger.info("正在启动机器人...")
        self.is_running = True
        
        # 加载插件
        await self._load_plugins()
        
        # 启动适配器
        await self._start_adapters()
        
        # 等待 WebSocket 连接（给一点时间建立连接）
        await asyncio.sleep(0.5)
        
        # 获取登录信息（此时 WebSocket 已连接）
        await self._get_login_info()
        
        # 启动心跳
        await self.heartbeat.start()
        
        logger.success("机器人启动完成")
    
    async def stop(self):
        """停止机器人"""
        if not self.is_running:
            return
        
        logger.info("正在停止机器人...")
        self.is_running = False
        
        # 停止心跳
        await self.heartbeat.stop()
        
        # 停止所有任务
        for task in self._tasks:
            task.cancel()
        await asyncio.gather(*self._tasks, return_exceptions=True)
        self._tasks.clear()
        
        # 停止适配器
        for adapter in self.adapters:
            try:
                await adapter.stop()
            except Exception as e:
                logger.error(f"停止适配器失败: {e}")
        
        # 清理插件
        await self.plugin_manager.cleanup_plugins()
        
        logger.success("机器人已停止")
    
    async def _load_plugins(self):
        """加载插件"""
        plugin_config = self.config.get("plugins", {})
        plugin_dirs = plugin_config.get("plugin_dirs", ["plugins"])
        enabled_plugins = plugin_config.get("enabled_plugins", [])
        disabled_plugins = plugin_config.get("disabled_plugins", [])
        
        total = 0
        for plugin_dir in plugin_dirs:
            count = self.plugin_manager.load_plugins_from_dir(
                plugin_dir,
                enabled_plugins if enabled_plugins else None,
                disabled_plugins
            )
            total += count
        
        logger.info(f"共加载 {total} 个插件")
        
        # 初始化插件
        await self.plugin_manager.initialize_plugins()
    
    async def _get_login_info(self):
        """获取登录信息"""
        try:
            # 通过 WebSocket API 获取
            if self._ws_api_adapter:
                logger.info("通过 WebSocket API 获取登录信息...")
                info = await self._ws_api_adapter.call_api("get_login_info")
                
                if info and isinstance(info, dict) and info.get("user_id"):
                    self.self_id = info.get("user_id")
                    self.nickname = info.get("nickname")
                    logger.success(f"✅ 登录账号: {self.nickname} ({self.self_id})")
                else:
                    logger.info("未能通过 API 获取登录信息，将从第一条消息中自动获取")
            else:
                logger.info("WebSocket API 未就绪，将从第一条消息中自动获取登录信息")
        except Exception as e:
            logger.warning(f"获取登录信息失败（不影响使用）: {e}")
    
    async def _start_adapters(self):
        """启动适配器（支持正向和反向 WebSocket）"""
        adapter_config = self.config.get("adapters", {})
        
        # 方式 1：使用 aiocqhttp（反向 WebSocket - EchoFrame 作为服务端）
        if adapter_config.get("aiocqhttp", {}).get("enabled", False):
            from adapters.aiocqhttp_adapter import AioCQHTTPAdapter
            
            aiocqhttp_config = adapter_config.get("aiocqhttp", {})
            aiocqhttp_adapter = AioCQHTTPAdapter(self, aiocqhttp_config)
            self.adapters.append(aiocqhttp_adapter)
            
            # 设置为 API 调用适配器
            if not self._ws_api_adapter:
                self._ws_api_adapter = aiocqhttp_adapter
                logger.info("✅ 使用 AioCQHTTP（反向 WebSocket：EchoFrame 作为服务端）")
            
            # 启动服务器
            host = aiocqhttp_config.get("host", "0.0.0.0")
            port = aiocqhttp_config.get("port", 8080)
            
            task = asyncio.create_task(aiocqhttp_adapter.start(host, port))
            self._tasks.append(task)
        
        # 方式 2：使用正向 WebSocket 客户端（EchoFrame 作为客户端）
        if adapter_config.get("websocket_client", {}).get("enabled", False):
            from adapters.ws_client import WebSocketClientAdapter
            
            ws_client_config = adapter_config.get("websocket_client", {})
            ws_client_adapter = WebSocketClientAdapter(self, ws_client_config)
            self.adapters.append(ws_client_adapter)
            
            # 设置为 API 调用适配器（优先级高于 aiocqhttp）
            self._ws_api_adapter = ws_client_adapter
            logger.info("✅ 使用正向 WebSocket 客户端（EchoFrame 连接到 OneBot 实现）")
            
            task = asyncio.create_task(ws_client_adapter.start())
            self._tasks.append(task)
        
        if not self.adapters:
            logger.error("❌ 未启用任何适配器！")
            raise RuntimeError("No adapters enabled")
    
    async def handle_event(self, event_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        处理事件（优化版：快速处理，支持快速操作）
        
        Args:
            event_data: 事件数据
            
        Returns:
            快速操作响应（如果有）
        """
        try:
            # 解析事件
            event = parse_event(event_data)
            
            # 如果还没有 self_id，从第一条消息中获取
            if self.self_id is None and hasattr(event, 'self_id'):
                self.self_id = event.self_id
                logger.info(f"✅ 从事件中获取到机器人 QQ: {self.self_id}")
            
            # 只打印重要日志（消息事件）
            if isinstance(event, MessageEvent):
                msg_type = "群聊" if event.is_group() else "私聊"
                sender_name = event.sender.get("nickname", "未知")
                group_info = f"[{event.group_id}]" if event.is_group() else ""
                msg_preview = event.get_message_text()[:50]  # 只显示前50个字符
                logger.info(f"📨 {msg_type}{group_info} {sender_name}: {msg_preview}")
            # 其他事件只在 DEBUG 级别记录
            elif logger.level("DEBUG").no <= logger._core.min_level:
                logger.debug(f"收到事件: {event.post_type}")
            
            # 通过中间件处理事件
            if self.middleware.middlewares:
                # 使用中间件链处理
                await self.middleware.process(
                    self, 
                    event, 
                    lambda bot, evt: self.plugin_manager.handle_event(bot, evt)
                )
            else:
                # 直接处理（无中间件）
                await self.plugin_manager.handle_event(self, event)
            
            # 检查是否有快速操作响应
            quick_operation = self._build_quick_operation(event)
            return quick_operation if quick_operation else None
            
        except Exception as e:
            logger.exception(f"处理事件时发生错误: {e}")
            return None
    
    def _build_quick_operation(self, event: Event) -> Optional[Dict[str, Any]]:
        """
        构建快速操作响应
        
        Args:
            event: 事件对象
            
        Returns:
            快速操作字典
        """
        from .event import MessageEvent, RequestEvent
        
        quick_op = {}
        
        # 消息事件的快速操作
        if isinstance(event, MessageEvent):
            if event.reply is not None:
                quick_op["reply"] = event.reply
            if event.auto_escape is not None:
                quick_op["auto_escape"] = event.auto_escape
            if event.at_sender is not None:
                quick_op["at_sender"] = event.at_sender
            if event.delete is not None:
                quick_op["delete"] = event.delete
            if event.kick is not None:
                quick_op["kick"] = event.kick
            if event.ban is not None:
                quick_op["ban"] = event.ban
            if event.ban_duration is not None:
                quick_op["ban_duration"] = event.ban_duration
        
        # 请求事件的快速操作
        elif isinstance(event, RequestEvent):
            if event.approve is not None:
                quick_op["approve"] = event.approve
            if event.remark is not None:
                quick_op["remark"] = event.remark
            if event.reason is not None:
                quick_op["reason"] = event.reason
        
        return quick_op if quick_op else None
    
    async def send_private_msg(self, user_id: int, message: Any) -> Dict[str, Any]:
        """发送私聊消息（便捷方法）"""
        if self._ws_api_adapter:
            result = await self._ws_api_adapter.send_private_msg(user_id, message)
            return result if result else {}
        else:
            logger.error("❌ 没有可用的 API 调用方式")
            return {}
    
    async def send_group_msg(self, group_id: int, message: Any) -> Dict[str, Any]:
        """发送群消息（便捷方法）"""
        if self._ws_api_adapter:
            result = await self._ws_api_adapter.send_group_msg(group_id, message)
            return result if result else {}
        else:
            logger.error("❌ 没有可用的 API 调用方式")
            return {}
    
    async def call_api(self, action: str, **params) -> Any:
        """
        调用 OneBot API（便捷方法）
        
        Args:
            action: API 动作名
            **params: API 参数
            
        Returns:
            API 响应
        """
        if self._ws_api_adapter:
            return await self._ws_api_adapter.call_api(action, **params)
        else:
            logger.error("❌ 没有可用的 API 调用方式")
            return None
    
    async def send(self, event: Any, message: Any) -> Dict[str, Any]:
        """
        根据事件自动发送消息（便捷方法）
        
        Args:
            event: 消息事件（MessageEvent 或事件字典）
            message: 要发送的消息
        """
        # 如果是 MessageEvent 对象
        if hasattr(event, 'is_group'):
            if event.is_group():
                return await self.send_group_msg(event.group_id, message)
            else:
                return await self.send_private_msg(event.user_id, message)
        
        # 如果是字典，通过 aiocqhttp 的 send 方法
        if self._ws_api_adapter and isinstance(event, dict):
            return await self._ws_api_adapter.send(event, message)
        
        logger.error("❌ 无法发送消息：事件类型不正确")
        return {}
    
    def is_superuser(self, user_id: int) -> bool:
        """检查是否为超级用户"""
        superusers = self.bot_config.get("superusers", [])
        return user_id in superusers


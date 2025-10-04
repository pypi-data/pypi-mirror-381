"""
AioCQHTTP 适配器

使用 aiocqhttp 库处理底层通信和 API 调用
大幅简化代码，同时保留 EchoFrame 的高级功能
"""

from typing import Dict, Any, Optional
from aiocqhttp import CQHttp, Event as CQEvent, Message as CQMessage
from loguru import logger


class AioCQHTTPAdapter:
    """AioCQHTTP 适配器"""
    
    def __init__(self, bot: 'Bot', config: Dict[str, Any]):
        """
        初始化适配器
        
        Args:
            bot: EchoFrame Bot 实例
            config: aiocqhttp 配置
        """
        self.bot = bot
        self.config = config
        
        # 创建 CQHttp 实例
        self.cqhttp = CQHttp(
            api_root=config.get("api_root"),  # OneBot HTTP API 地址
            access_token=config.get("access_token", ""),
            secret=config.get("secret"),
            message_class=CQMessage  # 使用 aiocqhttp 的 Message 类
        )
        
        # 注册事件处理器
        self._register_handlers()
        
        logger.info("✅ AioCQHTTP 适配器初始化完成")
    
    def _register_handlers(self):
        """注册 aiocqhttp 事件处理器"""
        
        # 消息事件
        @self.cqhttp.on_message
        async def handle_message(event: CQEvent):
            """处理消息事件"""
            logger.debug(f"📨 收到消息事件: {event.message_type}")
            await self.bot.handle_event(dict(event))
        
        # 通知事件
        @self.cqhttp.on_notice
        async def handle_notice(event: CQEvent):
            """处理通知事件"""
            logger.debug(f"📥 收到通知事件: {event.notice_type}")
            await self.bot.handle_event(dict(event))
        
        # 请求事件
        @self.cqhttp.on_request
        async def handle_request(event: CQEvent):
            """处理请求事件"""
            logger.debug(f"📮 收到请求事件: {event.request_type}")
            await self.bot.handle_event(dict(event))
        
        # 元事件
        @self.cqhttp.on_meta_event
        async def handle_meta(event: CQEvent):
            """处理元事件"""
            logger.debug(f"📡 收到元事件: {event.meta_event_type}")
            await self.bot.handle_event(dict(event))
        
        # WebSocket 连接事件
        @self.cqhttp.on_websocket_connection
        async def on_ws_connected(event: CQEvent):
            """WebSocket 连接成功"""
            logger.success(f"✅ WebSocket 已连接: Bot {event.self_id}")
            
            # 获取并设置 bot 信息
            if not self.bot.self_id:
                self.bot.self_id = event.self_id
                
                # 尝试获取昵称
                try:
                    info = await self.cqhttp.get_login_info(self_id=event.self_id)
                    if info:
                        self.bot.nickname = info.get("nickname")
                        logger.info(f"✅ 登录账号: {self.bot.nickname} ({self.bot.self_id})")
                except Exception as e:
                    logger.warning(f"获取登录信息失败: {e}")
    
    async def start(self, host: str = "0.0.0.0", port: int = 8080):
        """
        启动 aiocqhttp 服务器
        
        Args:
            host: 监听地址
            port: 监听端口
        """
        logger.info(f"🔌 启动 AioCQHTTP 服务器: {host}:{port}")
        
        try:
            await self.cqhttp.run_task(host=host, port=port)
        except Exception as e:
            logger.error(f"❌ AioCQHTTP 启动失败: {e}")
            raise
    
    async def stop(self):
        """停止适配器"""
        logger.info("🔌 AioCQHTTP 适配器已停止")
    
    async def call_api(self, action: str, **params) -> Any:
        """
        调用 OneBot API
        
        Args:
            action: API 动作名
            **params: API 参数
            
        Returns:
            API 响应数据
        """
        try:
            result = await self.cqhttp.call_action(action, **params)
            logger.debug(f"✅ API 调用: {action}")
            return result
        except Exception as e:
            logger.error(f"❌ API 调用失败: {action}, 错误: {e}")
            return None
    
    # ==================== OneBot-11 标准 API 完整实现 ====================
    
    # ===== 消息相关 =====
    
    async def send_private_msg(self, user_id: int, message: Any, auto_escape: bool = False) -> Dict[str, Any]:
        """发送私聊消息"""
        result = await self.call_api("send_private_msg", user_id=user_id, message=message, auto_escape=auto_escape)
        return result if result else {}
    
    async def send_group_msg(self, group_id: int, message: Any, auto_escape: bool = False) -> Dict[str, Any]:
        """发送群消息"""
        result = await self.call_api("send_group_msg", group_id=group_id, message=message, auto_escape=auto_escape)
        return result if result else {}
    
    async def send_msg(self, message_type: str = None, user_id: int = None, group_id: int = None,
                       message: Any = None, auto_escape: bool = False) -> Dict[str, Any]:
        """发送消息"""
        params = {}
        if message_type:
            params["message_type"] = message_type
        if user_id:
            params["user_id"] = user_id
        if group_id:
            params["group_id"] = group_id
        if message is not None:
            params["message"] = message
        if auto_escape:
            params["auto_escape"] = auto_escape
        result = await self.call_api("send_msg", **params)
        return result if result else {}
    
    async def delete_msg(self, message_id: int) -> Dict[str, Any]:
        """撤回消息"""
        result = await self.call_api("delete_msg", message_id=message_id)
        return result if result else {}
    
    async def get_msg(self, message_id: int) -> Dict[str, Any]:
        """获取消息"""
        result = await self.call_api("get_msg", message_id=message_id)
        return result if result else {}
    
    async def get_forward_msg(self, id: str) -> Dict[str, Any]:
        """获取合并转发消息"""
        result = await self.call_api("get_forward_msg", id=id)
        return result if result else {}
    
    async def send_like(self, user_id: int, times: int = 1) -> Dict[str, Any]:
        """发送好友赞"""
        result = await self.call_api("send_like", user_id=user_id, times=times)
        return result if result else {}
    
    # ===== 群组管理 =====
    
    async def set_group_kick(self, group_id: int, user_id: int, reject_add_request: bool = False) -> Dict[str, Any]:
        """群组踢人"""
        result = await self.call_api("set_group_kick", group_id=group_id, user_id=user_id, 
                                     reject_add_request=reject_add_request)
        return result if result else {}
    
    async def set_group_ban(self, group_id: int, user_id: int, duration: int = 30 * 60) -> Dict[str, Any]:
        """群组单人禁言"""
        result = await self.call_api("set_group_ban", group_id=group_id, user_id=user_id, duration=duration)
        return result if result else {}
    
    async def set_group_anonymous_ban(self, group_id: int, anonymous: Dict = None, anonymous_flag: str = None, 
                                      duration: int = 30 * 60) -> Dict[str, Any]:
        """群组匿名用户禁言"""
        params = {"group_id": group_id, "duration": duration}
        if anonymous:
            params["anonymous"] = anonymous
        if anonymous_flag:
            params["anonymous_flag"] = anonymous_flag
        result = await self.call_api("set_group_anonymous_ban", **params)
        return result if result else {}
    
    async def set_group_whole_ban(self, group_id: int, enable: bool = True) -> Dict[str, Any]:
        """群组全员禁言"""
        result = await self.call_api("set_group_whole_ban", group_id=group_id, enable=enable)
        return result if result else {}
    
    async def set_group_admin(self, group_id: int, user_id: int, enable: bool = True) -> Dict[str, Any]:
        """群组设置管理员"""
        result = await self.call_api("set_group_admin", group_id=group_id, user_id=user_id, enable=enable)
        return result if result else {}
    
    async def set_group_anonymous(self, group_id: int, enable: bool = True) -> Dict[str, Any]:
        """群组匿名"""
        result = await self.call_api("set_group_anonymous", group_id=group_id, enable=enable)
        return result if result else {}
    
    async def set_group_card(self, group_id: int, user_id: int, card: str = "") -> Dict[str, Any]:
        """设置群名片（群备注）"""
        result = await self.call_api("set_group_card", group_id=group_id, user_id=user_id, card=card)
        return result if result else {}
    
    async def set_group_name(self, group_id: int, group_name: str) -> Dict[str, Any]:
        """设置群名"""
        result = await self.call_api("set_group_name", group_id=group_id, group_name=group_name)
        return result if result else {}
    
    async def set_group_leave(self, group_id: int, is_dismiss: bool = False) -> Dict[str, Any]:
        """退出群组"""
        result = await self.call_api("set_group_leave", group_id=group_id, is_dismiss=is_dismiss)
        return result if result else {}
    
    async def set_group_special_title(self, group_id: int, user_id: int, special_title: str = "", 
                                      duration: int = -1) -> Dict[str, Any]:
        """设置群组专属头衔"""
        result = await self.call_api("set_group_special_title", group_id=group_id, user_id=user_id,
                                     special_title=special_title, duration=duration)
        return result if result else {}
    
    # ===== 请求处理 =====
    
    async def set_friend_add_request(self, flag: str, approve: bool = True, remark: str = "") -> Dict[str, Any]:
        """处理加好友请求"""
        result = await self.call_api("set_friend_add_request", flag=flag, approve=approve, remark=remark)
        return result if result else {}
    
    async def set_group_add_request(self, flag: str, sub_type: str, approve: bool = True, 
                                    reason: str = "") -> Dict[str, Any]:
        """处理加群请求/邀请"""
        result = await self.call_api("set_group_add_request", flag=flag, sub_type=sub_type, 
                                     approve=approve, reason=reason)
        return result if result else {}
    
    # ===== 信息获取 =====
    
    async def get_login_info(self) -> Dict[str, Any]:
        """获取登录号信息"""
        result = await self.call_api("get_login_info")
        return result if result else {}
    
    async def get_stranger_info(self, user_id: int, no_cache: bool = False) -> Dict[str, Any]:
        """获取陌生人信息"""
        result = await self.call_api("get_stranger_info", user_id=user_id, no_cache=no_cache)
        return result if result else {}
    
    async def get_friend_list(self) -> list:
        """获取好友列表"""
        result = await self.call_api("get_friend_list")
        return result if isinstance(result, list) else []
    
    async def get_group_info(self, group_id: int, no_cache: bool = False) -> Dict[str, Any]:
        """获取群信息"""
        result = await self.call_api("get_group_info", group_id=group_id, no_cache=no_cache)
        return result if result else {}
    
    async def get_group_list(self) -> list:
        """获取群列表"""
        result = await self.call_api("get_group_list")
        return result if isinstance(result, list) else []
    
    async def get_group_member_info(self, group_id: int, user_id: int, no_cache: bool = False) -> Dict[str, Any]:
        """获取群成员信息"""
        result = await self.call_api("get_group_member_info", group_id=group_id, user_id=user_id, no_cache=no_cache)
        return result if result else {}
    
    async def get_group_member_list(self, group_id: int) -> list:
        """获取群成员列表"""
        result = await self.call_api("get_group_member_list", group_id=group_id)
        return result if isinstance(result, list) else []
    
    async def get_group_honor_info(self, group_id: int, type: str) -> Dict[str, Any]:
        """获取群荣誉信息"""
        result = await self.call_api("get_group_honor_info", group_id=group_id, type=type)
        return result if result else {}
    
    # ===== 其他 API =====
    
    async def get_cookies(self, domain: str = "") -> Dict[str, Any]:
        """获取 Cookies"""
        result = await self.call_api("get_cookies", domain=domain)
        return result if result else {}
    
    async def get_csrf_token(self) -> Dict[str, Any]:
        """获取 CSRF Token"""
        result = await self.call_api("get_csrf_token")
        return result if result else {}
    
    async def get_credentials(self, domain: str = "") -> Dict[str, Any]:
        """获取 QQ 相关接口凭证"""
        result = await self.call_api("get_credentials", domain=domain)
        return result if result else {}
    
    async def get_record(self, file: str, out_format: str) -> Dict[str, Any]:
        """获取语音"""
        result = await self.call_api("get_record", file=file, out_format=out_format)
        return result if result else {}
    
    async def get_image(self, file: str) -> Dict[str, Any]:
        """获取图片"""
        result = await self.call_api("get_image", file=file)
        return result if result else {}
    
    async def can_send_image(self) -> Dict[str, Any]:
        """检查是否可以发送图片"""
        result = await self.call_api("can_send_image")
        return result if result else {}
    
    async def can_send_record(self) -> Dict[str, Any]:
        """检查是否可以发送语音"""
        result = await self.call_api("can_send_record")
        return result if result else {}
    
    async def get_status(self) -> Dict[str, Any]:
        """获取运行状态"""
        result = await self.call_api("get_status")
        return result if result else {}
    
    async def get_version_info(self) -> Dict[str, Any]:
        """获取版本信息"""
        result = await self.call_api("get_version_info")
        return result if result else {}
    
    async def set_restart(self, delay: int = 0) -> Dict[str, Any]:
        """重启 OneBot 实现"""
        result = await self.call_api("set_restart", delay=delay)
        return result if result else {}
    
    async def clean_cache(self) -> Dict[str, Any]:
        """清理缓存"""
        result = await self.call_api("clean_cache")
        return result if result else {}
    
    async def send(self, event_dict: Dict, message: Any, at_sender: bool = False) -> Dict[str, Any]:
        """
        根据事件自动发送消息
        
        Args:
            event_dict: 事件字典
            message: 消息内容
            at_sender: 是否 @ 发送者
            
        Returns:
            API 响应
        """
        try:
            # 转换为 CQEvent
            event = CQEvent(event_dict)
            result = await self.cqhttp.send(event, message, at_sender=at_sender)
            return result if result else {}
        except Exception as e:
            logger.error(f"❌ 发送消息失败: {e}")
            return {}


# 便捷导出
__all__ = ['AioCQHTTPAdapter']


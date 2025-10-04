"""
正向 WebSocket 客户端适配器（反向连接）

EchoFrame 作为客户端，主动连接到 OneBot 实现的 WebSocket 服务器
适用于 Lagrange 的 ForwardWebSocket 配置
"""

import json
import asyncio
from typing import Dict, Any, Optional
import websockets
from loguru import logger


class WebSocketClientAdapter:
    """
    正向 WebSocket 客户端适配器
    
    EchoFrame 主动连接到 OneBot 实现（如 Lagrange ForwardWebSocket）
    """
    
    def __init__(self, bot: 'Bot', config: Dict[str, Any]):
        """
        初始化适配器
        
        Args:
            bot: Bot 实例
            config: 配置
        """
        self.bot = bot
        self.config = config
        self.url = config.get("url", "ws://127.0.0.1:8082")
        self.access_token = config.get("access_token", "")
        self.reconnect_interval = config.get("reconnect_interval", 3)
        
        self.websocket = None
        self.is_running = False
        self._connected = False
        
        # API 调用支持
        self._api_seq = 0
        self._pending_api_calls = {}
    
    async def start(self):
        """启动适配器（自动连接和重连）"""
        self.is_running = True
        logger.info(f"🔌 正向 WebSocket 客户端启动，目标: {self.url}")
        
        while self.is_running:
            try:
                await self._connect()
            except Exception as e:
                logger.error(f"❌ WebSocket 连接错误: {e}")
            
            self._connected = False
            
            if self.is_running:
                logger.info(f"🔄 {self.reconnect_interval} 秒后重连...")
                await asyncio.sleep(self.reconnect_interval)
    
    async def _connect(self):
        """连接到 WebSocket 服务器"""
        # 连接参数
        connect_params = {
            "ping_interval": 10,
            "ping_timeout": 5,
            "close_timeout": 5
        }
        
        # 添加 Authorization header
        if self.access_token:
            connect_params["additional_headers"] = {
                "Authorization": f"Bearer {self.access_token}"
            }
        
        logger.info(f"🔗 正在连接到 {self.url}...")
        
        async with websockets.connect(self.url, **connect_params) as websocket:
            self.websocket = websocket
            self._connected = True
            logger.success(f"✅ WebSocket 已连接: {self.url}")
            
            # 连接成功，尝试获取登录信息
            if not self.bot.self_id:
                try:
                    info = await self.call_api("get_login_info")
                    if info and info.get("user_id"):
                        self.bot.self_id = info.get("user_id")
                        self.bot.nickname = info.get("nickname")
                        logger.success(f"✅ 登录账号: {self.bot.nickname} ({self.bot.self_id})")
                except Exception as e:
                    logger.debug(f"获取登录信息失败（不影响使用）: {e}")
            
            try:
                # 接收消息循环
                async for message in websocket:
                    asyncio.create_task(self._handle_message(message))
            except websockets.exceptions.ConnectionClosed as e:
                logger.warning(f"🔌 WebSocket 连接已关闭: {e.code}")
            finally:
                self.websocket = None
                self._connected = False
    
    async def _handle_message(self, message: str):
        """处理收到的消息"""
        try:
            data = json.loads(message)
            
            # 1. API 响应（优先）
            echo = data.get("echo")
            if echo and echo in self._pending_api_calls:
                future = self._pending_api_calls[echo]
                if not future.done():
                    if data.get("status") == "ok":
                        future.set_result(data.get("data", {}))
                    else:
                        future.set_result(None)
                return
            
            # 2. 事件
            if "post_type" in data:
                await self.bot.handle_event(data)
                return
            
            # 3. 心跳（忽略）
            if "interval" in data and "status" in data:
                return
            
        except json.JSONDecodeError:
            logger.error(f"❌ JSON 解析失败")
        except Exception as e:
            logger.exception(f"❌ 处理消息异常: {e}")
    
    async def call_api(self, action: str, **params) -> Any:
        """
        通过 WebSocket 调用 API
        
        Args:
            action: API 动作
            **params: API 参数
            
        Returns:
            API 响应数据
        """
        if not self.websocket or not self._connected:
            logger.warning(f"⚠️ WebSocket 未连接，无法调用 API: {action}")
            return None
        
        # 生成序列号
        self._api_seq += 1
        echo = f"api_{self._api_seq}_{action}"
        
        # 构建请求
        request = {
            "action": action,
            "params": params,
            "echo": echo
        }
        
        # 创建 Future 等待响应
        future = asyncio.Future()
        self._pending_api_calls[echo] = future
        
        try:
            # 发送请求
            await self.websocket.send(json.dumps(request, ensure_ascii=False))
            logger.debug(f"📤 API 请求: {action}")
            
            # 等待响应
            response = await asyncio.wait_for(future, timeout=10)
            logger.debug(f"✅ API 响应: {action}")
            return response
            
        except asyncio.TimeoutError:
            logger.warning(f"⏱️ API 超时: {action}")
            return None
        except Exception as e:
            logger.error(f"❌ API 异常: {action}, {e}")
            return None
        finally:
            self._pending_api_calls.pop(echo, None)
    
    async def send_private_msg(self, user_id: int, message: Any) -> Dict[str, Any]:
        """发送私聊消息"""
        result = await self.call_api("send_private_msg", user_id=user_id, message=message)
        return result if result else {}
    
    async def send_group_msg(self, group_id: int, message: Any) -> Dict[str, Any]:
        """发送群消息"""
        result = await self.call_api("send_group_msg", group_id=group_id, message=message)
        return result if result else {}
    
    async def stop(self):
        """停止适配器"""
        self.is_running = False
        self._connected = False
        
        # 取消所有待处理的 API 调用
        for future in self._pending_api_calls.values():
            if not future.done():
                future.cancel()
        self._pending_api_calls.clear()
        
        if self.websocket:
            await self.websocket.close()
        
        logger.info("🔌 正向 WebSocket 客户端已停止")


__all__ = ['WebSocketClientAdapter']


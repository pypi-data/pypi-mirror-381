"""
通信适配器模块

支持两种模式：
- AioCQHTTPAdapter: 反向 WebSocket（EchoFrame 作为服务端）
- WebSocketClientAdapter: 正向 WebSocket（EchoFrame 作为客户端）
"""

from .aiocqhttp_adapter import AioCQHTTPAdapter
from .ws_client import WebSocketClientAdapter

__all__ = [
    'AioCQHTTPAdapter',
    'WebSocketClientAdapter',
]

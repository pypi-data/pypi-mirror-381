"""EchoFrame 核心模块

这个模块可以作为 Python 库使用：
    pip install echoframe
    
    from echoframe import Bot, Plugin, on_command
"""

# 版本信息
__version__ = "2.0.0"
__author__ = "EchoFrame Team"

# Bot 核心
from .bot import Bot

# 插件系统
from .plugin import (
    Plugin,
    PluginMetadata,
    PluginStatus,
    PluginOperationResult,
    on_message,
    on_notice,
    on_request,
    on_command,
    get_plugin_manager,
)

# 事件系统
from .event import (
    Event,
    MessageEvent,
    PrivateMessageEvent,
    GroupMessageEvent,
    NoticeEvent,
    RequestEvent,
    MetaEvent,
    parse_event,
)

# 消息系统
from .message import MessageSegment, MS, Message

# API 接口已集成到 aiocqhttp，不再需要单独的 API 类

# 中间件系统
from .middleware import (
    MiddlewareManager,
    middleware,
    log_middleware,
    auth_middleware,
    rate_limit_middleware,
    error_handler_middleware,
)

# 心跳系统
from .heartbeat import HeartbeatManager

__all__ = [
    # 版本信息
    '__version__',
    '__author__',
    
    # Bot 核心
    'Bot',
    
    # 插件系统
    'Plugin',
    'PluginMetadata',
    'PluginStatus',
    'PluginOperationResult',
    'on_message',
    'on_notice',
    'on_request',
    'on_command',
    'get_plugin_manager',
    
    # 事件系统
    'Event',
    'MessageEvent',
    'PrivateMessageEvent',
    'GroupMessageEvent',
    'NoticeEvent',
    'RequestEvent',
    'MetaEvent',
    'parse_event',
    
    # 消息系统
    'MessageSegment',
    'MS',
    'Message',
    
    
    # 中间件
    'MiddlewareManager',
    'middleware',
    'log_middleware',
    'auth_middleware',
    'rate_limit_middleware',
    'error_handler_middleware',
    
    # 心跳
    'HeartbeatManager',
]



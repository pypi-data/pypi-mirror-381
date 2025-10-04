"""
EchoFrame - OneBot-11 协议机器人框架

一个完整的、可作为库使用的 OneBot-11 协议机器人框架

使用方法：
    pip install echoframe
    
    from echoframe import Bot, Plugin, on_command, MS

作者：EchoFrame Team
版本：2.0.0
"""

__version__ = "2.0.0"
__author__ = "EchoFrame Team"
__package_name__ = "echoframe"

# 从 core 导入所有内容
import sys
from pathlib import Path

# 添加父目录到路径（让 echoframe 可以访问 core 和 adapters）
_parent_dir = Path(__file__).parent.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

# 导入核心模块
from core import (
    Bot,
    Plugin,
    PluginMetadata,
    PluginStatus,
    PluginOperationResult,
    on_message,
    on_notice,
    on_request,
    on_command,
    get_plugin_manager,
    Event,
    MessageEvent,
    PrivateMessageEvent,
    GroupMessageEvent,
    NoticeEvent,
    RequestEvent,
    MetaEvent,
    parse_event,
    MessageSegment,
    MS,
    Message,
    MiddlewareManager,
    middleware,
    log_middleware,
    auth_middleware,
    rate_limit_middleware,
    error_handler_middleware,
    HeartbeatManager,
)

__all__ = [
    # 版本信息
    '__version__',
    '__author__',
    '__package_name__',
    
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


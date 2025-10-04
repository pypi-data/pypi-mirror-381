"""
EchoFrame 事件系统 - 轻量级包装

使用 aiocqhttp.Event 作为底层，添加 EchoFrame 的辅助方法
"""

from typing import Dict, Any, Optional, List

# 从 aiocqhttp 导入底层实现
try:
    from aiocqhttp import Event as AioEvent
    _has_aiocqhttp = True
except ImportError:
    _has_aiocqhttp = False
    # 基础 Event 类（fallback）
    class AioEvent(dict):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for k, v in self.items():
                setattr(self, k, v)


# ==================== Event 包装类 ====================

class Event(AioEvent):
    """
    EchoFrame 事件类 - 扩展 aiocqhttp.Event
    
    添加了便捷的辅助方法
    """
    
    # 快速操作字段（用于返回快速操作）
    reply: Optional[Any] = None
    auto_escape: Optional[bool] = None
    at_sender: Optional[bool] = None
    delete: Optional[bool] = None
    kick: Optional[bool] = None
    ban: Optional[bool] = None
    ban_duration: Optional[int] = None
    approve: Optional[bool] = None
    remark: Optional[str] = None
    reason: Optional[str] = None


class MessageEvent(Event):
    """消息事件 - 扩展方法"""
    
    def is_private(self) -> bool:
        """是否为私聊消息"""
        return self.get("message_type") == "private"
    
    def is_group(self) -> bool:
        """是否为群消息"""
        return self.get("message_type") == "group"
    
    def is_to_me(self) -> bool:
        """是否 @ 了机器人"""
        message = self.get("message", [])
        self_id = self.get("self_id")
        
        if isinstance(message, list):
            for seg in message:
                if isinstance(seg, dict) and seg.get("type") == "at":
                    if seg.get("data", {}).get("qq") == str(self_id):
                        return True
        return False
    
    def get_message_text(self) -> str:
        """获取消息文本内容（去除 CQ 码）"""
        raw_message = self.get("raw_message", "")
        if raw_message:
            return raw_message
        
        message = self.get("message", "")
        if isinstance(message, str):
            import re
            return re.sub(r'\[CQ:[^\]]+\]', '', message)
        elif isinstance(message, list):
            text_parts = []
            for seg in message:
                if isinstance(seg, dict) and seg.get("type") == "text":
                    text_parts.append(seg.get("data", {}).get("text", ""))
            return "".join(text_parts)
        return ""
    
    def get_plain_text(self) -> str:
        """获取纯文本（别名）"""
        return self.get_message_text()
    
    def has_image(self) -> bool:
        """是否包含图片"""
        message = self.get("message", [])
        if isinstance(message, list):
            return any(seg.get("type") == "image" for seg in message if isinstance(seg, dict))
        return False
    
    def get_images(self) -> List[str]:
        """获取所有图片的 file 参数"""
        images = []
        message = self.get("message", [])
        if isinstance(message, list):
            for seg in message:
                if isinstance(seg, dict) and seg.get("type") == "image":
                    file = seg.get("data", {}).get("file")
                    if file:
                        images.append(file)
        return images


# 定义事件类型别名（简化使用）
PrivateMessageEvent = MessageEvent
GroupMessageEvent = MessageEvent
NoticeEvent = Event
RequestEvent = Event
MetaEvent = Event

# 通知事件子类型
GroupUploadNoticeEvent = Event
GroupAdminNoticeEvent = Event
GroupDecreaseNoticeEvent = Event
GroupIncreaseNoticeEvent = Event
GroupBanNoticeEvent = Event
FriendAddNoticeEvent = Event
GroupRecallNoticeEvent = Event
FriendRecallNoticeEvent = Event
PokeNotifyEvent = Event
LuckyKingNotifyEvent = Event
HonorNotifyEvent = Event
NotifyEvent = Event

# 请求事件子类型
FriendRequestEvent = Event
GroupRequestEvent = Event

# 元事件子类型
LifecycleMetaEvent = Event
HeartbeatMetaEvent = Event


def parse_event(data: Dict[str, Any]) -> Event:
    """
    解析事件数据
    
    Args:
        data: 事件数据字典
        
    Returns:
        Event 对象
    """
    # 使用 aiocqhttp 的 Event.from_payload 或直接创建
    if _has_aiocqhttp:
        event = AioEvent.from_payload(data) if hasattr(AioEvent, 'from_payload') else AioEvent(data)
    else:
        event = Event(data)
    
    # 根据类型返回对应的事件类
    post_type = data.get("post_type")
    
    if post_type == "message":
        return MessageEvent(data)
    elif post_type in ("notice", "request", "meta_event"):
        return Event(data)
    else:
        return Event(data)


# 导出
__all__ = [
    'Event',
    'MessageEvent',
    'PrivateMessageEvent',
    'GroupMessageEvent',
    'NoticeEvent',
    'GroupUploadNoticeEvent',
    'GroupAdminNoticeEvent',
    'GroupDecreaseNoticeEvent',
    'GroupIncreaseNoticeEvent',
    'GroupBanNoticeEvent',
    'FriendAddNoticeEvent',
    'GroupRecallNoticeEvent',
    'FriendRecallNoticeEvent',
    'NotifyEvent',
    'PokeNotifyEvent',
    'LuckyKingNotifyEvent',
    'HonorNotifyEvent',
    'RequestEvent',
    'FriendRequestEvent',
    'GroupRequestEvent',
    'MetaEvent',
    'LifecycleMetaEvent',
    'HeartbeatMetaEvent',
    'parse_event',
]

"""
EchoFrame 消息系统 - 轻量级包装

映射到 aiocqhttp 的 Message 和 MessageSegment，保留简洁的 API
"""

from typing import Union, List, Dict, Any, Optional

# 从 aiocqhttp 导入底层实现
try:
    from aiocqhttp import Message as AioMessage, MessageSegment as AioMessageSegment
    _has_aiocqhttp = True
except ImportError:
    _has_aiocqhttp = False
    # 如果没有 aiocqhttp，提供基础实现
    class AioMessage(list):
        pass
    
    class AioMessageSegment(dict):
        @staticmethod
        def text(text):
            return {"type": "text", "data": {"text": text}}


# ==================== 轻量级包装 ====================

# 直接使用 aiocqhttp 的类
Message = AioMessage
MessageSegment = AioMessageSegment


# ==================== MS 工厂类（EchoFrame 特色 API）====================

class MS:
    """
    消息段工厂类 - EchoFrame 简洁 API
    
    底层使用 aiocqhttp.MessageSegment 实现
    """
    
    @staticmethod
    def text(text: str):
        """纯文本"""
        return MessageSegment.text(text)
    
    @staticmethod
    def face(id: Union[int, str]):
        """QQ 表情"""
        return MessageSegment.face(int(id) if isinstance(id, str) else id)
    
    @staticmethod
    def image(file: str, type: Optional[str] = None, cache: bool = True, 
              proxy: bool = True, timeout: Optional[int] = None):
        """图片"""
        return MessageSegment.image(
            file=file,
            type_=type,
            cache=cache,
            proxy=proxy,
            timeout=timeout
        )
    
    @staticmethod
    def record(file: str, magic: bool = False, cache: bool = True,
               proxy: bool = True, timeout: Optional[int] = None):
        """语音"""
        return MessageSegment.record(
            file=file,
            magic=magic,
            cache=cache,
            proxy=proxy,
            timeout=timeout
        )
    
    @staticmethod
    def video(file: str, cache: bool = True, proxy: bool = True,
              timeout: Optional[int] = None):
        """短视频"""
        return MessageSegment.video(
            file=file,
            cache=cache,
            proxy=proxy,
            timeout=timeout
        )
    
    @staticmethod
    def at(qq: Union[int, str]):
        """@某人"""
        return MessageSegment.at(qq)
    
    @staticmethod
    def at_all():
        """@全体成员"""
        return MessageSegment.at("all")
    
    @staticmethod
    def rps():
        """猜拳魔法表情"""
        return MessageSegment.rps()
    
    @staticmethod
    def dice():
        """掷骰子魔法表情"""
        return MessageSegment.dice()
    
    @staticmethod
    def shake():
        """窗口抖动"""
        return MessageSegment.shake()
    
    @staticmethod
    def poke(type: str, id: str):
        """戳一戳"""
        return MessageSegment.poke(type_=type, id_=id)
    
    @staticmethod
    def anonymous(ignore: bool = False):
        """匿名发消息"""
        return MessageSegment.anonymous(ignore_failure=ignore)
    
    @staticmethod
    def share(url: str, title: str, content: Optional[str] = None,
              image: Optional[str] = None):
        """链接分享"""
        return MessageSegment.share(
            url=url,
            title=title,
            content=content,
            image_url=image
        )
    
    @staticmethod
    def contact_user(id: Union[int, str]):
        """推荐好友"""
        return MessageSegment.contact_user(int(id) if isinstance(id, str) else id)
    
    @staticmethod
    def contact_group(id: Union[int, str]):
        """推荐群"""
        return MessageSegment.contact_group(int(id) if isinstance(id, str) else id)
    
    @staticmethod
    def location(lat: Union[float, str], lon: Union[float, str],
                 title: Optional[str] = None, content: Optional[str] = None):
        """位置"""
        return MessageSegment.location(
            latitude=float(lat),
            longitude=float(lon),
            title=title,
            content=content
        )
    
    @staticmethod
    def music(type: str, id: Union[int, str]):
        """音乐分享"""
        return MessageSegment.music(
            type_=type,
            id_=int(id) if isinstance(id, str) else id
        )
    
    @staticmethod
    def music_custom(url: str, audio: str, title: str,
                     content: Optional[str] = None, image: Optional[str] = None):
        """音乐自定义分享"""
        return MessageSegment.music_custom(
            url=url,
            audio_url=audio,
            title=title,
            content=content,
            image_url=image
        )
    
    @staticmethod
    def reply(id: Union[int, str]):
        """回复消息"""
        return MessageSegment.reply(int(id) if isinstance(id, str) else id)
    
    @staticmethod
    def forward(id: str):
        """合并转发"""
        return MessageSegment.forward(int(id))
    
    @staticmethod
    def node(id: Union[int, str]):
        """合并转发节点"""
        return MessageSegment.node(int(id) if isinstance(id, str) else id)
    
    @staticmethod
    def node_custom(user_id: Union[int, str], nickname: str, content: Any):
        """合并转发自定义节点"""
        return MessageSegment.node_custom(
            user_id=int(user_id) if isinstance(user_id, str) else user_id,
            nickname=nickname,
            content=content
        )
    
    @staticmethod
    def xml(data: str):
        """XML 消息"""
        return MessageSegment.xml(data)
    
    @staticmethod
    def json(data: str):
        """JSON 消息"""
        return MessageSegment.json(data)


# 便捷导出
__all__ = [
    'MessageSegment',  # aiocqhttp.MessageSegment
    'Message',         # aiocqhttp.Message
    'MS',              # EchoFrame 工厂类
]

"""
中间件系统

允许在事件处理前后执行自定义逻辑
"""

from typing import Callable, List, Any, Awaitable
from loguru import logger
from .event import Event


# 中间件类型定义
MiddlewareFunc = Callable[['Bot', Event, Callable], Awaitable[Any]]


class MiddlewareManager:
    """中间件管理器"""
    
    def __init__(self):
        self.middlewares: List[MiddlewareFunc] = []
    
    def use(self, middleware: MiddlewareFunc):
        """
        注册中间件
        
        Args:
            middleware: 中间件函数
        """
        self.middlewares.append(middleware)
        logger.debug(f"注册中间件: {middleware.__name__}")
    
    def remove(self, middleware: MiddlewareFunc):
        """
        移除中间件
        
        Args:
            middleware: 中间件函数
        """
        if middleware in self.middlewares:
            self.middlewares.remove(middleware)
            logger.debug(f"移除中间件: {middleware.__name__}")
    
    def clear(self):
        """清空所有中间件"""
        self.middlewares.clear()
        logger.debug("清空所有中间件")
    
    async def process(self, bot: 'Bot', event: Event, handler: Callable) -> Any:
        """
        执行中间件链
        
        Args:
            bot: Bot 实例
            event: 事件对象
            handler: 最终的事件处理器
            
        Returns:
            处理结果
        """
        # 如果没有中间件，直接执行处理器
        if not self.middlewares:
            return await handler(bot, event)
        
        # 构建中间件链
        async def execute(index: int):
            # 到达链尾，执行实际的处理器
            if index >= len(self.middlewares):
                return await handler(bot, event)
            
            # 执行当前中间件
            middleware = self.middlewares[index]
            
            # next 函数：执行下一个中间件
            async def next_middleware():
                return await execute(index + 1)
            
            try:
                return await middleware(bot, event, next_middleware)
            except Exception as e:
                logger.exception(f"中间件 {middleware.__name__} 执行异常: {e}")
                # 继续执行下一个中间件
                return await next_middleware()
        
        # 从第一个中间件开始执行
        return await execute(0)


# ==================== 内置中间件 ====================

async def log_middleware(bot: 'Bot', event: Event, next: Callable):
    """
    日志中间件 - 记录事件处理时间
    
    Args:
        bot: Bot 实例
        event: 事件对象
        next: 下一个中间件
    """
    import time
    start_time = time.time()
    
    # 执行下一个中间件
    result = await next()
    
    # 记录耗时
    duration = time.time() - start_time
    if duration > 1:  # 超过 1 秒才记录
        logger.warning(f"⏱️ 事件处理耗时: {duration:.3f}秒")
    
    return result


async def auth_middleware(bot: 'Bot', event: Event, next: Callable):
    """
    权限中间件 - 黑名单检查
    
    Args:
        bot: Bot 实例
        event: 事件对象
        next: 下一个中间件
    """
    from .event import MessageEvent
    
    # 只对消息事件检查
    if isinstance(event, MessageEvent):
        # 检查黑名单（示例）
        blacklist = bot.config.get("bot", {}).get("blacklist", [])
        if event.user_id in blacklist:
            logger.warning(f"🚫 用户 {event.user_id} 在黑名单中，拒绝处理")
            return None
    
    # 继续执行
    return await next()


async def rate_limit_middleware(bot: 'Bot', event: Event, next: Callable):
    """
    限流中间件 - 防止用户刷屏
    
    Args:
        bot: Bot 实例
        event: 事件对象
        next: 下一个中间件
    """
    from .event import MessageEvent
    import time
    
    if isinstance(event, MessageEvent):
        # 简单的限流：每个用户 1 秒最多 3 条消息
        if not hasattr(bot, '_user_message_times'):
            bot._user_message_times = {}
        
        user_id = event.user_id
        current_time = time.time()
        
        # 获取用户的消息时间列表
        if user_id not in bot._user_message_times:
            bot._user_message_times[user_id] = []
        
        # 清理 1 秒前的记录
        bot._user_message_times[user_id] = [
            t for t in bot._user_message_times[user_id]
            if current_time - t < 1
        ]
        
        # 检查是否超过限制
        if len(bot._user_message_times[user_id]) >= 3:
            logger.warning(f"⚠️ 用户 {user_id} 发送消息过快，跳过处理")
            return None
        
        # 记录当前时间
        bot._user_message_times[user_id].append(current_time)
    
    return await next()


async def error_handler_middleware(bot: 'Bot', event: Event, next: Callable):
    """
    错误处理中间件 - 统一错误处理
    
    Args:
        bot: Bot 实例
        event: 事件对象
        next: 下一个中间件
    """
    try:
        return await next()
    except Exception as e:
        logger.exception(f"❌ 事件处理发生未捕获异常: {e}")
        
        # 可以在这里发送错误通知给超级用户
        from .event import MessageEvent
        if isinstance(event, MessageEvent) and bot.is_superuser(event.user_id):
            try:
                await bot.send(event, f"⚠️ 发生错误: {str(e)[:100]}")
            except:
                pass
        
        return None


# ==================== 装饰器 ====================

def middleware(priority: int = 50):
    """
    中间件装饰器
    
    Args:
        priority: 优先级（越大越先执行）
    
    Usage:
        @middleware(priority=100)
        async def my_middleware(bot, event, next):
            # 前置处理
            result = await next()
            # 后置处理
            return result
    """
    def decorator(func: MiddlewareFunc):
        func._is_middleware = True
        func._priority = priority
        return func
    return decorator


# 导出
__all__ = [
    'MiddlewareManager',
    'MiddlewareFunc',
    'middleware',
    'log_middleware',
    'auth_middleware',
    'rate_limit_middleware',
    'error_handler_middleware',
]


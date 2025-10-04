"""
OneBot-11 心跳机制

定期生成心跳元事件，上报机器人运行状态
"""

import asyncio
import time
from typing import Dict, Any, Optional, Callable
from loguru import logger


class HeartbeatManager:
    """心跳管理器"""
    
    def __init__(self, bot: 'Bot', config: Dict[str, Any]):
        """
        初始化心跳管理器
        
        Args:
            bot: Bot 实例
            config: 心跳配置
        """
        self.bot = bot
        self.enabled = config.get("enable", False)
        self.interval = config.get("interval", 15000) / 1000  # 转换为秒
        
        self._task: Optional[asyncio.Task] = None
        self._is_running = False
        self._callbacks: list[Callable] = []
    
    async def start(self):
        """启动心跳"""
        if not self.enabled:
            logger.info("心跳功能未启用")
            return
        
        if self._is_running:
            logger.warning("心跳已在运行中")
            return
        
        self._is_running = True
        self._task = asyncio.create_task(self._heartbeat_loop())
        logger.info(f"心跳启动，间隔: {self.interval}秒")
    
    async def stop(self):
        """停止心跳"""
        self._is_running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            self._task = None
        logger.info("心跳已停止")
    
    def register_callback(self, callback: Callable):
        """
        注册心跳回调函数
        
        Args:
            callback: 回调函数，接收心跳事件数据
        """
        self._callbacks.append(callback)
    
    async def _heartbeat_loop(self):
        """心跳循环"""
        while self._is_running:
            try:
                # 等待指定间隔
                await asyncio.sleep(self.interval)
                
                if not self._is_running:
                    break
                
                # 生成心跳事件
                heartbeat_event = self._generate_heartbeat_event()
                
                # 调用所有回调
                for callback in self._callbacks:
                    try:
                        if asyncio.iscoroutinefunction(callback):
                            await callback(heartbeat_event)
                        else:
                            callback(heartbeat_event)
                    except Exception as e:
                        logger.error(f"心跳回调执行失败: {e}")
                
                logger.debug("心跳发送完成")
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"心跳循环异常: {e}")
                if self._is_running:
                    await asyncio.sleep(1)  # 发生错误时等待1秒再继续
    
    def _generate_heartbeat_event(self) -> Dict[str, Any]:
        """
        生成心跳事件数据
        
        Returns:
            心跳事件字典
        """
        return {
            "time": int(time.time()),
            "self_id": self.bot.self_id if self.bot.self_id else 0,
            "post_type": "meta_event",
            "meta_event_type": "heartbeat",
            "status": self._get_status(),
            "interval": int(self.interval * 1000)  # 转换回毫秒
        }
    
    def _get_status(self) -> Dict[str, Any]:
        """
        获取运行状态
        
        Returns:
            状态信息字典
        """
        # 这里可以添加更多状态信息
        status = {
            "online": self.bot.is_running,
            "good": self.bot.is_running
        }
        
        # 添加插件统计
        if hasattr(self.bot, 'plugin_manager'):
            plugin_count = len(self.bot.plugin_manager.get_all_plugins())
            status["plugin_count"] = plugin_count
        
        # 添加适配器统计
        if hasattr(self.bot, 'adapters'):
            status["adapter_count"] = len(self.bot.adapters)
        
        return status
    
    @property
    def is_running(self) -> bool:
        """心跳是否正在运行"""
        return self._is_running


__all__ = ['HeartbeatManager']


"""
插件系统 - 优化版

支持:
- 插件热加载/重载/卸载
- 插件启用/禁用状态管理
- 实时导入新插件
- 完整的操作结果返回（适合 Web API）
- 插件依赖管理
- 批量操作
"""

from typing import Dict, List, Callable, Any, Optional, Set, Tuple
from dataclasses import dataclass, field, asdict
from pathlib import Path
from enum import Enum
import importlib
import importlib.util
import inspect
import yaml
from loguru import logger
from datetime import datetime

from .event import Event, MessageEvent, NoticeEvent, RequestEvent


class PluginStatus(Enum):
    """插件状态枚举"""
    LOADED = "loaded"        # 已加载
    ENABLED = "enabled"      # 已启用
    DISABLED = "disabled"    # 已禁用
    ERROR = "error"          # 错误状态
    UNLOADED = "unloaded"    # 已卸载


@dataclass
class PluginOperationResult:
    """插件操作结果"""
    success: bool
    plugin_name: str
    operation: str  # load, reload, unload, enable, disable
    message: str = ""
    error: Optional[str] = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return asdict(self)


@dataclass
class PluginMetadata:
    """插件元数据"""
    name: str
    """插件名称"""
    
    description: str = ""
    """插件描述"""
    
    usage: str = ""
    """使用方法"""
    
    version: str = "1.0.0"
    """版本号"""
    
    author: str = ""
    """作者"""
    
    commands: List[str] = field(default_factory=list)
    """支持的命令列表"""
    
    extra: Dict[str, Any] = field(default_factory=dict)
    """额外信息"""
    
    @classmethod
    def from_yaml(cls, yaml_file: Path) -> 'PluginMetadata':
        """
        从 YAML 文件加载元数据
        
        Args:
            yaml_file: metadata.yaml 文件路径
            
        Returns:
            PluginMetadata 实例
        """
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        return cls(
            name=data.get('name', '未命名插件'),
            description=data.get('description', ''),
            usage=data.get('usage', ''),
            version=data.get('version', '1.0.0'),
            author=data.get('author', ''),
            commands=data.get('commands', []),
            extra=data.get('extra', {})
        )


class Plugin:
    """插件基类"""
    
    # 插件元数据
    metadata: PluginMetadata = PluginMetadata(name="未命名插件")
    
    def __init__(self):
        """初始化插件"""
        pass
    
    async def on_load(self):
        """插件加载时调用"""
        pass
    
    async def on_unload(self):
        """插件卸载时调用"""
        pass
    
    def get_help(self) -> str:
        """获取帮助信息"""
        help_text = f"【{self.metadata.name}】\n"
        if self.metadata.description:
            help_text += f"{self.metadata.description}\n"
        if self.metadata.usage:
            help_text += f"\n使用方法：\n{self.metadata.usage}\n"
        if self.metadata.commands:
            help_text += f"\n支持的命令：\n" + "\n".join(f"  - {cmd}" for cmd in self.metadata.commands)
        return help_text


@dataclass
class Handler:
    """事件处理器"""
    func: Callable
    plugin_name: str
    priority: int = 50
    block: bool = False
    
    async def __call__(self, bot: 'Bot', event: Event) -> bool:
        """
        调用处理器
        
        Returns:
            是否阻止后续处理器执行
        """
        try:
            result = self.func(bot, event)
            # 支持同步和异步函数
            if inspect.iscoroutine(result):
                await result
            return self.block
        except Exception as e:
            logger.exception(f"插件 {self.plugin_name} 处理事件时发生错误: {e}")
            return False


class PluginManager:
    """插件管理器"""
    
    def __init__(self):
        self.plugins: Dict[str, Plugin] = {}
        self.plugin_modules: Dict[str, Any] = {}
        
        # 事件处理器
        self.message_handlers: List[Handler] = []
        self.notice_handlers: List[Handler] = []
        self.request_handlers: List[Handler] = []
        self.command_handlers: Dict[str, Handler] = {}
        
        # 当前加载的插件名称（用于装饰器）
        self._current_plugin_name: Optional[str] = None
        
        # 插件状态管理
        self._disabled_plugins: Set[str] = set()  # 已禁用的插件
        self._plugin_dirs: List[str] = ["plugins"]  # 插件目录列表
        self._plugin_status: Dict[str, PluginStatus] = {}  # 插件状态映射
        self._plugin_load_time: Dict[str, str] = {}  # 插件加载时间
        self._plugin_errors: Dict[str, str] = {}  # 插件错误信息
        
        # 热加载配置
        self.hot_reload_enabled = True  # 热加载开关
        self.auto_reload = False  # 自动重载（文件监控）
        
        # 操作历史
        self._operation_history: List[PluginOperationResult] = []
        self._max_history = 100  # 最多保留 100 条历史
    
    def load_plugin_from_dir(self, plugin_dir: Path, plugin_name: str = None) -> bool:
        """
        从文件夹加载插件（新格式）
        
        插件文件夹结构：
        plugin_name/
            main.py           # 插件代码
            metadata.yaml     # 元数据
            README.md         # 说明文档（可选）
        
        Args:
            plugin_dir: 插件文件夹路径
            plugin_name: 插件名称，如果为 None 则使用文件夹名
            
        Returns:
            是否加载成功
        """
        if plugin_name is None:
            plugin_name = plugin_dir.name
        
        try:
            # 检查必需文件
            main_file = plugin_dir / "main.py"
            metadata_file = plugin_dir / "metadata.yaml"
            
            if not main_file.exists():
                logger.warning(f"插件 {plugin_name} 缺少 main.py")
                return False
            
            # 设置当前插件名称
            self._current_plugin_name = plugin_name
            
            # 动态导入模块
            spec = importlib.util.spec_from_file_location(f"plugins.{plugin_name}.main", main_file)
            module = importlib.util.module_from_spec(spec)
            self.plugin_modules[plugin_name] = module
            spec.loader.exec_module(module)
            
            # 查找插件类
            plugin_instance = None
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, Plugin) and obj != Plugin:
                    plugin_instance = obj()
                    break
            
            if not plugin_instance:
                logger.warning(f"插件 {plugin_name} 的 main.py 中未找到 Plugin 子类")
                return False
            
            # 加载元数据（如果存在 metadata.yaml）
            if metadata_file.exists():
                try:
                    plugin_instance.metadata = PluginMetadata.from_yaml(metadata_file)
                    logger.debug(f"从 metadata.yaml 加载元数据: {plugin_name}")
                except Exception as e:
                    logger.warning(f"加载插件 {plugin_name} 的 metadata.yaml 失败: {e}")
            
            self.plugins[plugin_name] = plugin_instance
            self._plugin_status[plugin_name] = PluginStatus.LOADED
            self._plugin_load_time[plugin_name] = datetime.now().isoformat()
            logger.success(f"加载插件: {plugin_name} ({plugin_instance.metadata.name})")
            return True
                
        except Exception as e:
            logger.error(f"加载插件 {plugin_name} 失败: {e}")
            logger.exception(e)
            return False
        finally:
            self._current_plugin_name = None
    
    def load_plugin_from_file(self, file_path: Path, plugin_name: str = None) -> bool:
        """
        从单文件加载插件（兼容旧格式）
        
        Args:
            file_path: 插件文件路径
            plugin_name: 插件名称，如果为 None 则使用文件名
            
        Returns:
            是否加载成功
        """
        if plugin_name is None:
            plugin_name = file_path.stem
        
        try:
            # 设置当前插件名称
            self._current_plugin_name = plugin_name
            
            # 动态导入模块
            spec = importlib.util.spec_from_file_location(plugin_name, file_path)
            module = importlib.util.module_from_spec(spec)
            self.plugin_modules[plugin_name] = module
            spec.loader.exec_module(module)
            
            # 查找插件类
            plugin_instance = None
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, Plugin) and obj != Plugin:
                    plugin_instance = obj()
                    break
            
            if plugin_instance:
                self.plugins[plugin_name] = plugin_instance
                logger.success(f"加载插件: {plugin_name} ({plugin_instance.metadata.name}) [单文件模式]")
                return True
            else:
                logger.warning(f"插件文件 {file_path} 中未找到 Plugin 子类")
                return False
                
        except Exception as e:
            logger.error(f"加载插件 {plugin_name} 失败: {e}")
            logger.exception(e)
            return False
        finally:
            self._current_plugin_name = None
    
    def load_plugins_from_dir(self, plugin_dir: str, enabled_plugins: List[str] = None,
                             disabled_plugins: List[str] = None) -> int:
        """
        从目录加载插件（支持新旧格式）
        
        新格式（推荐）：
            plugins/
                echo/
                    main.py
                    metadata.yaml
                    README.md
        
        旧格式（兼容）：
            plugins/
                echo.py
        
        Args:
            plugin_dir: 插件目录
            enabled_plugins: 启用的插件列表，为空则加载所有
            disabled_plugins: 禁用的插件列表
            
        Returns:
            成功加载的插件数量
        """
        plugin_path = Path(plugin_dir)
        if not plugin_path.exists():
            logger.warning(f"插件目录不存在: {plugin_dir}")
            return 0
        
        disabled_plugins = disabled_plugins or []
        count = 0
        
        # 1. 加载文件夹式插件（新格式）
        for item in plugin_path.iterdir():
            if not item.is_dir() or item.name.startswith("_"):
                continue
            
            plugin_name = item.name
            
            # 检查是否禁用
            if plugin_name in disabled_plugins:
                logger.info(f"跳过已禁用的插件: {plugin_name}")
                continue
            
            # 检查是否在启用列表中
            if enabled_plugins and plugin_name not in enabled_plugins:
                logger.info(f"跳过未启用的插件: {plugin_name}")
                continue
            
            if self.load_plugin_from_dir(item, plugin_name):
                count += 1
        
        # 2. 加载单文件插件（旧格式，兼容）
        for file in plugin_path.glob("*.py"):
            if file.stem.startswith("_"):
                continue
            
            plugin_name = file.stem
            
            # 检查是否禁用
            if plugin_name in disabled_plugins:
                logger.info(f"跳过已禁用的插件: {plugin_name}")
                continue
            
            # 检查是否在启用列表中
            if enabled_plugins and plugin_name not in enabled_plugins:
                logger.info(f"跳过未启用的插件: {plugin_name}")
                continue
            
            if self.load_plugin_from_file(file, plugin_name):
                count += 1
        
        return count
    
    async def initialize_plugins(self):
        """初始化所有插件"""
        for name, plugin in self.plugins.items():
            try:
                await plugin.on_load()
            except Exception as e:
                logger.error(f"插件 {name} 初始化失败: {e}")
    
    async def cleanup_plugins(self):
        """清理所有插件"""
        for name, plugin in self.plugins.items():
            try:
                await plugin.on_unload()
            except Exception as e:
                logger.error(f"插件 {name} 清理失败: {e}")
    
    def register_handler(self, event_type: str, handler: Handler):
        """注册事件处理器"""
        if event_type == "message":
            self.message_handlers.append(handler)
            self.message_handlers.sort(key=lambda h: h.priority, reverse=True)
        elif event_type == "notice":
            self.notice_handlers.append(handler)
            self.notice_handlers.sort(key=lambda h: h.priority, reverse=True)
        elif event_type == "request":
            self.request_handlers.append(handler)
            self.request_handlers.sort(key=lambda h: h.priority, reverse=True)
    
    def register_command_handler(self, command: str, handler: Handler):
        """注册命令处理器"""
        self.command_handlers[command] = handler
    
    def get_plugin(self, name: str) -> Optional[Plugin]:
        """获取插件实例"""
        return self.plugins.get(name)
    
    def get_all_plugins(self) -> Dict[str, Plugin]:
        """获取所有插件"""
        return self.plugins
    
    def get_help_info(self) -> str:
        """获取所有插件的帮助信息"""
        if not self.plugins:
            return "暂无可用插件"
        
        help_text = "=== 插件列表 ===\n\n"
        for name, plugin in self.plugins.items():
            help_text += f"{plugin.get_help()}\n\n"
        return help_text.strip()
    
    def _add_operation_history(self, result: PluginOperationResult):
        """添加操作历史"""
        self._operation_history.append(result)
        if len(self._operation_history) > self._max_history:
            self._operation_history.pop(0)
    
    async def reload_plugin(self, plugin_name: str) -> PluginOperationResult:
        """
        重新加载单个插件（热加载）- Web API 友好
        
        Args:
            plugin_name: 插件名称
            
        Returns:
            PluginOperationResult 操作结果对象
        """
        if plugin_name not in self.plugins:
            result = PluginOperationResult(
                success=False,
                plugin_name=plugin_name,
                operation="reload",
                message="插件不存在",
                error="Plugin not found"
            )
            self._add_operation_history(result)
            logger.warning(f"插件 {plugin_name} 不存在，无法重新加载")
            return result
        
        try:
            # 1. 先保存模块引用（在卸载前）
            old_module = self.plugin_modules.get(plugin_name)
            
            # 2. 卸载插件（移除处理器，但保留模块引用）
            logger.info(f"正在卸载插件: {plugin_name}")
            if plugin_name in self.plugins:
                plugin = self.plugins[plugin_name]
                await plugin.on_unload()
                
                # 移除事件处理器
                self.message_handlers = [h for h in self.message_handlers if h.plugin_name != plugin_name]
                self.notice_handlers = [h for h in self.notice_handlers if h.plugin_name != plugin_name]
                self.request_handlers = [h for h in self.request_handlers if h.plugin_name != plugin_name]
                self.command_handlers = {k: v for k, v in self.command_handlers.items() if v.plugin_name != plugin_name}
                
                # 移除插件实例
                del self.plugins[plugin_name]
            
            # 3. 重新导入模块
            if old_module:
                import importlib
                import sys
                # 先从 sys.modules 中删除所有相关模块
                modules_to_remove = [k for k in sys.modules.keys() if k.startswith(f'plugins.{plugin_name}')]
                for mod_name in modules_to_remove:
                    del sys.modules[mod_name]
                logger.debug(f"清理了 {len(modules_to_remove)} 个相关模块")
            
            # 4. 重新加载插件
            logger.info(f"正在重新加载插件: {plugin_name}")
            
            # 查找插件文件/目录
            from pathlib import Path
            import sys
            
            for plugin_dir in ["plugins", "examples"]:  # 可以扩展更多目录
                plugin_path = Path(plugin_dir)
                if not plugin_path.exists():
                    continue
                
                # 检查文件夹式插件
                folder_path = plugin_path / plugin_name
                if folder_path.is_dir() and (folder_path / "main.py").exists():
                    success = self.load_plugin_from_dir(folder_path, plugin_name)
                    if success:
                        await self.plugins[plugin_name].on_load()
                        self._plugin_status[plugin_name] = PluginStatus.ENABLED
                        self._plugin_load_time[plugin_name] = datetime.now().isoformat()
                        result = PluginOperationResult(
                            success=True,
                            plugin_name=plugin_name,
                            operation="reload",
                            message=f"插件 {plugin_name} 重新加载成功"
                        )
                        self._add_operation_history(result)
                        logger.success(f"插件 {plugin_name} 重新加载成功")
                        return result
                
                # 检查单文件插件
                file_path = plugin_path / f"{plugin_name}.py"
                if file_path.is_file():
                    success = self.load_plugin_from_file(file_path, plugin_name)
                    if success:
                        await self.plugins[plugin_name].on_load()
                        self._plugin_status[plugin_name] = PluginStatus.ENABLED
                        self._plugin_load_time[plugin_name] = datetime.now().isoformat()
                        result = PluginOperationResult(
                            success=True,
                            plugin_name=plugin_name,
                            operation="reload",
                            message=f"插件 {plugin_name} 重新加载成功"
                        )
                        self._add_operation_history(result)
                        logger.success(f"插件 {plugin_name} 重新加载成功")
                        return result
            
            result = PluginOperationResult(
                success=False,
                plugin_name=plugin_name,
                operation="reload",
                message="未找到插件文件",
                error=f"Plugin file not found: {plugin_name}"
            )
            self._add_operation_history(result)
            logger.error(f"未找到插件文件: {plugin_name}")
            return result
            
        except Exception as e:
            error_msg = str(e)
            result = PluginOperationResult(
                success=False,
                plugin_name=plugin_name,
                operation="reload",
                message="重新加载失败",
                error=error_msg
            )
            self._add_operation_history(result)
            self._plugin_status[plugin_name] = PluginStatus.ERROR
            self._plugin_errors[plugin_name] = error_msg
            logger.error(f"重新加载插件 {plugin_name} 失败: {e}")
            logger.exception(e)
            return result
    
    async def unload_plugin(self, plugin_name: str) -> PluginOperationResult:
        """
        卸载单个插件 - Web API 友好
        
        Args:
            plugin_name: 插件名称
            
        Returns:
            PluginOperationResult 操作结果对象
        """
        if plugin_name not in self.plugins:
            result = PluginOperationResult(
                success=False,
                plugin_name=plugin_name,
                operation="unload",
                message="插件不存在",
                error="Plugin not found"
            )
            self._add_operation_history(result)
            logger.warning(f"插件 {plugin_name} 不存在")
            return result
        
        try:
            # 调用插件的卸载钩子
            plugin = self.plugins[plugin_name]
            await plugin.on_unload()
            
            # 移除该插件的所有事件处理器
            self.message_handlers = [h for h in self.message_handlers if h.plugin_name != plugin_name]
            self.notice_handlers = [h for h in self.notice_handlers if h.plugin_name != plugin_name]
            self.request_handlers = [h for h in self.request_handlers if h.plugin_name != plugin_name]
            self.command_handlers = {k: v for k, v in self.command_handlers.items() if v.plugin_name != plugin_name}
            
            # 移除插件实例
            del self.plugins[plugin_name]
            
            # 更新状态
            self._plugin_status[plugin_name] = PluginStatus.UNLOADED
            self._plugin_errors.pop(plugin_name, None)
            
            result = PluginOperationResult(
                success=True,
                plugin_name=plugin_name,
                operation="unload",
                message=f"插件 {plugin_name} 已卸载"
            )
            self._add_operation_history(result)
            logger.info(f"插件 {plugin_name} 已卸载")
            return result
            
        except Exception as e:
            error_msg = str(e)
            result = PluginOperationResult(
                success=False,
                plugin_name=plugin_name,
                operation="unload",
                message="卸载失败",
                error=error_msg
            )
            self._add_operation_history(result)
            logger.error(f"卸载插件 {plugin_name} 失败: {e}")
            return result
    
    async def reload_all_plugins(self) -> tuple[int, int]:
        """
        重新加载所有插件
        
        Returns:
            (成功数量, 失败数量)
        """
        plugin_names = list(self.plugins.keys())
        success_count = 0
        fail_count = 0
        
        for plugin_name in plugin_names:
            logger.info(f"重新加载插件: {plugin_name}")
            if await self.reload_plugin(plugin_name):
                success_count += 1
            else:
                fail_count += 1
        
        logger.info(f"插件重新加载完成: 成功 {success_count}, 失败 {fail_count}")
        return success_count, fail_count
    
    def list_plugins(self) -> List[Dict[str, Any]]:
        """
        获取插件列表信息
        
        Returns:
            插件信息列表
        """
        plugin_list = []
        for name, plugin in self.plugins.items():
            info = {
                "name": name,
                "display_name": plugin.metadata.name,
                "description": plugin.metadata.description,
                "version": plugin.metadata.version,
                "author": plugin.metadata.author,
                "commands": plugin.metadata.commands,
                "category": plugin.metadata.extra.get("category", "其他"),
                "enabled": name not in self._disabled_plugins
            }
            plugin_list.append(info)
        return plugin_list
    
    def enable_plugin(self, plugin_name: str) -> PluginOperationResult:
        """
        启用插件（不重新加载，只是恢复处理器）- Web API 友好
        
        Args:
            plugin_name: 插件名称
            
        Returns:
            PluginOperationResult 操作结果对象
        """
        if plugin_name not in self.plugins:
            result = PluginOperationResult(
                success=False,
                plugin_name=plugin_name,
                operation="enable",
                message="插件不存在",
                error="Plugin not found"
            )
            self._add_operation_history(result)
            logger.warning(f"插件 {plugin_name} 不存在")
            return result
        
        if plugin_name not in self._disabled_plugins:
            result = PluginOperationResult(
                success=True,
                plugin_name=plugin_name,
                operation="enable",
                message="插件已经是启用状态"
            )
            logger.info(f"插件 {plugin_name} 已经是启用状态")
            return result
        
        self._disabled_plugins.remove(plugin_name)
        self._plugin_status[plugin_name] = PluginStatus.ENABLED
        result = PluginOperationResult(
            success=True,
            plugin_name=plugin_name,
            operation="enable",
            message=f"插件 {plugin_name} 已启用"
        )
        self._add_operation_history(result)
        logger.success(f"插件 {plugin_name} 已启用")
        return result
    
    def disable_plugin(self, plugin_name: str) -> PluginOperationResult:
        """
        禁用插件（不卸载，只是暂停处理事件）- Web API 友好
        
        Args:
            plugin_name: 插件名称
            
        Returns:
            PluginOperationResult 操作结果对象
        """
        if plugin_name not in self.plugins:
            result = PluginOperationResult(
                success=False,
                plugin_name=plugin_name,
                operation="disable",
                message="插件不存在",
                error="Plugin not found"
            )
            self._add_operation_history(result)
            logger.warning(f"插件 {plugin_name} 不存在")
            return result
        
        if plugin_name in self._disabled_plugins:
            result = PluginOperationResult(
                success=True,
                plugin_name=plugin_name,
                operation="disable",
                message="插件已经是禁用状态"
            )
            logger.info(f"插件 {plugin_name} 已经是禁用状态")
            return result
        
        self._disabled_plugins.add(plugin_name)
        self._plugin_status[plugin_name] = PluginStatus.DISABLED
        result = PluginOperationResult(
            success=True,
            plugin_name=plugin_name,
            operation="disable",
            message=f"插件 {plugin_name} 已禁用"
        )
        self._add_operation_history(result)
        logger.success(f"插件 {plugin_name} 已禁用（可通过 enable_plugin 恢复）")
        return result
    
    async def load_new_plugin(self, plugin_name: str, plugin_dir: str = "plugins") -> PluginOperationResult:
        """
        动态加载新插件（实时导入）- Web API 友好
        
        Args:
            plugin_name: 插件名称
            plugin_dir: 插件目录
            
        Returns:
            PluginOperationResult 操作结果对象
        """
        if plugin_name in self.plugins:
            result = PluginOperationResult(
                success=False,
                plugin_name=plugin_name,
                operation="load",
                message="插件已存在，请使用重载功能",
                error="Plugin already exists"
            )
            self._add_operation_history(result)
            logger.warning(f"插件 {plugin_name} 已存在，请使用 reload_plugin 重新加载")
            return result
        
        try:
            plugin_path = Path(plugin_dir)
            
            # 检查文件夹式插件
            folder_path = plugin_path / plugin_name
            if folder_path.is_dir() and (folder_path / "main.py").exists():
                success = self.load_plugin_from_dir(folder_path, plugin_name)
                if success:
                    await self.plugins[plugin_name].on_load()
                    self._plugin_status[plugin_name] = PluginStatus.ENABLED
                    self._plugin_load_time[plugin_name] = datetime.now().isoformat()
                    result = PluginOperationResult(
                        success=True,
                        plugin_name=plugin_name,
                        operation="load",
                        message=f"新插件 {plugin_name} 加载成功"
                    )
                    self._add_operation_history(result)
                    logger.success(f"✅ 新插件 {plugin_name} 加载成功")
                    return result
            
            # 检查单文件插件
            file_path = plugin_path / f"{plugin_name}.py"
            if file_path.is_file():
                success = self.load_plugin_from_file(file_path, plugin_name)
                if success:
                    await self.plugins[plugin_name].on_load()
                    self._plugin_status[plugin_name] = PluginStatus.ENABLED
                    self._plugin_load_time[plugin_name] = datetime.now().isoformat()
                    result = PluginOperationResult(
                        success=True,
                        plugin_name=plugin_name,
                        operation="load",
                        message=f"新插件 {plugin_name} 加载成功"
                    )
                    self._add_operation_history(result)
                    logger.success(f"✅ 新插件 {plugin_name} 加载成功")
                    return result
            
            result = PluginOperationResult(
                success=False,
                plugin_name=plugin_name,
                operation="load",
                message="未找到插件文件",
                error=f"Plugin file not found: {plugin_name}"
            )
            self._add_operation_history(result)
            logger.error(f"未找到插件: {plugin_name}")
            return result
            
        except Exception as e:
            error_msg = str(e)
            result = PluginOperationResult(
                success=False,
                plugin_name=plugin_name,
                operation="load",
                message="加载失败",
                error=error_msg
            )
            self._add_operation_history(result)
            logger.error(f"加载新插件 {plugin_name} 失败: {e}")
            logger.exception(e)
            return result
    
    async def scan_and_load_new_plugins(self) -> int:
        """
        扫描并加载所有新插件（实时导入）
        
        Returns:
            新加载的插件数量
        """
        loaded_count = 0
        
        for plugin_dir in self._plugin_dirs:
            plugin_path = Path(plugin_dir)
            if not plugin_path.exists():
                continue
            
            # 扫描文件夹式插件
            for item in plugin_path.iterdir():
                if item.is_dir() and not item.name.startswith("_"):
                    plugin_name = item.name
                    if plugin_name not in self.plugins:
                        if await self.load_new_plugin(plugin_name, plugin_dir):
                            loaded_count += 1
            
            # 扫描单文件插件
            for file in plugin_path.glob("*.py"):
                if not file.stem.startswith("_"):
                    plugin_name = file.stem
                    if plugin_name not in self.plugins:
                        if await self.load_new_plugin(plugin_name, plugin_dir):
                            loaded_count += 1
        
        if loaded_count > 0:
            logger.success(f"扫描完成，新加载了 {loaded_count} 个插件")
        else:
            logger.info("扫描完成，没有发现新插件")
        
        return loaded_count
    
    def set_hot_reload_enabled(self, enabled: bool):
        """
        设置热加载开关
        
        Args:
            enabled: 是否启用热加载
        """
        self.hot_reload_enabled = enabled
        status = "启用" if enabled else "禁用"
        logger.info(f"热加载功能已{status}")
    
    def is_plugin_enabled(self, plugin_name: str) -> bool:
        """
        检查插件是否启用
        
        Args:
            plugin_name: 插件名称
            
        Returns:
            是否启用
        """
        return plugin_name not in self._disabled_plugins
    
    def get_plugin_stats(self) -> Dict[str, Any]:
        """
        获取插件统计信息 - Web API 友好
        
        Returns:
            统计信息字典
        """
        total = len(self.plugins)
        enabled = len([p for p in self.plugins.keys() if p not in self._disabled_plugins])
        disabled = total - enabled
        error = len([p for p, s in self._plugin_status.items() if s == PluginStatus.ERROR])
        
        return {
            "total": total,
            "enabled": enabled,
            "disabled": disabled,
            "error": error,
            "message_handlers": len(self.message_handlers),
            "notice_handlers": len(self.notice_handlers),
            "request_handlers": len(self.request_handlers),
            "command_handlers": len(self.command_handlers),
            "hot_reload_enabled": self.hot_reload_enabled
        }
    
    def get_plugin_detail(self, plugin_name: str) -> Optional[Dict[str, Any]]:
        """
        获取插件详细信息 - Web API 友好
        
        Args:
            plugin_name: 插件名称
            
        Returns:
            插件详细信息字典，不存在返回 None
        """
        if plugin_name not in self.plugins:
            return None
        
        plugin = self.plugins[plugin_name]
        meta = plugin.metadata
        
        # 统计该插件的处理器数量
        msg_handlers = len([h for h in self.message_handlers if h.plugin_name == plugin_name])
        notice_handlers = len([h for h in self.notice_handlers if h.plugin_name == plugin_name])
        request_handlers = len([h for h in self.request_handlers if h.plugin_name == plugin_name])
        cmd_handlers = len([k for k, v in self.command_handlers.items() if v.plugin_name == plugin_name])
        
        return {
            "name": plugin_name,
            "display_name": meta.name,
            "description": meta.description,
            "version": meta.version,
            "author": meta.author,
            "commands": meta.commands,
            "usage": meta.usage,
            "category": meta.extra.get("category", "其他"),
            "extra": meta.extra,
            "status": self._plugin_status.get(plugin_name, PluginStatus.LOADED).value,
            "enabled": plugin_name not in self._disabled_plugins,
            "load_time": self._plugin_load_time.get(plugin_name),
            "error": self._plugin_errors.get(plugin_name),
            "handlers": {
                "message": msg_handlers,
                "notice": notice_handlers,
                "request": request_handlers,
                "command": cmd_handlers,
                "total": msg_handlers + notice_handlers + request_handlers + cmd_handlers
            }
        }
    
    def get_all_plugins_detail(self) -> List[Dict[str, Any]]:
        """
        获取所有插件的详细信息 - Web API 友好
        
        Returns:
            插件详细信息列表
        """
        plugins_detail = []
        for plugin_name in self.plugins.keys():
            detail = self.get_plugin_detail(plugin_name)
            if detail:
                plugins_detail.append(detail)
        return plugins_detail
    
    def get_operation_history(self, limit: int = 20) -> List[Dict[str, Any]]:
        """
        获取操作历史 - Web API 友好
        
        Args:
            limit: 返回的历史记录数量
            
        Returns:
            操作历史列表
        """
        history = self._operation_history[-limit:]
        return [r.to_dict() for r in reversed(history)]
    
    async def batch_enable_plugins(self, plugin_names: List[str]) -> List[PluginOperationResult]:
        """
        批量启用插件 - Web API 友好
        
        Args:
            plugin_names: 插件名称列表
            
        Returns:
            操作结果列表
        """
        results = []
        for plugin_name in plugin_names:
            result = self.enable_plugin(plugin_name)
            results.append(result)
        return results
    
    async def batch_disable_plugins(self, plugin_names: List[str]) -> List[PluginOperationResult]:
        """
        批量禁用插件 - Web API 友好
        
        Args:
            plugin_names: 插件名称列表
            
        Returns:
            操作结果列表
        """
        results = []
        for plugin_name in plugin_names:
            result = self.disable_plugin(plugin_name)
            results.append(result)
        return results
    
    async def batch_reload_plugins(self, plugin_names: List[str]) -> List[PluginOperationResult]:
        """
        批量重载插件 - Web API 友好
        
        Args:
            plugin_names: 插件名称列表
            
        Returns:
            操作结果列表
        """
        results = []
        for plugin_name in plugin_names:
            result = await self.reload_plugin(plugin_name)
            results.append(result)
        return results
    
    def search_plugins(self, keyword: str = "", category: str = "", enabled_only: bool = False) -> List[Dict[str, Any]]:
        """
        搜索插件 - Web API 友好
        
        Args:
            keyword: 关键词（搜索名称、描述、命令）
            category: 分类筛选
            enabled_only: 只返回启用的插件
            
        Returns:
            匹配的插件列表
        """
        results = []
        
        for plugin_name, plugin in self.plugins.items():
            # 启用状态过滤
            if enabled_only and plugin_name in self._disabled_plugins:
                continue
            
            meta = plugin.metadata
            
            # 分类过滤
            if category and meta.extra.get("category", "") != category:
                continue
            
            # 关键词搜索
            if keyword:
                search_text = f"{meta.name} {meta.description} {' '.join(meta.commands)}".lower()
                if keyword.lower() not in search_text:
                    continue
            
            detail = self.get_plugin_detail(plugin_name)
            if detail:
                results.append(detail)
        
        return results
    
    def get_plugin_categories(self) -> List[str]:
        """
        获取所有插件分类 - Web API 友好
        
        Returns:
            分类列表
        """
        categories = set()
        for plugin in self.plugins.values():
            category = plugin.metadata.extra.get("category", "其他")
            categories.add(category)
        return sorted(list(categories))
    
    async def handle_event(self, bot: 'Bot', event: Event) -> bool:
        """
        处理事件（支持插件启用/禁用）
        
        Returns:
            是否被处理
        """
        # 选择对应的处理器列表
        if isinstance(event, MessageEvent):
            handlers = self.message_handlers
            
            # 获取消息文本（去除 CQ 码）
            message_text = event.get_message_text().strip()
            
            # 如果消息是字符串且包含 CQ 码，解析它
            if isinstance(event.message, str) and '[CQ:' in event.message:
                # 使用 raw_message 作为纯文本
                message_text = event.raw_message.strip() if event.raw_message else message_text
                logger.debug(f"消息包含 CQ 码，使用 raw_message: {message_text}")
            
            # 检查是否为命令
            for command, handler in self.command_handlers.items():
                if message_text.startswith(command):
                    # 检查插件是否被禁用
                    if handler.plugin_name in self._disabled_plugins:
                        logger.debug(f"插件 {handler.plugin_name} 已禁用，跳过命令 {command}")
                        continue
                    
                    # 设置命令参数
                    event.command = command
                    event.args = message_text[len(command):].strip()
                    
                    logger.debug(f"🎯 识别命令: {command}, 参数: {event.args}")
                    
                    try:
                        await handler(bot, event)
                        return True
                    except Exception as e:
                        logger.exception(f"命令处理器异常: {e}")
                        return False
        elif isinstance(event, NoticeEvent):
            handlers = self.notice_handlers
        elif isinstance(event, RequestEvent):
            handlers = self.request_handlers
        else:
            return False
        
        # 执行处理器（跳过禁用的插件）
        for handler in handlers:
            # 检查插件是否被禁用
            if handler.plugin_name in self._disabled_plugins:
                continue
            
            try:
                should_block = await handler(bot, event)
                if should_block:
                    return True
            except Exception as e:
                logger.exception(f"事件处理器异常: {e}")
        
        return False


# 全局插件管理器实例
_plugin_manager: Optional[PluginManager] = None


def get_plugin_manager() -> PluginManager:
    """获取全局插件管理器"""
    global _plugin_manager
    if _plugin_manager is None:
        _plugin_manager = PluginManager()
    return _plugin_manager


# ==================== 装饰器 ====================

def on_message(priority: int = 50, block: bool = False):
    """
    消息事件装饰器
    
    Args:
        priority: 优先级，越大越先执行
        block: 是否阻止后续处理器执行
    """
    def decorator(func: Callable):
        manager = get_plugin_manager()
        handler = Handler(
            func=func,
            plugin_name=manager._current_plugin_name or "unknown",
            priority=priority,
            block=block
        )
        manager.register_handler("message", handler)
        return func
    return decorator


def on_notice(priority: int = 50, block: bool = False):
    """
    通知事件装饰器
    
    Args:
        priority: 优先级，越大越先执行
        block: 是否阻止后续处理器执行
    """
    def decorator(func: Callable):
        manager = get_plugin_manager()
        handler = Handler(
            func=func,
            plugin_name=manager._current_plugin_name or "unknown",
            priority=priority,
            block=block
        )
        manager.register_handler("notice", handler)
        return func
    return decorator


def on_request(priority: int = 50, block: bool = False):
    """
    请求事件装饰器
    
    Args:
        priority: 优先级，越大越先执行
        block: 是否阻止后续处理器执行
    """
    def decorator(func: Callable):
        manager = get_plugin_manager()
        handler = Handler(
            func=func,
            plugin_name=manager._current_plugin_name or "unknown",
            priority=priority,
            block=block
        )
        manager.register_handler("request", handler)
        return func
    return decorator


def on_command(command: str, priority: int = 50, block: bool = True):
    """
    命令装饰器
    
    Args:
        command: 命令关键字
        priority: 优先级
        block: 是否阻止后续处理器执行
    """
    def decorator(func: Callable):
        manager = get_plugin_manager()
        handler = Handler(
            func=func,
            plugin_name=manager._current_plugin_name or "unknown",
            priority=priority,
            block=block
        )
        manager.register_command_handler(command, handler)
        return func
    return decorator


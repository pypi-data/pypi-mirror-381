# 🏗️ EchoFrame 架构文档

## 架构概述

EchoFrame 是一个轻量级、可扩展的 OneBot-11 机器人框架，采用插件化和中间件设计。

---

## 📊 整体架构

```
┌─────────────────────────────────────────┐
│           EchoFrame 2.0                 │
├─────────────────────────────────────────┤
│                                         │
│  ┌───────────────────────────────────┐ │
│  │   核心层（Core Layer）            │ │
│  ├───────────────────────────────────┤ │
│  │  • Bot 核心                       │ │
│  │  • 插件系统（热加载）             │ │
│  │  • 中间件系统                     │ │
│  │  • 心跳管理                       │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │   包装层（Wrapper Layer）         │ │
│  ├───────────────────────────────────┤ │
│  │  • Message/Event 轻量包装         │ │
│  │  • MS 工厂类                      │ │
│  │  • 扩展方法                       │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │   通信层（Adapter Layer）         │ │
│  ├───────────────────────────────────┤ │
│  │  • AioCQHTTP 适配器（反向）       │ │
│  │  • WebSocket 客户端（正向）       │ │
│  └───────────────────────────────────┘ │
│                  ↓                      │
└──────────────────┼──────────────────────┘
                   ↓
         ┌─────────────────┐
         │   aiocqhttp     │
         │  （底层库）      │
         └─────────────────┘
                   ↓
         ┌─────────────────┐
         │  OneBot 实现    │
         │ (Lagrange等)    │
         └─────────────────┘
```

---

## 🎯 核心模块

### 1. Bot 核心（core/bot.py）

**职责**：
- 管理机器人生命周期
- 协调各个模块
- 提供统一的 API

**主要方法**：
```python
await bot.start()          # 启动
await bot.stop()           # 停止
await bot.send(event, msg) # 发送消息
bot.is_superuser(user_id)  # 权限检查
```

---

### 2. 插件系统（core/plugin.py）

**特色功能**：
- 热加载/热重载
- 启用/禁用
- 实时导入
- Web API 友好

**核心类**：
- `PluginManager` - 插件管理器
- `Plugin` - 插件基类
- `PluginMetadata` - 元数据
- `PluginStatus` - 状态枚举
- `PluginOperationResult` - 操作结果

**装饰器**：
```python
@on_command("/cmd")    # 命令处理
@on_message()          # 消息事件
@on_notice()           # 通知事件
@on_request()          # 请求事件
```

---

### 3. 中间件系统（core/middleware.py）

**职责**：
- 事件处理前后钩子
- 统一的处理流程

**内置中间件**：
- `log_middleware` - 日志和性能
- `auth_middleware` - 权限和黑名单
- `rate_limit_middleware` - 限流防刷
- `error_handler_middleware` - 错误处理

**自定义中间件**：
```python
@middleware(priority=100)
async def my_middleware(bot, event, next):
    # 前置处理
    result = await next()
    # 后置处理
    return result
```

---

### 4. 消息系统（core/message.py）

**轻量级包装**，底层使用 `aiocqhttp.Message`

**MS 工厂类**：
```python
msg = MS.text("文本") + MS.face(14) + MS.image(url)
```

**支持的消息段**：26 种 OneBot-11 标准消息段

---

### 5. 事件系统（core/event.py）

**轻量级包装**，底层使用 `aiocqhttp.Event`

**扩展方法**：
```python
event.is_group()           # 是否群聊
event.is_to_me()           # 是否 @ 机器人
event.get_message_text()   # 获取纯文本
event.has_image()          # 是否有图片
event.get_images()         # 获取图片列表
```

---

## 🔌 通信层

### 适配器模式

支持两种连接模式：

#### 1. AioCQHTTP 适配器（反向）
- 使用 aiocqhttp 库
- EchoFrame 作为服务端
- OneBot 实现连接过来

#### 2. WebSocket 客户端（正向）
- 轻量级实现（~180 行）
- EchoFrame 作为客户端
- 主动连接到 OneBot 实现

---

## 📦 数据流

```
OneBot 实现
    │
    ├─ [事件] ──→ AioCQHTTP/WebSocket 客户端
    │                      ↓
    │              Adapter Layer
    │                      ↓
    │              Event Parsing
    │                      ↓
    │              Middleware Chain
    │                      ↓
    │              Plugin Manager
    │                      ↓
    │              Event Handlers
    │                      ↓
    │              Bot.send()
    │                      ↓
    │              Adapter.call_api()
    │                      ↓
    ├─ [API 调用] ←─ AioCQHTTP/WebSocket 客户端
    │
OneBot 实现
```

---

## 🎯 插件生命周期

```
1. 启动阶段
   └─ load_plugins_from_dir()
      └─ load_plugin_from_dir()
         └─ Plugin.__init__()
            └─ Plugin.on_load()

2. 运行阶段
   ├─ 接收事件
   ├─ 中间件处理
   ├─ 插件处理
   └─ 发送响应

3. 热加载阶段
   └─ reload_plugin()
      ├─ Plugin.on_unload()
      ├─ 清理模块
      ├─ 重新导入
      └─ Plugin.on_load()

4. 停止阶段
   └─ cleanup_plugins()
      └─ Plugin.on_unload()
```

---

## 💡 设计原则

### 1. 分层设计
- 核心层：核心功能
- 包装层：简化 API
- 通信层：底层实现

### 2. 插件化
- 所有功能都可以插件化
- 热加载支持
- 最小依赖

### 3. 可扩展性
- 中间件系统
- 装饰器风格
- Web API 友好

### 4. 轻量级
- 使用成熟的库（aiocqhttp）
- 代码精简（~2700 行）
- 最小依赖

---

## 📈 性能特点

- **异步 I/O** - 高并发
- **事件驱动** - 低延迟
- **连接池** - aiocqhttp 自动管理
- **自动重连** - 网络稳定

---

## 🔧 扩展点

### 1. 自定义适配器

```python
class MyAdapter:
    async def start(self): ...
    async def call_api(self, action, **params): ...
```

### 2. 自定义中间件

```python
@middleware(priority=100)
async def my_middleware(bot, event, next):
    return await next()
```

### 3. 自定义插件

```python
class MyPlugin(Plugin):
    async def on_load(self): ...
    async def on_unload(self): ...
```

---

## 📚 相关文档

- [QUICK_START.md](QUICK_START.md) - 快速开始
- [CONFIG_GUIDE.md](CONFIG_GUIDE.md) - 配置指南
- [PLUGIN_DEVELOPMENT_GUIDE.md](../PLUGIN_DEVELOPMENT_GUIDE.md) - 插件开发

---

**了解 EchoFrame 的架构设计！** 🏗️


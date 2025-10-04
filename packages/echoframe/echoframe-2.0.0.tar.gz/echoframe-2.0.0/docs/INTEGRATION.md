# 🔄 aiocqhttp 集成说明

## 集成概述

EchoFrame 2.0 使用 aiocqhttp 库处理底层通信，大幅精简代码的同时保留所有核心特色功能。

---

## 📊 集成成果

### 代码精简

| 模块 | 集成前 | 集成后 | 减少 |
|------|--------|--------|------|
| WebSocket 通信 | 511 行 | 0 行 | -100% |
| HTTP 通信 | 387 行 | 0 行 | -100% |
| API 调用 | 385 行 | 0 行 | -100% |
| Message 类 | 542 行 | 200 行 | -63% |
| Event 类 | 389 行 | 180 行 | -54% |
| **总计** | **2214 行** | **380 行** | **-82%** |

**净减少：1834 行代码！**

---

## ⭐ 保留的核心功能

### 完整保留
- ✅ 插件热加载系统
- ✅ 中间件系统
- ✅ Web API 管理接口
- ✅ MS 工厂类（简洁 API）
- ✅ Event 扩展方法
- ✅ 详细状态管理
- ✅ 操作历史记录

### 底层使用 aiocqhttp
- ✅ WebSocket 通信
- ✅ HTTP 通信（如需要）
- ✅ API 调用
- ✅ Message/Event 基类

---

## 🏗️ 架构设计

```
EchoFrame 框架
├─ 核心特色（~1800 行）
│  ├─ 插件系统（热加载、Web API）
│  ├─ 中间件系统
│  └─ Bot 核心
│
├─ 轻量包装（~380 行）
│  ├─ MS 工厂类
│  └─ Event 扩展方法
│
├─ aiocqhttp 适配器（~380 行）
│  └─ 事件转发 + API 调用
│
└─ aiocqhttp 库（无需维护）
   ├─ WebSocket 通信
   ├─ HTTP 通信
   └─ Message/Event
```

---

## 💻 使用方式（不变）

### 插件开发

```python
from echoframe import Plugin, on_command, MS

class MyPlugin(Plugin):
    pass

@on_command("/hello")
async def hello(bot, event):
    msg = MS.text("Hello!") + MS.face(14)
    await bot.send(event, msg.to_array())
```

**完全相同的 API！用户无感知！**

---

## 🎯 优势

### 1. 代码量大幅减少
- 82% 的底层代码由库提供
- 专注于核心功能开发

### 2. 稳定性提升
- aiocqhttp 是成熟的库
- 经过大量项目验证

### 3. 维护成本降低
- 通信层交给库维护
- 只需维护核心特色

### 4. 功能不减反增
- 保留所有 EchoFrame 特色
- 获得 aiocqhttp 的稳定性

---

## 📚 技术栈

- **Python** 3.8+
- **aiocqhttp** 1.4.4+ （底层通信）
- **Quart** （Web 框架，aiocqhttp 依赖）
- **pydantic** （数据验证）
- **loguru** （日志）
- **pyyaml** （配置）

---

## 🔗 相关资源

- [aiocqhttp 文档](https://github.com/nonebot/aiocqhttp)
- [OneBot-11 标准](https://github.com/botuniverse/onebot-11)
- [Quart 文档](https://quart.palletsprojects.com/)

---

**通过集成 aiocqhttp，EchoFrame 变得更轻量、更稳定！** 🚀


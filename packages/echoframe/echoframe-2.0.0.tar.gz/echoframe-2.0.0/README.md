# EchoFrame

<div align="center">

```
╔═══════════════════════════════╗
║                               ║
║        EchoFrame 2.0          ║
║                               ║
║   OneBot-11 机器人框架        ║
║                               ║
╚═══════════════════════════════╝
```

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OneBot](https://img.shields.io/badge/OneBot-11-black.svg)](https://github.com/botuniverse/onebot-11)

**轻量级、高性能的 OneBot-11 机器人框架**

[快速开始](#快速开始) · [文档](docs/README.md) · [插件开发](PLUGIN_DEVELOPMENT_GUIDE.md) · [特性](#特性)

</div>

---

## ✨ 特性

- 🔥 **插件热加载** - 修改代码立即生效，无需重启
- 🎨 **中间件系统** - 灵活的事件处理流程
- 🌐 **Web API 友好** - 完善的管理接口，适合 Web 面板
- ⚡ **高性能** - 基于 aiocqhttp，异步架构
- 📦 **可作为库** - `pip install echoframe` 即可使用
- 💬 **完整实现** - 支持所有 OneBot-11 标准
- 🛠️ **简单易用** - 装饰器风格，优雅简洁

---

## 🚀 快速开始

### 安装

```bash
# 作为库安装（推荐）
pip install echoframe

# 或从源码运行
git clone https://github.com/your-repo/echoframe
cd echoframe
pip install -r requirements.txt
```

### 配置

1. 复制配置文件：
   ```bash
   cp config.example.yaml config.yaml
   ```

2. 修改配置：
   ```yaml
   adapters:
     aiocqhttp:
       enabled: true
       port: 6789
       access_token: ""
   
   bot:
     superusers:
       - 123456789  # 你的 QQ 号
   ```

3. 配置 OneBot 实现（如 Lagrange）：
   ```json
   {
       "Type": "ReverseWebSocket",
       "Host": "127.0.0.1",
       "Port": 6789,
       "Suffix": "/ws/"
   }
   ```

### 运行

```bash
python bot.py
```

查看日志确认连接成功！

---

## 💡 创建第一个插件

**plugins/hello/main.py**:
```python
from echoframe import Plugin, on_command, MS

class HelloPlugin(Plugin):
    pass

@on_command("/hello")
async def hello(bot, event):
    msg = MS.text("Hello from EchoFrame!") + MS.face(14)
    await bot.send(event, msg.to_array())
```

**plugins/hello/metadata.yaml**:
```yaml
name: "Hello 插件"
commands:
  - "/hello"
```

重启或热加载，然后在 QQ 中发送 `/hello` 测试！

---

## 📚 文档

- 📖 [文档中心](docs/README.md) - 所有文档索引
- 🚀 [快速开始](docs/QUICK_START.md) - 5分钟上手
- 📝 [插件开发指南](PLUGIN_DEVELOPMENT_GUIDE.md) - 完整教程
- ⚙️ [配置指南](docs/CONFIG_GUIDE.md) - 详细配置
- ❓ [FAQ](docs/FAQ.md) - 常见问题
- 🏗️ [架构文档](docs/ARCHITECTURE.md) - 设计说明

---

## 🎯 核心功能

### 插件系统
- 热加载/热重载 - 修改代码立即生效
- 启用/禁用控制
- 实时导入新插件
- Web API 管理接口

### 中间件系统
- 灵活的事件处理流程
- 内置常用中间件
- 自定义中间件支持

### 消息系统
- 26 种消息段类型
- MS 工厂类（简洁 API）
- 完整的 CQ 码支持

### 通信层
- 基于 aiocqhttp
- WebSocket 双向通信
- 自动重连

---

## 📊 性能

- **代码量**：~2700 行（精简 82%）
- **启动速度**：< 1 秒
- **消息延迟**：~10-30ms
- **内存占用**：< 100MB

---

## 🛠️ 技术栈

- Python 3.8+
- aiocqhttp 1.4.4+
- Pydantic 2.0+
- Loguru 0.7+

---

## 📄 许可证

[MIT License](LICENSE)

---

## 🙏 鸣谢

- [OneBot-11 标准](https://github.com/botuniverse/onebot-11)
- [aiocqhttp](https://github.com/nonebot/aiocqhttp)
- [Lagrange.OneBot](https://github.com/LagrangeDev/Lagrange.Core)
- 所有贡献者

---

<div align="center">

**开始使用 EchoFrame！** 🚀

`pip install echoframe`

[快速开始](docs/QUICK_START.md) · [插件开发](PLUGIN_DEVELOPMENT_GUIDE.md) · [文档](docs/README.md)

</div>

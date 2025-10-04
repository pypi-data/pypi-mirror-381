# 🚀 EchoFrame 快速开始

## 5 分钟上手指南

---

## 📦 安装

### 方式 A：作为库使用（推荐）

```bash
pip install echoframe
```

### 方式 B：从源码使用

```bash
git clone https://github.com/your-repo/echoframe
cd echoframe
pip install -r requirements.txt
```

---

## ⚙️ 配置

### 1. 创建配置文件

复制 `config.example.yaml` 为 `config.yaml`：

```bash
cp config.example.yaml config.yaml
```

### 2. 修改配置

```yaml
adapters:
  # 使用 aiocqhttp（反向 WebSocket）
  aiocqhttp:
    enabled: true
    host: "0.0.0.0"
    port: 6789
    access_token: ""      # 与 OneBot 实现保持一致

bot:
  superusers:
    - 123456789           # 改为你的 QQ 号
```

---

## 🔌 配置 OneBot 实现

### Lagrange

编辑 `appsettings.json`：

```json
{
    "Implementations": [
        {
            "Type": "ReverseWebSocket",
            "Host": "127.0.0.1",
            "Port": 6789,
            "Suffix": "/ws/",
            "AccessToken": ""
        }
    ]
}
```

### go-cqhttp

编辑 `config.yml`：

```yaml
servers:
  - ws-reverse:
      universal: ws://127.0.0.1:6789/ws/
      access-token: ""
```

---

## 🎯 启动

### 1. 启动 EchoFrame

```bash
python bot.py
```

应该看到：
```
Running on http://0.0.0.0:6789
✅ AioCQHTTP 适配器初始化完成
```

### 2. 启动 OneBot 实现

启动 Lagrange 或 go-cqhttp

### 3. 验证连接

看到以下日志表示成功：
```
✅ WebSocket 已连接: Bot 919727785
✅ 登录账号: 昵称 (919727785)
```

---

## 🧪 测试

在 QQ 中发送任何消息，应该能在日志中看到：
```
📨 群聊[668670096] 用户: 消息内容
```

---

## 📝 创建第一个插件

### 1. 创建插件目录

```bash
mkdir -p plugins/hello
```

### 2. 创建插件代码

**`plugins/hello/main.py`**:

```python
from echoframe import Plugin, on_command

class HelloPlugin(Plugin):
    pass

@on_command("/hello")
async def hello(bot, event):
    await bot.send(event, "Hello, EchoFrame!")
```

### 3. 创建元数据

**`plugins/hello/metadata.yaml`**:

```yaml
name: "Hello 插件"
description: "简单的问候插件"
commands:
  - "/hello"
```

### 4. 重启或热加载

```bash
# 重启
python bot.py

# 或使用热加载（如果有 plugin_manager 插件）
/加载新插件 hello
```

### 5. 测试

在 QQ 中发送 `/hello`，应该收到回复！

---

## ✅ 完成！

恭喜！您已经成功：
- ✅ 安装并配置 EchoFrame
- ✅ 连接到 OneBot 实现
- ✅ 创建了第一个插件

---

## 📚 下一步

- [插件开发指南](../PLUGIN_DEVELOPMENT_GUIDE.md) - 学习更多插件开发知识
- [配置指南](CONFIG_GUIDE.md) - 了解详细配置选项
- [示例插件](../examples/) - 查看更多示例

---

**开始享受 EchoFrame 吧！** 🎉


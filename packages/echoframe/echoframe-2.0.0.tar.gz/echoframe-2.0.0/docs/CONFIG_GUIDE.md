# ⚙️ EchoFrame 配置指南

## 配置文件概述

EchoFrame 使用 YAML 格式的配置文件。

---

## 📁 配置文件位置

- **主配置**：`config.yaml`
- **示例配置**：`config.example.yaml`

---

## 🔌 通信配置

### 反向 WebSocket（推荐用于 Lagrange）

**EchoFrame 作为服务端，等待 OneBot 实现连接**

```yaml
adapters:
  aiocqhttp:
    enabled: true
    host: "0.0.0.0"         # 监听地址
    port: 6789              # 监听端口
    access_token: ""        # 访问令牌（与 OneBot 实现一致）
  
  websocket_client:
    enabled: false
```

**对应的 Lagrange 配置**：
```json
{
    "Type": "ReverseWebSocket",
    "Host": "127.0.0.1",
    "Port": 6789,
    "Suffix": "/ws/",
    "AccessToken": ""
}
```

**连接地址**：`ws://127.0.0.1:6789/ws/`

---

### 正向 WebSocket 客户端

**EchoFrame 主动连接到 OneBot 实现**

```yaml
adapters:
  aiocqhttp:
    enabled: false
  
  websocket_client:
    enabled: true
    url: "ws://127.0.0.1:8082"
    access_token: ""
    reconnect_interval: 3    # 重连间隔（秒）
```

**对应的 Lagrange 配置**：
```json
{
    "Type": "ForwardWebSocket",
    "Host": "127.0.0.1",
    "Port": 8082,
    "AccessToken": ""
}
```

---

## 🔐 安全配置

### access_token（访问令牌）

```yaml
adapters:
  aiocqhttp:
    access_token: "your_secret_token"
```

**注意**：
- 两边必须完全一致
- 留空表示不验证（不推荐生产环境）
- 建议使用随机字符串

### secret（密钥）

```yaml
adapters:
  aiocqhttp:
    secret: "your_secret"
```

用于签名验证（可选）

---

## 📦 插件配置

```yaml
plugins:
  plugin_dirs:
    - "plugins"              # 插件目录
    - "custom_plugins"       # 可以添加多个目录
  
  enabled_plugins: []        # 留空表示加载所有
  # enabled_plugins:         # 或只启用特定插件
  #   - plugin1
  #   - plugin2
  
  disabled_plugins: []       # 禁用的插件
  # disabled_plugins:
  #   - unwanted_plugin
```

---

## 🤖 机器人配置

```yaml
bot:
  command_prefix: "/"        # 命令前缀
  
  superusers:                # 超级用户（拥有所有权限）
    - 123456789
    - 987654321
  
  nicknames:                 # 机器人昵称（用于 @ 触发）
    - "小助手"
    - "bot"
    - "机器人"
```

---

## 💓 心跳配置

```yaml
heartbeat:
  enable: false              # 是否启用心跳
  interval: 15000            # 心跳间隔（毫秒）
```

**注意**：OneBot 实现通常会自己发送心跳，无需启用。

---

## 📝 日志配置

```yaml
logging:
  level: "INFO"              # 日志级别
  # level: "DEBUG"           # 调试时使用
  
  format: "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan> - <level>{message}</level>"
  
  file: "logs/bot.log"      # 日志文件路径
  # file: ""                 # 留空表示不保存到文件
```

**日志级别**：
- `DEBUG` - 显示所有日志（调试用）
- `INFO` - 显示重要信息（推荐）
- `WARNING` - 只显示警告和错误
- `ERROR` - 只显示错误

---

## 📊 完整配置示例

```yaml
# EchoFrame 完整配置

adapters:
  aiocqhttp:
    enabled: true
    host: "0.0.0.0"
    port: 6789
    access_token: ""
  
  websocket_client:
    enabled: false

plugins:
  plugin_dirs:
    - "plugins"
  enabled_plugins: []
  disabled_plugins: []

bot:
  command_prefix: "/"
  superusers:
    - 123456789
  nicknames:
    - "小助手"

heartbeat:
  enable: false
  interval: 15000

logging:
  level: "INFO"
  file: "logs/bot.log"
```

---

## 💡 配置技巧

### 1. 环境变量

```python
# 使用环境变量
import os

config = {
    "adapters": {
        "aiocqhttp": {
            "access_token": os.getenv("ECHOFRAME_TOKEN", "")
        }
    }
}
```

### 2. 多配置文件

```python
import yaml

# 加载不同环境的配置
env = os.getenv("ENV", "dev")
config_file = f"config.{env}.yaml"

with open(config_file) as f:
    config = yaml.safe_load(f)
```

### 3. 配置验证

```python
# 检查必需配置
if not config["bot"]["superusers"]:
    raise ValueError("必须配置至少一个超级用户")
```

---

## ⚠️ 常见问题

### Q: access_token 不匹配

**错误**：`401 Unauthorized` 或 `authorization header is missed`

**解决**：确保 EchoFrame 和 OneBot 实现的 access_token 完全一致。

### Q: 端口被占用

**错误**：`Address already in use`

**解决**：修改 port 配置为其他端口。

### Q: 连接失败

**检查**：
1. 端口是否正确
2. OneBot 实现是否启动
3. 防火墙是否阻止

---

## 📚 相关文档

- [WEBSOCKET_MODE_GUIDE.md](../WEBSOCKET_MODE_GUIDE.md) - WebSocket 模式详解
- [README.md](../README.md) - 项目主页

---

**需要帮助？查看 [FAQ.md](FAQ.md)！**


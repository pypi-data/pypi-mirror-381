# ❓ 常见问题（FAQ）

## 安装和配置

### Q1: 如何安装 EchoFrame？

**A**: 两种方式：

```bash
# 方式 1：作为库安装（推荐）
pip install echoframe

# 方式 2：从源码运行
git clone https://github.com/your-repo/echoframe
cd echoframe
pip install -r requirements.txt
```

---

### Q2: 401 Unauthorized 错误？

**A**: access_token 不匹配。

**解决**：确保两边 token 完全一致：

```yaml
# EchoFrame
access_token: "your_token"
```

```json
// Lagrange
"AccessToken": "your_token"
```

或两边都留空：
```yaml
access_token: ""
```

---

### Q3: 端口被占用？

**A**: 修改配置文件的端口。

```yaml
adapters:
  aiocqhttp:
    port: 6789    # 改为其他端口
```

---

## 连接问题

### Q4: WebSocket 连接失败？

**A**: 检查清单：

1. EchoFrame 是否启动？
2. 端口是否匹配？
3. access_token 是否一致？
4. 防火墙是否阻止？

**调试**：
```yaml
logging:
  level: "DEBUG"    # 开启详细日志
```

---

### Q5: 收到消息但不回复？

**A**: 可能原因：

1. **没有插件** - 创建插件或加载示例插件
2. **API 调用失败** - 检查日志错误信息
3. **插件被禁用** - 使用 `/插件列表` 检查

---

## 插件问题

### Q6: 如何创建插件？

**A**: 参考 [插件开发指南](../PLUGIN_DEVELOPMENT_GUIDE.md)

最简单的插件：
```python
from echoframe import Plugin, on_command

class MyPlugin(Plugin):
    pass

@on_command("/hello")
async def hello(bot, event):
    await bot.send(event, "Hello!")
```

---

### Q7: 如何热加载插件？

**A**: 使用插件管理器插件：

```
/重载插件 <插件名>
/加载新插件 <插件名>
```

或通过代码：
```python
from echoframe import get_plugin_manager

manager = get_plugin_manager()
result = await manager.reload_plugin("my_plugin")
```

---

### Q8: 插件数据会丢失吗？

**A**: 正确实现 on_load 和 on_unload 就不会丢失。

```python
class MyPlugin(Plugin):
    async def on_load(self):
        # 加载数据
        pass
    
    async def on_unload(self):
        # 保存数据
        pass
```

---

## 使用问题

### Q9: 如何发送图片？

**A**: 使用 MS.image()

```python
from echoframe import MS

msg = MS.image("https://example.com/image.jpg")
await bot.send(event, msg.to_array())
```

---

### Q10: 如何 @ 用户？

**A**: 使用 MS.at()

```python
from echoframe import MS

msg = MS.at(user_id) + MS.text(" 你好！")
await bot.send(event, msg.to_array())
```

---

### Q11: 如何获取群成员列表？

**A**: 调用 API

```python
members = await bot.call_api("get_group_member_list", group_id=group_id)
```

---

### Q12: 如何实现定时任务？

**A**: 在 on_load 中启动后台任务

```python
import asyncio

class MyPlugin(Plugin):
    async def on_load(self):
        self.task = asyncio.create_task(self.daily_task())
    
    async def on_unload(self):
        self.task.cancel()
    
    async def daily_task(self):
        while True:
            await asyncio.sleep(86400)  # 24小时
            # 执行任务
```

---

## 性能问题

### Q13: 机器人响应慢？

**A**: 
1. 检查网络延迟
2. 优化插件代码（避免阻塞操作）
3. 使用异步方法

---

### Q14: 如何限制发送频率？

**A**: 使用 rate_limit_middleware

```python
from echoframe import Bot, rate_limit_middleware

bot = Bot(config)
bot.middleware.use(rate_limit_middleware)
```

---

## 错误处理

### Q15: 插件加载失败？

**A**: 查看日志错误信息：

1. **语法错误** - 检查 Python 语法
2. **导入错误** - 检查依赖是否安装
3. **缺少文件** - 检查 main.py 是否存在

**验证**：
```bash
python -m py_compile plugins/my_plugin/main.py
```

---

### Q16: 如何调试插件？

**A**: 
1. 设置日志级别为 DEBUG
2. 使用 logger.debug() 输出调试信息
3. 使用热加载快速迭代

```python
from loguru import logger

@on_command("/test")
async def test(bot, event):
    logger.debug(f"收到命令，用户: {event.user_id}")
    # ...
```

---

## 高级问题

### Q17: 如何支持多个机器人？

**A**: 创建多个 Bot 实例

```python
bot1 = Bot(config1)
bot2 = Bot(config2)

await asyncio.gather(
    bot1.start(),
    bot2.start()
)
```

---

### Q18: 如何使用数据库？

**A**: 在插件中集成数据库

```python
import aiosqlite

class MyPlugin(Plugin):
    async def on_load(self):
        self.db = await aiosqlite.connect("data.db")
    
    async def on_unload(self):
        await self.db.close()
```

---

### Q19: 如何创建 Web 管理面板？

**A**: 参考 [WEB_API_PLUGIN_MANAGEMENT.md](../WEB_API_PLUGIN_MANAGEMENT.md)

使用 FastAPI 创建 RESTful API。

---

### Q20: 如何贡献代码？

**A**: 
1. Fork 项目
2. 创建分支
3. 提交 PR

---

## 🆘 获取更多帮助

- 查看 [文档中心](README.md)
- 提交 [Issue](https://github.com/your-repo/echoframe/issues)
- 查看 [示例代码](../examples/)

---

**找不到答案？提交 Issue 或查看其他文档！** 💬


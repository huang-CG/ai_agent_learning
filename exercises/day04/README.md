# Day 4 · 天气 API

## 这题要你做什么？（一句话）

> 用 Python **`requests` 库**向互联网发 **GET 请求**，拿到天气 JSON 并**打印出来**。

这是第一次调**外部 HTTP API**，和 D7 调 DeepSeek 是同一套路。

---

## 用户用起来是什么样

```powershell
python exercises/day04/weather.py
请输入城市：北京

（终端打印一大段 JSON，里面有温度、天气描述等）
```

---

## 用哪个 API？（免费，无需 Key）

**wttr.in** — 零注册，直接 GET：

```
https://wttr.in/{城市}?format=j1
```

示例：`https://wttr.in/Beijing?format=j1`

---

## 核心代码（只有 3 行）

```python
import requests

city = input("请输入城市：").strip()
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url, timeout=10)
print(response.json())
```

| 行 | 含义 |
|----|------|
| `requests.get(url)` | 发 GET 请求，等服务器回复 |
| `response.json()` | 把回复体解析成 Python 字典 |
| `timeout=10` | 最多等 10 秒，避免卡死 |

---

## 建议怎么写（分步）

| 步骤 | 做什么 |
|------|--------|
| 1 | `get_weather(city)` — 发请求，返回 JSON 字典 |
| 2 | `main()` — 读城市名，调用上面，打印结果 |
| 3 | （可选）从 JSON 里取出温度，只打印一行 |

JSON 结构较深，**Day 4 验收只要求打印完整 JSON**；提取温度是加分项。

---

## 运行前

```powershell
cd e:\AI_agent_Quick
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python exercises/day04/weather.py
```

---

## 验收自检

- [ ] 用了 `requests.get()`
- [ ] 输入城市后能打印 JSON（不是报错）
- [ ] 知道 `response.status_code` 200 表示成功
- [ ] （可选）加了 `try/except` 处理网络错误

---

## 常见问题

| 现象 | 原因 |
|------|------|
| `ModuleNotFoundError: requests` | 没装依赖 → `pip install requests` |
| 超时 / 连接失败 | 网络问题，检查网络或加 `timeout` |
| 乱码 | URL 里的中文城市用 `city` 变量拼进 f-string 即可 |

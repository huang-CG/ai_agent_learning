# Day 7 · 首次 LLM API 调用

## 这题要你做什么？（一句话）

> 用 Python **`requests.post`** 调用 **DeepSeek Chat Completions**，实现命令行**单轮 AI 问答**。

和 D4 天气 API 同一套路：发 HTTP 请求 → 拿 JSON → 解析打印。区别是 D4 用 `GET`，D7 用 `POST`，且要带 API Key。

---

## 用户用起来是什么样

```powershell
cd e:\AI_agent_Quick
.\venv\Scripts\Activate.ps1
python exercises/day07/chat.py
```

```
请输入你的问题：Python 里 list 和 tuple 有什么区别？
AI：list 可变，tuple 不可变……
```

输入 `quit` 或 `exit` 退出。

---

## 和 D4 的对比

| | D4 天气 | D7 DeepSeek |
|---|---------|-------------|
| 方法 | `requests.get` | `requests.post` |
| URL | `https://wttr.in/{city}?format=j1` | `{DEEPSEEK_BASE_URL}/chat/completions` |
| 鉴权 | 无 | `Authorization: Bearer <API_KEY>` |
| Body | 无（参数在 URL） | JSON：`model` + `messages` |
| 取结果 | `response.json()` 里找天气字段 | `choices[0].message.content` |

---

## 请求骨架（预习已写过）

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = f"{os.getenv('DEEPSEEK_BASE_URL', 'https://api.deepseek.com')}/chat/completions"
headers = {
    "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
    "Content-Type": "application/json",
}
body = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "你好"}],
}

response = requests.post(url, headers=headers, json=body, timeout=30)
response.raise_for_status()
answer = response.json()["choices"][0]["message"]["content"]
print(answer)
```

---

## 目标结构

```python
def ask_ai(question: str) -> str:
    """发 POST 请求，返回 AI 回答文本"""
    ...

def main():
    """循环：input 问题 → 打印回答；quit/exit 退出"""
    ...
```

---

## 建议实现顺序

1. 跑 `python scripts/check_env.py`，确认 Key 已配置
2. 写 `ask_ai(question)`：组 headers + body → `requests.post` → 解析 `content`
3. 写 `main()`：`while True` + `input` + 打印
4. 验收：问 2–3 个不同问题，都能拿到回答
5. 写 Phase 0 复盘（约 200 字，见 `LEARNING_PLAN.md` D7）

---

## 验收自检

- [ ] 终端输入问题 → 打印 AI 回答
- [ ] API Key 从 `.env` 读取，**没有写死在代码里**
- [ ] 用了 `requests.post` + `json=body`
- [ ] 能处理网络错误（`try/except requests.RequestException`）
- [ ] Phase 0 复盘写入 `notes/学习笔记.md`

---

## 常见问题

| 现象 | 可能原因 |
|------|----------|
| 401 Unauthorized | Key 错或未加载 `.env` |
| KeyError: choices | 响应结构异常，先 `print(response.json())` 看全文 |
| 超时 | `timeout=30` 或检查网络 |

---

## 拓展（可选，≤20min）

- 加 `system` 角色：`{"role": "system", "content": "你是简洁的 Python 助教"}`
- 对比同一问题 `temperature=0` vs `1.0`（D8 会细讲）

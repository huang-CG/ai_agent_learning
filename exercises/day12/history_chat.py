"""
Day 12 练习：多轮对话（带 messages 历史）

在 D7 chat.py 基础上，用列表攒住 user/assistant 历史，每轮整包发给 API。
"""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
MODEL = "deepseek-chat"

# 最多保留几「轮」对话（1 轮 = 1 条 user + 1 条 assistant）
MAX_TURNS = 10


def trim_history(messages: list[dict], max_turns: int = MAX_TURNS) -> list[dict]:
    """
    限制历史长度，防止 Token 爆炸。

    规则：若有 system，永远保留；其余只留最近 max_turns 轮（user+assistant）。
    """
    if not messages:
        return messages

    # 第一条若是 system，单独拎出来不参与裁剪计数
    if messages[0].get("role") == "system":
        system_msg = messages[0]
        rest = messages[1:]
    else:
        system_msg = None
        rest = messages

    # 一轮最多 2 条（user + assistant），保留最后 max_turns 轮
    max_messages = max_turns * 2
    if len(rest) > max_messages:
        rest = rest[-max_messages:]

    if system_msg:
        return [system_msg] + rest
    return rest


def ask_ai(messages: list[dict], temperature: float = 0.7) -> str:
    """
    把整段 messages 发给 API，返回 assistant 的回答文本。

    和 D7 区别：D7 的 messages 只有 1 条 user；这里是一整段历史。
    """
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        raise RuntimeError("请先在 .env 中配置 DEEPSEEK_API_KEY")

    url = f"{DEEPSEEK_BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": MODEL,
        "messages": messages,  # ★ 整段历史，不是单条 question
        "temperature": temperature,
    }
    response = requests.post(url, headers=headers, json=body, timeout=60)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def main() -> None:
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        return

    # ---------- messages 就是「会话笔记本」----------
    # 可选：加 system 定规矩（D9 学过）
    messages: list[dict] = [
        {"role": "system", "content": "你是友好的助手。回答简洁，记得用户说过的话。"},
    ]

    print("Day 12 · 多轮对话（输入 quit/exit 退出）")
    print("试试：先说我叫小明，再问 我叫什么？\n")

    while True:
        question = input("你：").strip()
        if not question:
            print("问题不能为空")
            continue
        if question.lower() in ("quit", "exit"):
            print("再见！")
            break

        # ① 用户这句记入历史
        messages.append({"role": "user", "content": question})

        # ② 太长就砍掉旧的（保留 system）
        messages = trim_history(messages, MAX_TURNS)

        try:
            # ③ 整包 messages 发给 API
            answer = ask_ai(messages)
            print(f"AI：{answer}\n")

            # ④ AI 回答也记入历史，下一轮才能记得
            messages.append({"role": "assistant", "content": answer})
            messages = trim_history(messages, MAX_TURNS)

        except requests.RequestException as e:
            # 请求失败时，把刚加的 user 撤掉，避免历史里留下「没回答的问题」
            if messages and messages[-1].get("role") == "user":
                messages.pop()
            print(f"请求失败: {e}\n")


if __name__ == "__main__":
    main()

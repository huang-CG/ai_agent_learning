"""
Day 11 练习：流式输出（Streaming）CLI

在 D7 chat.py 基础上增加 stream=True，边生成边打印。

和 D7 的核心区别（先记这三点）：
  1. body 里加 "stream": True
  2. post 时加 stream=True
  3. 用 iter_lines 一行行读，取 delta.content（一小块字），不是 message.content（整段）
"""

import json
import os

import requests
from dotenv import load_dotenv

# 从 .env 读取 API Key（和 D7 一样）
load_dotenv()

DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
MODEL = "deepseek-chat"


def ask_ai_stream(
    question: str,
    *,
    temperature: float = 0.7,
    top_p: float = 1.0,
    max_tokens: int | None = None,
    stop: list[str] | None = None,
) -> str:
    """
    流式问 AI：边收边打印，最后返回拼好的完整回答。

    参数说明（类型注解可先略过，知道含义即可）：
      question     用户问题
      temperature  随机性，越低越稳（D8 学过）
      top_p        核采样，一般固定 1.0
      max_tokens   回答最多生成几个 token，None 表示不限制
      stop         遇到这些字符串就停止生成
    """
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        raise RuntimeError("请先在 .env 中配置 DEEPSEEK_API_KEY")

    # ---------- ① 组装请求（和 D7 几乎一样）----------
    url = f"{DEEPSEEK_BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }
    body: dict = {
        "model": MODEL,
        "messages": [{"role": "user", "content": question}],
        "temperature": temperature,
        "top_p": top_p,
        "stream": True,  # ★ 今天关键：开启流式，服务器会一行行推数据
    }
    # 只有传了值才放进 body（没传就不限制）
    if max_tokens is not None:
        body["max_tokens"] = max_tokens
    if stop is not None:
        body["stop"] = stop

    # 用来把每一块字拼起来，最后 return 完整回答
    full_parts: list[str] = []

    # ---------- ② 发请求 + 边读边处理 ----------
    # with ... as response：请求结束后自动关闭连接（固定写法，先记住即可）
    # stream=True：不要等整包 JSON，要流式读
    with requests.post(url, headers=headers, json=body, stream=True, timeout=60) as response:
        response.raise_for_status()  # HTTP 非 2xx 就抛异常（D7 学过）

        # iter_lines：每次循环拿到服务器推来的「一行」
        for raw_line in response.iter_lines(decode_unicode=True):
            # 调试时可打开，看原始 SSE 行；日常用请保持注释
            # print(repr(raw_line))

            if not raw_line:
                continue  # SSE 事件之间常有空行，跳过

            if not raw_line.startswith("data: "):
                continue  # 只处理以 "data: " 开头的行

            # 去掉行首 "data: "，剩下是 JSON 或 [DONE]
            payload = raw_line[6:].strip()

            if payload == "[DONE]":
                break  # ★ 流结束信号，停止循环

            try:
                chunk = json.loads(payload)  # 字符串 → dict（和 D7 的 response.json() 同类操作）
            except json.JSONDecodeError:
                continue  # 解析失败就跳过这一行

            # D7 取整段：data["choices"][0]["message"]["content"]
            # D11 取增量：data["choices"][0]["delta"]["content"]（本次新增的字）
            delta = chunk["choices"][0].get("delta", {})
            text = delta.get("content") or ""

            if text:
                # end="" 不换行，字接在一起；flush=True 立刻显示到屏幕
                print(text, end="", flush=True)
                full_parts.append(text)  # 同时存起来，便于最后返回完整文本

    print()  # 流式结束后补一个换行
    return "".join(full_parts)  # 把 ["梅","州","位于"] 拼成 "梅州位于"


def main() -> None:
    """主循环：输入问题 → 流式打印 AI 回答；quit/exit 退出（和 D7 main 结构一样）"""
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        return

    print("Day 11 · 流式问答（输入 quit/exit 退出）\n")

    while True:
        question = input("你：").strip()
        if not question:
            print("问题不能为空")
            continue
        if question.lower() in ("quit", "exit"):
            print("再见！")
            break
        try:
            print("AI：", end="", flush=True)
            ask_ai_stream(
                question,
                temperature=0.7,
                top_p=1.0,
                # max_tokens=30,   # 取消注释：故意设小，看截断 + finish_reason:"length"
            )
        except requests.RequestException as e:
            print(f"\n请求失败: {e}")


if __name__ == "__main__":
    main()

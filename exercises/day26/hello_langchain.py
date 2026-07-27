"""
Day 26 · LangChain Hello（骨架 · 请自己填 TODO）

目标：用 LangChain + DeepSeek 成功打印一句模型回复。
不要删掉 load_dotenv；模型请用 deepseek-v4-flash（或 .env 的 DEEPSEEK_MODEL）。
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

# TODO 1: 从 langchain_openai 导入 ChatOpenAI
from langchain_openai import ChatOpenAI

load_dotenv()


def main() -> None:
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash")

    if not api_key or api_key.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        return

    # TODO 2: 创建 ChatOpenAI
    # 提示：需要 model=..., api_key=..., base_url=...
    # temperature 可先设 0.3
    llm = ChatOpenAI(model=model, api_key=api_key, base_url=base_url, temperature=0.3)

    # TODO 3: 调用模型
    # 提示：llm.invoke("用一句话介绍你自己")
    # 返回值通常有 .content 属性
    reply = llm.invoke("用一句话介绍你自己")
    print("Day 26 · LangChain Hello")
    print(reply.content)


if __name__ == "__main__":
    main()

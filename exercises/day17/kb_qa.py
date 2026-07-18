"""
Day 17：个人知识库问答 Bot（拼 Prompt，无向量库）

核心思路：
  读 knowledge.md 全文 → 放进 system（或 user）→ 用户提问 → DeepSeek 基于文档回答

对比：
  - 带文档：应回答文档里的事实
  - nodoc 模式：不塞文档，容易胡编（对应 D16 关知识库实验）
"""

from __future__ import annotations

import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
MODEL = "deepseek-chat"

# 本目录下的知识库文件
KB_PATH = Path(__file__).with_name("knowledge.md")

SYSTEM_WITH_DOC = """你是个人知识库助手。只能根据下面「参考文档」回答用户问题。
如果文档里没有相关信息，就明确说「文档中没有提及」，不要编造。

【参考文档】
{document}
"""

SYSTEM_NO_DOC = """你是一个助手。用简洁中文回答用户问题。"""


def load_document(path: Path = KB_PATH) -> str:
    """读取 markdown 全文。文件不存在时抛出清晰错误。"""
    if not path.exists():
        raise FileNotFoundError(f"找不到知识库文件：{path}")
    return path.read_text(encoding="utf-8")


def ask_ai(question: str, document: str | None, temperature: float = 0.2) -> str:
    """
    向 DeepSeek 提问。
    document 有内容 → 拼进 system（简易知识库）；
    document 为 None → 不塞文档（对比幻觉）。
    """
    if document is not None:
        system = SYSTEM_WITH_DOC.format(document=document)
    else:
        system = SYSTEM_NO_DOC

    url = f"{DEEPSEEK_BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": question},
        ],
        "temperature": temperature,
    }
    response = requests.post(url, headers=headers, json=body, timeout=60)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]


def main() -> None:
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        return

    document = load_document()
    use_doc = True
    print(f"已加载知识库：{KB_PATH.name}（{len(document)} 字符）")
    print("命令：普通提问 | nodoc 切换无文档模式 | doc 切回带文档 | quit 退出\n")

    while True:
        mode = "带文档" if use_doc else "无文档"
        question = input(f"[{mode}] 你的问题：").strip()
        if not question:
            print("问题不能为空！")
            continue
        if question.lower() in ("quit", "exit"):
            print("再见！")
            break
        if question.lower() == "nodoc":
            use_doc = False
            print("→ 已切换：无文档模式（容易胡编，用来对比）\n")
            continue
        if question.lower() == "doc":
            use_doc = True
            print("→ 已切换：带文档模式\n")
            continue

        try:
            answer = ask_ai(question, document if use_doc else None)
            print(f"\nAI：{answer}\n")
        except requests.RequestException as e:
            print(f"请求失败：{e}\n")


if __name__ == "__main__":
    main()

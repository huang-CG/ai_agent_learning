"""
Day 9 练习：5 种 Prompt 实验

在 D7 chat.py 基础上增加 system prompt，练习翻译/摘要/分类/提取/生成。
"""

import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

# 复用 day07 目录已在 path 时可 import；这里独立实现便于学习
load_dotenv()

DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
MODEL = "deepseek-chat"


def ask_with_prompt(system: str, user: str, temperature: float = 0.3) -> str:
    """发 Chat Completions；system=规则，user=具体任务+输入"""
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        raise RuntimeError("请先在 .env 中配置 DEEPSEEK_API_KEY")

    url = f"{DEEPSEEK_BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": temperature,
    }
    response = requests.post(url, headers=headers, json=body, timeout=30)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def demo_translate() -> None:
    """1. 翻译"""
    system = "你是专业翻译。只输出英文译文，不要解释。"
    user = "把下面中文翻译成英文：今天天气不错，适合出去散步。"
    print("=== 翻译 ===")
    print(ask_with_prompt(system, user))


def demo_summary() -> None:
    """2. 摘要"""
    system = "你是摘要助手。用不超过 50 字概括下面文章要点。"
    article = (
        "OpenAI 发布新一代大模型，上下文窗口扩大至百万 token。"
        "开发者可通过 API 调用，价格较前代下降约 30%。"
        "业界认为这将推动 RAG 与 Agent 应用普及。"
    )
    user = f"请摘要：\n{article}"
    print("=== 摘要 ===")
    print(ask_with_prompt(system, user))


def demo_classify() -> None:
    """3. 分类"""
    system = "你是文本分类器。判断情感：正面、负面或中性。"
    user = "这家餐厅的服务员态度很好，但等位太久了。"
    print("=== 分类 ===")
    print(ask_with_prompt(system, user))


def demo_extract() -> None:
    """4. 提取"""
    system = (
        "你是信息提取助手。从文本中提取姓名、公司、职位。"
        "只输出 JSON，格式：{\"name\":\"\",\"company\":\"\",\"title\":\"\"}"
    )
    user = "张三目前在字节跳动担任算法工程师。"
    print("=== 提取 ===")
    print(ask_with_prompt(system, user))


def demo_generate() -> None:
    """5. 生成"""
    system = "你是 Python 助教。根据需求生成简短示例代码，并加一行注释说明。"
    user = "写一个函数，判断字符串是否为回文。"
    print("=== 生成 ===")
    print(ask_with_prompt(system, user))


def main() -> None:
    demos = [
        ("1 翻译", demo_translate),
        ("2 摘要", demo_summary),
        ("3 分类", demo_classify),
        ("4 提取", demo_extract),
        ("5 生成", demo_generate),
    ]
    print("Prompt 实验（依次运行 5 种）\n")
    for label, fn in demos:
        try:
            fn()
        except requests.RequestException as e:
            print(f"{label} 请求失败: {e}")
        print()


if __name__ == "__main__":
    main()

"""
Day 10 练习：Chain-of-Thought（思维链）对比实验

对比同一批数学题：普通 Prompt（直接答） vs CoT Prompt（逐步推理）。
"""

import os
import re

import requests
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
MODEL = "deepseek-chat"

# 普通：直接要答案
SYSTEM_DIRECT = "你是数学助手。直接给出最终数字答案，不要解释。"

# CoT：先推理再答
SYSTEM_COT = (
    "你是数学助手。请一步一步思考，写出中间计算过程。"
    "最后一行单独写：答案：数字（只写整数）。"
)

# 3 道多步算术题（故意需要中间步骤）
MATH_QUESTIONS = [
    {
        "q": "小明有 15 个苹果，给出 1/3 给小红，又买了 8 个，现在几个？",
        "answer": 18,
    },
    {
        "q": "一本书 48 页，第一天读了 1/4，第二天读了剩下的 1/3，还剩几页？",
        "answer": 24,
    },
    {
        "q": "商店有 120 个玩具，上午卖出 1/5，下午卖出剩下的 1/4，还剩几个？",
        "answer": 72,
    },
]


def ask_with_prompt(system: str, user: str, temperature: float = 0.0) -> str:
    """发 Chat Completions；CoT 对比用 temperature=0 减少随机性"""
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
    response = requests.post(url, headers=headers, json=body, timeout=60)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def extract_number(text: str) -> int | None:
    """从回复里尽量提取最终数字（支持「答案：18」或纯数字）"""
    match = re.search(r"答案[：:]\s*(-?\d+)", text)
    if match:
        return int(match.group(1))
    numbers = re.findall(r"-?\d+", text)
    if numbers:
        return int(numbers[-1])
    return None


def run_comparison() -> None:
    """3 道题 × 2 种模式，打印对错"""
    print("=" * 50)
    print("普通 Prompt vs CoT 对比（temperature=0）")
    print("=" * 50)

    direct_ok = cot_ok = 0

    for i, item in enumerate(MATH_QUESTIONS, 1):
        q, expected = item["q"], item["answer"]
        print(f"\n--- 第 {i} 题 ---")
        print(f"题目：{q}")
        print(f"标准答案：{expected}\n")

        direct_reply = ask_with_prompt(SYSTEM_DIRECT, q)
        direct_num = extract_number(direct_reply)
        direct_hit = direct_num == expected
        direct_ok += direct_hit
        print(f"[普通] {'✓' if direct_hit else '✗'} 提取={direct_num}")
        print(f"  回复：{direct_reply[:200]}{'...' if len(direct_reply) > 200 else ''}\n")

        cot_reply = ask_with_prompt(SYSTEM_COT, q)
        cot_num = extract_number(cot_reply)
        cot_hit = cot_num == expected
        cot_ok += cot_hit
        print(f"[CoT]  {'✓' if cot_hit else '✗'} 提取={cot_num}")
        print(f"  回复：{cot_reply[:300]}{'...' if len(cot_reply) > 300 else ''}")

    print("\n" + "=" * 50)
    print(f"普通 Prompt 正确：{direct_ok}/3")
    print(f"CoT Prompt   正确：{cot_ok}/3")
    print("=" * 50)


def interactive_cot() -> None:
    """交互：用户出题，CoT 逐步推理"""
    print("\n逐步推理模式（输入 quit 退出）\n")
    while True:
        question = input("请输入数学题：").strip()
        if not question:
            print("题目不能为空")
            continue
        if question.lower() in ("quit", "exit"):
            print("再见！")
            break
        try:
            reply = ask_with_prompt(SYSTEM_COT, question)
            print(f"\n{reply}\n")
        except requests.RequestException as e:
            print(f"请求失败: {e}")


def main() -> None:
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        return

    print("Day 10 · CoT 实验")
    print("1. 跑 3 道对比题（普通 vs CoT）")
    print("2. 交互式逐步推理")
    choice = input("请选择 (1/2，默认 1)：").strip() or "1"

    try:
        if choice == "2":
            interactive_cot()
        else:
            run_comparison()
    except requests.RequestException as e:
        print(f"请求失败: {e}")


if __name__ == "__main__":
    main()

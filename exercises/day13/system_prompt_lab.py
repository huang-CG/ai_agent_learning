"""
Day 13 练习：System Prompt 三版对比

同一组测试题，分别用 A/B/C 三版 system prompt 调用 API，对比输出差异。
"""

import argparse
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
MODEL = "deepseek-chat"

# ---------- 三版 System Prompt（对比用）----------

PROMPT_A = "你是 Python 学习助手。"

PROMPT_B = """你是 Python 学习助手，面向零基础学员。

职责：
- 解释 Python 概念，用简单中文
- 给出简短可运行的代码示例
- 指出常见错误

限制：
- 只回答 Python 相关问题；其他话题礼貌拒绝
- 不编造不存在的库或 API
- 回答控制在 200 字以内，除非用户要求详细"""

PROMPT_C = """你是 Python 学习助手，面向零基础学员。每次回答必须严格按以下结构（Markdown 标题）：

## 概念
用 1～2 句话说明

## 示例
```python
# 可运行的小例子
```

## 注意
1 条常见坑或最佳实践

规则：
- 只答 Python；非 Python 问题回复：「我专注 Python，这个问题超出范围。」
- 代码必须能直接运行，加必要注释
- 总字数不超过 250 字"""

PROMPTS = {"A": PROMPT_A, "B": PROMPT_B, "C": PROMPT_C}

# 固定测试题：覆盖解释 / 生成 / 边界 / 纠错
TEST_QUESTIONS = [
    "什么是列表推导式？",
    "帮我写一段读取 JSON 文件的代码",
    "Python 和 Java 哪个更好？",
    "帮我看看这段代码有没有 bug：for i in range(10) print(i)",
]


def ask_with_system(system: str, user: str, temperature: float = 0.3) -> str:
    """单轮：system 定规矩，user 是具体问题"""
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


def run_compare(versions: list[str]) -> None:
    """对每道题 × 每版 prompt 打印回答"""
    for q_idx, question in enumerate(TEST_QUESTIONS, 1):
        print(f"\n{'=' * 60}")
        print(f"测试题 {q_idx}：{question}")
        print("=" * 60)
        for ver in versions:
            system = PROMPTS[ver]
            print(f"\n--- 版本 {ver} ---")
            print(f"[system 预览] {system[:60].replace(chr(10), ' ')}...")
            try:
                answer = ask_with_system(system, question)
                print(answer)
            except requests.RequestException as e:
                print(f"请求失败: {e}")
            time.sleep(0.5)  # 避免连续请求过快


def main() -> None:
    parser = argparse.ArgumentParser(description="Day 13 System Prompt 对比实验")
    parser.add_argument(
        "--version",
        choices=["A", "B", "C"],
        help="只跑指定版本；默认 A/B/C 全跑",
    )
    args = parser.parse_args()

    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        return

    versions = [args.version] if args.version else ["A", "B", "C"]
    print("Day 13 · System Prompt 三版对比")
    print(f"测试题 {len(TEST_QUESTIONS)} 道 × 版本 {', '.join(versions)}")
    print("temperature=0.3（偏低，便于对比 prompt 本身差异）\n")
    run_compare(versions)


if __name__ == "__main__":
    main()

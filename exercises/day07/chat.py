"""
Day 7 练习：命令行单轮 AI 问答（DeepSeek Chat Completions）

建议顺序：ask_ai(question) → main()
对照：exercises/day04/weather.py（HTTP 请求套路相同）
预习：notes/学习笔记.md · D7 预习
"""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
# 旧版兼容名，仍可用；官方主推 deepseek-v4-flash（日常）/ deepseek-v4-pro（复杂任务）
# deepseek-chat ≈ v4-flash 非思考模式；deepseek-reasoner ≈ v4-flash 思考模式（2026-07-24 起旧名将退役）
MODEL = "deepseek-chat"


def ask_ai(question: str, temperature: float = 0.7) -> str:
    """向 DeepSeek 发 POST 请求，返回 AI 回答文本"""
    # TODO: 组 url / headers / body，requests.post，解析 choices[0].message.content
    url = f"{DEEPSEEK_BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": MODEL,
        "messages": [{"role": "user", "content": question}],
        "temperature": temperature,
    }
    response = requests.post(url, headers=headers, json=body, timeout=30)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]

def test_temperature():
    question = "用三句话介绍广州"
    for temp in (0, 0.7, 1.2):
        print(f"\n========== temperature: {temp} ==========")
        answer = ask_ai(question, temp)
        print(answer)

def main() -> None:
    """主循环：输入问题 → 打印 AI 回答；quit/exit 退出"""
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        return

    # TODO: while True + input + ask_ai + 异常处理
    while True:
        question = input("请输入你的问题(输入quit/exit退出)：").strip()
        if not question:
            print("问题不能为空！")
            continue
        if question.lower() in ["quit", "exit"]:
            print("再见！")
            break
        try:
            answer = ask_ai(question)
            print(f"AI回答：{answer}")
        except requests.RequestException as e:
            print(f"请求失败: {e}")



if __name__ == "__main__":
    main()
    #test_temperature()
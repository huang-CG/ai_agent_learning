"""
Day 38 · Prompt 工程进阶（骨架 · 请自己填 TODO）

目标：
  1. 写 PROMPT_WEAK / PROMPT_STRONG
  2. create_agent（或 ChatOpenAI.invoke）对同一组句子做分类
  3. 强版输出 json.loads 成功，含 label / reason
  4. 打印弱版 vs 强版，看谁更稳

对照：
  - D13：三版 system prompt
  - D38：加 Few-shot + JSON，挂到 Agent

跑法：
  python exercises/day38/prompt_agent_lab.py
"""

from __future__ import annotations

import json
import os
import re

from dotenv import load_dotenv

# TODO 1: 补导入
#   - langchain.agents.create_agent
#   - langchain_openai.ChatOpenAI
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

load_dotenv()

QUESTIONS = [
    "今天天气真好，广场有人跳舞。",
    "我的订单两周了还没发货，要投诉。",
]


# TODO 2: 弱版 —— 一两句话「请用 JSON 回答」即可，不要 Few-shot
PROMPT_WEAK = """
你是一个客服助手，你的任务是根据用户的问题，判断用户的问题是闲聊、投诉还是咨询，并给出相应的回答。
请用JSON格式回答。

"""


# TODO 3: 强版 —— 必须包含：
#   角色、只输出 JSON、字段 label/reason、label 只能是 闲聊/投诉/咨询
#   至少 2 条用户句 → JSON 的 Few-shot 示例（不要和 QUESTIONS 一模一样）
PROMPT_STRONG = """
你是一个客服助手，你的任务是根据用户的问题，判断用户的问题是闲聊、投诉还是咨询，并给出相应的回答。
你只能输出 JSON 格式，字段为 label 和 reason，label 只能是闲聊、投诉或咨询，reason 是判断的依据。
以下是一些示例：
用户：今晚真凉爽，我要去散散步。
{
    
    "label": "闲聊",
    "reason": "用户的问题是关于天气的，不是投诉或咨询。"
}
用户：我收到的货物有问题，联系客服不处理，我要投诉。
{
    
    "label": "投诉",
    "reason": "用户的问题是关于订单的，是投诉。"
}
用户：我想知道商品的退货流程，请告诉我。
{
    
    "label": "咨询",
    "reason": "用户的问题是关于商品的，是咨询。"
}
"""


def strip_fence(text: str) -> str:
    """去掉 ```json ... ``` 围栏，方便 json.loads。"""
    # TODO 4: 用正则或 replace；拿不到围栏就 strip() 后原样返回
    text = text.strip()
    if not text.startswith("```") or not text.endswith("```"):
        return text
    return re.sub(r"```\s*|\s*```", "", text)


def try_parse(text: str) -> dict | None:
    """解析成功返回 dict，失败返回 None。"""
    # TODO 5: json.loads(strip_fence(text))；except 则 None
    try:
        return json.loads(strip_fence(text))
    except json.JSONDecodeError:
        return None


def build_llm():
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 DEEPSEEK_API_KEY")
    # TODO 6: temperature=0（格式任务）
    return ChatOpenAI(model=model, api_key=api_key, base_url=base_url, temperature=0)


def build_agent(llm, system_prompt: str):
    """今天可不挂工具：create_agent(model=llm, tools=[], system_prompt=...)。"""
    # TODO 7
    return create_agent(model=llm, tools=[], system_prompt=system_prompt)


def ask(agent, question: str) -> str:
    """返回最后一条 message 的文本。"""
    # TODO 8: invoke + result["messages"][-1].content（不要用 result.content）
    result = agent.invoke({"messages":[{"role": "user", "content": question}]})
    last = result["messages"][-1]
    return last.content


def run_suite(title: str, system_prompt: str) -> None:
    print(f"\n===== {title} =====")
    # TODO 9: agent = build_agent(build_llm(), system_prompt)
    #   for q in QUESTIONS:
    #       raw = ask(agent, q)
    #       parsed = try_parse(raw)
    #       print 问句、原文、解析结果或失败
    agent = build_agent(build_llm(), system_prompt)
    for q in QUESTIONS:
        raw = ask(agent, q)
        parsed = try_parse(raw)
        print(f"问句：{q}")
        print(f"原文：{raw}")
        if parsed is None:
            print(f"❌ JSON 解析失败")
        elif 'label' in parsed and 'reason' in parsed:
            print(f"解析成功：✅ 可用：label={parsed['label']}, reason={parsed['reason']}")
        else:
            print(f"⚠ 键名不对：实际 keys = {list(parsed.keys())}")

def main() -> None:
    print("Day 38 · Prompt + JSON\n")
    # TODO 10: 先检查 PROMPT_STRONG 非空，再 run_suite 弱版、强版
    run_suite("弱版", PROMPT_WEAK)
    run_suite("强版", PROMPT_STRONG)


if __name__ == "__main__":
    main()

"""
Day 29 · LangChain Agent 组装（骨架 · 请自己填 TODO）

目标：
  1. 用 @tool 准备至少 2 个工具（可参考 D28，勿整文件复制粘贴完事）
  2. create_agent 组装：LLM + Tools + system_prompt
  3. invoke 后从 result["messages"] 取出最终回答
  4. 打印中间消息类型（ai / tool），确认工具真的执行了（对比 D28）
  5. try/except：异常时打印可读错误，程序不崩

对照：
  - D28：bind_tools → 只有 tool_calls，无 Observation
  - D27：create_agent 天气版；今天换工具集，重点看「闭环」与错误处理

跑法：venv 激活后
  python exercises/day29/agent_lab.py
"""

from __future__ import annotations

import os
from datetime import datetime

from dotenv import load_dotenv

# TODO 1: 补导入
#   - langchain.agents.create_agent
from langchain.agents import create_agent
#   - langchain.tools.tool
from langchain.tools import tool
#   - langchain_openai.ChatOpenAI
from langchain_openai import ChatOpenAI
load_dotenv()


# ---------- 工具 ----------
# 至少 2 个；能力不重叠；docstring 写清何时用 / 参数 / 不要用于
# 建议：get_current_time + celsius_to_fahrenheit（或 count_words）


# TODO 2: 写工具 1
@tool
def get_current_time():
    """
    获取当前时间.
    无参数。
    不要用于温度换算。
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")



# TODO 3: 写工具 2
@tool
def celsius_to_fahrenheit(celsius: float) -> float:
    """
    将摄氏度转换为华氏度。
    参数 celsius: 摄氏度。
    不要用于获取当前时间。
    """
    return (celsius * 9/5) + 32


# TODO 4: TOOLS = [...]
TOOLS = [get_current_time, celsius_to_fahrenheit]


def build_agent():
    """组装并返回 LangChain Agent。"""
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model_name = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash")

    # TODO 5: ChatOpenAI(...)
    model = ChatOpenAI(api_key=api_key, base_url=base_url, model=model_name)

    # TODO 6: create_agent(model=..., tools=TOOLS, system_prompt=...)
    # system_prompt：角色 + 需要时必须调工具、禁止编造时间/换算结果
    system_prompt = "你是一个时间/温度转换助手，请根据用户的问题调用工具获取当前时间或摄氏度转换为华氏度。"
    # 注意：prompt 里声明的能力要和 TOOLS 对齐（Phase 2 复盘踩过的坑）
    agent = create_agent(model=model, tools=TOOLS, system_prompt=system_prompt)
    return agent


def ask(agent, question: str) -> str:
    """问一句，打印消息轨迹，返回最终回答文本。"""
    # TODO 7:
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    messages = result["messages"]
    # 遍历打印：type + 简短 content（tool 消息 = Observation）
    for message in messages:
        print(f"type: {message.type}, content: {message.content}")
    # 返回 messages[-1].content（或最后一条 ai 的 content）
    return messages[-1].content


def main() -> None:
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    if not api_key or api_key.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        return

    if len(TOOLS) < 2:
        print("请先完成 TODO 2～4：至少 2 个工具")
        return

    print("Day 29 · LangChain Agent Lab\n")

    # TODO 8: try/except 包住 build + 两次提问
    # 验收题 1：「现在几点了？」
    # 验收题 2：换另一个工具，如「25 摄氏度是多少华氏度？」
    # 失败时 print(f"出错了: {e}")，不要让脚本直接 Traceback 退出
    try:
        agent = build_agent()
        print("--- 问1 ---")
        print("最终答:", ask(agent, "现在几点了？"), "\n")
        print("--- 问2 ---")
        print("最终答:", ask(agent, "25摄氏度是多少华氏度？"), "\n")
    except Exception as e:
        print(f"出错了: {e}")

if __name__ == "__main__":
    main()

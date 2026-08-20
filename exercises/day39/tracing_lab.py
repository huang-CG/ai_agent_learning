"""
Day 39 · LangSmith 调试（骨架 · 请自己填 TODO）

目标：
  1. .env 打开 LANGSMITH_TRACING + API_KEY（不要把 Key 打印出来）
  2. 两个工具：get_current_time + divide_numbers（除数为 0 必须 raise）
  3. create_agent 跑：成功问 + 失败问
  4. 去 LangSmith 网页对照完整 trace，分析失败发生在哪一层

对照：
  - D25：终端 [LOG]
  - D29：create_agent + messages 轨迹
  - D39：同一条链路，多一个云端 Trace

跑法：
  python exercises/day39/tracing_lab.py
"""

from __future__ import annotations

import os
from datetime import datetime

from dotenv import load_dotenv

# TODO 1: 补导入
#   - langchain.agents.create_agent
#   - langchain.tools.tool
#   - langchain_openai.ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()


def print_trace_status() -> None:
    """只打印 tracing 开没开、Key 有没有、项目名。禁止打印完整 API Key。"""
    # TODO 2:
    #   tracing = os.getenv("LANGSMITH_TRACING", "")
    #   key = os.getenv("LANGSMITH_API_KEY", "")
    #   project = os.getenv("LANGSMITH_PROJECT", "default")
    #   打印 tracing、project、key_ok（True/False 即可）
    #   若没开 tracing 或没有 Key：打印一句提醒后 return（main 里决定是否继续）
    tracing = os.getenv("LANGSMITH_TRACING", "")
    key = os.getenv("LANGSMITH_API_KEY", "")
    project = os.getenv("LANGSMITH_PROJECT", "default")
    if not tracing or not key or not project:
        print("请配置 LANGSMITH_TRACING, LANGSMITH_API_KEY, LANGSMITH_PROJECT")
        return
    print(f"tracing: {tracing}")
    print(f"project: {project}")
    key_ok = bool(key)
    print(f"key_ok: {key_ok}")


# ---------- 工具 ----------


# TODO 3: 时间工具（可参考 D29 思路，勿整文件粘贴）
# @tool
# def get_current_time() -> str:
#     """何时用 / 不要用于计算。"""
#     ...
@tool
def get_current_time() -> str:
    """
    获取当前时间。
    何时用：需要当前时间时。
    不要用于：计算。
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# TODO 4: 除法工具
# @tool
# def divide_numbers(a: float, b: float) -> float:
#     """
#     做除法。参数 a 被除数、b 除数。
#     不要用于查时间。
#     """
#     # b == 0 时必须 raise ValueError("除数不能为 0")
#     # 不要 return 0 或返回中文句子假装成功
@tool
def divide_numbers(a: float, b: float) -> float:
    """
    做除法。参数 a 被除数、b 除数。
    不要用于查时间。
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("除数不能为 0")


# TODO 5: TOOLS = [..., ...]
TOOLS = [get_current_time, divide_numbers]


def build_agent():
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model_name = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 DEEPSEEK_API_KEY")

    # TODO 6: ChatOpenAI(...)  + create_agent(...)
    # system_prompt：需要计算就调 divide_numbers；需要时间就调 get_current_time；
    #   禁止口算除法、禁止编造时间
        llm = ChatOpenAI(model=model_name, api_key=api_key, base_url=base_url)
        agent = create_agent(model=llm, tools=TOOLS, system_prompt="你需要计算就调 divide_numbers；需要时间就调 get_current_time；禁止口算除法、禁止编造时间")
        return agent


def ask(agent, question: str, tag: str) -> str:
    """
    invoke 一句。
    tag 用来在 LangSmith 里好找，例如 ok / fail。
    返回最后一条 message 的文本。
    """
    # TODO 7:
    #   result = agent.invoke(
    #       {"messages": [{"role": "user", "content": question}]},
    #       config={"tags": ["day39", tag]},
    #   )
    #   遍历打印 type + 短 content（和 D29 一样，方便对照网页）
    #   return messages[-1].content
    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
        config={"tags": ["day39", tag]},
    )
    for message in result["messages"]:
        print(f"type: {message.type}, content: {message.content[:10]}...")
    return result["messages"][-1].content


def main() -> None:
    print("Day 39 · LangSmith tracing\n")
    print_trace_status()

    if len(TOOLS) < 2:
        print("请先完成 TODO 3～5：至少 2 个工具")
        return

    # TODO 8: try/except 包住
    #   agent = build_agent()
    #   成功问：「36 除以 6 等于几？」 tag="ok"
    #   失败问：「100 除以 0 等于几？」 tag="fail"
    #   （可选第三问：「现在几点了？」 tag="time"）
    #   失败问允许工具报错；脚本不要直接 Traceback 退出
    #   跑完打印：去 LangSmith 项目页刷新，找带 day39 / fail 标签的那条
    agent = build_agent()
    try:
        ask(agent, "36 除以 6 等于几？", "ok")
        ask(agent, "100 除以 0 等于几？", "fail")
        ask(agent, "现在几点了？", "time")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

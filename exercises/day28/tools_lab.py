"""
Day 28 · LangChain Tools 实验（骨架 · 请自己填 TODO）

目标：
  1. 用 @tool 自建 3 个自定义工具（docstring = description）
  2. 打印每个工具的 name / description / args
  3. 直接 tool.invoke(...) 验证工具本身能跑
  4. llm.bind_tools(tools) 后问一句，打印 tool_calls（看模型选没选对）

对照：
  - D20：Schema 三字段 name / description / parameters
  - D27：@tool 已用过；今天重点是「工具本身」，不是完整 Agent

跑法：venv 激活后
  python exercises/day28/tools_lab.py
"""

from __future__ import annotations

import os
from datetime import datetime

from dotenv import load_dotenv

# TODO 1: 补导入
#   - 从 langchain.tools 导入 tool
from langchain.tools import tool
#   - 从 langchain_openai 导入 ChatOpenAI
from langchain_openai import ChatOpenAI
#   （拓展）from langchain_core.tools import StructuredTool

load_dotenv()


# ---------- 工具（厨房）----------
# 要求：3 个工具能力不重叠；docstring 写清「何时用 / 参数 / 不要用于」
# 建议：时间 / 文本统计 / 温度换算（可自定，但不要照搬 D27 的 get_weather/calculator）


# TODO 2: 写第 1 个工具（示例方向：get_current_time）
# @tool
# def ...
@tool
def get_current_time():
    """
    查询本机当前时间。
    无参数。
    不要说查询某城市。
    不要用于：数学计算、网页搜索、查历史新闻、天气查询。
    """
    return f"当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


# TODO 3: 写第 2 个工具（示例方向：count_words）
# @tool
# def ...
@tool
def count_words(text: str) -> int:
    """
    统计指定文本中的单词数量。
    参数 text: 文本内容。
    不要用于：数学计算、网页搜索、查历史新闻、天气查询。
    """
    return len(text.split())


# TODO 4: 写第 3 个工具（示例方向：celsius_to_fahrenheit）
# @tool
# def ...
@tool
def celsius_to_fahrenheit(celsius: float) -> float:
    """
    将摄氏温度转换为华氏温度。
    参数 celsius: 摄氏温度。
    不要用于：数学计算、网页搜索、查历史新闻、天气查询。
    """
    return (celsius * 9/5) + 32


# TODO 5: 把三个工具放进列表
# TOOLS = [...]
TOOLS = [get_current_time, count_words, celsius_to_fahrenheit]


def print_tool_schemas(tools: list) -> None:
    """打印工具 Schema，对应 D20 的三字段。"""
    print("=== Tool Schemas ===")
    for t in tools:
        # TODO 6: 打印 name、description、args（或 args_schema）
        # 提示：BaseTool 通常有 .name / .description / .args
        print(t.name, t.description, t.args)
    print()


def demo_direct_invoke(tools: list) -> None:
    """不经过 LLM，直接调用工具，确认函数本身正确。"""
    print("=== Direct invoke ===")
    # TODO 7: 任选 1～3 个工具，用 .invoke({...}) 或 .invoke("...") 测一遍
    # 有参数的工具一般传 dict，例如 {"celsius": 25}
    print(get_current_time.invoke({}))
    print(count_words.invoke({"text": "Hello, world!"}))
    print(celsius_to_fahrenheit.invoke({"celsius": 25}))


def demo_bind_tools(tools: list) -> None:
    """绑定工具到 LLM，看模型是否选出正确 tool_calls（今天不必执行工具循环）。"""
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash")

    if not api_key or api_key.startswith("sk-your"):
        print("跳过 bind_tools：请先在 .env 配置 DEEPSEEK_API_KEY")
        return

    # TODO 8: 创建 ChatOpenAI（同 D26），temperature 建议 0.2～0.3
    # llm = ...
    llm = ChatOpenAI(model=model, api_key=api_key, base_url=base_url, temperature=0.2)

    # TODO 9: llm_with_tools = llm.bind_tools(tools)
    llm_with_tools = llm.bind_tools(tools)
    # 问一句会触发某个工具的问题，例如「现在几点了？」或「25 摄氏度是多少华氏度？」
    # resp = llm_with_tools.invoke("...")
    resp = llm_with_tools.invoke("25摄氏度是多少华氏度？")
    # 打印 resp.content 和 resp.tool_calls
    print("=== bind_tools ===")
    print(resp.content)
    print(resp.tool_calls)


def main() -> None:
    if len(TOOLS) < 3:
        print("请先完成 TODO 2～5：至少定义 3 个 @tool 并放入 TOOLS")
        return

    print("Day 28 · LangChain Tools Lab\n")
    print_tool_schemas(TOOLS)
    demo_direct_invoke(TOOLS)
    demo_bind_tools(TOOLS)


if __name__ == "__main__":
    main()

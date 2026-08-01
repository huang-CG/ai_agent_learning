"""
Day 27 · 用 LangChain 重写 ReAct 天气 Agent（骨架 · 请自己填 TODO）

对照 D22 手写版（exercises/day22/react_weather_agent.py）：
  - 手写的 REACT_SYSTEM 提示词 + parse_react 正则解析 + run_react 主循环
    → 全部交给 create_agent，你不用再写
  - get_weather / calculator 两个工具函数 → 你自己写（可参考/移植 D22 的实现）
  - @tool 装饰器会把「函数名 + docstring + 参数」变成工具 Schema
    （对应 D20 学的 name / description / parameters 三字段）

跑法：venv 激活后 python exercises/day27/langchain_weather_agent.py
验收：问「广州天气怎么样」能调用 get_weather 并正确回答；
      问「(3+5)*2 等于几」能调用 calculator。
"""

from __future__ import annotations

import os
from urllib.parse import quote

import requests
from dotenv import load_dotenv

# TODO 1: 补两行导入
#   - 从 langchain.agents 导入 create_agent
from langchain.agents import create_agent
#   - 从 langchain.tools 导入 tool
from langchain.tools import tool
#   - 从 langchain_openai 导入 ChatOpenAI（D26 用过）
from langchain_openai import ChatOpenAI

from datetime import datetime

load_dotenv()


# ---------- 工具（厨房）----------

# TODO 2: 给下面两个函数加上 @tool 装饰器，并写好 docstring
# 注意：docstring 就是工具的 description，模型靠它决定「何时调用」（D20 知识点）

@tool
def get_time():
    """
    查询指定城市的当前时间。
    参数 city: 城市名（如 北京、广州）。
    不要用于：数学计算、网页搜索、查历史新闻、天气查询。
    """
    return f"当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

@tool
def get_weather(city: str) -> str:
    """
    查询指定城市的当前天气状况，包括气温、天气现象（晴/阴/雨等）、湿度。
    用户问某地天气、气温、冷不冷、热不热、要不要带伞、是否下雨时使用。
    参数 city: 城市名（如 北京、广州）。
    不要用于：数学计算、网页搜索、查历史新闻。
    
    """
    # TODO 3: 调 wttr.in 拿天气，返回一行中文摘要
    # 可移植 D22 的实现：url = f"https://wttr.in/{quote(city)}?format=j1"
    # 记得处理请求失败 / 解析失败
    city = city.strip()
    if not city:
        return "错误：城市名不能为空"

    url = f"https://wttr.in/{quote(city)}?format=j1"
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()
        current = data["current_condition"][0]
        desc = current["weatherDesc"][0]["value"]
        temp = current["temp_C"]
        humidity = current["humidity"]
        feels = current.get("FeelsLikeC", temp)
        return (
            f"{city}：{desc}，气温 {temp}℃，体感 {feels}℃，湿度 {humidity}%"
        )
    except requests.RequestException as e:
        return f"错误：天气 API 请求失败（{e}）"
    except (KeyError, IndexError, TypeError) as e:
        return f"错误：天气数据解析失败（{e}）"

@tool
def calculator(expression: str) -> str:
    """
    计算算术表达式，如 (3+5)*2。
    参数 expression: 数学表达式（如 3+5*2）。
    表达式只能包含数字和 + - * / ( ) . 空格。
    不要用于：天气查询、网页搜索、查历史新闻。
    
    """
    # TODO 4: 移植 D22 的受限 eval 实现（白名单字符 + 空 __builtins__）
    expression = expression.strip()
    allowed = set("0123456789+-*/(). %")
    if not expression or any(ch not in allowed for ch in expression):
        return "错误：表达式只能包含数字和 + - * / ( ) . 空格"
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"计算失败: {e}"


# ---------- Agent ----------


def build_agent():
    """创建并返回 LangChain Agent。"""
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model_name = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash")

    # TODO 5: 创建 ChatOpenAI（同 D26），temperature 建议 0.3
    model = ChatOpenAI(model=model_name, api_key=api_key, base_url=base_url, temperature=0.3)

    # TODO 6: 用 create_agent 创建 agent 并 return
    # 提示：create_agent(model=..., tools=[...], system_prompt=...)
    # system_prompt 写一两句就够（角色 + 问天气必须调工具，禁止编造）
    # 对比 D22：不用再教模型 Thought/Action 格式，框架自己处理
    agent = create_agent(model=model, tools=[get_weather, calculator, get_time], system_prompt="你是一个天气预报员，请根据用户的问题调用工具获取天气信息、计算数学表达式和当前时间。")
    return agent


def ask(agent, question: str) -> str:
    """问一个问题，返回最终回答文本。"""
    final_answer = ""
    for message_chunk, metadata in agent.stream(
        {"messages": [{"role": "user", "content": question}]},
        stream_mode="messages"
        ):
        text = message_chunk.content
        if not text:
            continue
        print(text, end="", flush=True)
        if message_chunk.type == "AIMessageChunk":
            final_answer += text
    return final_answer


    # final_answer = ""
    # TODO 7: 调用 agent
    # 提示：result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    # for chuk in agent.stream(
    #     {"messages": [{"role": "user", "content": question}]},
    #     stream_mode="updates",
    #     ):
        
    # # result["messages"] 是完整消息列表，最后一条是最终回答（取 .content）
    # # 进阶（选做）：打印中间每条消息，观察工具调用过程（相当于 D22 的 Observation 日志）
    #     for node, update in chuk.items():
    #         for message in update.get("messages",[]):
    #             text = getattr(message, "content", "") or ""
    #             if not text:
    #                 continue
    #             print(f"{node}: {text}",end="",flush=True)
    #             if getattr(message, "type", "") == "ai":
    #                 final_answer = text
    # return final_answer


def main() -> None:
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    if not api_key or api_key.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        return

    agent = build_agent()
    print("Day 27 · LangChain 天气 Agent（输入 quit 退出）\n")

    while True:
        q = input("你：").strip()
        if not q:
            continue
        if q.lower() in ("quit", "exit"):
            print("再见！")
            break
        try:
            print(f"\nAI：{ask(agent, q)}\n")
        except Exception as e:
            print(f"出错了: {e}\n")


if __name__ == "__main__":
    main()

"""
Day 35 · 搜索工具集成（骨架 · 请自己填 TODO）

目标：
  1. 用 ddgs 做一次「裸搜索」冒烟（不经 Agent）
  2. @tool web_search(query)：内部搜索，返回可读文本（标题/摘要/链接）
  3. 再准备 1 个非搜索工具（如 get_current_time）
  4. create_agent：让模型决定何时联网搜
  5. 两问验收 + 打印 messages 里是否出现 tool

对照：
  - D22：假 web_search（字典假数据）
  - D34：本地 RAG 工具
  - D35：真外网搜索工具

跑法：
  pip install ddgs   # 若尚未安装
  python exercises/day35/search_agent_lab.py
"""

from __future__ import annotations

import os
from datetime import datetime

from dotenv import load_dotenv

# TODO 1: 补导入
#   - langchain.agents.create_agent
#   - langchain.tools.tool
#   - langchain_openai.ChatOpenAI
#   - ddgs.DDGS
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from ddgs import DDGS

load_dotenv()


def raw_search(query: str, max_results: int = 5) -> list[dict]:
    """
    裸调用 ddgs，返回结果列表（每项通常含 title / href / body）。
    不存在网络/包时：打印错误并返回 []。
    """
    # TODO 2:
    #   from ddgs import DDGS
    #   with DDGS() as client:
    #       return list(client.text(query, max_results=max_results))
    #   捕获异常 → print + return []
    try:
        with DDGS() as client:
            return list(client.text(query, max_results=max_results))
    except Exception as e:
        print(f"Error: {e}")
        return []


def format_results(results: list[dict]) -> str:
    """把搜索结果拼成给 LLM 读的纯文本。"""
    # TODO 3:
    #   空列表 → 「未搜到相关结果」
    #   否则逐条：标题 / 摘要(body) / 链接(href)，用换行拼起来
    if not results:
        return "未搜到相关结果"
    return "\n".join([f"标题: {result['title']}\n摘要: {result['body']}\n链接: {result['href']}" for result in results])


# ---------- 工具 ----------


# TODO 4: 非搜索工具（可抄思路自 D29/D34，勿整文件粘贴）
# @tool
# def get_current_time() -> str:
#     """... docstring：何时用 / 不要用于搜索 ..."""
#     ...
@tool
def get_current_time() -> str:
    """
    获取当前时间。
    何时用：需要当前时间时。
    不要用于：搜索。
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# TODO 5: 搜索工具
@tool
def web_search(query: str) -> str:
    """
    联网搜索当前公开信息。
    何时用：新闻、近期赛事、需要最新事实、本地知识库没有的信息。
    不要用于：简单算术、闲聊、已知常识（可直接答）。
    """
    results = raw_search(query, max_results=5)
    return format_results(results)


def build_llm():
    """DeepSeek Chat。"""
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 DEEPSEEK_API_KEY")
    # TODO 6: return ChatOpenAI(..., temperature=0.2)
    return ChatOpenAI(api_key=api_key, base_url=base_url, model=model, temperature=0.2)


def build_agent(llm, tools: list):
    """create_agent + system_prompt。"""
    # TODO 7:
    # system_prompt 写清：
    #   - 需要最新/外网事实 → web_search
    #   - 简单题直接答，不要硬搜
    #   - 根据工具返回内容回答；搜不到就老实说
    # return create_agent(model=llm, tools=tools, system_prompt=...)
    return create_agent(model=llm, tools=tools, system_prompt="""
    你需要根据用户的问题决定使用哪个工具。
    如果问题需要最新/外网事实，使用 web_search 工具。
    如果问题很简单，直接回答，不要硬搜。
    根据工具返回的内容回答，如果搜不到就老实说。
    """)


def ask(agent, question: str) -> None:
    """invoke，打印最终回答，并简要列出 messages 类型（看有没有 tool）。"""
    # messages 是 Message 对象：用 .type / .content，不要 message["type"]
    # TODO 8: 参考 D34 ask；try/except 别让程序崩
    try:
        result = agent.invoke({"messages":[{"role": "user", "content": question}]})
        last = result["messages"][-1]
        print(last.content)
        print([message.type for message in result["messages"]])
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("Day 35 · web_search Agent\n")

    # --- 冒烟：不经 Agent，先确认搜索能通 ---
    smoke_q = "DeepSeek AI"
    print(f"=== 冒烟搜索：{smoke_q} ===")
    # TODO 9: raw = raw_search(smoke_q, max_results=3)
    #         print(format_results(raw))
    #         若为空：先解决网络/ddgs 安装，再继续 Agent
    raw = raw_search(smoke_q, max_results=3)
    if not raw:
        print("未搜到相关结果，请检查网络/ddgs 安装")
        return
    print(format_results(raw))

    # --- Agent ---
    # TODO 10:
    tools = [get_current_time, web_search]
    agent = build_agent(build_llm(), tools)
    q_web = "最近发生了什么大事？"
    q_direct = "1+1等于几？请直接回答，不必搜索。"
    print("=== 应调 web_search ===")
    ask(agent, q_web)
    print("\n=== 应直接回答 ===")
    ask(agent, q_direct)


if __name__ == "__main__":
    main()

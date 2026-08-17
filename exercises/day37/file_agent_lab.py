"""
Day 37 · 文件操作工具（骨架 · 请自己填 TODO）

目标：
  1. safe_path：相对文件名 → 沙箱内绝对路径；逃出则拒绝
  2. @tool：list_dir / read_file / write_file
  3. 冒烟：列出、读 note.txt、故意 ../ 应被拒
  4. create_agent 总结 note.txt
  5. 打印 messages 类型，确认有 tool

对照：
  - D36：SQL 只允许 SELECT
  - D37：文件只允许 sandbox 目录

跑法：
  python exercises/day37/file_agent_lab.py
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# TODO 1: 补导入
#   - langchain.agents.create_agent
#   - langchain.tools.tool
#   - langchain_openai.ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

SANDBOX = Path(__file__).resolve().parent / "sandbox"


def safe_path(name: str) -> Path | None:
    """
    把用户给的文件名接到 SANDBOX 下，resolve 后再检查仍在沙箱内。
    合法 → 返回 Path；非法 / 试图逃出 → 返回 None。
    """
    # TODO 2:
    #   candidate = (SANDBOX / name).resolve()
    #   用 candidate.relative_to(SANDBOX.resolve()) 判断
    #   失败（ValueError）→ None
    #   空 name 或不安全字符可一并拒绝（可选）
    candidate = (SANDBOX / name).resolve()
    try:
        candidate.relative_to(SANDBOX.resolve())
    except ValueError:
        return None
    return candidate


# ---------- 工具 ----------


# TODO 3: 三个工具。docstring 写清：何时用、参数是沙箱内文件名、不要用于沙箱外。
#
@tool
def list_dir() -> str:
    """列出沙箱目录下的文件名。无参数。不要用于读取文件内容。"""
    return "\n".join(p.name for p in SANDBOX.iterdir())

@tool
def read_file(name: str) -> str:
    """读取沙箱内文本文件。参数 name: 文件名（如 note.txt）。不要用于写文件或读沙箱外路径。"""
#     若 p 是 None 或不是文件 → 返回拒绝说明
#     读 utf-8 文本返回
    p = safe_path(name)
    if p is None or not p.is_file():
        return "文件不存在"
    with open(p, "r", encoding="utf-8") as f:
        return f.read()
#
@tool
def write_file(name: str, content: str) -> str:
    """把文本写入沙箱内文件（覆盖）。只写沙箱。"""
#     同样先 safe_path
    p = safe_path(name)
    if p is None or not p.is_file():
        return "文件不存在"
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    return "文件写入成功"


def build_llm():
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 DEEPSEEK_API_KEY")
    # TODO 4: return ChatOpenAI(...)
    return ChatOpenAI(api_key=api_key, base_url=base_url, model=model)


def build_agent(llm, tools: list):
    # TODO 5:
    # prompt：只能通过工具操作 sandbox 里的文件；总结时先 read_file
    # 用户给的路径如果你觉得可疑，仍然调用工具（工具会拒绝），不要自己去读磁盘
    system_prompt = """
    只能通过工具操作 sandbox 里的文件；总结时先 read_file
    用户给的路径如果你觉得可疑，仍然调用工具（工具会拒绝），不要自己去读磁盘
    """
    return create_agent(llm, tools, system_prompt=system_prompt)


def ask(agent, question: str) -> None:
    # TODO 6: 同 D35/D36
    # result = agent.invoke({"messages":[{"role":"user","content": question}]})
    # result 是 dict；message 用 .type / .content
    try:
        result = agent.invoke({"messages":[{"role":"user","content": question}]})
        last = result["messages"][-1]
        print(last.content)
        print([message.type for message in result["messages"]])
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("Day 37 · 文件工具（沙箱）\n")
    SANDBOX.mkdir(parents=True, exist_ok=True)

    # --- 冒烟（不经 Agent）---
    print("=== 冒烟：列目录 ===")
    # TODO 7: print(list_dir.invoke({}))  或直接调底层函数
    print(list_dir.invoke({}))
    print("=== 冒烟：读 note.txt ===")
    print(read_file.invoke({"name": "note.txt"}))
    # TODO 8:
    print("=== 冒烟：拒绝逃出 ===")
    # TODO 9: print(safe_path("../CONTEXT.md"))  应是 None
    #         print(safe_path("note.txt"))       应是沙箱里的路径
    print(safe_path("../CONTEXT.md"))
    print(safe_path("note.txt"))

    # --- Agent ---
    # TODO 10:
    agent = build_agent(build_llm(), [list_dir, read_file, write_file])
    print("=== 应读文件并总结 ===")
    ask(agent, "请总结 sandbox 里 note.txt 的要点。")


if __name__ == "__main__":
    main()

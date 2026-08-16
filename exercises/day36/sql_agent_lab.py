"""
Day 36 · SQL Agent（骨架 · 请自己填 TODO）

目标：
  1. 建 SQLite 示例库（users 表 + 几行数据）
  2. 裸 SQL 冒烟：COUNT(*) 能查出人数
  3. @tool run_sql(sql)：只允许 SELECT，返回查询结果文本
  4. create_agent：自然语言 → SQL → 工具执行 → 回答
  5. 两问验收 + 打印 messages 里是否出现 tool

对照：
  - D34：非结构化文档检索
  - D35：外网搜索
  - D36：结构化表查询（Text-to-SQL）

跑法：
  python exercises/day36/sql_agent_lab.py
"""

from __future__ import annotations

import os
import sqlite3
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

DB_PATH = Path(__file__).resolve().parent / "demo.db"

SCHEMA_HINT = """
请遵循以下要求：
1. 先写 SELECT，再调 run_sql；根据工具返回回答
2. 闲聊/算术不要查库
表 users:
  - id INTEGER 主键
  - name TEXT 姓名
  - city TEXT 城市
"""


def init_db(path: Path) -> None:
    """
    若库不存在或你想重置：建 users 表并插入示例行。
    建议每次启动都重建，避免脏数据干扰验收。
    """
    # TODO 2:
    #   连接 sqlite3.connect(path)
    #   CREATE TABLE 若你选择先 DROP TABLE IF EXISTS users
    #   INSERT 至少 4 行，其中至少 2 人 city='广州'（方便第二问）
    #   commit + close
    with sqlite3.connect(path) as conn:
        conn.execute("DROP TABLE IF EXISTS users")
        conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, city TEXT)")
        conn.execute("INSERT INTO users (name, city) VALUES ('Alice', '广州')")
        conn.execute("INSERT INTO users (name, city) VALUES ('Bob', '北京')")
        conn.execute("INSERT INTO users (name, city) VALUES ('Charlie', '上海')")
        conn.execute("INSERT INTO users (name, city) VALUES ('David', '广州')")
        conn.commit()


def execute_select(sql: str) -> str:
    """
    真正跑 SQL。不是工具说明书；给工具内部调用。
    非 SELECT（忽略大小写、前后空格）→ 返回拒绝说明，不要执行。
    """
    # TODO 3:
    #   stripped = sql.strip()
    #   若不是以 SELECT 开头 → return "只允许 SELECT 查询"
    #   sqlite3.connect → execute → fetchall
    #   把行拼成字符串；无行则「查询无结果」
    #   try/except：SQL 写错时返回错误文字，程序不崩
    stripped = sql.strip()
    if not stripped.startswith("SELECT"):
        return "只允许 SELECT 查询"
    with sqlite3.connect(DB_PATH) as conn:
        try:
            cursor = conn.execute(stripped)
            result = cursor.fetchall()
            if not result:
                return "查询无结果"
            return "\n".join([str(row) for row in result])
        except Exception as e:
            return str(e)


# ---------- 工具 ----------


# TODO 4:
@tool
def run_sql(sql: str) -> str:
    """
    在本地 users 表上执行只读 SQL。
    何时用：问人数、名单、某个城市有谁 —— 需要查表时。
    参数 sql: 一条 SELECT 语句（不要写 DROP/DELETE/INSERT/UPDATE）。
    """
    return execute_select(sql)


def build_llm():
    """DeepSeek Chat。"""
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 DEEPSEEK_API_KEY")
    # TODO 5: return ChatOpenAI(..., temperature=0.1)  # SQL 宜低温度
    return ChatOpenAI(api_key=api_key, base_url=base_url, model=model, temperature=0.1)


def build_agent(llm, tools: list):
    """create_agent + system_prompt。"""
    # TODO 6:
    # 把 SCHEMA_HINT 写进 prompt，让模型知道有哪些列
    # 要求：先写 SELECT，再调 run_sql；根据工具返回回答
    # 闲聊/算术不要查库
    return create_agent(llm, tools, system_prompt=SCHEMA_HINT)


def ask(agent, question: str) -> None:
    """invoke，打印最终回答，并列出 messages 类型（看有没有 tool）。"""
    # messages 是对象：.type / .content
    # 容器 result 是 dict：result["messages"]
    # TODO 7: 参考 D35 ask；try/except
    try:
      result = agent.invoke({"messages":[{"role": "user", "content": question}]})
      last = result["messages"][-1]
      print(last.content)
      print([message.type for message in result["messages"]])
    except Exception as e:
      print(f"Error: {e}")


def main() -> None:
    print("Day 36 · SQL Agent\n")

    # --- 建库 + 冒烟（不经 Agent）---
    print("=== 建库 ===")
    # TODO 8: init_db(DB_PATH)
    #         print(execute_select("SELECT COUNT(*) FROM users;"))
    #         应能看到人数
    init_db(DB_PATH)
    print(execute_select("SELECT COUNT(*) FROM users;"))

    # --- Agent ---
    # TODO 9:
    agent = build_agent(build_llm(), [run_sql])
    print("=== 应查人数 ===")
    ask(agent, "有多少用户？")
    print("\n=== 应查城市 ===")
    ask(agent, "广州有几个用户？")


if __name__ == "__main__":
    main()

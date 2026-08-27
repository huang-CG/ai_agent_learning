"""
Day 43 · 智能文档助手 CLI（骨架 · 请自己填 TODO）

目标：
  1. 复用 D42：向量库 + 三工具 + create_agent
  2. 收紧 system_prompt（读文件不写死 memo.txt）
  3. ask：返回最终回答字符串；打印 type 轨迹；异常不崩
  4. run_cli：input 循环 + quit/exit/q + 空输入跳过 + 多轮 messages
  5.（可选）--demo：自动跑三问

对照：
  - D12：多轮 messages 历史
  - D42：三工具雏形
  - D43：交互 CLI 打磨完整

跑法：
  .\\venv\\Scripts\\python.exe exercises\\day43\\doc_assistant_cli.py
  .\\venv\\Scripts\\python.exe exercises\\day43\\doc_assistant_cli.py --demo
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# TODO 1: 补导入（与 D42 相同套件）
#   create_agent, tool, ChatOpenAI, OpenAIEmbeddings,
#   Document, InMemoryVectorStore, RecursiveCharacterTextSplitter,
#   PdfReader, DDGS
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from ddgs import DDGS

load_dotenv()

HERE = Path(__file__).resolve().parent
DOC_PATH = HERE.parent / "day32" / "sample_kb.pdf"
# 默认读 day42 沙箱；若你复制了 memo，也可改成 HERE / "sandbox"
SANqingzongDBOX = HERE.parent / "day42" / "sandbox"

VECTOR_STORE = None


def load_pdf(path: Path) -> str:
    """读取 PDF。不存在返回 ""。"""
    # TODO 2: 同 D42
    if not path.exists():
        print(f"文件不存在：{path}")
        return ""
    reader = PdfReader(str(path))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def build_embeddings():
    """硅基 Embedding。"""
    # TODO 3: 同 D42
    api_key = os.getenv("SILICONFLOW_API_KEY", "")
    base_url = os.getenv("SILICONFLOW_BASE_URL", "https://api.siliconflow.cn/v1")
    model = os.getenv("SILICONFLOW_EMBEDDING_MODEL", "BAAI/bge-m3")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 SILICONFLOW_API_KEY（DeepSeek Key 不能做 Embedding）")
    return OpenAIEmbeddings(model=model, base_url=base_url, api_key=api_key)


def build_vector_store():
    """Load→Split→Embed→InMemory。"""
    # TODO 4: 同 D42
    text = load_pdf(DOC_PATH)
    if not text:
        print("文件为空")
        return None
    document = Document(page_content=text)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=30)
    chunks = text_splitter.split_documents([document])
    embeddings = build_embeddings()
    return InMemoryVectorStore.from_documents(chunks, embeddings)


def safe_path(name: str) -> Path | None:
    """沙箱防逃逸。"""
    # TODO 5: 同 D37/D42
    candidate = (SANDBOX / name).resolve()
    try:
        candidate.relative_to(SANDBOX.resolve())
    except ValueError:
        return None
    return candidate


def raw_search(query: str, max_results: int = 5) -> list[dict]:
    # TODO 6
    try:
        with DDGS() as client:
            return list(client.text(query, max_results=max_results))
    except Exception as e:
        print(f"Error: {e}")
        return []


def format_results(results: list[dict]) -> str:
    # TODO 7
    if not results:
        return "未搜到相关结果"
    return "\n".join([f"标题: {result['title']}\n摘要: {result['body']}\n链接: {result['href']}" for result in results])


# ---------- 工具 ----------


# TODO 8–10: 三个 @tool（对照 D42；docstring 写清何时用/不要用于）
# search_knowledge / web_search / read_workspace_file
@tool
def search_knowledge(query: str) -> str:
    """本地知识库检索。何时用：青云助手设定、库内固定事实。不要用于新闻/实时。"""
    if VECTOR_STORE is None:
        return "向量库未初始化"
    results = VECTOR_STORE.similarity_search(query, k=3)
    if not results:
        return "未搜到相关结果"
    return "\n".join([result.page_content for result in results])
    results = raw_search(query)
    return format_results(results)

@tool
def web_search(query: str) -> str:
    """联网搜索。何时用：新闻、最新事实。不要用于库内设定题、简单算术。"""
    results = raw_search(query)
    return format_results(results)

@tool
def read_workspace_file(name: str) -> str:
    """读取 sandbox 内文本文件，供总结/摘录。参数 name 如 memo.txt。不要用于沙箱外。"""
    p = safe_path(name)
    if p is None or not p.is_file():
        return "文件不存在"
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


def build_llm():
    # TODO 11
    api_key = os.getenv("deepseek_api_key", "")
    base_url = os.getenv("deepseek_base_url", "https://api.deepseek.com")
    model = os.getenv("deepseek_model", "deepseek-chat")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 deepseek_api_key")
    return ChatOpenAI(api_key=api_key, base_url=base_url, model=model, temperature=0.2)

def build_agent(llm, tools: list):
    """create_agent；system_prompt 必须写宽：sandbox 内任意文本文件。"""
    # TODO 12:
    #   - RAG / 搜索 / 读文件 / 闲聊算术 的选型规则
    #   - 读文件：用 read_workspace_file，参数是文件名（如 memo.txt），不要写死「只能 memo」
    #   - 搜不到 / 读不到时诚实说明
    system_prompt = """
    你是一个智能文档助手，可以帮助用户回答问题。
    需要你根据用户的问题，选择合适的工具来回答问题。
    当用户的问题是关于知识库时，使用 search_knowledge 工具。
    （如：吉祥物 / 青云助手相关）
    当用户的问题是关于新闻时，使用 web_search 工具。
    （如：最新新闻）
    当用户的问题是关于总结 sandbox 里的任意文件时，使用 read_workspace_file 工具。
    （如：请总结 sandbox 里的 memo.txt）
    闲聊/算术可直接答。
    """
    return create_agent(model=llm, tools=tools, system_prompt=system_prompt)


def ask(agent, messages: list) -> list:
    """
    用「整段对话 messages」调用 agent。
    成功：打印最终回答 + type 列表；返回更新后的 messages（供下一轮）。
    失败：打印 Error: ...；返回原来的 messages（历史不丢）。
    """
    # TODO 13:
    try:
        result = agent.invoke({"messages": messages})
        new_messages = result["messages"]
        last = new_messages[-1]
        print(last.content)   # Message 对象用 .content
        print([m.type for m in new_messages])
        return new_messages
    except Exception as e:
        print(f"Error: {e}")
        return messages


def run_cli(agent) -> None:
    """交互主循环。"""
    print("智能文档助手 CLI（输入 quit / exit / q 退出）\n")
    # TODO 14:
    #   messages: list = []   # 多轮历史；首轮之前是空列表
    #   while True:
    #       text = input("你：").strip()
    #       若 text 小写 in {"quit","exit","q"} → 打印再见并 break
    #       若 text 为空 → print 提示，continue
    #       messages.append({"role":"user","content": text})
    #       messages = ask(agent, messages)
    messages: list = []
    while True:
        text = input("你：").strip()
        if text.lower() in {"quit","exit","q"}:
            print("再见")
            break
        if not text:
            print("请输入内容")
            continue
        messages.append({"role":"user","content": text})
        messages = ask(agent, messages)


def run_demo(agent) -> None:
    """可选：自动三问，不进交互。"""
    # TODO 15（可选，时间不够可先空实现 return）
    #   三问各 ask 一次；可用独立 messages=[] 每问重置，或一条龙多轮
    print("（可选 demo 未实现也可过主验收）")


def main() -> None:
    global VECTOR_STORE
    print("Day 43 · 智能文档助手 CLI\n")

    # TODO 16:
    #   VECTOR_STORE = build_vector_store()
    #   若为 None：打印错误并 return（别硬跑）
    #   tools = [...]
    #   agent = build_agent(build_llm(), tools)
    #   若 "--demo" in sys.argv → run_demo(agent)
    #   否则 → run_cli(agent)
    VECTOR_STORE = build_vector_store()
    if VECTOR_STORE is None:
        print("向量库初始化失败")
        return
    tools = [search_knowledge, web_search, read_workspace_file]
    agent = build_agent(build_llm(), tools)
    if "--demo" in sys.argv:
        run_demo(agent)
    else:
        run_cli(agent)


if __name__ == "__main__":
    main()

"""
Day 42 · 智能文档助手（骨架 · 请自己填 TODO）

目标：
  1. 启动时建向量库（复用 day32 PDF + 硅基 Embed + InMemory）
  2. 三个 @tool：search_knowledge / web_search / read_workspace_file
  3. create_agent + system_prompt（写清何时用哪个工具）
  4. 三问验收 + 打印 messages 类型

对照：
  - D34 RAG@tool、D35 web_search、D37 safe_path
  - 今天：三件套装同一个 Agent

跑法：
  .\\venv\\Scripts\\python.exe exercises\\day42\\doc_assistant.py
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# TODO 1: 补导入（按需）
#   langchain.agents.create_agent
from langchain.agents import create_agent
#   langchain.tools.tool
from langchain.tools import tool
#   langchain_openai.ChatOpenAI, OpenAIEmbeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
#   langchain_core.documents.Document
from langchain_core.documents import Document
#   langchain_core.vectorstores.InMemoryVectorStore
from langchain_core.vectorstores import InMemoryVectorStore
#   langchain_text_splitters.RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
#   pypdf.PdfReader
from pypdf import PdfReader
#   ddgs.DDGS
from ddgs import DDGS

load_dotenv()

HERE = Path(__file__).resolve().parent
DOC_PATH = HERE.parent / "day32" / "sample_kb.pdf"
SANDBOX = HERE / "sandbox"

# 模块级向量库：启动时建一次，工具里读它
VECTOR_STORE = None


def load_pdf(path: Path) -> str:
    """读取 PDF 全文。不存在则返回 ""。"""
    # TODO 2: 参考 D32/D34（exists → PdfReader → 拼页文本）
    if not path.exists():
        print(f"文件不存在：{path}")
        return ""
    reader = PdfReader(str(path))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def build_embeddings():
    """硅基流动 Embedding（DeepSeek 不能做 Embed）。"""
    # TODO 3: OpenAIEmbeddings(model, api_key, base_url)
    #   环境变量：SILICONFLOW_API_KEY / SILICONFLOW_BASE_URL / SILICONFLOW_EMBEDDING_MODEL
    api_key = os.getenv("SILICONFLOW_API_KEY", "")
    base_url = os.getenv("SILICONFLOW_BASE_URL", "https://api.siliconflow.cn/v1")
    model = os.getenv("SILICONFLOW_EMBEDDING_MODEL", "BAAI/bge-m3")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 SILICONFLOW_API_KEY（DeepSeek Key 不能做 Embedding）")
    return OpenAIEmbeddings(model=model, base_url=base_url, api_key=api_key)


def build_vector_store():
    """Load → Split → Embed → InMemoryVectorStore。"""
    # TODO 4:
    #   text = load_pdf(DOC_PATH)；空则 raise 或 print 后返回 None
    #   Document(page_content=text) + RecursiveCharacterTextSplitter(chunk_size≈150, overlap≈30)
    #   InMemoryVectorStore.from_documents(chunks, embedding=build_embeddings())
    text = load_pdf(DOC_PATH)
    if not text:
        print("文件为空")
        return None
    doc = Document(page_content=text)
    splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=30)
    chunks = splitter.split_documents([doc])
    return InMemoryVectorStore.from_documents(chunks, embedding=build_embeddings())


def safe_path(name: str) -> Path | None:
    """沙箱内相对文件名 → 绝对路径；逃出则 None。"""
    # TODO 5: 同 D37 —— (SANDBOX / name).resolve() + relative_to
    candidate = (SANDBOX / name).resolve()
    try:
        candidate.relative_to(SANDBOX.resolve())
    except ValueError:
        return None
    return candidate


def raw_search(query: str, max_results: int = 5) -> list[dict]:
    """裸调 ddgs；失败返回 []。"""
    # TODO 6: 参考 D35
    try:
        with DDGS() as client:
            return list(client.text(query, max_results=max_results))
    except Exception as e:
        print(f"Error: {e}")
        return []


def format_results(results: list[dict]) -> str:
    """搜索结果拼成可读文本。"""
    # TODO 7: 空 → 「未搜到」；否则 title/body/href
    if not results:
        return "未搜到相关结果"
    return "\n".join([f"标题: {result['title']}\n摘要: {result['body']}\n链接: {result['href']}" for result in results])


# ---------- 工具（docstring 写清：何时用 / 不要用于） ----------


# TODO 8:
@tool
def search_knowledge(query: str) -> str:
    """本地知识库检索。何时用：青云助手设定、库内固定事实。不要用于新闻/实时。"""
    # VECTOR_STORE.similarity_search(query, k=3) → 拼 page_content 后 return
    if VECTOR_STORE is None:
        return "向量库未初始化"
    results = VECTOR_STORE.similarity_search(query, k=3)
    if not results:
        return "未搜到相关结果"
    return "\n".join([result.page_content for result in results])

# TODO 9:
@tool
def web_search(query: str) -> str:
    """联网搜索。何时用：新闻、最新事实。不要用于库内设定题、简单算术。"""
    results = raw_search(query)
    return format_results(results)


# TODO 10:
@tool
def read_workspace_file(name: str) -> str:
    """读取 sandbox 内文本文件，供总结/摘录。参数 name 如 memo.txt。不要用于沙箱外。"""
#     # safe_path → 读 utf-8；失败 return 拒绝说明（必须 return，勿只 print）
    p = safe_path(name)
    if p is None or not p.is_file():
        return "文件不存在"
    with open(p, "r", encoding="utf-8") as f:
        return f.read()


def build_llm():
    """DeepSeek Chat。"""
    # TODO 11: ChatOpenAI(... temperature≈0.2)
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 DEEPSEEK_API_KEY")
    return ChatOpenAI(api_key=api_key, base_url=base_url, model=model, temperature=0.2)


def build_agent(llm, tools: list):
    """create_agent + system_prompt。"""
    # TODO 12: system_prompt 写清三工具选型，闲聊/算术可直接答
    # return create_agent(model=llm, tools=tools, system_prompt=...)
    system_prompt = """
    你是一个智能文档助手，可以帮助用户回答问题。
    需要你根据用户的问题，选择合适的工具来回答问题。
    当用户的问题是关于知识库时，使用 search_knowledge 工具。
    （如：吉祥物 / 青云助手相关）
    当用户的问题是关于新闻时，使用 web_search 工具。
    （如：最新新闻）
    当用户的问题是关于总结 sandbox 里的 memo.txt 时，使用 read_workspace_file 工具。
    （如：请总结 sandbox 里的 memo.txt）
    闲聊/算术可直接答。
    """
    return create_agent(model=llm, tools=tools, system_prompt=system_prompt)


def ask(agent, question: str) -> None:
    """invoke，打印最终回答 + messages 的 type 列表。"""
    # TODO 13:
    #   result = agent.invoke({"messages":[{"role":"user","content":question}]})
    #   last = result["messages"][-1]  → 用 .content
    #   print([m.type for m in result["messages"]])
    #   try/except，别让一整趟崩掉
    try:
        result = agent.invoke({"messages":[{"role":"user","content":question}]})
        last = result["messages"][-1]
        print(last.content)
        print([m.type for m in result["messages"]])
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("Day 42 · 智能文档助手（CLI 雏形）\n")

    global VECTOR_STORE
    # TODO 14:
    #   VECTOR_STORE = build_vector_store()
    #   tools = [search_knowledge, web_search, read_workspace_file]
    #   agent = build_agent(build_llm(), tools)
    #   三问：
    #     1) 知识库内（吉祥物 / 青云助手相关）
    #     2) 需要联网的新闻类
    #     3) 请总结 sandbox 里的 memo.txt
    #   每问 ask(...)
    VECTOR_STORE = build_vector_store()
    tools = [search_knowledge, web_search, read_workspace_file]
    agent = build_agent(build_llm(), tools)
    ask(agent, "吉祥物是什么？")
    ask(agent, "最新新闻是什么？")
    ask(agent, "请总结 sandbox 里的 memo.txt")
    ask(agent, "1+2+3+...+10=?")
    ask(agent, "你是谁？有什么能力？")


if __name__ == "__main__":
    main()

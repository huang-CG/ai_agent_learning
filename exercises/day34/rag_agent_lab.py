"""
Day 34 · RAG + Agent（骨架 · 请自己填 TODO）

目标：
  1. 启动时建好向量库（复用 D32/D33：PDF → 切块 → Embed → InMemory）
  2. @tool search_knowledge(query)：内部 similarity_search，返回文本片段
  3. 再准备 1 个非知识库工具（如 get_current_time）
  4. create_agent：让模型决定何时查库
  5. 两问验收 + 打印 messages 里是否出现 tool

对照：
  - D32：每次手动 Retrieve → Generate
  - D29：create_agent 闭环
  - D34：检索变成工具，按需调用

跑法：
  python exercises/day34/rag_agent_lab.py
"""

from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

# TODO 1: 补导入
#   - langchain.agents.create_agent
from langchain.agents import create_agent
#   - langchain.tools.tool
from langchain.tools import tool
#   - langchain_openai.ChatOpenAI, OpenAIEmbeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
#   - langchain_core.documents.Document
from langchain_core.documents import Document
#   - langchain_core.vectorstores.InMemoryVectorStore
from langchain_core.vectorstores import InMemoryVectorStore
#   - langchain_text_splitters.RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
#   - pypdf.PdfReader
from pypdf import PdfReader

load_dotenv()

DOC_PATH = Path(__file__).resolve().parent.parent / "day32" / "sample_kb.pdf"

# 模块级向量库，供工具闭包/全局使用（启动时初始化一次）
VECTOR_STORE = None


def load_pdf(path: Path) -> str:
    """读取 PDF。不存在则返回 ""。"""
    # TODO 2: 同 D32
    if not path.exists():
        print(f"文件不存在：{path}")
        return ""
    reader = PdfReader(str(path))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def build_embeddings():
    """硅基流动 Embedding（同 D32/D33；DeepSeek 不能做 Embed）。"""
    api_key = os.getenv("SILICONFLOW_API_KEY", "")
    base_url = os.getenv("SILICONFLOW_BASE_URL", "https://api.siliconflow.cn/v1")
    model = os.getenv("SILICONFLOW_EMBEDDING_MODEL", "BAAI/bge-m3")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 SILICONFLOW_API_KEY（DeepSeek Key 不能做 Embedding）")
    # TODO 3a: return OpenAIEmbeddings(model=..., api_key=..., base_url=...)
    return OpenAIEmbeddings(model=model, api_key=api_key, base_url=base_url)


def build_vector_store():
    """Load→Split→Embed→InMemory，返回 store。"""
    # TODO 3: 参考 D32/D33；chunk_size 可用 120～200
    # 提示：load_pdf → Document + splitter → build_embeddings() → InMemoryVectorStore
    text = load_pdf(DOC_PATH)
    docs = [Document(page_content=text, metadata={"source": str(DOC_PATH)})]
    splitter = RecursiveCharacterTextSplitter(chunk_size=120, chunk_overlap=20)
    chunks = splitter.split_documents(docs)
    embeddings = build_embeddings()
    store = InMemoryVectorStore.from_documents(chunks, embeddings)
    return store


# TODO 4: 写非 RAG 工具（示例：当前时间）
# @tool
# def get_current_time() -> str:
#     """... docstring：何时用 / 不要用于查知识库 ..."""
#     ...
@tool
def get_current_time() -> str:
    """
    获取当前时间
    何时用：当用户询问当前时间时使用
    不要用于：查知识库
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# TODO 5: 写 RAG 工具
@tool
def search_knowledge(query: str) -> str:
    """
    从本地学习站知识库检索相关片段。
    何时用：问题涉及吉祥物、毕业项目、答疑时间、站规等文档内容时。
    不要用于：普通闲聊、简单算术、与知识库无关的问题。
    """
#     若 VECTOR_STORE 为空 → 返回提示
#     docs = VECTOR_STORE.similarity_search(query, k=3)
#     拼接 page_content 返回；没有片段则返回「未检索到相关内容」
    if VECTOR_STORE is None:
        return "向量库未初始化"
    docs = VECTOR_STORE.similarity_search(query, k=3)
    if not docs:
        return "未检索到相关内容"
    return "\n".join([doc.page_content for doc in docs])


def build_llm():
    """DeepSeek Chat。"""
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 DEEPSEEK_API_KEY")
    # TODO 6: return ChatOpenAI(..., temperature=0.2)
    return ChatOpenAI(model=model, api_key=api_key, base_url=base_url, temperature=0.2)


def build_agent(llm, tools: list):
    """create_agent + system_prompt。"""
    # TODO 7:
    # system_prompt 写清：
    #   - 知识库相关问题先 search_knowledge
    #   - 无关问题直接答，不要硬查库
    #   - 查库后根据工具返回内容回答；没有就说没有
    # return create_agent(model=llm, tools=tools, system_prompt=...)
    system_prompt = """
    知识库相关问题先 search_knowledge
    无关问题直接答，不要硬查库
    查库后根据工具返回内容回答；没有就说没有
    """
    return create_agent(model=llm, tools=tools, system_prompt=system_prompt)


def ask(agent, question: str) -> None:
    """invoke，打印最终回答，并简要列出 messages 类型（看有没有 tool）。"""
    # messages 是 Message 对象：用 .type / .content，不要 message["type"]
    try:
        result = agent.invoke({"messages": [{"role": "user", "content": question}]})
        for message in result["messages"]:
            msg_type = getattr(message, "type", type(message).__name__)
            content = getattr(message, "content", "") or ""
            if msg_type == "tool":
                print(f"tool: {str(content)[:80]}")
            else:
                print(f"{msg_type}: {content}")
        last = result["messages"][-1]
        print(f"answer: {getattr(last, 'content', last)}")
    except Exception as e:
        print(f"出错: {e}")


def main() -> None:
    global VECTOR_STORE
    print("Day 34 · RAG + Agent\n")

    # TODO 9: 初始化
    print("正在构建向量库...")
    VECTOR_STORE = build_vector_store()
    tools = [get_current_time, search_knowledge]
    agent = build_agent(build_llm(), tools)

    # 验收问题
    q_kb = "学习站的吉祥物叫什么？它吃什么？"
    q_direct = "1+1等于几？请直接回答，不必查资料。"
    print("=== 应查知识库 ===")
    ask(agent, q_kb)
    print("\n=== 应直接回答 ===")
    ask(agent, q_direct)
    


if __name__ == "__main__":
    main()

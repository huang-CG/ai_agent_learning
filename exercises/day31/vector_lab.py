"""
Day 31 · Embedding + Chroma 向量库（骨架 · 请自己填 TODO）

目标：
  1. 复用 D30：加载 Markdown + 切块
  2. 用硅基流动 Embedding（OpenAI 兼容）把 chunks 变成向量
  3. 写入本地 Chroma
  4. similarity_search 取 top-3 并打印

对照：
  - D16：概念（Embedding / 向量 / top-k）；DeepSeek 无 Embedding
  - D30：Load + Split
  - D32：才会把检索结果交给 LLM 生成答案

跑法：
  pip install chromadb langchain-chroma
  配置 .env 里 SILICONFLOW_API_KEY
  python exercises/day31/vector_lab.py
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

from dotenv import load_dotenv

# TODO 1: 补导入
#   - langchain_core.documents.Document
from langchain_core.documents import Document
#   - langchain_text_splitters.RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
#   - langchain_openai.OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
#   - langchain_chroma.Chroma
# from langchain_chroma import Chroma
from langchain_core.vectorstores import InMemoryVectorStore

load_dotenv()

DOC_PATH = Path(__file__).resolve().parent.parent / "day30" / "sample_doc.md"
# 向量库落盘目录（可删了重跑）
CHROMA_DIR = Path(__file__).resolve().parent / "chroma_db"


def load_and_split(path: Path, chunk_size: int = 200, chunk_overlap: int = 40) -> list:
    """加载 md 并切块，返回 Document 列表。"""
    # TODO 2: 参考 D30
    # 若 path 不存在 → 打印提示 return []
    if not path.exists():
        print(f"文件不存在: {path}")
        return []
    # text = path.read_text(encoding="utf-8")
    # docs = [Document(page_content=text, metadata={"source": str(path)})]
    # splitter = RecursiveCharacterTextSplitter(chunk_size=..., chunk_overlap=...)
    # return splitter.split_documents(docs)
    text = path.read_text(encoding="utf-8")
    docs = [Document(page_content=text, metadata={"source": str(path)})]
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)


def build_embeddings():
    """创建 Embedding 客户端（硅基流动，OpenAI 兼容）。"""
    api_key = os.getenv("SILICONFLOW_API_KEY", "")
    base_url = os.getenv("SILICONFLOW_BASE_URL", "https://api.siliconflow.cn/v1")
    model = os.getenv("SILICONFLOW_EMBEDDING_MODEL", "BAAI/bge-m3")

    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请在 .env 配置 SILICONFLOW_API_KEY（DeepSeek Key 不能做 Embedding）")

    # TODO 3: return OpenAIEmbeddings(model=..., api_key=..., base_url=...)
    return OpenAIEmbeddings(model=model, api_key=api_key,base_url=base_url)


def build_vectorstore(chunks: list, embeddings):
    """把 chunks 写入 Chroma 并返回 vectorstore。"""
    # TODO 4:
    # 提示：Chroma.from_documents(
    #     documents=chunks,
    #     embedding=embeddings,
    #     persist_directory=str(CHROMA_DIR),
    # )
    # 若目录已存在想重跑：可先删 chroma_db 文件夹，或换 collection_name
    vectorstore = InMemoryVectorStore.from_documents(chunks, embeddings)
    return vectorstore


def search(vectorstore, query: str, k: int = 3) -> None:
    """相似度检索并打印 top-k。"""
    # TODO 5:
    # results = vectorstore.similarity_search(query, k=k)
    # 或 similarity_search_with_score(...)
    # 打印每条：排名、长度、前 100 字预览
    results = vectorstore.similarity_search(query, k=k)
    for i, result in enumerate(results):
        print(f"排名: {i+1}")
        print(f"长度: {len(result.page_content)}")
        print(f"前 100 字预览: {result.page_content[:100]}")
        print("-"*100)


def main() -> None:
    print("Day 31 · Embedding + Chroma\n")

    # TODO 6: 串起来
    # chunks = load_and_split(DOC_PATH)
    chunks = load_and_split(DOC_PATH)
    # print(f"切块数: {len(chunks)}")
    print(f"切块数: {len(chunks)}")
    # embeddings = build_embeddings()
    print("正在创建 Embedding 客户端...")
    embeddings = build_embeddings()
    # vs = build_vectorstore(chunks, embeddings)
    print("正在写入 Chroma...")
    vs = build_vectorstore(chunks, embeddings)
    print("写入完成，开始检索...")
    # search(vs, "什么是 RAG？为什么要切块？", k=3)
    search(vs, "什么是 RAG？为什么要切块？", k=3)
    # 再试一个问题，如：「番茄炒蛋怎么做？」
    search(vs, "番茄炒蛋怎么做？", k=3)


if __name__ == "__main__":
    main()

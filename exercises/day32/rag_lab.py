"""
Day 32 · 完整 RAG 管道（关键路径 · 骨架 · 请自己填 TODO）

流水线：
  Load → Split → Embed → Store → Retrieve → Generate
                                              ▲
                                           今天补上这步

对照：
  - D17：整份文档拼进 Prompt（无检索）
  - D30：Load + Split
  - D31：Embed + Store + Retrieve（InMemory）
  - D32：把 top-k 片段 + 问题交给 DeepSeek 生成答案

跑法：
  pip install pypdf
  配置 .env：DEEPSEEK_API_KEY + SILICONFLOW_API_KEY
  python exercises/day32/rag_lab.py
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# TODO 1: 补导入
#   - langchain_core.documents.Document
from langchain_core.documents import Document
#   - langchain_text_splitters.RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
#   - langchain_openai.OpenAIEmbeddings, ChatOpenAI
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
#   - langchain_core.vectorstores.InMemoryVectorStore
from langchain_core.vectorstores import InMemoryVectorStore
#   - pypdf.PdfReader（读 PDF 文本；不必上 langchain_community）
from pypdf import PdfReader

load_dotenv()

DOC_PATH = Path(__file__).resolve().parent / "sample_kb.pdf"


def load_pdf(path: Path) -> str:
    """读取 PDF 全文。文件不存在 → 打印提示并返回空串。"""
    # TODO 2:
    # if not path.exists(): ...
    # reader = PdfReader(str(path))
    # 拼所有 page.extract_text()（注意 None）
    # return 全文
    if not path.exists():
        print(f"文件不存在：{path}")
        return ""
    reader = PdfReader(str(path))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def split_text(text: str, chunk_size: int, chunk_overlap: int) -> list:
    """切块，返回 Document 列表。metadata 建议带 source。"""
    # TODO 3: 参考 D30 / D31
    # docs = [Document(page_content=text, metadata={"source": str(DOC_PATH)})]
    # splitter = RecursiveCharacterTextSplitter(...)
    # return splitter.split_documents(docs)
    doc = Document(page_content=text, metadata={"source": str(DOC_PATH)})
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents([doc])


def build_embeddings():
    """硅基流动 Embedding（同 D31）。"""
    api_key = os.getenv("SILICONFLOW_API_KEY", "")
    base_url = os.getenv("SILICONFLOW_BASE_URL", "https://api.siliconflow.cn/v1")
    model = os.getenv("SILICONFLOW_EMBEDDING_MODEL", "BAAI/bge-m3")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 SILICONFLOW_API_KEY（DeepSeek Key 不能做 Embedding）")
    # TODO 4: return OpenAIEmbeddings(...)
    return OpenAIEmbeddings(model=model, api_key=api_key, base_url=base_url)


def build_llm():
    """DeepSeek Chat（同 D26/D29）。"""
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 DEEPSEEK_API_KEY")
    # TODO 5: return ChatOpenAI(..., temperature=0.2)
    return ChatOpenAI(model=model, api_key=api_key, base_url=base_url, temperature=0.2)


def build_store(chunks: list, embeddings):
    """写入 InMemoryVectorStore（同 D31，避开 Chroma 崩溃）。"""
    # TODO 6: return InMemoryVectorStore.from_documents(chunks, embeddings)
    return InMemoryVectorStore.from_documents(chunks, embeddings)


def retrieve(store, question: str, k: int = 3) -> list:
    """相似度检索 top-k，返回 Document 列表。"""
    # TODO 7: return store.similarity_search(question, k=k)
    return store.similarity_search(question, k=k)


def generate(llm, question: str, docs: list) -> str:
    """把检索片段拼进 Prompt，调用 LLM 生成答案。"""
    # TODO 8:
    # context = "\n\n".join(d.page_content for d in docs)
    # prompt 要求：只根据参考片段回答；没有就说「文档中没有提及」
    # resp = llm.invoke(prompt) 或 messages
    # return resp.content
    context = "\n\n".join(d.page_content for d in docs)
    prompt = f"""
    你是一个知识库助手。
    问题：{question}。
    请根据以下文档内容回答问题：{context}。
    请只根据参考片段回答，不要编造。如果文档中没有相关信息，请回答「文档中没有提及」。
    """
    resp = llm.invoke(prompt)
    return resp.content


def run_rag(question: str, chunk_size: int, chunk_overlap: int = 40, k: int = 3) -> str:
    """完整管道：Load→Split→Embed→Store→Retrieve→Generate。"""
    # TODO 9: 串起来并打印：切块数、每条检索预览（前 80 字）、最终答案
    chunks = split_text(load_pdf(DOC_PATH), chunk_size, chunk_overlap)
    embeddings = build_embeddings()
    store = build_store(chunks, embeddings)
    docs = retrieve(store, question, k)
    llm = build_llm()
    answer = generate(llm, question, docs)
    print(f"切块数: {len(chunks)}")
    for doc in docs:
        print(f"检索预览: {doc.page_content[:80]}")
    print(f"最终答案: {answer}")
    print("-" * 100)
    return answer


def main() -> None:
    print("Day 32 · 完整 RAG 管道（关键路径）\n")

    # 验收问题（文档里有明确答案）
    q1 = "学习站的吉祥物叫什么？它吃什么？"
    q2 = "毕业项目代号是什么？有什么硬性要求？"
    # 文档没有的问题（应拒绝编造）
    q3 = "学习站的月费是多少？"

    # TODO 10: 先用 chunk_size=200 跑 q1/q2/q3
    # 再用 chunk_size=80 跑同一题，口头对比：切块更碎时答案是否变差/变好？
    print("（填完 TODO 后取消注释下面调用）")
    print("=== chunk_size=200 ===")
    run_rag(q1, chunk_size=200)
    run_rag(q2, chunk_size=200)
    run_rag(q3, chunk_size=200)
    print("\n=== chunk_size=80 ===")
    run_rag(q1, chunk_size=80, chunk_overlap=20)


if __name__ == "__main__":
    main()

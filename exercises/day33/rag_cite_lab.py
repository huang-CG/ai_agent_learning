"""
Day 33 · RAG 优化（骨架 · 请自己填 TODO）

在 D32 完整管道上增加：
  1) 切块 metadata：source / chunk_id / topic
  2) 回答带出处（片段编号 + 文件名）
  3) 无答案时固定拒编话术
  4) 可选：按 metadata 过滤后再检索

对照：
  - D32：能答对
  - D33：答对 + 可追溯 + 过滤干扰段

跑法：
  python exercises/day33/rag_cite_lab.py
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# TODO 1: 补导入（同 D32）
# Document, RecursiveCharacterTextSplitter, OpenAIEmbeddings, ChatOpenAI,
# InMemoryVectorStore, PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.vectorstores import InMemoryVectorStore
from pypdf import PdfReader

load_dotenv()

DOC_PATH = Path(__file__).resolve().parent.parent / "day32" / "sample_kb.pdf"


def load_pdf(path: Path) -> str:
    """读取 PDF 全文。不存在则提示并返回 ""。"""
    # TODO 2: 同 D32
    if not path.exists():
        print(f"文件不存在：{path}")
        return ""
    reader = PdfReader(str(path))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def guess_topic(text: str) -> str:
    """根据片段内容打一个粗标签，供 metadata 过滤用。"""
    # TODO 3: 简单规则即可，例如：
    # 含「番茄」「苹果」「烹饪」→ "cooking"
    # 含「吉祥物」「毕业」「答疑」「API Key」「学习时长」→ "rules"
    # 否则 → "other"
    if "番茄" in text or "苹果" in text or "烹饪" in text:
        return "cooking"
    elif "吉祥物" in text or "毕业" in text or "答疑" in text or "API Key" in text or "学习时长" in text:
        return "rules"
    else:
        return "other"


def split_text(text: str, chunk_size: int = 120, chunk_overlap: int = 30) -> list:
    """切块，并为每块写入 metadata。"""
    # TODO 4:
    # 1) Document(page_content=text, metadata={"source": DOC_PATH.name})
    document = Document(page_content=text, metadata={"source": DOC_PATH.name})
    # 2) splitter.split_documents(...)
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    # 3) 遍历 chunks，补：
    #      metadata["chunk_id"] = i
    #      metadata["topic"] = guess_topic(chunk.page_content)
    chunks = splitter.split_documents([document])
    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i
        chunk.metadata["topic"] = guess_topic(chunk.page_content)
    # 4) return chunks
    return chunks


def build_embeddings():
    """硅基流动 Embedding（同 D32）。"""
    api_key = os.getenv("SILICONFLOW_API_KEY", "")
    base_url = os.getenv("SILICONFLOW_BASE_URL", "https://api.siliconflow.cn/v1")
    model = os.getenv("SILICONFLOW_EMBEDDING_MODEL", "BAAI/bge-m3")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 SILICONFLOW_API_KEY")
    # TODO 5: return OpenAIEmbeddings(...)
    return OpenAIEmbeddings(model=model, api_key=api_key, base_url=base_url)


def build_llm():
    """DeepSeek Chat（同 D32）。"""
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 DEEPSEEK_API_KEY")
    # TODO 6: return ChatOpenAI(..., temperature=0.2)
    return ChatOpenAI(model=model, api_key=api_key, base_url=base_url, temperature=0.2)


def build_store(chunks: list, embeddings):
    # TODO 7: InMemoryVectorStore.from_documents(...)
    return InMemoryVectorStore.from_documents(chunks, embeddings)


def retrieve(store, question: str, k: int = 3, topic: str | None = None) -> list:
    """检索 top-k；若 topic 给定，只保留 metadata['topic']==topic 的结果。"""
    # TODO 8:
    # docs = store.similarity_search(question, k=k)  # 可先多取一点再过滤，如 k*3
    docs = store.similarity_search(question, k=k*3)
    # 若 topic：docs = [d for d in docs if d.metadata.get("topic") == topic][:k]
    if topic:
        docs = [d for d in docs if d.metadata.get("topic") == topic][:k]
    # return docs
    return docs


def format_context(docs: list) -> str:
    """把片段编成 [1] [2] ... 方便模型引用。"""
    # TODO 9:
    # 每段类似：
    # [1] (source=sample_kb.pdf, chunk_id=2, topic=rules)
    # 片段正文...
    parts = []
    for i, d in enumerate(docs, start=1):
        meta = d.metadata
        header = f"[{i}] (source={meta.get('source')}, chunk_id={meta.get('chunk_id')}, topic={meta.get('topic')})"
        parts.append(header + "\n" + d.page_content)
    return "\n\n".join(parts)


def format_sources(docs: list) -> str:
    """用代码打印出处（不依赖模型记性）。"""
    # TODO 10: 返回多行字符串，例如：
    # [1] sample_kb.pdf #2 (rules)
    # [2] ...
    parts = []
    for i, d in enumerate(docs, start=1):
        meta = d.metadata
        parts.append(f"[{i}] {meta.get('source')} #{meta.get('chunk_id')} ({meta.get('topic')})")
    return "\n".join(parts)


def generate(llm, question: str, docs: list) -> str:
    """根据带编号的 context 生成答案；要求引用 [n]；没有则固定拒答。"""
    # TODO 11:
    # 若 docs 为空 → 直接 return "文档中没有提及"
    if not docs:
        return "文档中没有提及"
    # context = format_context(docs)
    context = format_context(docs)
    # prompt 要求：
    #   - 只根据参考片段回答
    #   - 答案末尾用「出处：[1][2]」这种形式标注
    #   - 没有相关信息 → 只回答「文档中没有提及」（不要编造）
    prompt = f"""
    你是一个知识库助手。
    问题：{question}。
    请根据以下文档内容回答问题：{context}。
    请只根据参考片段回答，不要编造。如果文档中没有相关信息，请回答「文档中没有提及」。
    请在答案末尾用「出处：[1][2]」这种形式标注。
    若回答「文档中没有提及」,不要写出处。
    """
    resp = llm.invoke(prompt)
    return resp.content


def run_rag(
    question: str,
    *,
    topic: str | None = None,
    chunk_size: int = 120,
    k: int = 3,
) -> str:
    """串起来：并打印检索预览、代码侧出处、模型答案。"""
    # TODO 12:
    # chunks = split_text(load_pdf(DOC_PATH), chunk_size=chunk_size)
    # store = build_store(chunks, build_embeddings())
    # docs = retrieve(store, question, k=k, topic=topic)
    # answer = generate(build_llm(), question, docs)
    # 打印：切块数、过滤条件、每条预览、format_sources(docs)、answer
    # return answer
    chunks = split_text(load_pdf(DOC_PATH), chunk_size=chunk_size)
    store = build_store(chunks, build_embeddings())
    docs = retrieve(store, question, k=k, topic=topic)
    answer = generate(build_llm(), question, docs)
    print(f"切块数：{len(chunks)}")
    print(f"过滤条件：{topic}")
    print(f"每条预览：{format_context(docs)}")
    print(f"出处：{format_sources(docs)}")
    print(f"答案：{answer}")


def main() -> None:
    print("Day 33 · RAG 优化（引用 / 无答案 / metadata）\n")

    q1 = "学习站的吉祥物叫什么？它吃什么？"
    q2 = "学习站的月费是多少？"
    q3 = "番茄炒蛋怎么做？"  # 文档有，但应用 topic=rules 过滤后应「没有」或检不到菜谱

    # TODO 13: 取消注释跑验收
    print("=== 带引用：吉祥物 ===")
    run_rag(q1, topic="rules")
    print("\n=== 无答案：月费 ===")
    run_rag(q2, topic="rules")
    print("\n=== metadata 过滤：问烹饪但只查 rules ===")
    run_rag(q3, topic="rules")


if __name__ == "__main__":
    main()

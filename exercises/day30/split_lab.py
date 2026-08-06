"""
Day 30 · 文档加载与分割（骨架 · 请自己填 TODO）

目标：
  1. 读取本地 Markdown 为 Document（或 documents 列表）
  2. 用 RecursiveCharacterTextSplitter 切块
  3. 打印：块数、每块长度、前几块内容预览
  4. （建议）换一组 chunk_size / chunk_overlap 再跑一次，对比块数

对照：
  - D16/D17：RAG 概念、拼 Prompt
  - 今天只做 Load + Split；Embedding / 向量库是 D31

跑法：
  pip install langchain-text-splitters
  python exercises/day30/split_lab.py
"""

from __future__ import annotations

from pathlib import Path

# TODO 1: 补导入
#   - from langchain_core.documents import Document
from langchain_core.documents import Document
#   - from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
# 样例文档路径（相对项目根目录运行）
DOC_PATH = Path(__file__).resolve().parent / "sample_doc.md"


def load_markdown(path: Path) -> list:
    """加载 Markdown，返回 Document 列表（今天可以只有 1 个 Document）。"""
    # TODO 2:
    # text = path.read_text(encoding="utf-8")
    text = path.read_text(encoding="utf-8")
    # 若文件不存在，打印提示并 return []
    if not text:
        print(f"文件 {path} 不存在")
        return []
    # return [Document(page_content=text, metadata={"source": str(path)})]
    return [Document(page_content=text, metadata={"source": str(path)})]


def split_documents(docs: list, chunk_size: int = 200, chunk_overlap: int = 40) -> list:
    """把 Document 列表切成更小的 chunks。"""
    # TODO 3:
    # splitter = RecursiveCharacterTextSplitter(
    #     chunk_size=chunk_size,
    #     chunk_overlap=chunk_overlap,
    # )
    # return splitter.split_documents(docs)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_documents(docs)

def print_stats(chunks: list, title: str = "") -> None:
    """打印切块统计与预览。"""
    # TODO 4:
    # 打印 title、总块数
    print(f"{title}总块数：{len(chunks)}")
    # 对每个 chunk：打印 index、len(page_content)、metadata
    for index, chunk in enumerate(chunks):
        print(f"块 {index}：长度 {len(chunk.page_content)}，metadata {chunk.metadata}")
    # 前 2～3 块打印 page_content 的前 80 个字符（后面加 ...）
    for index, chunk in enumerate(chunks[:3]):
        print(f"块 {index}：内容 {chunk.page_content[:80]}...")
    print()


def main() -> None:
    print("Day 30 · Document Load & Split\n")

    docs = load_markdown(DOC_PATH)
    if not docs:
        print("未加载到文档")
        return

    # TODO 5: 第一组参数切块并 print_stats

    chunks = split_documents(docs, chunk_size=200, chunk_overlap=40)
    print_stats(chunks, title="size=200 overlap=40")

    # TODO 6（建议）：换参数再跑一组，例如 size=100 overlap=20
    # 观察：块数变多还是变少？边界处句子是否更碎？
    chunks = split_documents(docs, chunk_size=100, chunk_overlap=20)
    print_stats(chunks, title="size=100 overlap=20")
    print()
    


if __name__ == "__main__":
    main()

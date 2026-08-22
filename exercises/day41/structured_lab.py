"""
Day 41 · 结构化输出（骨架 · 请自己填 TODO）

目标：
  1. 用 Pydantic BaseModel 定义报告字段（含约束）
  2. ChatOpenAI.with_structured_output(...) 拿到模型对象
  3. 至少两问：打印类型 + model_dump()
  4. （可选）本地 ValidationError：非法 priority

对照：
  - D38：Prompt 逼 JSON + json.loads
  - D41：Schema 先定好，框架帮你解析并校验

跑法：
  python exercises/day41/structured_lab.py
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

# TODO 1: 补导入
#   - pydantic: BaseModel, Field
#   - langchain_openai.ChatOpenAI
#   - （可选）pydantic.ValidationError 做失败实验
from pydantic import BaseModel, Field, ValidationError
from langchain_openai import ChatOpenAI
from typing import Literal


load_dotenv()

QUESTIONS = [
    "今天天气真好，广场有人跳舞。",
    "我的订单两周了还没发货，要投诉。",
]


# TODO 2: 定义 TicketReport(BaseModel)
#   label: str  —— Field 里 description 写清：只能是 闲聊/投诉/咨询
#   reason: str
#   priority: int —— 用 Field(ge=1, le=3) 或等价约束
# 提示：可用 Literal["闲聊", "投诉", "咨询"] 钉死 label（若会用）
class TicketReport(BaseModel):
    label: Literal["闲聊", "投诉", "咨询"]
    reason: str
    priority: int = Field(ge=1, le=3)


def build_structured_llm():
    api_key = os.getenv("DEEPSEEK_API_KEY", "")
    base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    if not api_key or api_key.startswith("sk-your"):
        raise RuntimeError("请配置 DEEPSEEK_API_KEY")

    # TODO 3:
    #   llm = ChatOpenAI(..., temperature=0)
    #   return llm.with_structured_output(TicketReport, method="function_calling")
    # DeepSeek：优先 function_calling；json_schema 若不支持再换回
    llm = ChatOpenAI(api_key=api_key, base_url=base_url, model=model, temperature=0)
    return llm.with_structured_output(TicketReport, method="function_calling")


def run_questions(structured_llm) -> None:
    """对 QUESTIONS 逐条 invoke，打印类型与 model_dump。"""
    # TODO 4:
    #   for q in QUESTIONS:
    #       result = structured_llm.invoke(f"请根据用户话生成客服工单报告。\n用户：{q}")
    #       print(type(result), result.model_dump())
    # 若 result 不是 TicketReport，说明 structured 没接上
    for q in QUESTIONS:
        result = structured_llm.invoke(f"请根据用户话生成客服工单报告。\n用户：{q}")
        if not isinstance(result, TicketReport):
            raise ValueError("structured 没接上")
        print(type(result), result.model_dump())


def demo_validation_error() -> None:
    """不调模型：故意用非法数据构造 TicketReport，应抛 ValidationError。"""
    # TODO 5（可选但建议）：
    #   try:
    #       TicketReport(label="闲聊", reason="ok", priority=9)
    #   except ValidationError as e:
    #       print("校验失败（预期）:", e)
    try:
        TicketReport(label="闲聊", reason="ok", priority=9)
    except ValidationError as e:
        print("校验失败（预期）:", e)


def main() -> None:
    print("Day 41 · structured output\n")
    # TODO 6: build → run_questions → demo_validation_error
    structured_llm = build_structured_llm()
    run_questions(structured_llm)
    demo_validation_error()

if __name__ == "__main__":
    main()

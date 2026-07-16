"""
Day 15 练习：Function Calling 实战

两个真工具：
  - get_current_time：当前时间
  - calculator：计算简单算术表达式

流程（D14）：发 messages+tools → 看 tool_calls → 执行函数
       → role:tool 回传 → 再请求 → 打印最终回答

重要：模型可能连续多轮 tool_calls；必须循环到拿到最终 content 为止。
旧版只处理一轮，第二轮若仍是 tool_calls 且 content 为空，
会提前出现「你：」提示，看起来像程序自己在刷。
"""

from __future__ import annotations

import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
MODEL = "deepseek-chat"


# ---------- ① 真函数（厨房：模型调不到，只有你的程序能跑）----------

def get_current_time() -> str:
    """返回当前本地日期时间字符串。"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculator(expression: str) -> str:
    """
    计算只含数字和 + - * / ( ) 的表达式。
    注意：生产环境不要用 eval；这里用受限方式演示。
    """
    allowed = set("0123456789+-*/(). %")
    if not expression or any(ch not in allowed for ch in expression):
        return "错误：表达式只能包含数字和 + - * / ( ) 空格"
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"计算失败: {e}"


TOOL_IMPL = {
    "get_current_time": lambda **kwargs: get_current_time(),
    "calculator": lambda **kwargs: calculator(kwargs.get("expression", "")),
}

SYSTEM_PROMPT = """你是助手。规则：
1. 用户问时间、日期、几点、今天几号 → 必须调用 get_current_time，禁止自己编造时间。
2. 用户要求计算、算一下、求值 → 必须调用 calculator，禁止口算。
3. 普通闲聊 → 不调用工具，直接简短回答。
"""


# ---------- ② tools 说明书（菜单）----------

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": (
                "获取当前真实日期和时间。"
                "凡是用户问现在几点、当前时间、今天日期、星期几，都必须调用本工具；"
                "不要凭记忆回答时间。"
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "计算数学表达式，支持加减乘除和括号。用户要求算数、计算、求值时使用。",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "数学表达式，例如 (3+5)*2 或 10/4",
                    }
                },
                "required": ["expression"],
            },
        },
    },
]


# ---------- ③ 发请求（≈ 官方 send_messages）----------

def chat(messages: list[dict]) -> tuple[dict, str | None]:
    """返回 (message, finish_reason)。"""
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        raise RuntimeError("请先在 .env 中配置 DEEPSEEK_API_KEY")

    url = f"{DEEPSEEK_BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "model": MODEL,
        "messages": messages,
        "tools": TOOLS,
        "tool_choice": "auto",
    }
    response = requests.post(url, headers=headers, json=body, timeout=60)
    response.raise_for_status()
    choice = response.json()["choices"][0]
    return choice["message"], choice.get("finish_reason")


def run_tool(name: str, arguments_json: str) -> str:
    """解析 arguments → 调用对应 Python 函数 → 返回字符串结果。"""
    try:
        args = json.loads(arguments_json) if arguments_json else {}
    except json.JSONDecodeError:
        return f"错误：无法解析参数 JSON: {arguments_json}"

    if name not in TOOL_IMPL:
        return f"错误：未知工具 {name}"

    return str(TOOL_IMPL[name](**args))


def message_to_dict(message: dict) -> dict:
    """把 API 的 assistant message（含 tool_calls）原样转为可回传的 dict。"""
    out: dict = {
        "role": message.get("role", "assistant"),
        "content": message.get("content"),  # 即使是 null 也保留
    }
    if message.get("tool_calls"):
        out["tool_calls"] = message["tool_calls"]
    return out


def chat_with_tools(user_text: str) -> str:
    """
    完整一轮：用户一句话 →（可能多轮调工具）→ 最终自然语言回答。
    """
    messages: list[dict] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_text},#将问题塞进messages中的user角色中
    ]

    # 最多允许 5 次「点菜+做菜」，防止模型反复调工具死循环（不是用户聊 5 句）
    max_tool_rounds = 5
    for round_idx in range(1, max_tool_rounds + 1):
        print(
            f"  [调试][pid={os.getpid()}] 第 {round_idx} 次请求模型…",
            flush=True,
        )
        # 每一轮都一样：① chat 发请求 → ② 有 tool_calls 就执行 → ③ 再循环 chat
        # 第 1 轮也可能调工具；后面某轮没有 tool_calls 时，content 就是最终回答
        message, finish_reason = chat(messages)
        tool_calls = message.get("tool_calls") or []

        print(
            f"  [调试][pid={os.getpid()}] finish_reason={finish_reason!r}, "
            f"tool_calls={len(tool_calls)}, content={message.get('content')!r}",
            flush=True,
        )

        # ① 没有工具：直接返回最终回答，结束本轮用户提问
        if not tool_calls:
            return message.get("content") or ""

        # ② 有工具：把「点菜」的 assistant 记入历史，再执行并塞 role:tool
        messages.append(message_to_dict(message))
        for call in tool_calls:
            fn = call["function"]
            print(f"         → {fn['name']}({fn.get('arguments', '')})", flush=True)
            result = run_tool(fn["name"], fn.get("arguments") or "{}")
            print(f"         ← 结果: {result}", flush=True)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call["id"],
                    "content": result,
                }
            )

        # ③ 工具结果已进 messages，进入下一轮 for → 再 chat
        print(
            f"  [调试][pid={os.getpid()}] 工具已执行，继续请求模型生成最终回答…",
            flush=True,
        )

    return "错误：工具调用轮数过多，已中止。"


def main() -> None:
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY", flush=True)
        return

    print(f"Day 15 · Function Calling 实战  [pid={os.getpid()}]", flush=True)
    print(
        "输入 quit/exit 退出；试试：现在几点了？ / 帮我算 (3+5)*2 / 你好\n",
        flush=True,
    )

    while True:
        question = input("你：").strip()
        if not question:
            print("问题不能为空", flush=True)
            continue
        if question.lower() in ("quit", "exit"):
            print("再见！", flush=True)
            break
        try:
            answer = chat_with_tools(question)
            if answer:
                print(f"AI：{answer}\n", flush=True)
            else:
                print("AI：（空响应）\n", flush=True)
        except requests.RequestException as e:
            print(f"请求失败: {e}\n", flush=True)
        except RuntimeError as e:
            print(f"{e}\n", flush=True)


if __name__ == "__main__":
    main()

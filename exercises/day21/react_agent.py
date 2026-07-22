"""
Day 21 · 手写 ReAct Agent（一）

不含真实工具：simulate_tool 返回假 Observation。
验收：主循环能跑多轮，max_steps 可停。

D22：把 simulate_tool 换成真天气 API。
"""

from __future__ import annotations

import os
import re

import requests
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
MODEL = "deepseek-chat"

# 要求模型严格按此格式输出（Thought/Action 或 Final Answer）
REACT_SYSTEM = """你是 ReAct 助手。每次回复必须且只能使用下列格式之一。

格式 A（还需要调工具）：
Thought: （简短推理，不要编造工具结果）
Action: 工具名[参数]

格式 B（信息已够）：
Thought: （简短总结）
Final Answer: （给用户的最终回答）

可用工具（今日为模拟，参数写在方括号里）：
- get_weather[城市]  例：get_weather[广州]
- calculator[表达式]  例：calculator[(3+5)*2]
- web_search[关键词]  例：web_search[DeepSeek 新闻]

规则：
1. 一次只写一个 Thought + 一个 Action，或 Thought + Final Answer
2. Action 必须用 工具名[参数]，不要编造 Observation
3. 需要实时信息或计算时必须 Action，不要直接 Final Answer 瞎编
"""

# 假工具库（D21 模拟；D22 换真 API）
FAKE_TOOL_RESULTS = {
    ("get_weather", "广州"): "广州：晴，28℃，湿度 65%",
    ("get_weather", "北京"): "北京：阴，22℃，湿度 50%",
    ("get_weather", "深圳"): "深圳：多云，30℃，湿度 70%",
    ("calculator", "(3+5)*2"): "16",
    ("calculator", "10/4"): "2.5",
    ("web_search", "DeepSeek"): "DeepSeek 是国产大模型公司，提供 Chat API。",
}


def chat(messages: list[dict]) -> str:
    """发一轮请求，返回 assistant 文本。"""
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
        "temperature": 0.3,
    }
    response = requests.post(url, headers=headers, json=body, timeout=60)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"] or ""


def parse_react(text: str) -> dict:
    """
    从 LLM 输出解析 ReAct 字段。
    返回 dict，可能含：thought, action, final_answer（未出现的键为 None）
    """
    result: dict[str, str | None] = {
        "thought": None,
        "action": None,
        "final_answer": None,
    }

    # Final Answer 优先（有了就结束循环）
    m_final = re.search(r"Final Answer:\s*(.+)", text, re.DOTALL | re.IGNORECASE)
    if m_final:
        result["final_answer"] = m_final.group(1).strip()
        # 仍尝试抓 Thought
        m_th = re.search(r"Thought:\s*(.+?)(?=Final Answer:|$)", text, re.DOTALL | re.IGNORECASE)
        if m_th:
            result["thought"] = m_th.group(1).strip()
        return result

    m_th = re.search(r"Thought:\s*(.+?)(?=Action:|$)", text, re.DOTALL | re.IGNORECASE)
    if m_th:
        result["thought"] = m_th.group(1).strip()

    m_act = re.search(r"Action:\s*(.+)", text, re.IGNORECASE)
    if m_act:
        result["action"] = m_act.group(1).strip().split("\n")[0].strip()

    return result


def parse_action(action_line: str) -> tuple[str, str]:
    """
  解析 Action 行：get_weather[广州] → ("get_weather", "广州")
  也兼容 get_weather(广州)
    """
    action_line = action_line.strip()
    m = re.match(r"^(\w+)\s*\[(.+)\]\s*$", action_line)
    if m:
        return m.group(1), m.group(2).strip()

    m = re.match(r"^(\w+)\s*\((.+)\)\s*$", action_line)
    if m:
        return m.group(1), m.group(2).strip()

    raise ValueError(f"无法解析 Action: {action_line!r}")


def simulate_tool(tool_name: str, tool_arg: str) -> str:
    """模拟工具执行，返回 Observation 文本。"""
    # 统一去掉首尾空格，避免匹配不到假数据
    tool_arg = tool_arg.strip()

    key = (tool_name, tool_arg)
    if key in FAKE_TOOL_RESULTS:
        return FAKE_TOOL_RESULTS[key]

    # calculator 支持任意简单表达式，避免只靠字典命中
    if tool_name == "calculator":
        allowed = set("0123456789+-*/(). %")
        if not tool_arg or any(ch not in allowed for ch in tool_arg):
            return "错误：calculator 参数只允许数字与 + - * / ( ) . 空格"
        try:
            return str(eval(tool_arg, {"__builtins__": {}}, {}))
        except Exception as e:
            return f"计算失败: {e}"

    # 未知工具/参数：返回明确错误，便于调试
    return f"错误：模拟工具无此结果（{tool_name}[{tool_arg}]）。请换参数或检查 Action 格式。"


def run_react(question: str, max_steps: int = 5) -> str:
    """
    ReAct 主循环。
    scratchpad：累加每轮 Thought/Action/Observation，作为下一轮上下文。
    """
    messages: list[dict] = [
        {"role": "system", "content": REACT_SYSTEM},
        {"role": "user", "content": f"Question: {question}"},
    ]
    scratchpad = ""

    for step in range(1, max_steps + 1):
        print(f"\n{'='*50}\n[Step {step}] 请求模型…", flush=True)
        print(f"[配置] max_steps={max_steps}", flush=True)

        # 把 scratchpad 附在用户问题后，让模型看到历史 T/A/O
        if scratchpad:
            messages[1] = {
                "role": "user",
                "content": f"Question: {question}\n\n{scratchpad.strip()}\n\n请继续：若信息足够请 Final Answer，否则 Thought + Action。",
            }

        raw = chat(messages)
        print(f"[模型输出]\n{raw}\n", flush=True)

        parsed = parse_react(raw)
        thought = parsed.get("thought")
        action = parsed.get("action")
        final_answer = parsed.get("final_answer")

        if thought:
            print(f"[解析] Thought: {thought[:80]}…" if len(thought or "") > 80 else f"[解析] Thought: {thought}", flush=True)

        if final_answer:
            print(f"[解析] Final Answer: {final_answer}", flush=True)
            return final_answer

        if not action:
            return f"错误：第 {step} 步既没有 Final Answer 也没有 Action。\n原始输出：{raw}"

        print(f"[解析] Action: {action}", flush=True)
        try:
            tool_name, tool_arg = parse_action(action)
        except ValueError as e:
            return str(e)

        observation = simulate_tool(tool_name, tool_arg)
        print(f"[模拟] Observation: {observation}", flush=True)

        scratchpad += f"Thought: {thought or ''}\nAction: {action}\nObservation: {observation}\n"

    print(f"[停止] 已达 max_steps={max_steps}，强制结束", flush=True)
    return f"错误：已达 max_steps={max_steps}，未得到 Final Answer。"


def main() -> None:
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY", flush=True)
        return

    print("Day 21 · ReAct Agent（模拟工具）", flush=True)
    print("输入 quit 退出。试试：广州现在气温多少？ / 帮我算 (3+5)*2\n", flush=True)

    while True:
        q = input("你：").strip()
        if not q:
            continue
        if q.lower() in ("quit", "exit"):
            print("再见！", flush=True)
            break
        try:
            answer = run_react(q)
            print(f"\nAI：{answer}\n", flush=True)
        except requests.RequestException as e:
            print(f"请求失败: {e}\n", flush=True)
        except RuntimeError as e:
            print(f"{e}\n", flush=True)


if __name__ == "__main__":
    main()

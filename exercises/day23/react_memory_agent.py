"""
Day 23 · Agent 记忆系统 · 短期历史 + ReAct

在 D22 真工具 ReAct 基础上：
  - 外层：多轮对话历史（短期记忆，同 D12）
  - 内层：每问仍跑 Thought/Action/Observation + scratchpad
  - trim_history 防 Token 爆炸

验收：先说「我叫小明」，再问「我叫什么名字？」能答对。
"""

from __future__ import annotations

import os
import re
from urllib.parse import quote

import requests
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
MODEL = "deepseek-chat"

# 最多保留几「轮」对话（1 轮 = 1 条 user + 1 条 assistant）
MAX_TURNS = 10

REACT_SYSTEM = """你是带记忆的 ReAct 助手。你能看见之前的对话历史。

每次回复必须且只能使用下列格式之一。

格式 A（还需要调工具）：
Thought: （简短推理，不要编造工具结果）
Action: 工具名[参数]

格式 B（信息已够）：
Thought: （简短总结）
Final Answer: （给用户的最终回答）

可用工具：
- get_weather[城市]  例：get_weather[北京]  查询实时天气
- calculator[表达式]  例：calculator[(3+5)*2]  计算算术

规则：
1. 一次只写一个 Thought + 一个 Action，或 Thought + Final Answer
2. Action 必须用 工具名[参数]，不要编造 Observation
3. 问天气/气温必须调用 get_weather，禁止凭记忆编造天气
4. 问计算必须调用 calculator
5. 用户的名字、偏好等个人事实：从对话历史里找，不必调工具
6. 若历史里已有答案（如用户说过名字），直接 Final Answer
"""


def trim_history(messages: list[dict], max_turns: int = MAX_TURNS) -> list[dict]:
    """
    限制历史长度（同 D12）。
    有 system 则永远保留；其余只留最近 max_turns 轮。
    """
    if not messages:
        return messages

    if messages[0].get("role") == "system":
        system_msg = messages[0]
        rest = messages[1:]
    else:
        system_msg = None
        rest = messages

    max_messages = max_turns * 2
    if len(rest) > max_messages:
        rest = rest[-max_messages:]

    if system_msg:
        return [system_msg] + rest
    return rest


def chat(messages: list[dict]) -> str:
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
    解析 Thought / Action / Final Answer。
    容忍模型偶发 Markdown：**Final Answer:** / **Thought:**
    """
    result: dict[str, str | None] = {
        "thought": None,
        "action": None,
        "final_answer": None,
    }

    # \*? = 可选 *，兼容 **Final Answer:**
    label_final = r"\*{0,2}Final Answer\*{0,2}\s*:"
    label_thought = r"\*{0,2}Thought\*{0,2}\s*:"
    label_action = r"\*{0,2}Action\*{0,2}\s*:"

    m_final = re.search(rf"{label_final}\s*(.+)", text, re.DOTALL | re.IGNORECASE)
    if m_final:
        result["final_answer"] = m_final.group(1).strip()
        m_th = re.search(
            rf"{label_thought}\s*(.+?)(?={label_final}|$)",
            text,
            re.DOTALL | re.IGNORECASE,
        )
        if m_th:
            result["thought"] = m_th.group(1).strip()
        return result

    m_th = re.search(
        rf"{label_thought}\s*(.+?)(?={label_action}|$)",
        text,
        re.DOTALL | re.IGNORECASE,
    )
    if m_th:
        result["thought"] = m_th.group(1).strip()

    m_act = re.search(rf"{label_action}\s*(.+)", text, re.IGNORECASE)
    if m_act:
        result["action"] = m_act.group(1).strip().split("\n")[0].strip()

    return result


def parse_action(action_line: str) -> tuple[str, str]:
    """get_weather[北京] → ("get_weather", "北京")"""
    action_line = action_line.strip()
    m = re.match(r"^(\w+)\s*\[(.+)\]\s*$", action_line)
    if m:
        return m.group(1), m.group(2).strip()

    m = re.match(r"^(\w+)\s*\((.+)\)\s*$", action_line)
    if m:
        return m.group(1), m.group(2).strip()

    raise ValueError(f"无法解析 Action: {action_line!r}")


# ---------- 真工具（厨房）----------

def get_weather(city: str) -> str:
    city = city.strip()
    if not city:
        return "错误：城市名不能为空"

    url = f"https://wttr.in/{quote(city)}?format=j1"
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()
        current = data["current_condition"][0]
        desc = current["weatherDesc"][0]["value"]
        temp = current["temp_C"]
        humidity = current["humidity"]
        feels = current.get("FeelsLikeC", temp)
        return (
            f"{city}：{desc}，气温 {temp}℃，体感 {feels}℃，湿度 {humidity}%"
        )
    except requests.RequestException as e:
        return f"错误：天气 API 请求失败（{e}）"
    except (KeyError, IndexError, TypeError) as e:
        return f"错误：天气数据解析失败（{e}）"


def calculator(expression: str) -> str:
    expression = expression.strip()
    allowed = set("0123456789+-*/(). %")
    if not expression or any(ch not in allowed for ch in expression):
        return "错误：表达式只能包含数字和 + - * / ( ) . 空格"
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"计算失败: {e}"


def run_tool(tool_name: str, tool_arg: str) -> str:
    tool_arg = tool_arg.strip()
    if tool_name == "get_weather":
        return get_weather(tool_arg)
    if tool_name == "calculator":
        return calculator(tool_arg)
    return f"错误：未知工具 {tool_name}"


def run_react(
    question: str,
    history: list[dict],
    max_steps: int = 5,
) -> str:
    """
    带短期记忆的 ReAct。

    history：跨轮的 user/assistant 列表（不含 system）。
    本轮结束后，调用方把本轮 Q/A append 进 history。
    scratchpad 只服务本轮，不写入 history。
    """
    scratchpad = ""

    for step in range(1, max_steps + 1):
        print(f"\n{'=' * 50}\n[Step {step}] 请求模型…", flush=True)
        print(
            f"[配置] max_steps={max_steps} | 历史轮数≈{len(history) // 2}",
            flush=True,
        )

        if scratchpad:
            user_content = (
                f"Question: {question}\n\n{scratchpad.strip()}\n\n"
                "请继续：若信息足够请 Final Answer，否则 Thought + Action。"
            )
        else:
            user_content = f"Question: {question}"

        # system + 短期历史 + 本轮问题（含 scratchpad）
        messages: list[dict] = [{"role": "system", "content": REACT_SYSTEM}]
        messages.extend(history)
        messages.append({"role": "user", "content": user_content})
        messages = trim_history(messages, MAX_TURNS)

        raw = chat(messages)
        print(f"[模型输出]\n{raw}\n", flush=True)

        parsed = parse_react(raw)
        thought = parsed.get("thought")
        action = parsed.get("action")
        final_answer = parsed.get("final_answer")

        if thought:
            short = thought if len(thought) <= 80 else thought[:80] + "…"
            print(f"[解析] Thought: {short}", flush=True)

        if final_answer:
            print(f"[解析] Final Answer: {final_answer}", flush=True)
            return final_answer

        if not action:
            return (
                f"错误：第 {step} 步既没有 Final Answer 也没有 Action。\n"
                f"原始输出：{raw}"
            )

        print(f"[解析] Action: {action}", flush=True)
        try:
            tool_name, tool_arg = parse_action(action)
        except ValueError as e:
            return str(e)

        observation = run_tool(tool_name, tool_arg)
        print(f"[工具] Observation: {observation}", flush=True)

        scratchpad += (
            f"Thought: {thought or ''}\n"
            f"Action: {action}\n"
            f"Observation: {observation}\n"
        )

    print(f"[停止] 已达 max_steps={max_steps}，强制结束", flush=True)
    return f"错误：已达 max_steps={max_steps}，未得到 Final Answer。"


def main() -> None:
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY", flush=True)
        return

    print("Day 23 · ReAct Agent（短期记忆）", flush=True)
    print(
        "验收：先说「我叫小明」，再问「我叫什么名字？」\n"
        "输入 quit 退出；输入 clear 清空短期记忆。\n",
        flush=True,
    )

    # ★ 短期记忆：跨轮保存；程序退出即清空（不写磁盘）
    history: list[dict] = []

    while True:
        q = input("你：").strip()
        if not q:
            continue
        if q.lower() in ("quit", "exit"):
            print("再见！", flush=True)
            break
        if q.lower() == "clear":
            history.clear()
            print("（已清空短期记忆）\n", flush=True)
            continue

        try:
            answer = run_react(q, history)
            print(f"\nAI：{answer}\n", flush=True)
            # 本轮结束：把 Q/A 写入短期记忆（不含 scratchpad）
            history.append({"role": "user", "content": q})
            history.append({"role": "assistant", "content": answer})
            max_messages = MAX_TURNS * 2
            if len(history) > max_messages:
                history = history[-max_messages:]
        except requests.RequestException as e:
            print(f"请求失败: {e}\n", flush=True)
        except RuntimeError as e:
            print(f"{e}\n", flush=True)


if __name__ == "__main__":
    main()

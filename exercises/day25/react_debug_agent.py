"""
Day 25 · Agent 调试 · 结构化日志版 ReAct

基于 D22：真天气 + 计算器。
增强：每步统一 [LOG] 字段，便于排查「未调用 / 调错 / 参数错」。
run_react 可返回 trace，供 run_eval.py 统计准确率。
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
# DeepSeek 现网模型名：deepseek-v4-flash / deepseek-v4-pro（deepseek-chat 已不可用）
MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash")

# 调试后可改这里的规则；改完重跑 run_eval.py
REACT_SYSTEM = """你是 ReAct 助手。每次回复必须且只能使用下列格式之一。

格式 A（还需要调工具）：
Thought: （简短推理，不要编造工具结果）
Action: 工具名[参数]

格式 B（信息已够）：
Thought: （简短总结）
Final Answer: （给用户的最终回答）

可用工具：
- get_weather[城市]  例：get_weather[北京]
  何时用：问天气、气温、冷不冷、下雨、适合出门等与实时天气相关
  何时不用：纯闲聊、自我介绍、算术题
- calculator[表达式]  例：calculator[(3+5)*2]
  何时用：加减乘除等算术（可用 + - * / ( )）
  何时不用：天气问题；不要用它算「冷不冷」

规则：
1. 一次只写一个 Thought + 一个 Action，或 Thought + Final Answer
2. Action 必须用 工具名[参数]，不要编造 Observation
3. 问天气/气温/降雨必须调用 get_weather，禁止凭记忆编造
4. 问计算必须调用 calculator
5. 纯打招呼/自我介绍：不要调工具，直接 Final Answer
6. 不要输出 Markdown 加粗（不要写 **Final Answer:**）
"""


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
        "temperature": 0.2,
    }
    response = requests.post(url, headers=headers, json=body, timeout=60)
    if not response.ok:
        # 把服务端原因打出来，避免只看到笼统的 400
        raise requests.HTTPError(
            f"{response.status_code} {response.reason}: {response.text}",
            response=response,
        )
    return response.json()["choices"][0]["message"]["content"] or ""


def parse_react(text: str) -> dict:
    """容忍偶发 **Final Answer:** 等 Markdown。"""
    result: dict[str, str | None] = {
        "thought": None,
        "action": None,
        "final_answer": None,
    }
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
    action_line = action_line.strip()
    m = re.match(r"^(\w+)\s*\[(.+)\]\s*$", action_line)
    if m:
        return m.group(1), m.group(2).strip()
    m = re.match(r"^(\w+)\s*\((.+)\)\s*$", action_line)
    if m:
        return m.group(1), m.group(2).strip()
    raise ValueError(f"无法解析 Action: {action_line!r}")


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
        return f"{city}：{desc}，气温 {temp}℃，体感 {feels}℃，湿度 {humidity}%"
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


def log_line(tag: str, msg: str) -> None:
    print(f"[LOG] {tag}: {msg}", flush=True)


def run_react(
    question: str,
    max_steps: int = 5,
    *,
    verbose: bool = True,
) -> tuple[str, list[dict]]:
    """
    返回 (final_answer或错误信息, trace)。
    trace 每步含：step, thought, action, tool_name, tool_arg, observation, final_answer
    """
    messages: list[dict] = [
        {"role": "system", "content": REACT_SYSTEM},
        {"role": "user", "content": f"Question: {question}"},
    ]
    scratchpad = ""
    trace: list[dict] = []

    for step in range(1, max_steps + 1):
        if verbose:
            print(f"\n{'=' * 50}", flush=True)
            log_line("step", str(step))
            log_line("question", question)

        if scratchpad:
            messages[1] = {
                "role": "user",
                "content": (
                    f"Question: {question}\n\n{scratchpad.strip()}\n\n"
                    "请继续：若信息足够请 Final Answer，否则 Thought + Action。"
                ),
            }

        raw = chat(messages)
        if verbose:
            log_line("raw", raw.replace("\n", " | "))

        parsed = parse_react(raw)
        thought = parsed.get("thought")
        action = parsed.get("action")
        final_answer = parsed.get("final_answer")

        step_rec: dict = {
            "step": step,
            "thought": thought,
            "action": action,
            "tool_name": None,
            "tool_arg": None,
            "observation": None,
            "final_answer": final_answer,
        }

        if verbose and thought:
            short = thought if len(thought) <= 100 else thought[:100] + "…"
            log_line("Thought", short)

        if final_answer:
            if verbose:
                log_line("Final Answer", final_answer)
            step_rec["final_answer"] = final_answer
            trace.append(step_rec)
            return final_answer, trace

        if not action:
            err = f"错误：第 {step} 步既没有 Final Answer 也没有 Action。"
            if verbose:
                log_line("error", err)
            step_rec["observation"] = err
            trace.append(step_rec)
            return err, trace

        if verbose:
            log_line("Action", action)

        try:
            tool_name, tool_arg = parse_action(action)
        except ValueError as e:
            if verbose:
                log_line("error", str(e))
            step_rec["observation"] = str(e)
            trace.append(step_rec)
            return str(e), trace

        step_rec["tool_name"] = tool_name
        step_rec["tool_arg"] = tool_arg
        if verbose:
            log_line("tool_name", tool_name)
            log_line("tool_arg", tool_arg)

        observation = run_tool(tool_name, tool_arg)
        step_rec["observation"] = observation
        if verbose:
            log_line("Observation", observation)

        scratchpad += (
            f"Thought: {thought or ''}\n"
            f"Action: {action}\n"
            f"Observation: {observation}\n"
        )
        trace.append(step_rec)

    msg = f"错误：已达 max_steps={max_steps}，未得到 Final Answer。"
    if verbose:
        log_line("stop", msg)
    return msg, trace


def main() -> None:
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY.startswith("sk-your"):
        print("请先在 .env 中配置 DEEPSEEK_API_KEY", flush=True)
        return

    print("Day 25 · ReAct 调试（结构化日志）", flush=True)
    print("输入 quit 退出。建议先跑：北京天气 / (3+5)*2\n", flush=True)

    while True:
        q = input("你：").strip()
        if not q:
            continue
        if q.lower() in ("quit", "exit"):
            print("再见！", flush=True)
            break
        try:
            answer, _ = run_react(q)
            print(f"\nAI：{answer}\n", flush=True)
        except requests.RequestException as e:
            print(f"请求失败: {e}\n", flush=True)
        except RuntimeError as e:
            print(f"{e}\n", flush=True)


if __name__ == "__main__":
    main()

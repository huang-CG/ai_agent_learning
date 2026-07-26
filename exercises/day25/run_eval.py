"""
Day 25 · 10 题工具选择准确率评测

统计：期望工具是否在本轮 trace 里被调用过（expect_tool=None 则要求全程无工具）。
验收：准确率 > 80%（建议 ≥ 9/10）。
"""

from __future__ import annotations

import sys
from pathlib import Path

# 保证可直接 python exercises/day25/run_eval.py
sys.path.insert(0, str(Path(__file__).resolve().parent))

from react_debug_agent import run_react  # noqa: E402
from test_cases import TEST_CASES  # noqa: E402


def tools_used(trace: list[dict]) -> list[str]:
    return [s["tool_name"] for s in trace if s.get("tool_name")]


def judge(expect: str | None, used: list[str]) -> bool:
    if expect is None:
        return len(used) == 0
    return expect in used


def main() -> None:
    print("Day 25 · 工具选择评测（10 题）\n", flush=True)
    ok = 0
    total = len(TEST_CASES)
    fails: list[str] = []

    for case in TEST_CASES:
        cid, q, expect = case["id"], case["q"], case["expect_tool"]
        print(f"\n----- 题 {cid}/{total}: {q}", flush=True)
        print(f"期望工具: {expect!r}", flush=True)
        try:
            answer, trace = run_react(q, verbose=True)
        except Exception as e:
            print(f"[评测] 异常: {e}", flush=True)
            fails.append(f"#{cid} 异常: {e}")
            continue

        used = tools_used(trace)
        passed = judge(expect, used)
        if passed:
            ok += 1
            mark = "PASS"
        else:
            mark = "FAIL"
            fails.append(
                f"#{cid} 期望={expect!r} 实际调用={used} | 答={answer[:60]}"
            )
        print(f"[评测] {mark} | 实际调用: {used}", flush=True)

    acc = ok / total if total else 0.0
    print("\n" + "=" * 50, flush=True)
    print(f"得分: {ok}/{total}  准确率: {acc:.0%}", flush=True)
    if acc > 0.8:
        print("验收：准确率 > 80% ✅", flush=True)
    else:
        print("验收：未过 80% ❌ → 对照 FAIL 题改 REACT_SYSTEM 后重跑", flush=True)
    if fails:
        print("\n失败明细:", flush=True)
        for line in fails:
            print(f"  - {line}", flush=True)


if __name__ == "__main__":
    main()

"""
Day 20 · 工具 Schema 设计

三个工具：天气 / 搜索 / 计算
- GOOD_*：给模型看的「好说明书」
- BAD_*：故意写差的，对比为什么容易调错

今天不调 API；只打印 JSON，建立 Schema 设计手感。
D21 手写 ReAct 解析时，Action 里的工具名应对齐这里的 name。
"""

from __future__ import annotations

import json

# ---------------------------------------------------------------------------
# 好版：三个生产级 Schema（验收用这份）
# ---------------------------------------------------------------------------

GOOD_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": (
                "查询指定城市的当前天气状况，包括气温、天气现象（晴/阴/雨等）、湿度。"
                "用户问某地天气、气温、冷不冷、热不热、要不要带伞、是否下雨时使用。"
                "不要用于：数学计算、网页搜索、查历史新闻。"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名，使用中文简称，例如：广州、北京、深圳。不要带「市」「区」后缀。",
                    }
                },
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": (
                "在互联网上搜索实时或近期信息，返回摘要结果。"
                "用户问新闻、最新政策、某公司股价、某产品评测、「搜一下」「查资料」时使用。"
                "不要用于：已知城市的当前天气（用 get_weather）、纯数学算式（用 calculator）。"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "搜索关键词或完整问句，例如：DeepSeek 最新模型、2026 广州车展",
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "最多返回几条结果，默认 5，范围 1～10",
                    },
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "计算数学表达式，支持加减乘除、括号、小数。"
                "用户要求算数、计算、求值、口算验证时使用，例如「帮我算 (3+5)*2」。"
                "不要用于：查天气、搜索网页、需要联网的事实性问题。"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "数学表达式字符串，例如 (3+5)*2、10/4、3.14*2",
                    }
                },
                "required": ["expression"],
            },
        },
    },
]


# ---------------------------------------------------------------------------
# 差版：故意写烂，方便对比（不要发给真实 API）
# ---------------------------------------------------------------------------

BAD_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "天气工具",  # 太 vague：模型不知道何时该调
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"},  # 缺 description：可能传「广州市天河区」
                },
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "搜索",  # 与 calculator 边界不清
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "算一下",  # 用户说「算一下广州热不热」可能误调
            "parameters": {
                "type": "object",
                "properties": {
                    "input": {  # 字段名与 D15 的 expression 不一致，代码难对接
                        "type": "string",
                        "description": "输入",
                    }
                },
                "required": ["input"],
            },
        },
    },
]


def print_comparison() -> None:
    print("=" * 60)
    print("GOOD_TOOLS（验收用 · 发给模型的说明书）")
    print("=" * 60)
    print(json.dumps(GOOD_TOOLS, ensure_ascii=False, indent=2))

    print("\n" + "=" * 60)
    print("BAD vs GOOD 对照（背 4 条）")
    print("=" * 60)
    pairs = [
        ("get_weather description", BAD_TOOLS[0]["function"]["description"], GOOD_TOOLS[0]["function"]["description"][:40] + "…"),
        ("city 参数说明", "（无）", "中文简称、不要市区后缀"),
        ("web_search 边界", "仅「搜索」二字", "写明不用于天气/计算"),
        ("calculator 参数字段名", "input", "expression（与实现一致）"),
    ]
    for label, bad, good in pairs:
        print(f"  · {label}")
        print(f"      差：{bad}")
        print(f"      好：{good}")


def main() -> None:
    print_comparison()
    print("\n=== 心智模型（3 句）===")
    print("1. description = 给模型的「使用场景 + 禁止场景」")
    print("2. 每个 parameter 也要 description + 正确 type")
    print("3. name 和 Python 函数名对齐，否则 run_tool 对不上")
    print("\n下一步：D21 手写 ReAct 循环，Action 用 get_weather[广州] 这种格式")


if __name__ == "__main__":
    main()

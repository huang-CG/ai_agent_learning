"""
Day 25 · 评测题（期望工具名）

expect_tool:
  - "get_weather" / "calculator"：跑完后至少调用过该工具一次
  - None：不应调用任何工具（直接 Final Answer）
"""

TEST_CASES: list[dict] = [
    {"id": 1, "q": "北京天气怎么样？", "expect_tool": "get_weather"},
    {"id": 2, "q": "广州现在气温多少？", "expect_tool": "get_weather"},
    {"id": 3, "q": "帮我算一下 (3+5)*2", "expect_tool": "calculator"},
    {"id": 4, "q": "100 除以 4 等于多少？", "expect_tool": "calculator"},
    {"id": 5, "q": "上海今天冷不冷？", "expect_tool": "get_weather"},
    {"id": 6, "q": "15 乘以 8 再加 7 是多少？", "expect_tool": "calculator"},
    {"id": 7, "q": "深圳今天下雨吗？", "expect_tool": "get_weather"},
    {"id": 8, "q": "把 99 加上 1", "expect_tool": "calculator"},
    {"id": 9, "q": "你好，请简单介绍你自己", "expect_tool": None},
    {"id": 10, "q": "杭州天气如何？", "expect_tool": "get_weather"},
]

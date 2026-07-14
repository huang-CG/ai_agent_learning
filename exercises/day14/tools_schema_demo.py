"""
Day 14 演示：Function Calling 的「说明书」和「消息长什么样」

今天不调真实 tools API；只打印结构，帮你建立心智模型。
D15 再接 DeepSeek 真调时间 / 计算器。
"""

import json

# ---------- ① 给模型看的 tools 列表（函数说明书）----------
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市的当前天气。用户问天气、气温、是否下雨时使用。",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名，例如：广州、深圳",
                    }
                },
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "获取当前日期和时间。用户问几点、今天几号时使用。",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
]


# ---------- ② 模拟：模型返回的 tool_calls（不是最终给用户的话）----------
# 真实 API 里会出现在 response["choices"][0]["message"] 上
FAKE_ASSISTANT_TOOL_CALL = {
    "role": "assistant",
    "content": None,  # 决定调工具时，content 常常是 null
    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "get_weather",
                "arguments": '{"city": "广州"}',  # 注意：这里是 JSON 字符串
            },
        }
    ],
}


# ---------- ③ 你的程序执行函数后，回传 role: tool ----------
FAKE_TOOL_RESULT = {
    "role": "tool",
    "tool_call_id": "call_abc123",  # 必须对应上面的 id
    "content": "广州：晴，28℃，湿度 65%",
}


def main() -> None:
    print("=== 1. tools（发给 API 的函数说明书）===\n")
    print(json.dumps(TOOLS, ensure_ascii=False, indent=2))

    print("\n=== 2. 模型若决定调工具，assistant 消息大致长这样 ===\n")
    print(json.dumps(FAKE_ASSISTANT_TOOL_CALL, ensure_ascii=False, indent=2))

    print("\n=== 3. 你执行完函数后，塞回 messages 的 tool 消息 ===\n")
    print(json.dumps(FAKE_TOOL_RESULT, ensure_ascii=False, indent=2))

    print("\n=== 4. 心智模型（背这 3 句）===")
    print("· LLM：只产出「调哪个函数 + 参数 JSON」，不执行代码")
    print("· 你的程序：真正跑 get_weather / get_current_time")
    print("· 再请求一轮：把 tool 结果放进 messages，LLM 才说人话给用户")
    print("\n下一步：手绘流程图 → 对照 notes/diagrams/day14-function-calling-flow.md")


if __name__ == "__main__":
    main()

"""
Day 4 练习：调用免费天气 API

建议顺序：get_weather(city) → format_weather → main()
"""

import requests

# 16 方位 → 中文（wttr.in 返回 winddir16Point）
WIND_DIR_ZH = {
    "N": "北风", "NNE": "北东北风", "NE": "东北风", "ENE": "东东北风",
    "E": "东风", "ESE": "东东南风", "SE": "东南风", "SSE": "南东南风",
    "S": "南风", "SSW": "南西南风", "SW": "西南风", "WSW": "西西南风",
    "W": "西风", "WNW": "西西北风", "NW": "西北风", "NNW": "北西北风",
}

# 常见英文天气描述 → 中文（wttr.in 的 j1 格式多为英文）
WEATHER_ZH = {
    "Clear": "晴",
    "Sunny": "晴",
    "Partly Cloudy": "多云",
    "Partly cloudy": "多云",
    "Cloudy": "阴",
    "Overcast": "阴",
    "Light rain": "小雨",
    "Light rain shower": "小阵雨",
    "Light Rain Shower": "小阵雨",
    "Moderate rain": "中雨",
    "Moderate rain at times": "时有中雨",
    "Heavy rain": "大雨",
    "Patchy rain nearby": "附近有零星小雨",
    "Mist": "薄雾",
    "Fog": "雾",
    "Thunderstorm": "雷暴",
}


def get_weather(city: str) -> dict:
    """向 wttr.in 发 GET 请求，返回天气 JSON（字典）"""
    url = f"https://wttr.in/{city}?format=j1"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()


def _to_chinese_weather(desc: str) -> str:
    """尽量把英文天气描述转成中文，没有映射则保留原文"""
    desc = desc.strip()
    return WEATHER_ZH.get(desc, desc)


def format_weather(weather: dict, city: str) -> str:
    """从 JSON 提取字段，格式化为中文一行摘要"""
    current = weather["current_condition"][0]
    weather_desc = current["weatherDesc"][0]["value"]
    wind_dir = WIND_DIR_ZH.get(current["winddir16Point"], current["winddir16Point"])

    return (
        f"城市：{city}\n"
        f"天气：{_to_chinese_weather(weather_desc)}\n"
        f"温度：{current['temp_C']}°C\n"
        f"风向：{wind_dir}\n"
        f"风速：{current['windspeedKmph']} km/h\n"
        f"湿度：{current['humidity']}%"
    )


def show_menu() -> None:
    """打印菜单"""
    print("\n===== 天气查询功能菜单 =====")
    print("1. 查询天气")
    print("2. 退出")
    print("==================")


def main() -> None:
    """主循环：菜单 → 查天气 → 中文显示"""
    while True:
        show_menu()
        choice = input("请选择 1-2: ").strip()

        if choice == "2":
            print("再见！")
            break
        if choice != "1":
            print("无效的操作，请重新输入")
            continue

        city = input("请输入城市名称：").strip()
        if not city:
            print("城市名称不能为空！")
            continue

        try:
            weather = get_weather(city)
            print(format_weather(weather, city))
        except requests.RequestException as e:
            print(f"请求失败: {e}")


if __name__ == "__main__":
    main()

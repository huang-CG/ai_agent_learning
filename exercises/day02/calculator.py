"""
Day 2 练习：命令行计算器

TODO: 你来完成这个文件
提示：先写 show_menu()，再写 calculate(a, op, b)，最后写 main 循环
"""


def show_menu() -> None:
    """打印菜单"""
    print("\n===== 计算器 =====")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 退出")
    print("==================")


def calculate(a: float, op: str, b: float) -> float | None:
    """
    根据运算符 op 计算 a 和 b
    除零时返回 None
    """
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return None
        return a / b
    else:
        return None

def main() -> None:
    """主循环：显示菜单 → 读输入 → 计算 → 打印结果"""
    ops = {"1": "+", "2": "-", "3": "*", "4": "/"}

    while True:
        show_menu()
        choice = input("请选择 1-5: ")

        if choice == "5":
            print("再见！")
            break
        if choice not in ops:
            print("无效选项，请重新选择")
            continue

        try:
            a = float(input("请输入第一个数: "))
            b = float(input("请输入第二个数: "))
        except ValueError:
            print("请输入有效数字")
            continue

        result = calculate(a, ops[choice], b)
        if result is None:
            print("错误：除数不能为 0")
        else:
            print(f"结果: {result}")


if __name__ == "__main__":
    main()

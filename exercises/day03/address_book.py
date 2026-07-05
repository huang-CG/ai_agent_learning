"""
Day 3 练习：命令行通讯录

TODO: 你来完成这个文件
建议顺序：load/save → show_menu → add/delete/find/list → main
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "contacts.json"


def load_contacts() -> list:
    """从 JSON 加载联系人列表，文件不存在返回空列表"""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_contacts(contacts: list) -> None:
    """保存联系人列表到 JSON"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def show_menu() -> None:
    """打印菜单"""
    print("\n===== 通讯录功能菜单 =====")
    print("1. 显示所有联系人")
    print("2. 添加联系人")
    print("3. 删除联系人")
    print("4. 查找联系人")
    print("5. 退出")
    print("==================")


def add_contact(contacts: list) -> None:
    name = input("请输入联系人姓名：").strip()
    phone = input("请输入电话号码：").strip()

    if not name:
        name = "未知"

    if not phone:
        print("电话号码不能为空，请重新输入！")
        return

    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print("添加成功！")

def delete_contact(contacts: list) -> None:
    """按姓名删除联系人，然后保存"""
    name = input("请输入要删除的联系人姓名：").strip()
    if not name:
        print("姓名不能为空，请重新输入！")
        return
    
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("删除成功！")
            return
    print("联系人不存在，请重新输入！")

def find_contact(contacts: list) -> None:
    """按姓名查找，打印电话；找不到给提示"""
    name = input("请输入要查找的联系人姓名：").strip()
    if not name:
        print("姓名不能为空，请重新输入！")
        return
    for contact in contacts:
        if contact['name'] == name:
            print(f"电话号码：{contact['phone']}")
            return
    print("联系人不存在，请重新输入！")


def list_contacts(contacts: list) -> None:
    """打印所有联系人"""
    if not contacts:
        print("联系人列表为空，请添加联系人！")
        return
    for contact in contacts:
        print(f"姓名：{contact['name']} 电话号码：{contact['phone']}")



def main() -> None:
    """主循环"""
    contacts = load_contacts()
    while True:
        show_menu()
        c = input("请输入要执行的操作: ")
        if c == "1":
            list_contacts(contacts)
        elif c == "2":
            add_contact(contacts)
        elif c == "3":
            delete_contact(contacts)
        elif c == "4":
            find_contact(contacts)
        elif c == "5":
            print("再见！")
            break
        else:
            print("无效的操作，请重新输入")


if __name__ == "__main__":
    main()

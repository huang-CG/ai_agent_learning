"""
Day 6 练习：OOP 版通讯录

TODO: 你来完成这个文件
建议顺序：Contact → AddressBook(load/save) → add/delete/find/list_all → main
对照：exercises/day03/address_book.py
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "contacts.json"


class Contact:
    """单个联系人"""
    def __init__(self, name: str, phone: str) -> None:
        self.name = name
        self.phone = phone

    def show(self) -> None:
        """打印：姓名：… 电话号码：…"""
        # TODO
        print(f"姓名：{self.name} 电话号码：{self.phone}")


class AddressBook:
    """通讯录：管理联系人列表 + JSON 文件"""
    def __init__(self, data_file: Path) -> None:
        # TODO: self.data_file, self.contacts = self.load()
        self.data_file = data_file
        self.contacts = self.load()

    def load(self) -> list:
        """从 JSON 加载；文件不存在返回 []"""
        if not self.data_file.exists():
            return []
        with open(self.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Contact(d["name"], d["phone"]) for d in data]

    def save(self) -> None:
        """把 self.contacts 写入 JSON"""
        with open(self.data_file, "w", encoding="utf-8") as f:
            data = [{"name": c.name, "phone": c.phone} for c in self.contacts]
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add(self) -> None:
        """添加联系人并 save"""
        name = input("请输入联系人姓名：").strip()
        phone = input("请输入电话号码：").strip()
        if not name:
            name = "未知"
        if not phone:
            print("电话号码不能为空，请重新输入！")
            return
        self.contacts.append(Contact(name, phone))
        self.save()
        print("添加成功！")

        
    def delete(self) -> None:
        """按姓名删除并 save"""
        name = input("请输入联系人姓名：").strip()
        if not name:
            print("姓名不能为空，请重新输入！")
            return

        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                self.save()
                print(f"联系人{name}删除成功！")
                return
        print("联系人不存在，请重新输入！")

    def find(self) -> None:
        """按姓名查找并打印电话"""
        name = input("请输入联系人姓名：").strip()
        if not name:
            print("姓名不能为空，请重新输入！")
            return

        for contact in self.contacts:
            if contact.name == name:
                print(f"电话号码：{contact.phone}")
                return
        print("联系人不存在，请重新输入！")

    def list_all(self) -> None:
        """显示全部联系人"""
        if not self.contacts:
            print("暂无联系人！")
            return
        for contact in self.contacts:
            contact.show()


def show_menu() -> None:
    """打印菜单（可直接复制 D3）"""
    print("\n===== 通讯录功能菜单 =====")
    print("1. 显示所有联系人")
    print("2. 添加联系人")
    print("3. 删除联系人")
    print("4. 查找联系人")
    print("5. 退出")
    print("==================")


def main() -> None:
    """主循环：book = AddressBook(DATA_FILE)"""
    book = AddressBook(DATA_FILE)
    while True:
        show_menu()
        c = input("请输入要执行的操作: ")
        if c == "1":
            book.list_all()
        elif c == "2":
            book.add()
        elif c == "3":
            book.delete()
        elif c == "4":
            book.find()
        elif c == "5":
            print("再见！")
            break
        else:
            print("无效的操作，请重新输入")

if __name__ == "__main__":
    main()

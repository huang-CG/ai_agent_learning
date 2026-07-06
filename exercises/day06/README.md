# Day 6 · OOP 通讯录

## 这题要你做什么？（一句话）

> 把 D3 函数版通讯录**改成面向对象**：用 `Contact` + `AddressBook` 两个类，功能不变，JSON 持久化不变。

D5 已在笔记里写好 **D3 → D6 映射表**，今天对照 `exercises/day03/address_book.py` 动手重构。

---

## 和 D3 的区别

| D3 函数版 | D6 类版 |
|-----------|---------|
| `contacts` 列表到处传参 | `self.contacts` 绑在对象上 |
| `{"name","phone"}` 字典 | `Contact` 实例 |
| `add_contact(contacts)` | `book.add()` |
| `load_contacts()` | `book.load()`（在 `__init__` 里调用） |

---

## 目标结构

```python
class Contact:
    def __init__(self, name, phone): ...
    def show(self): ...          # 打印「姓名：… 电话号码：…」

class AddressBook:
    def __init__(self, data_file): ...
    def load(self): ...          # 读 JSON → self.contacts
    def save(self): ...          # self.contacts → 写 JSON
    def add(self): ...           # input 姓名电话，append，save
    def delete(self): ...
    def find(self): ...
    def list_all(self): ...

def show_menu(): ...             # 可保留为函数
def main():
    book = AddressBook(DATA_FILE)
    while True: ...              # 调 book.add() 等
```

---

## JSON 存什么？

**简单做法（推荐）**：`self.contacts` 仍是字典列表，和 D3 格式兼容：

```json
[{"name": "张三", "phone": "13800138000"}]
```

`load` 用 `json.load` 读列表；`save` 用 `json.dump` 写列表。  
**加分**：读写时转成 `Contact` 对象（见下方提示）。

---

## 建议实现顺序

1. `Contact` 类（`__init__` + `show`）
2. `AddressBook.__init__` + `load` + `save`
3. `add` → `delete` → `find` → `list_all`
4. `main` 菜单循环
5. 验收：增删查 + 退出再运行数据还在

---

## 运行

```powershell
cd e:\AI_agent_Quick
.\venv\Scripts\Activate.ps1
python exercises/day06/address_book_oop.py
```

数据文件：`exercises/day06/contacts.json`（与 D3 分开，互不影响）

---

## 验收自检

- [ ] 菜单 1–5，5 退出
- [ ] 增 / 删 / 查 / 显示全部
- [ ] 退出再运行，数据仍在
- [ ] 用了 **`class`**、**`__init__`**、**`self`**
- [ ] 用了 **`AddressBook` 实例**（`book = AddressBook(...)`）

---

## 加分（有余力）

- `load` 时把 dict 转成 `Contact` 对象；`save` 时转回 dict
- 加一个 `Contact.__str__` 或 `@property`

---

## 拓展（可选，≤20min）

只读浏览 [LangChain Quickstart](https://python.langchain.com/docs/tutorials/) 里的 class 用法，不用安装。

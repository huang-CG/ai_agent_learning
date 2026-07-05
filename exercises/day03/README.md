# Day 3 · 通讯录 CLI

## 这题要你做什么？（一句话）

> 做一个**命令行通讯录**：能增、删、查联系人，关掉程序再打开，数据还在（存在 JSON 文件里）。

和 D2 计算器一样：**菜单 + 循环**，只是操作对象从「数字」变成「联系人列表」。

---

## 用户用起来是什么样

```
===== 通讯录 =====
1. 添加联系人
2. 删除联系人
3. 查找联系人
4. 显示全部
5. 退出
==================
请选择 1-5: 1
姓名: 张三
电话: 13800138000
添加成功！

（选 5 退出程序，再重新运行，张三还在 → 验收通过）
```

---

## 数据怎么存

用 **列表 + 字典**，存到 `contacts.json`：

```json
[
  {"name": "张三", "phone": "13800138000"},
  {"name": "李四", "phone": "13900139000"}
]
```

- **列表** `[]`：放很多联系人
- **字典** `{}`：每个联系人有 `name` 和 `phone` 两个键

---

## 建议怎么写（分函数，和计算器一样）

| 函数 | 干什么 |
|------|--------|
| `load_contacts()` | 启动时从 JSON 读列表；文件不存在就返回 `[]` |
| `save_contacts(contacts)` | 把列表写回 JSON |
| `add_contact(contacts)` | 读姓名电话，追加到列表，保存 |
| `delete_contact(contacts)` | 按姓名删除，保存 |
| `find_contact(contacts)` | 按姓名查找，打印电话 |
| `list_contacts(contacts)` | 打印所有人 |
| `show_menu()` | 打印 1-5 菜单 |
| `main()` | `while` 循环调度上面这些 |

**每次增删后都要 `save_contacts()`**，这样数据才会持久化。

---

## JSON 读写（复制参考）

```python
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "contacts.json"

def load_contacts() -> list:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_contacts(contacts: list) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
```

---

## 运行

```powershell
cd e:\AI_agent_Quick
.\venv\Scripts\Activate.ps1
python exercises/day03/address_book.py
```

---

## 验收自检

- [ ] 菜单 1-5，循环运行，5 退出
- [ ] 能添加联系人（姓名 + 电话）
- [ ] 能按姓名删除
- [ ] 能按姓名查找
- [ ] 能显示全部
- [ ] **退出再运行，数据还在**（`contacts.json` 有内容）
- [ ] 用了**列表**和**字典**
- [ ] 代码拆成多个**函数**

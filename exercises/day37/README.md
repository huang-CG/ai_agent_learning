# Day 37 · 文件操作工具

## 这题要你做什么？（一句话）

> 给 Agent 三个文件工具（列目录 / 读 / 写），但**只能动沙箱目录**，并让它总结指定文件。

```
D35：外网搜索
D36：本地 SQL 表
D37：本地文件（有围栏）
```

路径请用全路径：

- 今日说明：`exercises/day37/README.md`
- 代码骨架：`exercises/day37/file_agent_lab.py`
- 沙箱样例：`exercises/day37/sandbox/note.txt`

---

## 和前后天的关系

| 天 | 停在哪 |
|----|--------|
| D36 | SQL 只允许 SELECT |
| **D37** | 文件只允许沙箱路径 |
| D38 | Agent Prompt / 输出格式 |

核心词：**沙箱（sandbox）**。工具可以读文件，但不能读到仓库根目录、`.env`、或任意 `C:\...`。

---

## 验收

1. 三个 `@tool`：`list_dir`、`read_file`、`write_file`  
2. 有函数把相对路径变成沙箱内的绝对路径；逃出沙箱则拒绝（不要执行）  
3. 冒烟（不经 Agent）：能列出沙箱、读到 `note.txt`；故意写 `../` 之类应被拒绝  
4. `create_agent` 问「总结一下 note.txt」→ 轨迹含 **tool**，内容提到值班时间/小周等要点  
5. 能口述：为什么要限制目录；检查路径时为什么要用 `resolve()`  

时间不够：砍「让 Agent 自己写新文件」的花活；**不砍** 三个工具 + 沙箱拒绝 + 总结 `note.txt`。

---

## 环境

无新依赖。DeepSeek 照旧。

```powershell
.\venv\Scripts\python.exe exercises\day37\file_agent_lab.py
```

沙箱目录：`exercises/day37/sandbox/`（程序不要去读别的地方）。

路径小抄：

```python
from pathlib import Path
sandbox = Path(__file__).resolve().parent / "sandbox"
target = (sandbox / name).resolve()
target.relative_to(sandbox.resolve())  # 不在沙箱内会抛 ValueError
```

---

## 今日时间盒（约 3h）

| 段 | 时长 | 内容 |
|----|------|------|
| A | ~15min | 口述：为何要沙箱 |
| B | ~50min | `safe_path` + 三工具 + 冒烟（含拒绝逃出） |
| C | ~80min | `create_agent` + 总结 note.txt |
| D | ~25min | 力扣 + 收工 |

实践日：先自己填骨架；卡住约 15～20 分钟再要最小提示。

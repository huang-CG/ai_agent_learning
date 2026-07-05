# Day 2 · 计算器练习

## 要求

写一个命令行计算器，满足：

1. 启动后显示菜单（加减乘除 + 退出）
2. 用户输入选项 → 输入两个数字 → 打印结果
3. 用 `while True` 循环，选「退出」才结束
4. 非法输入（非数字、无效选项）要有友好提示，不崩溃
5. 除法要处理除数为 0

## 运行

```powershell
cd e:\AI_agent_Quick
.\venv\Scripts\Activate.ps1
python exercises/day02/calculator.py
```

## 验收自检

- [ ] 用了 `if/elif/else`
- [ ] 用了 `while` 循环
- [ ] 四种运算都正确
- [ ] 除零有提示
- [ ] 能连续算多题，输入 q 或选退出才结束

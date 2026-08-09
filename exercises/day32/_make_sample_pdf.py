"""一次性生成 sample_kb.pdf（中文）。跑完可删本脚本。"""
from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).with_name("sample_kb.pdf")
FONT = Path(r"C:\Windows\Fonts\msyh.ttc")

TEXT = """Day32 RAG 样例知识库（虚构设定，便于验收）

广州 AI Agent 学习站规则：
1. 每日学习时长建议 2 到 4 小时，先保关键路径验收。
2. 本站的吉祥物叫「小向量」，它只吃向量，不吃 Token。
3. 毕业项目代号是「青云助手」，要求必须包含 RAG 与 Agent 工具调用。
4. 答疑窗口：每周二和周四 20:00-21:00（北京时间）。
5. 禁止事项：不要把 API Key 提交到 GitHub。

烹饪备忘（用于干扰检索）：
苹果派：烤箱预热 190 摄氏度，烤约 45 分钟。
番茄炒蛋：先滑蛋再炒番茄出汁后合炒。

RAG 提醒：
检索只返回相关片段，再交给 LLM 生成；文档没有的内容要明确说没有，不要编造。
"""


def main() -> None:
    if not FONT.exists():
        raise SystemExit(f"找不到中文字体: {FONT}")

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_margins(left=15, top=15, right=15)
    pdf.add_font("msyh", fname=str(FONT))
    pdf.set_font("msyh", size=12)
    usable = pdf.epw
    for line in TEXT.strip().split("\n"):
        pdf.multi_cell(usable, 8, line if line.strip() else " ")
    pdf.output(str(OUT))
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

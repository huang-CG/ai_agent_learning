"""Day 1 环境检查：验证 Python 与 DeepSeek 配置。"""
import os
import sys

from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    print(f"Python: {sys.version.split()[0]}")
    key = os.getenv("DEEPSEEK_API_KEY", "")
    base = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    if not key or key.startswith("sk-your"):
        print("DEEPSEEK_API_KEY: 未配置（请复制 .env.example → .env 并填入 Key）")
        sys.exit(1)
    print(f"DEEPSEEK_API_KEY: {key[:8]}...（已配置）")
    print(f"DEEPSEEK_BASE_URL: {base}")
    print("环境检查通过 ✓")


if __name__ == "__main__":
    main()

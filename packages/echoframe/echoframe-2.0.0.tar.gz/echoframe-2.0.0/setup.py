"""
EchoFrame - OneBot-11 协议机器人框架
"""

from setuptools import setup, find_packages
from pathlib import Path

# 读取 README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# 读取版本
version = "2.0.0"

setup(
    name="echoframe",
    version=version,
    author="EchoFrame Team",
    author_email="",
    description="一个完整的 OneBot-11 协议插件化机器人框架",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-repo/echoframe",
    packages=['echoframe', 'core', 'adapters'],  # 手动指定包
    package_dir={'': '.'},  # 包的根目录
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.8",
    install_requires=[
        "aiohttp>=3.8.0",
        "websockets>=11.0",
        "pyyaml>=6.0",
        "pydantic>=2.0.0",
        "loguru>=0.7.0",
    ],
    extras_require={
        "scheduler": ["apscheduler>=3.10.0"],  # 定时任务
        "database": ["sqlalchemy>=2.0.0", "aiosqlite>=0.19.0"],  # 数据库
        "dev": ["pytest>=7.0.0", "pytest-asyncio>=0.21.0"],  # 开发工具
    },
    entry_points={
        "console_scripts": [
            "onebot=core.cli:main",  # 命令行工具
        ],
    },
    include_package_data=True,
    zip_safe=False,
)


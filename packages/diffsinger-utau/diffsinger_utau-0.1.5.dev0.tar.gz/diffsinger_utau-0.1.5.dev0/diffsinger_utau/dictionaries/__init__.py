"""
DiffSinger UTAU 字典文件

这个目录包含了用于语音合成的字典和映射文件。
"""

import os
from pathlib import Path

# 获取字典目录路径
DICTIONARIES_DIR = Path(__file__).parent

def get_dictionary_path(filename):
    """获取字典文件的完整路径"""
    return DICTIONARIES_DIR / filename

def list_dictionaries():
    """列出所有可用的字典文件"""
    return [f.name for f in DICTIONARIES_DIR.glob("*.txt")]
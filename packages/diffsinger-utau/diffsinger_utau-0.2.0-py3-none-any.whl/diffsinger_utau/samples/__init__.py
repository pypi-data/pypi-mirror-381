"""
DiffSinger UTAU 样本文件

这个目录包含了用于测试和演示的 DiffSinger 样本文件。
"""

import os
from pathlib import Path

# 获取样本目录路径
SAMPLES_DIR = Path(__file__).parent

def get_sample_path(filename):
    """获取样本文件的完整路径"""
    return SAMPLES_DIR / filename

def list_samples():
    """列出所有可用的样本文件"""
    return [f.name for f in SAMPLES_DIR.glob("*.ds")]
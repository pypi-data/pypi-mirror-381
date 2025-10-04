# -*- coding: utf-8 -*-
"""
DevAssist - 提供开发辅助功能的Python包
"""

# 包元数据
__name__ = "DevAssist"
__version__ = "0.0.2"
__author__ = "Tensor Py Ops"
__author_email__ = "TensorPyOps@outlook.com"
__description__ = "Auxiliary development tools or services"
__url__ = "https://github.com/TensorPyOps/DevAssist"
__license__ = "Apache Software License"

# 控制公开接口，定义from DevAssist import *时可导入的内容
__all__ = [
    "debug",            # 导出 debug 模块
    "msg",              # 导出 debug 模块中的 msg 函数
]

# 从子模块导入公共组件
from .debug import msg

# 定义包级别的工具函数
def get_version():
    """返回当前包的版本号"""
    return __version__

# 包初始化操作（可选）
def _initialize_package():
    """包初始化逻辑，首次导入时执行"""
    # 可以在这里添加日志配置、检查依赖等初始化操作
    pass

# 执行初始化
_initialize_package()

# 清理临时变量，避免被导入
del _initialize_package

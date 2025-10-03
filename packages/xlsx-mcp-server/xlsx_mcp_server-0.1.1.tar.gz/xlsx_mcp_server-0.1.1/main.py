#!/usr/bin/env python3
"""
Excel MCP Server based on FastMCP
提供完整的 Excel 文件操作功能

注意：此文件是兼容性包装器，所有功能已移至 excel_mcp_server 包中
"""

# 从 xlsx_mcp_server 包导入所有内容
from xlsx_mcp_server import *

if __name__ == "__main__":
    # 运行 MCP 服务器
    main()
import asyncio
from fastmcp import Client
import os

# 配置 MCP 服务器地址
config = {
    "mcpServers": {
        "excel_server": {
            "url": "http://127.0.0.1:9000/mcp",
            "transport": "streamable-http"
        }
    }
}

# 初始化客户端
client = Client(config)

async def main():
    async with client:
        try:
            # 测试文件路径
            test_file = "test_excel.xlsx"
            workbook_id = "test_workbook"
            
            # 1. 创建一个新的 Excel 工作簿
            print("1. 创建新的 Excel 工作簿...")
            create_result = await client.call_tool(
                "excel_server", 
                "create_workbook", 
                {
                    "workbook_id": workbook_id,
                    "sheets": ["Sheet1", "Sheet2"]
                }
            )
            print(f"创建结果: {create_result}")
            
            # 2. 列出工作簿中的工作表
            print("\n2. 列出工作簿中的工作表...")
            sheets_result = await client.call_tool(
                "excel_server", 
                "list_sheets", 
                {"workbook_id": workbook_id}
            )
            print(f"工作表列表: {sheets_result}")
            
            # 3. 写入数据到工作表
            print("\n3. 写入数据到工作表...")
            # 写入 Sheet1 数据
            sheet1_data = [
                {"Name": "Alice", "Age": 30, "City": "New York"},
                {"Name": "Bob", "Age": 25, "City": "London"},
                {"Name": "Charlie", "Age": 35, "City": "Paris"}
            ]
            write_sheet1_result = await client.call_tool(
                "excel_server", 
                "write_dataframe", 
                {
                    "workbook_id": workbook_id,
                    "sheet_name": "Sheet1",
                    "data": sheet1_data,
                    "start_cell": "A1"
                }
            )
            print(f"Sheet1 写入结果: {write_sheet1_result}")
            
            # 写入 Sheet2 数据
            sheet2_data = [
                {"Product": "Apple", "Price": 1.5, "Quantity": 10},
                {"Product": "Banana", "Price": 0.75, "Quantity": 20},
                {"Product": "Cherry", "Price": 5.0, "Quantity": 5}
            ]
            write_sheet2_result = await client.call_tool(
                "excel_server", 
                "write_dataframe", 
                {
                    "workbook_id": workbook_id,
                    "sheet_name": "Sheet2",
                    "data": sheet2_data,
                    "start_cell": "A1"
                }
            )
            print(f"Sheet2 写入结果: {write_sheet2_result}")
            
            # 4. 保存工作簿到文件
            print("\n4. 保存工作簿到文件...")
            save_result = await client.call_tool(
                "excel_server", 
                "save_workbook_file", 
                {
                    "workbook_id": workbook_id,
                    "file_path": test_file
                }
            )
            print(f"保存结果: {save_result}")
            
            # 5. 关闭工作簿
            print("\n5. 关闭工作簿...")
            close_result = await client.call_tool(
                "excel_server", 
                "close_workbook", 
                {"workbook_id": workbook_id}
            )
            print(f"关闭结果: {close_result}")
            
            # 清理测试文件
            if os.path.exists(test_file):
                os.remove(test_file)
                print(f"\n测试文件 '{test_file}' 已清理")
                
        except Exception as e:
            print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
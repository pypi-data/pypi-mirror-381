import asyncio
import sys
import os
from datetime import datetime

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(__file__))

from stock_mcp import stock_analyzer, analyze_stock_price, search_stock_symbols, get_stock_examples, get_candlestick_patterns_info

class TestResultExporter:
    def __init__(self):
        self.output_lines = []
        self.test_start_time = datetime.now()
    
    def add_section(self, title, level=1):
        """添加章节标题"""
        prefix = "#" * level
        self.output_lines.append(f"\n{prefix} {title}\n")
    
    def add_content(self, content):
        """添加内容"""
        self.output_lines.append(content)
    
    def add_code_block(self, code, language="text"):
        """添加代码块"""
        self.output_lines.append(f"```{language}")
        self.output_lines.append(code)
        self.output_lines.append("```")
    
    def add_table(self, headers, rows):
        """添加表格"""
        # 表头
        header_line = "| " + " | ".join(headers) + " |"
        separator_line = "|" + "|".join([" --- " for _ in headers]) + "|"
        
        self.output_lines.append(header_line)
        self.output_lines.append(separator_line)
        
        # 数据行
        for row in rows:
            row_line = "| " + " | ".join(str(cell) for cell in row) + " |"
            self.output_lines.append(row_line)
    
    def save_to_file(self, filename=None):
        """保存到文件"""
        if filename is None:
            filename = f"stock_analysis_test_{self.test_start_time.strftime('%Y%m%d_%H%M%S')}.md"
        
        # 添加文件头信息
        header = [
            "# 股票分析MCP测试报告",
            f"**测试时间**: {self.test_start_time.strftime('%Y-%m-%d %H:%M:%S')}",
            f"**生成文件**: {filename}",
            ""
        ]
        
        full_content = "\n".join(header + self.output_lines)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"✅ 测试报告已保存到: {filename}")
        return filename

# 创建导出器实例
exporter = TestResultExporter()

async def test_search_functionality():
    """测试搜索功能"""
    exporter.add_section("搜索功能测试", 2)
    
    test_cases = [
        ("Apple", "测试搜索'Apple'"),
        ("Microsoft", "测试搜索'Microsoft'"), 
        ("BABA", "测试搜索股票代码'BABA'")
    ]
    
    for keyword, description in test_cases:
        exporter.add_section(description, 3)
        result = await search_stock_symbols(keyword)
        exporter.add_content(result)

async def test_stock_analysis():
    """测试股票分析功能"""
    exporter.add_section("股票分析功能测试", 2)
    
    # 测试不同市场的股票
    test_cases = [
        ("AAPL", "1d", "苹果(AAPL)日线分析"),
        ("0700.HK", "4h", "腾讯(0700.HK)4小时线分析"),
        ("000001.SS", "1d", "上证指数(000001.SS)日线分析"),
        ("^GSPC", "1d", "标普500(^GSPC)日线分析"),
        ("BABA", "1d", "阿里巴巴(BABA)日线分析")
    ]
    
    analysis_results = []
    
    for symbol, interval, description in test_cases:
        exporter.add_section(description, 3)
        result = await analyze_stock_price(symbol, interval)
        exporter.add_content(result)
        
        # 提取关键信息用于汇总表格
        lines = result.split('\n')
        price_line = next((line for line in lines if "当前价格:" in line), "N/A")
        change_line = next((line for line in lines if "涨跌幅:" in line), "N/A")
        patterns = "有形态" if "检测到的K线形态:" in result else "无形态"
        
        price_value = price_line.split(":")[1].strip() if ":" in price_line else "N/A"
        change_value = change_line.split(":")[1].strip() if ":" in change_line else "N/A"
        
        analysis_results.append([
            symbol, interval, price_value, change_value, patterns
        ])
    
    # 添加汇总表格
    exporter.add_section("分析结果汇总", 3)
    exporter.add_table(
        ["股票代码", "周期", "当前价格", "涨跌幅", "K线形态"],
        analysis_results
    )

async def test_different_intervals():
    """测试不同时间周期"""
    exporter.add_section("不同时间周期测试", 2)
    
    symbol = "AAPL"
    intervals = ["1h", "4h", "1d", "1wk"]
    
    interval_results = []
    
    for interval in intervals:
        exporter.add_section(f"AAPL {interval}周期分析", 3)
        result = await analyze_stock_price(symbol, interval)
        exporter.add_content(result)
        
        # 提取技术指标信息
        lines = result.split('\n')
        rsi_line = next((line for line in lines if "RSI:" in line), "RSI: N/A")
        macd_line = next((line for line in lines if "MACD:" in line), "MACD: N/A")
        bb_line = next((line for line in lines if "布林带:" in line), "布林带: N/A")
        
        interval_results.append([
            interval, rsi_line, macd_line, bb_line
        ])
    
    # 添加技术指标对比表格
    exporter.add_section("不同周期技术指标对比", 3)
    exporter.add_table(
        ["周期", "RSI", "MACD", "布林带"],
        interval_results
    )

async def test_examples_and_info():
    """测试示例和信息功能"""
    exporter.add_section("示例和信息功能测试", 2)
    
    # 测试获取股票示例
    exporter.add_section("股票代码示例", 3)
    result = await get_stock_examples()
    # 限制输出长度避免重复问题
    lines = result.split('\n')
    if len(lines) > 40:
        lines = lines[:40] + ["", "... (内容已截断)"]
    exporter.add_content("\n".join(lines))
    
    # 测试K线形态说明
    exporter.add_section("K线形态说明", 3)
    result = await get_candlestick_patterns_info()
    exporter.add_content(result)

async def test_error_handling():
    """测试错误处理"""
    exporter.add_section("错误处理测试", 2)
    
    error_cases = [
        ("INVALID_STOCK", "1d", "测试无效股票代码"),
        ("AAPL", "1w", "测试无效时间周期"),
        ("", "搜索空关键词")
    ]
    
    for case1, case2, description in error_cases:
        exporter.add_section(description, 3)
        if description == "搜索空关键词":
            result = await search_stock_symbols(case1)
        else:
            result = await analyze_stock_price(case1, case2)
        exporter.add_content(result)

async def test_advanced_analysis():
    """测试高级分析功能"""
    exporter.add_section("高级分析测试", 2)
    
    # 测试多个热门股票
    popular_stocks = [
        ("TSLA", "1d", "特斯拉"),
        ("NVDA", "1d", "英伟达"), 
        ("MSFT", "1d", "微软"),
        ("GOOGL", "1d", "谷歌")
    ]
    
    performance_summary = []
    
    for symbol, interval, description in popular_stocks:
        exporter.add_section(f"{description}({symbol})日线分析", 3)
        result = await analyze_stock_price(symbol, interval)
        exporter.add_content(result)
        
        # 分析性能指标
        lines = result.split('\n')
        price_line = next((line for line in lines if "当前价格:" in line), "")
        change_line = next((line for line in lines if "涨跌幅:" in line), "")
        rsi_line = next((line for line in lines if "RSI:" in line), "")
        
        # 提取数值
        try:
            price_text = price_line.split(":")[1].strip() if ":" in price_line else "N/A"
            price = float(price_text) if price_text.replace('.', '').replace('-', '').isdigit() else "N/A"
            
            change_parts = change_line.split("(")
            change_pct = change_parts[1].split(")")[0] if len(change_parts) > 1 else "N/A"
            
            rsi_parts = rsi_line.split(":")
            rsi_value = rsi_parts[1].split("(")[0].strip() if len(rsi_parts) > 1 else "N/A"
            
            performance_summary.append([
                symbol, description, price, change_pct, rsi_value
            ])
        except (IndexError, ValueError, AttributeError):
            performance_summary.append([symbol, description, "N/A", "N/A", "N/A"])
    
    # 添加性能汇总表格
    exporter.add_section("热门股票性能汇总", 3)
    exporter.add_table(
        ["股票代码", "描述", "当前价格", "涨跌幅", "RSI"],
        performance_summary
    )

async def test_specific_stocks():
    """测试特定股票分析功能"""
    exporter.add_section("特定股票分析测试", 2)
    
    # 用户可以在这里添加想要测试的特定股票
    specific_stocks = [
        # 格式: (股票代码, 时间周期, 描述)
        ("AAPL", "1d", "苹果日线"),
        ("MSFT", "1d", "微软日线"),
        ("TSLA", "1d", "特斯拉日线"),
        ("NVDA", "1d", "英伟达日线"),
        ("AMZN", "1d", "亚马逊日线"),
        ("BABA", "1d", "阿里巴巴日线"),
        ("0700.HK", "1d", "腾讯日线"),
        ("000001.SS", "1d", "上证指数日线"),
        ("^GSPC", "1d", "标普500日线"),
        ("^HSI", "1d", "恒生指数日线"),
    ]
    
    specific_results = []
    
    for symbol, interval, description in specific_stocks:
        exporter.add_section(f"{description} ({symbol})", 3)
        print(f"正在分析 {symbol} {interval}...")
        result = await analyze_stock_price(symbol, interval)
        exporter.add_content(result)
        
        # 提取关键信息
        lines = result.split('\n')
        price_line = next((line for line in lines if "当前价格:" in line), "N/A")
        change_line = next((line for line in lines if "涨跌幅:" in line), "N/A")
        rsi_line = next((line for line in lines if "RSI:" in line), "RSI: N/A")
        
        price_value = price_line.split(":")[1].strip() if ":" in price_line else "N/A"
        change_value = change_line.split(":")[1].strip() if ":" in change_line else "N/A"
        rsi_value = rsi_line.split(":")[1].split("(")[0].strip() if ":" in rsi_line else "N/A"
        
        # 检测K线形态
        patterns = []
        if "检测到的K线形态:" in result:
            pattern_section = result.split("检测到的K线形态:")[1]
            if "技术指标:" in pattern_section:
                pattern_section = pattern_section.split("技术指标:")[0]
            pattern_lines = pattern_section.strip().split('\n')
            for line in pattern_lines:
                if "🟢" in line or "🔴" in line or "🟡" in line:
                    # 提取形态名称
                    pattern_name = line.split(" ")[-1].strip("()")
                    patterns.append(pattern_name)
        
        pattern_str = ", ".join(patterns) if patterns else "无"
        
        specific_results.append([
            symbol, description, price_value, change_value, rsi_value, pattern_str
        ])
    
    # 添加特定股票汇总表格
    exporter.add_section("特定股票分析汇总", 3)
    exporter.add_table(
        ["股票代码", "描述", "当前价格", "涨跌幅", "RSI", "K线形态"],
        specific_results
    )

async def test_custom_stock_analysis():
    """测试自定义股票分析"""
    exporter.add_section("自定义股票分析测试", 2)
    
    # 这里可以添加用户自定义的股票分析
    custom_stocks = [
        # 添加您想要分析的特定股票
        # 格式: (股票代码, 时间周期, 描述)
        ("005930.KS", "1d", "三星电子"),  # 三星电子
        ("7203.T", "1d", "丰田汽车"),     # 丰田汽车
        ("9984.T", "1d", "软银集团"),     # 软银集团
        ("BTC-USD", "1d", "比特币"),      # 比特币
        ("ETH-USD", "1d", "以太坊"),      # 以太坊
    ]
    
    if custom_stocks:
        custom_results = []
        
        for symbol, interval, description in custom_stocks:
            exporter.add_section(f"自定义分析: {description} ({symbol})", 3)
            print(f"正在分析自定义股票 {symbol} {interval}...")
            result = await analyze_stock_price(symbol, interval)
            exporter.add_content(result)
            
            # 检查是否分析成功
            if "分析失败" not in result and "无效" not in result:
                lines = result.split('\n')
                price_line = next((line for line in lines if "当前价格:" in line), "N/A")
                change_line = next((line for line in lines if "涨跌幅:" in line), "N/A")
                
                price_value = price_line.split(":")[1].strip() if ":" in price_line else "N/A"
                change_value = change_line.split(":")[1].strip() if ":" in change_line else "N/A"
                
                custom_results.append([
                    symbol, description, price_value, change_value, "✅ 成功"
                ])
            else:
                custom_results.append([
                    symbol, description, "N/A", "N/A", "❌ 失败"
                ])
        
        # 添加自定义分析汇总表格
        exporter.add_section("自定义股票分析汇总", 3)
        exporter.add_table(
            ["股票代码", "描述", "当前价格", "涨跌幅", "状态"],
            custom_results
        )
    else:
        exporter.add_content("暂无自定义股票分析")

async def test_quick_analysis():
    """快速分析测试 - 只测试几个关键股票"""
    exporter.add_section("快速分析测试", 2)
    
    # 只测试几个关键股票，节省时间
    quick_stocks = [
        ("AAPL", "15m", "苹果"),
        ("MSFT", "1d", "微软"),
        ("TSLA", "1d", "特斯拉"),
        ("0700.HK", "1d", "腾讯"),
        ("^GSPC", "1d", "标普500"),
    ]
    
    quick_results = []
    
    for symbol, interval, description in quick_stocks:
        exporter.add_section(f"快速分析: {description} ({symbol})", 3)
        print(f"快速分析 {symbol}...")
        result = await analyze_stock_price(symbol, interval)
        
        # 只显示关键信息，避免输出过长
        key_lines = []
        for line in result.split('\n'):
            if any(keyword in line for keyword in ["📈", "⏰", "💰", "📊", "🕯️", "RSI", "MACD", "布林带"]):
                key_lines.append(line)
        
        exporter.add_content("\n".join(key_lines))
        
        # 提取关键指标
        lines = result.split('\n')
        price_line = next((line for line in lines if "当前价格:" in line), "N/A")
        change_line = next((line for line in lines if "涨跌幅:" in line), "N/A")
        rsi_line = next((line for line in lines if "RSI:" in line), "RSI: N/A")
        
        price_value = price_line.split(":")[1].strip() if ":" in price_line else "N/A"
        change_value = change_line.split(":")[1].strip() if ":" in change_line else "N/A"
        rsi_value = rsi_line.split(":")[1].split("(")[0].strip() if ":" in rsi_line else "N/A"
        
        quick_results.append([
            symbol, description, price_value, change_value, rsi_value
        ])
    
    # 添加快速分析汇总表格
    exporter.add_section("快速分析汇总", 3)
    exporter.add_table(
        ["股票代码", "描述", "当前价格", "涨跌幅", "RSI"],
        quick_results
    )

async def generate_summary():
    """生成测试总结"""
    exporter.add_section("测试总结", 2)
    
summary_content = """
## 🎯 测试概览

本次测试全面验证了股票分析MCP工具的以下功能：

### ✅ 已测试功能
1. **股票搜索功能** - 支持通过公司名称搜索股票代码
2. **多周期分析** - 支持1小时、4小时、日线、周线分析
3. **K线形态识别** - 自动识别常见K线形态
4. **技术指标计算** - RSI、MACD、布林带、移动平均线等
5. **错误处理** - 无效输入和错误情况的处理
6. **多市场支持** - 美股、港股、A股、指数等
7. **特定股票分析** - 支持用户指定股票代码进行分析

### 📊 测试覆盖
- **股票数量**: 20+ 只热门股票
- **时间周期**: 4种不同周期
- **市场类型**: 美股、港股、A股、指数、加密货币
- **技术指标**: 5+ 种常用指标
- **K线形态**: 10+ 种常见形态

### 🔧 技术特点
- 基于雅虎财经API的实时数据
- 改进的K线形态识别算法
- 多维度技术分析
- 友好的中文输出界面
- 冲突形态检测和过滤

### ⚠️ 已知限制
- 中文搜索功能受限（雅虎财经API限制）
- 部分技术指标需要TA-Lib支持
- 数据获取依赖网络连接

### 📈 使用建议
1. 对于短线交易，建议使用1小时或4小时线
2. 对于中长期投资，建议使用日线或周线
3. 结合多个技术指标进行综合判断
4. K线形态需要结合趋势背景分析
5. 特定股票分析可用于监控投资组合

### 🔍 如何添加自定义股票
在 `test_specific_stocks()` 函数中的 `specific_stocks` 列表中添加：
```python
("股票代码", "时间周期", "描述")"""


exporter.add_content(summary_content)

async def main():
    """主测试函数"""
    print("🚀 股票分析MCP全面测试开始...")
    print("=" * 60)

 
    # 添加测试报告标题
    exporter.add_section("股票分析MCP测试报告", 1)
    exporter.add_content(f"**测试执行时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        # 初始化
        await stock_analyzer.initialize()
        
        # 询问用户想要运行哪种测试
        print("\n请选择测试模式:")
        print("1. 完整测试 (所有功能)")
        print("2. 快速测试 (关键股票)")
        print("3. 特定股票测试")
        
        choice = input("\n请输入选择 (1/2/3, 默认为1): ").strip()
        
        if choice == "2":
            # 快速测试模式
            print("🔍 运行快速测试...")
            await test_quick_analysis()
        elif choice == "3":
            # 特定股票测试模式
            print("🎯 运行特定股票测试...")
            await test_specific_stocks()
            await test_custom_stock_analysis()
        else:
            # 完整测试模式
            print("🔍 测试搜索功能...")
            await test_search_functionality()
            
            print("📈 测试股票分析...")
            await test_stock_analysis()
            
            print("⏰ 测试不同时间周期...")
            await test_different_intervals()
            
            print("📋 测试示例和信息...")
            await test_examples_and_info()
            
            print("❌ 测试错误处理...")
            await test_error_handling()
            
            print("🚀 测试高级分析...")
            await test_advanced_analysis()
            
            print("🎯 测试特定股票分析...")
            await test_specific_stocks()
            
            print("🔧 测试自定义股票分析...")
            await test_custom_stock_analysis()
        
        print("📝 生成测试总结...")
        await generate_summary()
        
        # 保存测试报告
        filename = exporter.save_to_file()
        
        print(f"\n✅ 所有测试完成!")
        print(f"📄 详细测试报告已保存至: {filename}")
        
    except Exception as e:
        error_msg = f"❌ 测试过程中出现错误: {e}"
        print(error_msg)
        import traceback
        traceback.print_exc()
        
        exporter.add_section("测试错误", 2)
        exporter.add_content(error_msg)
        
        # 即使出错也保存报告
        filename = exporter.save_to_file("stock_analysis_test_ERROR.md")

    finally:
        # 清理资源
        await stock_analyzer.close()


if __name__ == "__main__":
    asyncio.run(main())
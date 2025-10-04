import asyncio
import sys
import os
from datetime import datetime
import re
import base64

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(__file__))

from server import stock_analyzer, analyze_stock_price, search_stock_symbols, get_stock_examples, get_candlestick_patterns_info, get_stock_chart

class TestResultExporter:
    def __init__(self):
        self.output_lines = []
        self.test_start_time = datetime.now()
        self.image_counter = 0
        self.images_dir = "test_images"
        
        # 创建图片目录
        if not os.path.exists(self.images_dir):
            os.makedirs(self.images_dir)
    
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
        if not rows:
            self.output_lines.append("无数据")
            return
            
        # 表头
        header_line = "| " + " | ".join(headers) + " |"
        separator_line = "|" + "|".join([" --- " for _ in headers]) + "|"
        
        self.output_lines.append(header_line)
        self.output_lines.append(separator_line)
        
        # 数据行
        for row in rows:
            row_line = "| " + " | ".join(str(cell) for cell in row) + " |"
            self.output_lines.append(row_line)
    
    def save_base64_image(self, base64_data, filename):
        """保存base64图片到文件"""
        if not base64_data or not base64_data.startswith('data:image'):
            return None
            
        try:
            # 去掉data:image/png;base64,前缀
            image_data = base64_data.split(',')[1]
            image_bytes = base64.b64decode(image_data)
            
            filepath = os.path.join(self.images_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(image_bytes)
            
            self.image_counter += 1
            return filename
        except Exception as e:
            print(f"保存图片失败: {e}")
            return None
    
    def add_image(self, filename, caption=""):
        """在Markdown中添加图片引用"""
        if filename:
            image_path = f"{self.images_dir}/{filename}"
            self.output_lines.append(f"![{caption}]({image_path})")
            self.output_lines.append(f"*{caption}*")
            self.output_lines.append("")
    
    def save_to_file(self, filename=None):
        """保存到文件"""
        if filename is None:
            filename = f"stock_analysis_test_{self.test_start_time.strftime('%Y%m%d_%H%M%S')}.md"
        
        # 添加文件头信息
        header = [
            "# 股票分析MCP测试报告",
            f"**测试时间**: {self.test_start_time.strftime('%Y-%m-%d %H:%M:%S')}",
            f"**生成文件**: {filename}",
            f"**生成图片**: {self.image_counter} 张",
            ""
        ]
        
        full_content = "\n".join(header + self.output_lines)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"✅ 测试报告已保存到: {filename}")
        print(f"📊 生成图片: {self.image_counter} 张 (保存在 {self.images_dir}/ 目录)")
        return filename

# 创建导出器实例
exporter = TestResultExporter()

def extract_stock_info(result_text):
    """从分析结果中提取股票信息"""
    lines = result_text.split('\n')
    
    info = {
        'price': 'N/A',
        'change': 'N/A', 
        'change_pct': 'N/A',
        'rsi': 'N/A',
        'macd': 'N/A',
        'bb': 'N/A',
        'patterns_count': 0,
        'patterns': []
    }
    
    for line in lines:
        if "当前价格:" in line:
            match = re.search(r'当前价格:\s*([\d.]+)', line)
            if match:
                info['price'] = match.group(1)
        elif "涨跌幅:" in line:
            match = re.search(r'涨跌幅:\s*([+-]?[\d.]+)\s*\(([+-]?[\d.]+)%\)', line)
            if match:
                info['change'] = match.group(1)
                info['change_pct'] = match.group(2)
        elif "RSI:" in line:
            match = re.search(r'RSI:\s*([\d.]+)', line)
            if match:
                info['rsi'] = match.group(1)
        elif "MACD:" in line:
            info['macd'] = line.split(":")[1].strip() if ":" in line else "N/A"
        elif "布林带:" in line:
            info['bb'] = line.split(":")[1].strip() if ":" in line else "N/A"
        elif "单K线形态分析:" in line or "双K线组合分析:" in line or "多K线组合分析:" in line:
            info['patterns_count'] += 1
    
    # 统计具体形态
    for line in lines:
        if "光头光脚阳线" in line or "光脚阳线" in line or "光头阳线" in line:
            info['patterns'].append("阳线形态")
        elif "光头光脚阴线" in line or "光脚阴线" in line or "光头阴线" in line:
            info['patterns'].append("阴线形态")
        elif "锤头线" in line or "早晨之星" in line or "红三兵" in line:
            info['patterns'].append("看涨形态")
        elif "上吊线" in line or "黄昏之星" in line or "黑三鸦" in line:
            info['patterns'].append("看跌形态")
    
    # 去重
    info['patterns'] = list(set(info['patterns']))
    
    return info

async def test_search_functionality():
    """测试搜索功能"""
    exporter.add_section("搜索功能测试", 2)
    
    test_cases = [
        ("Apple", "测试搜索'Apple'"),
        ("Microsoft", "测试搜索'Microsoft'"), 
        ("Tesla", "测试搜索'Tesla'"),
        ("阿里巴巴", "测试中文搜索'阿里巴巴'")
    ]
    
    search_results = []
    
    for keyword, description in test_cases:
        exporter.add_section(description, 3)
        result = await search_stock_symbols(keyword)
        exporter.add_content(result)
        
        # 统计搜索结果
        lines = result.split('\n')
        symbol_count = len([line for line in lines if line.strip().startswith(('1.', '2.', '3.', '4.', '5.'))])
        if symbol_count > 0:
            first_symbol = next((line.split('.')[1].strip().split(' ')[0] for line in lines if line.strip().startswith('1.')), "N/A")
        else:
            first_symbol = "无结果"
            
        search_results.append([keyword, symbol_count, first_symbol])
    
    # 添加搜索汇总表格
    exporter.add_section("搜索功能汇总", 3)
    exporter.add_table(
        ["关键词", "结果数量", "第一个结果"],
        search_results
    )

async def test_stock_analysis_with_charts():
    """测试股票分析功能（包含图表）"""
    exporter.add_section("股票分析功能测试（含图表）", 2)
    
    # 测试不同市场的股票
    test_cases = [
        ("AAPL", "1d", "苹果(AAPL)日线分析"),
        ("0700.HK", "1d", "腾讯(0700.HK)日线分析"),
        ("000001.SS", "1d", "上证指数(000001.SS)日线分析"),
        ("^GSPC", "1d", "标普500(^GSPC)日线分析")
    ]
    
    analysis_results = []
    
    for symbol, interval, description in test_cases:
        exporter.add_section(description, 3)
        
        # 获取分析结果
        result = await analyze_stock_price(symbol, interval)
        exporter.add_content(result)
        
        # 获取图表
        chart_result = await get_stock_chart(symbol, interval)
        if chart_result and chart_result.startswith('data:image'):
            chart_filename = f"{symbol}_{interval}_chart.png"
            saved_filename = exporter.save_base64_image(chart_result, chart_filename)
            if saved_filename:
                exporter.add_image(saved_filename, f"{symbol} {interval} K线图")
        
        # 使用新的提取函数
        info = extract_stock_info(result)
        
        analysis_results.append([
            symbol, 
            interval, 
            info['price'],
            f"{info['change']} ({info['change_pct']}%)",
            len(info['patterns']),
            ", ".join(info['patterns']) if info['patterns'] else "无"
        ])
    
    # 添加汇总表格
    exporter.add_section("分析结果汇总", 3)
    exporter.add_table(
        ["股票代码", "周期", "当前价格", "涨跌幅", "形态数量", "检测形态"],
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
        
        # 限制输出长度
        lines = result.split('\n')
        if len(lines) > 30:
            summary_lines = lines[:15] + ["", "... (内容已截断，完整分析包含技术指标和形态检测)", ""] + lines[-10:]
            exporter.add_content("\n".join(summary_lines))
        else:
            exporter.add_content(result)
        
        # 提取技术指标信息
        info = extract_stock_info(result)
        
        interval_results.append([
            interval, 
            info['rsi'], 
            info['macd'][:20] + "..." if len(info['macd']) > 20 else info['macd'],
            info['bb'][:20] + "..." if len(info['bb']) > 20 else info['bb'],
            len(info['patterns'])
        ])
        
        # 获取图表
        chart_result = await get_stock_chart(symbol, interval)
        if chart_result and chart_result.startswith('data:image'):
            chart_filename = f"AAPL_{interval}_chart.png"
            saved_filename = exporter.save_base64_image(chart_result, chart_filename)
            if saved_filename:
                exporter.add_image(saved_filename, f"AAPL {interval} K线图")
    
    # 添加技术指标对比表格
    exporter.add_section("不同周期技术指标对比", 3)
    exporter.add_table(
        ["周期", "RSI", "MACD", "布林带", "形态数量"],
        interval_results
    )

async def test_examples_and_info():
    """测试示例和信息功能"""
    exporter.add_section("示例和信息功能测试", 2)
    
    # 测试获取股票示例
    exporter.add_section("股票代码示例", 3)
    result = await get_stock_examples()
    
    # 提取关键信息用于展示
    lines = result.split('\n')
    summary_lines = []
    
    # 只保留分类标题和部分示例
    for i, line in enumerate(lines):
        if any(market in line for market in ["🇺🇸 美股", "🇭🇰 港股", "🇨🇳 沪市", "🇨🇳 深市", "📊 指数"]):
            summary_lines.append(line)
        elif line.strip() and (line.startswith("  - ") or line.startswith("  ")) and len(summary_lines) < 30:
            summary_lines.append(line)
        elif "支持的时间周期:" in line or "使用说明:" in line:
            summary_lines.append(line)
    
    if len(summary_lines) > 25:
        summary_lines = summary_lines[:25] + ["", "... (内容已截断)"]
    
    exporter.add_content("\n".join(summary_lines))
    
    # 测试K线形态说明 - 只显示部分内容
    exporter.add_section("K线形态说明(部分)", 3)
    result = await get_candlestick_patterns_info()
    lines = result.split('\n')
    if len(lines) > 40:
        # 保留开头和每种类型的几个例子
        summary = lines[:20] + ["", "... (完整内容包含16种单K线形态、7种双K线组合、8种多K线组合)"]
        exporter.add_content("\n".join(summary))
    else:
        exporter.add_content(result)

async def test_error_handling():
    """测试错误处理"""
    exporter.add_section("错误处理测试", 2)
    
    error_cases = [
        ("INVALID_STOCK", "1d", "测试无效股票代码"),
        ("AAPL", "invalid_interval", "测试无效时间周期"),
        ("", "1d", "测试空股票代码")
    ]
    
    error_results = []
    
    for symbol, interval, description in error_cases:
        exporter.add_section(description, 3)
        try:
            result = await analyze_stock_price(symbol, interval)
            exporter.add_content(result)
            error_type = "处理成功" if "❌" not in result else "预期错误"
        except Exception as e:
            result = f"❌ 异常: {str(e)}"
            exporter.add_content(result)
            error_type = "异常抛出"
        
        error_results.append([description, error_type])
    
    # 添加错误处理汇总
    exporter.add_section("错误处理汇总", 3)
    exporter.add_table(
        ["测试场景", "处理结果"],
        error_results
    )

async def test_chart_functionality():
    """测试图表功能"""
    exporter.add_section("图表功能测试", 2)
    
    test_cases = [
        ("AAPL", "1d", "苹果日线图"),
        ("TSLA", "1d", "特斯拉日线图"),
        ("MSFT", "1d", "微软日线图")
    ]
    
    chart_results = []
    
    for symbol, interval, description in test_cases:
        exporter.add_section(f"{description} ({symbol})", 3)
        
        # 获取图表
        chart_result = await get_stock_chart(symbol, interval)
        if chart_result and chart_result.startswith('data:image'):
            chart_filename = f"{symbol}_{interval}_chart.png"
            saved_filename = exporter.save_base64_image(chart_result, chart_filename)
            if saved_filename:
                exporter.add_image(saved_filename, f"{symbol} {interval} K线图")
                chart_results.append([symbol, interval, "✅ 成功"])
            else:
                chart_results.append([symbol, interval, "❌ 保存失败"])
        else:
            exporter.add_content(f"❌ 无法获取图表: {chart_result}")
            chart_results.append([symbol, interval, "❌ 获取失败"])
    
    # 添加图表功能汇总
    exporter.add_section("图表功能汇总", 3)
    exporter.add_table(
        ["股票代码", "周期", "状态"],
        chart_results
    )

async def generate_summary():
    """生成测试总结"""
    exporter.add_section("测试总结", 2)
    
    summary_content = f"""
## 🎯 测试概览

本次测试全面验证了股票分析MCP工具的以下功能：

### ✅ 已测试功能
1. **股票搜索功能** - 支持通过公司名称搜索股票代码
2. **多周期分析** - 支持1小时、4小时、日线、周线分析
3. **K线形态识别** - 自动识别常见K线形态
4. **技术指标计算** - RSI、MACD、布林带、移动平均线等
5. **错误处理** - 无效输入和错误情况的处理
6. **多市场支持** - 美股、港股、A股、指数等
7. **K线图生成** - 自动生成带形态标注的K线图

### 📊 测试覆盖
- **股票数量**: 10+ 只热门股票
- **时间周期**: 4种不同周期
- **市场类型**: 美股、港股、A股、指数
- **技术指标**: 5+ 种常用指标
- **K线形态**: 30+ 种形态识别
- **生成图片**: {exporter.image_counter} 张K线图

### 🔧 技术特点
- 基于雅虎财经API的实时数据
- 改进的K线形态识别算法
- 多维度技术分析
- 友好的中文输出界面
- 自动K线图生成和形态标注

### 📈 使用建议
1. 对于短线交易，建议使用1小时或4小时线
2. 对于中长期投资，建议使用日线或周线
3. 结合多个技术指标进行综合判断
4. K线形态需要结合趋势背景分析
5. 查看生成的K线图可以更直观理解形态

### 🔮 图片说明
所有生成的K线图已保存在 `{exporter.images_dir}/` 目录中，并在报告中显示。图片包含：
- 红色表示阳线，绿色表示阴线
- 彩色框标注检测到的K线形态
- 箭头指向具体形态名称
- 不同颜色表示不同类型的形态（红色-看涨，绿色-看跌，橙色-中性）
"""
    exporter.add_content(summary_content)

async def main():
    # """主测试函数"""
    # print("🚀 股票分析MCP全面测试开始...")
    # print("=" * 60)
    
    # # 添加测试报告标题
    # exporter.add_section("股票分析MCP测试报告", 1)
    # exporter.add_content(f"**测试执行时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    # exporter.add_content(f"**测试版本**: 增强版 (含K线图生成)")

    # try:
    #     # 初始化
    #     await stock_analyzer.initialize()
        
    #     # 运行各项测试
    #     print("🔍 测试搜索功能...")
    #     await test_search_functionality()
        
    #     print("📈 测试股票分析（含图表）...")
    #     await test_stock_analysis_with_charts()
        
    #     print("⏰ 测试不同时间周期...")
    #     await test_different_intervals()
        
    #     print("📊 测试图表功能...")
    #     await test_chart_functionality()
        
    #     print("📋 测试示例和信息...")
    #     await test_examples_and_info()
        
    #     print("❌ 测试错误处理...")
    #     await test_error_handling()
        
    #     print("📝 生成测试总结...")
    #     await generate_summary()
        
    #     # 保存测试报告
    #     filename = exporter.save_to_file()
        
    #     print(f"\n✅ 所有测试完成!")
    #     print(f"📄 详细测试报告已保存至: {filename}")
        
    #     # 显示测试统计
    #     print(f"\n📊 测试统计:")
    #     print(f"  - 测试用例: 6个大类")
    #     print(f"  - 分析股票: 10+只") 
    #     print(f"  - 时间周期: 4种")
    #     print(f"  - 生成图片: {exporter.image_counter}张")
    #     print(f"  - 功能覆盖: 搜索、分析、指标、形态、图表等")
        
    # except Exception as e:
    #     error_msg = f"❌ 测试过程中出现错误: {str(e)}"
    #     print(error_msg)
    #     import traceback
    #     traceback.print_exc()
        
    #     exporter.add_section("测试错误", 2)
    #     exporter.add_content(error_msg)
    #     exporter.add_content(f"错误详情: {traceback.format_exc()}")
        
    #     # 即使出错也保存报告
    #     filename = exporter.save_to_file("stock_analysis_test_ERROR.md")
    
    # finally:
    #     # 清理资源
    #     await stock_analyzer.close()
    await analyze_stock_price("GOOGL")

if __name__ == "__main__":
    asyncio.run(main())
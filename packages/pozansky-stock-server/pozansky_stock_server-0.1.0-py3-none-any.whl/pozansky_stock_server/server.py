import asyncio
import httpx
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from mcp.server.fastmcp import FastMCP
import json

# 创建 FastMCP 实例
mcp = FastMCP("StockAnalysisServer")

class StockAnalyzer:
    def __init__(self):
        self.client = None
        # 扩展支持的股票列表
        self.market_examples = {
            "US": [
                "AAPL", "GOOGL", "TSLA", "MSFT", "AMZN", "META", "NVDA", "NFLX", 
                "AMD", "INTC", "BABA", "PDD", "JD", "BAC", "JPM", "WMT", "DIS", "V", "MA"
            ],
            "HK": [
                "0700.HK", "0005.HK", "1299.HK", "0939.HK", "2318.HK", "3988.HK",
                "0883.HK", "0388.HK", "0288.HK", "2628.HK", "0960.HK", "1810.HK"
            ],
            "CN_SH": [  # 沪市
                "000001.SS", "600036.SS", "601318.SS", "600519.SS", "601888.SS",
                "601398.SS", "601857.SS", "601766.SS", "601668.SS", "601989.SS"
            ],
            "CN_SZ": [  # 深市
                "399001.SZ", "000858.SZ", "000333.SZ", "002415.SZ", "000001.SZ",
                "000002.SZ", "000063.SZ", "002594.SZ", "300750.SZ", "300059.SZ"
            ],
            "INDEX": [  # 指数
                "^GSPC",  # 标普500
                "^IXIC",  # 纳斯达克
                "^DJI",   # 道琼斯
                "^HSI",   # 恒生指数
                "000001.SS",  # 上证指数
                "399001.SZ"   # 深证成指
            ]
        }
        
        # K线形态分类
        self.patterns = {
            "SINGLE": [
                "光头光脚阳线", "光脚阳线", "光头阳线", "带上下影线的阳线",
                "光头光脚阴线", "光脚阴线", "光头阴线", "带上下影线的阴线",
                "十字线", "T字线", "倒T字线", "一字线", "锤头线", "上吊线", 
                "倒锤头线", "射击之星"
            ],
            "DOUBLE": [
                "乌云盖顶组合", "旭日东升组合", "抱线组合", "孕线组合", 
                "插入线组合", "跳空组合", "双飞乌鸦组合"
            ],
            "MULTI": [
                "黄昏之星", "红三兵", "多方炮", "上升三法", "早晨之星", 
                "黑三鸦", "空方炮", "下降三法"
            ]
        }
        
        # 支持的时间周期及其对应的数据范围
        self.supported_intervals = {
            "1m": "1d",    # 1分钟线，1天数据
            "2m": "1d",    # 2分钟线，1天数据
            "5m": "1d",    # 5分钟线，1天数据
            "15m": "5d",   # 15分钟线，5天数据
            "30m": "5d",   # 30分钟线，5天数据
            "60m": "10d",  # 60分钟线，10天数据
            "90m": "10d",  # 90分钟线，10天数据
            "1h": "1mo",   # 1小时线，1个月数据
            "4h": "3mo",   # 4小时线，3个月数据
            "1d": "1y",    # 日线，1年数据
            "1wk": "2y",   # 周线，2年数据
            "1mo": "5y"    # 月线，5年数据
        }

    async def initialize(self):
        """初始化HTTP客户端"""
        if self.client is None:
            self.client = httpx.AsyncClient(
                timeout=30.0,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
            )
        return True

    async def validate_symbol(self, symbol: str) -> bool:
        """验证股票代码是否有效"""
        try:
            # 尝试获取少量数据来验证代码
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
            params = {"range": "1d", "interval": "1d"}
            
            response = await self.client.get(url, params=params)
            data = response.json()
            
            if "chart" in data and "result" in data["chart"]:
                result = data["chart"]["result"][0]
                return "timestamp" in result and len(result["timestamp"]) > 0
            return False
            
        except Exception:
            return False

    async def search_symbols(self, keyword: str) -> List[Dict]:
        """搜索股票代码"""
        await self.initialize()
        
        try:
            url = f"https://query1.finance.yahoo.com/v1/finance/search"
            params = {"q": keyword, "quotesCount": 10, "newsCount": 0}
            
            response = await self.client.get(url, params=params)
            
            if response.status_code != 200:
                return []
                
            data = response.json()
            
            symbols = []
            if "quotes" in data:
                for quote in data["quotes"]:
                    if "symbol" in quote:
                        symbols.append({
                            "symbol": quote["symbol"],
                            "name": quote.get("longname", quote.get("shortname", "")),
                            "exchange": quote.get("exchange", ""),
                            "type": quote.get("quoteType", "")
                        })
            return symbols
            
        except Exception as e:
            print(f"搜索股票失败: {e}")
            return []

    async def get_stock_data(self, symbol: str, period: str = "1mo", interval: str = "1d") -> Optional[pd.DataFrame]:
        """获取股票数据"""
        await self.initialize()
        
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
            params = {
                "range": period,
                "interval": interval,
                "includePrePost": "false"
            }
            
            response = await self.client.get(url, params=params)
            data = response.json()
            
            if "chart" not in data or "result" not in data["chart"] or not data["chart"]["result"]:
                return None
                
            result = data["chart"]["result"][0]
            
            if "timestamp" not in result or not result["timestamp"]:
                return None
                
            timestamps = result["timestamp"]
            quotes = result["indicators"]["quote"][0]
            
            df = pd.DataFrame({
                'timestamp': timestamps,
                'open': quotes['open'],
                'high': quotes['high'], 
                'low': quotes['low'],
                'close': quotes['close'],
                'volume': quotes['volume']
            })
            
            df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')
            df = df.dropna()
            
            return df
            
        except Exception as e:
            print(f"获取股票数据失败 {symbol}: {e}")
            return None

    def _calculate_trend(self, df: pd.DataFrame, period: int) -> str:
        """计算趋势方向"""
        if len(df) < period:
            return "neutral"
        
        closes = df['close'].tail(period)
        if len(closes) < 2:
            return "neutral"
        
        price_change = (closes.iloc[-1] - closes.iloc[0]) / closes.iloc[0] * 100
        
        if price_change > 3:
            return "up"
        elif price_change < -3:
            return "down"
        else:
            return "neutral"

    def _analyze_candle_features(self, candle):
        """分析单根K线特征"""
        body = abs(candle['close'] - candle['open'])
        upper_shadow = candle['high'] - max(candle['open'], candle['close'])
        lower_shadow = min(candle['open'], candle['close']) - candle['low']
        total_range = candle['high'] - candle['low']
        
        if total_range == 0:
            return {}
            
        body_ratio = body / total_range
        upper_ratio = upper_shadow / total_range
        lower_ratio = lower_shadow / total_range
        
        is_bullish = candle['close'] > candle['open']
        is_bearish = candle['close'] < candle['open']
        
        return {
            'body': body,
            'upper_shadow': upper_shadow,
            'lower_shadow': lower_shadow,
            'total_range': total_range,
            'body_ratio': body_ratio,
            'upper_ratio': upper_ratio,
            'lower_ratio': lower_ratio,
            'is_bullish': is_bullish,
            'is_bearish': is_bearish
        }

    def detect_single_candle_patterns(self, current_candle, trend) -> List[Dict]:
        """检测单K线形态"""
        patterns = []
        candle_data = self._analyze_candle_features(current_candle)
        
        if not candle_data:
            return patterns
            
        body_ratio = candle_data['body_ratio']
        upper_ratio = candle_data['upper_ratio']
        lower_ratio = candle_data['lower_ratio']
        is_bullish = candle_data['is_bullish']
        is_bearish = candle_data['is_bearish']
        
        # 1. 光头光脚阳线
        if (is_bullish and upper_ratio < 0.05 and lower_ratio < 0.05 and body_ratio > 0.8):
            patterns.append({
                "name": "光头光脚阳线",
                "type": "BULLISH",
                "category": "SINGLE",
                "confidence": 0.9,
                "description": "没有上下影线，开盘价即最低价，收盘价即最高价，表示强烈的看涨信号"
            })
        
        # 2. 光脚阳线
        elif (is_bullish and lower_ratio < 0.05 and upper_ratio > 0.1 and body_ratio > 0.5):
            patterns.append({
                "name": "光脚阳线",
                "type": "BULLISH",
                "category": "SINGLE",
                "confidence": 0.7,
                "description": "没有下影线，表示买方力量强劲，但上方有压力"
            })
        
        # 3. 光头阳线
        elif (is_bullish and upper_ratio < 0.05 and lower_ratio > 0.1 and body_ratio > 0.5):
            patterns.append({
                "name": "光头阳线",
                "type": "BULLISH",
                "category": "SINGLE",
                "confidence": 0.7,
                "description": "没有上影线，收盘价即最高价，表示买方完全控制局面"
            })
        
        # 4. 带上下影线的阳线
        elif (is_bullish and upper_ratio > 0.1 and lower_ratio > 0.1 and body_ratio > 0.3):
            patterns.append({
                "name": "带上下影线的阳线",
                "type": "BULLISH",
                "category": "SINGLE",
                "confidence": 0.5,
                "description": "有上下影线，表示多空双方有争夺，但最终买方获胜"
            })
        
        # 5. 光头光脚阴线
        elif (is_bearish and upper_ratio < 0.05 and lower_ratio < 0.05 and body_ratio > 0.8):
            patterns.append({
                "name": "光头光脚阴线",
                "type": "BEARISH",
                "category": "SINGLE",
                "confidence": 0.9,
                "description": "没有上下影线，开盘价即最高价，收盘价即最低价，表示强烈的看跌信号"
            })
        
        # 6. 光脚阴线
        elif (is_bearish and lower_ratio < 0.05 and upper_ratio > 0.1 and body_ratio > 0.5):
            patterns.append({
                "name": "光脚阴线",
                "type": "BEARISH",
                "category": "SINGLE",
                "confidence": 0.7,
                "description": "没有下影线，表示卖方力量强劲，开盘后价格一路下跌"
            })
        
        # 7. 光头阴线
        elif (is_bearish and upper_ratio < 0.05 and lower_ratio > 0.1 and body_ratio > 0.5):
            patterns.append({
                "name": "光头阴线",
                "type": "BEARISH",
                "category": "SINGLE",
                "confidence": 0.7,
                "description": "没有上影线，开盘价即最高价，表示卖方完全控制局面"
            })
        
        # 8. 带上下影线的阴线
        elif (is_bearish and upper_ratio > 0.1 and lower_ratio > 0.1 and body_ratio > 0.3):
            patterns.append({
                "name": "带上下影线的阴线",
                "type": "BEARISH",
                "category": "SINGLE",
                "confidence": 0.5,
                "description": "有上下影线，表示多空双方有争夺，但最终卖方获胜"
            })
        
        # 9. 十字线
        elif (body_ratio < 0.1 and upper_ratio > 0.3 and lower_ratio > 0.3):
            patterns.append({
                "name": "十字线",
                "type": "NEUTRAL",
                "category": "SINGLE",
                "confidence": 0.8,
                "description": "开盘收盘价接近，表示市场犹豫不决，可能预示反转"
            })
        
        # 10. T字线
        elif (is_bullish and upper_ratio < 0.1 and lower_ratio > 0.6 and body_ratio < 0.3):
            patterns.append({
                "name": "T字线",
                "type": "BULLISH",
                "category": "SINGLE",
                "confidence": 0.7,
                "description": "卖方打压后买方收复失地，出现在底部时看涨信号更强"
            })
        
        # 11. 倒T字线
        elif (is_bearish and upper_ratio > 0.6 and lower_ratio < 0.1 and body_ratio < 0.3):
            patterns.append({
                "name": "倒T字线",
                "type": "BEARISH",
                "category": "SINGLE",
                "confidence": 0.7,
                "description": "买方推高后卖方打压回落，出现在顶部时看跌信号更强"
            })
        
        # 12. 一字线 (涨停或跌停)
        elif (body_ratio > 0.95 and upper_ratio < 0.05 and lower_ratio < 0.05):
            if is_bullish:
                patterns.append({
                    "name": "一字线(涨停)",
                    "type": "BULLISH",
                    "category": "SINGLE",
                    "confidence": 0.9,
                    "description": "开盘即涨停，表示极强的买盘力量"
                })
            else:
                patterns.append({
                    "name": "一字线(跌停)",
                    "type": "BEARISH",
                    "category": "SINGLE",
                    "confidence": 0.9,
                    "description": "开盘即跌停，表示极强的卖盘力量"
                })
        
        # 13. 锤头线 (出现在下跌趋势中)
        elif (trend == "down" and is_bullish and lower_ratio > 0.6 and upper_ratio < 0.2 and 0.1 < body_ratio < 0.4):
            patterns.append({
                "name": "锤头线",
                "type": "BULLISH",
                "category": "SINGLE",
                "confidence": 0.8,
                "description": "出现在下跌趋势中，长下影线表示买方力量开始增强"
            })
        
        # 14. 上吊线 (出现在上涨趋势中)
        elif (trend == "up" and is_bearish and lower_ratio > 0.6 and upper_ratio < 0.2 and 0.1 < body_ratio < 0.4):
            patterns.append({
                "name": "上吊线",
                "type": "BEARISH",
                "category": "SINGLE",
                "confidence": 0.8,
                "description": "出现在上涨趋势中，长下影线表示卖方力量开始增强"
            })
        
        # 15. 倒锤头线 (出现在下跌趋势中)
        elif (trend == "down" and is_bullish and upper_ratio > 0.6 and lower_ratio < 0.2 and 0.1 < body_ratio < 0.4):
            patterns.append({
                "name": "倒锤头线",
                "type": "BULLISH",
                "category": "SINGLE",
                "confidence": 0.7,
                "description": "出现在下跌趋势中，长上影线表示买方尝试反攻"
            })
        
        # 16. 射击之星 (出现在上涨趋势中)
        elif (trend == "up" and is_bearish and upper_ratio > 0.6 and lower_ratio < 0.2 and 0.1 < body_ratio < 0.4):
            patterns.append({
                "name": "射击之星",
                "type": "BEARISH",
                "category": "SINGLE",
                "confidence": 0.8,
                "description": "出现在上涨趋势中，长上影线表示上方压力巨大"
            })
        
        return patterns

    def detect_double_candle_patterns(self, current_candle, prev_candle, trend) -> List[Dict]:
        """检测双K线组合形态"""
        patterns = []
        
        current_data = self._analyze_candle_features(current_candle)
        prev_data = self._analyze_candle_features(prev_candle)
        
        if not current_data or not prev_data:
            return patterns
        
        # 1. 乌云盖顶组合
        if (trend == "up" and 
            prev_data['is_bullish'] and current_data['is_bearish'] and
            current_candle['open'] > prev_candle['high'] and
            current_candle['close'] < (prev_candle['open'] + prev_candle['close']) / 2 and
            current_candle['close'] > prev_candle['open']):
            patterns.append({
                "name": "乌云盖顶组合",
                "type": "BEARISH",
                "category": "DOUBLE",
                "confidence": 0.8,
                "description": "第二根阴线开盘高于前一根高点，收盘低于前一根中点，预示上涨趋势可能结束"
            })
        
        # 2. 旭日东升组合
        if (trend == "down" and 
            prev_data['is_bearish'] and current_data['is_bullish'] and
            current_candle['open'] < prev_candle['low'] and
            current_candle['close'] > (prev_candle['open'] + prev_candle['close']) / 2 and
            current_candle['close'] < prev_candle['open']):
            patterns.append({
                "name": "旭日东升组合",
                "type": "BULLISH",
                "category": "DOUBLE",
                "confidence": 0.8,
                "description": "第二根阳线开盘低于前一根低点，收盘高于前一根中点，预示下跌趋势可能结束"
            })
        
        # 3. 抱线组合 (吞没形态)
        if (trend == "down" and 
            current_data['is_bullish'] and prev_data['is_bearish'] and
            current_candle['close'] > prev_candle['open'] and 
            current_candle['open'] < prev_candle['close'] and
            current_data['body'] > prev_data['body'] * 1.2):
            patterns.append({
                "name": "抱线组合(看涨吞没)",
                "type": "BULLISH",
                "category": "DOUBLE",
                "confidence": 0.8,
                "description": "阳线完全吞没前一根阴线，强烈看涨反转信号"
            })
        
        if (trend == "up" and 
            current_data['is_bearish'] and prev_data['is_bullish'] and
            current_candle['close'] < prev_candle['open'] and 
            current_candle['open'] > prev_candle['close'] and
            current_data['body'] > prev_data['body'] * 1.2):
            patterns.append({
                "name": "抱线组合(看跌吞没)",
                "type": "BEARISH",
                "category": "DOUBLE",
                "confidence": 0.8,
                "description": "阴线完全吞没前一根阳线，强烈看跌反转信号"
            })
        
        # 4. 孕线组合
        if (abs(current_data['body']) < 0.5 * abs(prev_data['body']) and
            current_candle['high'] < prev_candle['high'] and 
            current_candle['low'] > prev_candle['low']):
            
            if trend == "down" and current_data['is_bullish'] and prev_data['is_bearish']:
                patterns.append({
                    "name": "孕线组合(看涨)",
                    "type": "BULLISH",
                    "category": "DOUBLE",
                    "confidence": 0.6,
                    "description": "小实体在大实体内，出现在下跌趋势中可能反转"
                })
            elif trend == "up" and current_data['is_bearish'] and prev_data['is_bullish']:
                patterns.append({
                    "name": "孕线组合(看跌)",
                    "type": "BEARISH",
                    "category": "DOUBLE",
                    "confidence": 0.6,
                    "description": "小实体在大实体内，出现在上涨趋势中可能反转"
                })
        
        # 5. 插入线组合
        if (trend == "down" and 
            prev_data['is_bearish'] and current_data['is_bullish'] and
            current_candle['open'] < prev_candle['low'] and
            current_candle['close'] > prev_candle['close'] and
            current_candle['close'] < (prev_candle['open'] + prev_candle['close']) / 2):
            patterns.append({
                "name": "插入线组合",
                "type": "BULLISH",
                "category": "DOUBLE",
                "confidence": 0.7,
                "description": "阳线插入到前一根阴线实体内部，显示买方力量增强"
            })
        
        # 6. 跳空组合
        gap_up = current_candle['low'] > prev_candle['high']
        gap_down = current_candle['high'] < prev_candle['low']
        
        if gap_up and current_data['is_bullish']:
            patterns.append({
                "name": "向上跳空组合",
                "type": "BULLISH",
                "category": "DOUBLE",
                "confidence": 0.7,
                "description": "第二根K线向上跳空，显示强劲的买方力量"
            })
        elif gap_down and current_data['is_bearish']:
            patterns.append({
                "name": "向下跳空组合",
                "type": "BEARISH",
                "category": "DOUBLE",
                "confidence": 0.7,
                "description": "第二根K线向下跳空，显示强劲的卖方力量"
            })
        
        # 7. 双飞乌鸦组合
        if (trend == "up" and 
            prev_data['is_bearish'] and current_data['is_bearish'] and
            current_candle['open'] > prev_candle['open'] and
            current_candle['close'] < prev_candle['close']):
            patterns.append({
                "name": "双飞乌鸦组合",
                "type": "BEARISH",
                "category": "DOUBLE",
                "confidence": 0.7,
                "description": "连续两根阴线，第二根开盘高于第一根但收盘更低，预示上涨乏力"
            })
        
        return patterns

    def detect_multi_candle_patterns(self, df, trend) -> List[Dict]:
        """检测多K线组合形态"""
        patterns = []
        
        if len(df) < 3:
            return patterns
        
        # 获取最近几根K线
        current = df.iloc[-1]
        prev = df.iloc[-2]
        prev2 = df.iloc[-3]
        prev3 = df.iloc[-4] if len(df) >= 4 else None
        
        current_data = self._analyze_candle_features(current)
        prev_data = self._analyze_candle_features(prev)
        prev2_data = self._analyze_candle_features(prev2)
        
        if not all([current_data, prev_data, prev2_data]):
            return patterns
        
        # 1. 黄昏之星
        if (trend == "up" and 
            prev2_data['is_bullish'] and  # 第一根阳线
            prev_data['body_ratio'] < 0.3 and  # 第二根小实体
            current_data['is_bearish'] and  # 第三根阴线
            current['close'] < (prev2['open'] + prev2['close']) / 2):  # 收盘低于第一根中点
            patterns.append({
                "name": "黄昏之星",
                "type": "BEARISH",
                "category": "MULTI",
                "confidence": 0.8,
                "description": "三根K线组合，出现在上涨趋势顶部，强烈看跌反转信号"
            })
        
        # 2. 红三兵
        if (trend == "down" and 
            current_data['is_bullish'] and prev_data['is_bullish'] and prev2_data['is_bullish'] and
            current['open'] > prev['open'] and prev['open'] > prev2['open'] and
            current['close'] > prev['close'] and prev['close'] > prev2['close'] and
            all(data['body_ratio'] > 0.5 for data in [current_data, prev_data, prev2_data])):
            patterns.append({
                "name": "红三兵",
                "type": "BULLISH",
                "category": "MULTI",
                "confidence": 0.8,
                "description": "连续三根实体逐渐增长的阳线，显示强劲的买方力量"
            })
        
        # 3. 多方炮
        if (prev3 is not None and 
            self._analyze_candle_features(prev3)['is_bullish'] and  # 第一根阳线
            prev2_data['is_bearish'] and  # 第二根阴线
            prev_data['is_bullish'] and  # 第三根阳线
            current_data['is_bullish'] and  # 第四根阳线
            prev['close'] > prev2['open'] and  # 第三根收盘高于第二根开盘
            current['close'] > prev['close']):  # 第四根收盘高于第三根
            patterns.append({
                "name": "多方炮",
                "type": "BULLISH",
                "category": "MULTI",
                "confidence": 0.7,
                "description": "两阳夹一阴形态，显示洗盘后继续上涨的强势信号"
            })
        
        # 4. 上升三法
        if (trend == "up" and 
            prev2_data['is_bullish'] and  # 第一根大阳线
            prev2_data['body_ratio'] > 0.6 and
            prev_data['is_bearish'] and  # 第二根小阴线
            prev_data['body_ratio'] < 0.4 and
            current_data['is_bullish'] and  # 第三根阳线
            current['close'] > prev2['close'] and  # 收盘创出新高
            prev['high'] < prev2['high'] and prev['low'] > prev2['low']):  # 小阴线在第一根范围内
            patterns.append({
                "name": "上升三法",
                "type": "BULLISH",
                "category": "MULTI",
                "confidence": 0.7,
                "description": "大阳线后跟随小阴线，再出现创新高的大阳线，上升中继形态"
            })
        
        # 5. 早晨之星
        if (trend == "down" and 
            prev2_data['is_bearish'] and  # 第一根阴线
            prev_data['body_ratio'] < 0.3 and  # 第二根小实体
            current_data['is_bullish'] and  # 第三根阳线
            current['close'] > (prev2['open'] + prev2['close']) / 2):  # 收盘超过第一根中点
            patterns.append({
                "name": "早晨之星",
                "type": "BULLISH",
                "category": "MULTI",
                "confidence": 0.8,
                "description": "三根K线组合，出现在下跌趋势底部，强烈看涨反转信号"
            })
        
        # 6. 黑三鸦 (三只乌鸦)
        if (trend == "up" and 
            current_data['is_bearish'] and prev_data['is_bearish'] and prev2_data['is_bearish'] and
            current['open'] < prev['open'] and prev['open'] < prev2['open'] and
            current['close'] < prev['close'] and prev['close'] < prev2['close'] and
            all(data['body_ratio'] > 0.4 for data in [current_data, prev_data, prev2_data])):
            patterns.append({
                "name": "黑三鸦",
                "type": "BEARISH",
                "category": "MULTI",
                "confidence": 0.8,
                "description": "连续三根实体逐渐增长的阴线，显示强劲的卖方力量"
            })
        
        # 7. 空方炮
        if (prev3 is not None and 
            self._analyze_candle_features(prev3)['is_bearish'] and  # 第一根阴线
            prev2_data['is_bullish'] and  # 第二根阳线
            prev_data['is_bearish'] and  # 第三根阴线
            current_data['is_bearish'] and  # 第四根阴线
            prev['close'] < prev2['open'] and  # 第三根收盘低于第二根开盘
            current['close'] < prev['close']):  # 第四根收盘低于第三根
            patterns.append({
                "name": "空方炮",
                "type": "BEARISH",
                "category": "MULTI",
                "confidence": 0.7,
                "description": "两阴夹一阳形态，显示反弹后继续下跌的弱势信号"
            })
        
        # 8. 下降三法
        if (trend == "down" and 
            prev2_data['is_bearish'] and  # 第一根大阴线
            prev2_data['body_ratio'] > 0.6 and
            prev_data['is_bullish'] and  # 第二根小阳线
            prev_data['body_ratio'] < 0.4 and
            current_data['is_bearish'] and  # 第三根阴线
            current['close'] < prev2['close'] and  # 收盘创出新低
            prev['high'] < prev2['high'] and prev['low'] > prev2['low']):  # 小阳线在第一根范围内
            patterns.append({
                "name": "下降三法",
                "type": "BEARISH",
                "category": "MULTI",
                "confidence": 0.7,
                "description": "大阴线后跟随小阳线，再出现创新低的大阴线，下降中继形态"
            })
        
        return patterns

    def detect_candlestick_patterns(self, df: pd.DataFrame) -> Dict[str, List[Dict]]:
        """检测所有K线形态 - 按类别分类"""
        if df is None or len(df) < 3:
            return {"SINGLE": [], "DOUBLE": [], "MULTI": []}
        
        # 计算趋势
        short_trend = self._calculate_trend(df, period=10)
        
        # 获取最近的K线
        current = df.iloc[-1]
        prev = df.iloc[-2] if len(df) >= 2 else None
        
        # 分别检测各类形态
        single_patterns = self.detect_single_candle_patterns(current, short_trend)
        double_patterns = self.detect_double_candle_patterns(current, prev, short_trend) if prev is not None else []
        multi_patterns = self.detect_multi_candle_patterns(df, short_trend)
        
        return {
            "SINGLE": single_patterns,
            "DOUBLE": double_patterns,
            "MULTI": multi_patterns
        }

    def calculate_technical_indicators(self, df: pd.DataFrame) -> Dict:
        """计算技术指标"""
        if df is None or len(df) < 20:
            return {}
            
        close_prices = df['close'].astype(np.float64).values
        high_prices = df['high'].astype(np.float64).values
        low_prices = df['low'].astype(np.float64).values
        
        indicators = {}
        
        try:
            # 简单移动平均线
            indicators['MA5'] = df['close'].tail(5).mean()
            indicators['MA10'] = df['close'].tail(10).mean()
            indicators['MA20'] = df['close'].tail(20).mean()
            
            # 简单RSI计算
            delta = df['close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            indicators['RSI'] = rsi.iloc[-1] if not pd.isna(rsi.iloc[-1]) else 50
            
            # 简单布林带
            rolling_mean = df['close'].rolling(window=20).mean()
            rolling_std = df['close'].rolling(window=20).std()
            indicators['BB_Upper'] = rolling_mean.iloc[-1] + (rolling_std.iloc[-1] * 2)
            indicators['BB_Middle'] = rolling_mean.iloc[-1]
            indicators['BB_Lower'] = rolling_mean.iloc[-1] - (rolling_std.iloc[-1] * 2)
            
            # 布林带位置
            current_price = df['close'].iloc[-1]
            bb_range = indicators['BB_Upper'] - indicators['BB_Lower']
            if bb_range > 0:
                indicators['BB_Position'] = (current_price - indicators['BB_Lower']) / bb_range
            
            # 简单MACD
            ema12 = df['close'].ewm(span=12).mean()
            ema26 = df['close'].ewm(span=26).mean()
            indicators['MACD'] = (ema12 - ema26).iloc[-1]
            indicators['MACD_Signal'] = (ema12 - ema26).ewm(span=9).mean().iloc[-1]
            
        except Exception as e:
            print(f"技术指标计算失败: {e}")
            
        return indicators

    async def analyze_stock(self, symbol: str, interval: str = "1d") -> Dict:
        """分析股票"""
        if interval not in self.supported_intervals:
            return {"error": f"不支持的K线周期: {interval}"}
            
        period = self.supported_intervals.get(interval)
        df = await self.get_stock_data(symbol, period, interval)
        
        if df is None or len(df) == 0:
            return {"error": f"无法获取 {symbol} 的数据，请检查股票代码是否正确"}
            
        candle_patterns = self.detect_candlestick_patterns(df)
        
        analysis = {
            "symbol": symbol,
            "interval": interval,
            "current_price": df['close'].iloc[-1],
            "price_change": df['close'].iloc[-1] - df['close'].iloc[-2] if len(df) >= 2 else 0,
            "price_change_pct": ((df['close'].iloc[-1] - df['close'].iloc[-2]) / df['close'].iloc[-2] * 100) if len(df) >= 2 else 0,
            "candle_patterns": candle_patterns,
            "technical_indicators": self.calculate_technical_indicators(df),
            "data_points": len(df),
            "analysis_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return analysis

    async def close(self):
        """关闭客户端"""
        if self.client:
            await self.client.aclose()
            self.client = None

# 创建全局实例
stock_analyzer = StockAnalyzer()

def _format_analysis(analysis: Dict) -> str:
    """格式化分析结果"""
    if "error" in analysis:
        return f"❌ 分析失败: {analysis['error']}"
    
    result = [
        f"📈 **{analysis['symbol']} 股票分析**",
        f"⏰ 时间周期: {analysis['interval']}",
        f"💰 当前价格: {analysis['current_price']:.2f}",
        f"📊 涨跌幅: {analysis['price_change']:+.2f} ({analysis['price_change_pct']:+.2f}%)",
        f"📊 数据点数: {analysis.get('data_points', 0)}",
        f"🕒 分析时间: {analysis['analysis_time']}",
        ""
    ]
    
    # K线形态分类显示
    candle_patterns = analysis.get('candle_patterns', {})
    
    total_patterns = sum(len(patterns) for patterns in candle_patterns.values())
    
    if total_patterns == 0:
        result.append("ℹ️ 未检测到明显的K线形态")
        result.append("")
    else:
        # 单K线形态
        single_patterns = candle_patterns.get('SINGLE', [])
        if single_patterns:
            result.append("🕯️ **单K线形态分析:**")
            for pattern in single_patterns:
                emoji = "🟢" if pattern['type'] == 'BULLISH' else "🔴" if pattern['type'] == 'BEARISH' else "🟡"
                result.append(f"  {emoji} {pattern['name']} (置信度: {pattern['confidence']:.1f})")
                result.append(f"     📝 {pattern['description']}")
            result.append("")
        
        # 双K线组合
        double_patterns = candle_patterns.get('DOUBLE', [])
        if double_patterns:
            result.append("🕯️ **双K线组合分析:**")
            for pattern in double_patterns:
                emoji = "🟢" if pattern['type'] == 'BULLISH' else "🔴" if pattern['type'] == 'BEARISH' else "🟡"
                result.append(f"  {emoji} {pattern['name']} (置信度: {pattern['confidence']:.1f})")
                result.append(f"     📝 {pattern['description']}")
            result.append("")
        
        # 多K线组合
        multi_patterns = candle_patterns.get('MULTI', [])
        if multi_patterns:
            result.append("🕯️ **多K线组合分析:**")
            for pattern in multi_patterns:
                emoji = "🟢" if pattern['type'] == 'BULLISH' else "🔴" if pattern['type'] == 'BEARISH' else "🟡"
                result.append(f"  {emoji} {pattern['name']} (置信度: {pattern['confidence']:.1f})")
                result.append(f"     📝 {pattern['description']}")
            result.append("")
    
    # 技术指标
    if analysis['technical_indicators']:
        result.append("📊 **技术指标分析:**")
        indicators = analysis['technical_indicators']
        
        # 移动平均线
        if all(k in indicators for k in ['MA5', 'MA10', 'MA20']):
            ma_signal = "看涨" if indicators['MA5'] > indicators['MA10'] > indicators['MA20'] else "看跌" if indicators['MA5'] < indicators['MA10'] < indicators['MA20'] else "震荡"
            result.append(f"  📈 移动平均线: {ma_signal} (5日: {indicators['MA5']:.2f}, 10日: {indicators['MA10']:.2f}, 20日: {indicators['MA20']:.2f})")
        
        # RSI
        if 'RSI' in indicators:
            rsi = indicators['RSI']
            if isinstance(rsi, (int, float)):
                if rsi > 70:
                    rsi_signal = "超买"
                elif rsi < 30:
                    rsi_signal = "超卖" 
                else:
                    rsi_signal = "正常"
                result.append(f"  🔄 RSI: {rsi:.1f} ({rsi_signal})")
        
        # MACD
        if all(k in indicators for k in ['MACD', 'MACD_Signal']):
            if indicators['MACD'] > indicators['MACD_Signal']:
                macd_signal = "金叉看涨"
            else:
                macd_signal = "死叉看跌"
            result.append(f"  📉 MACD: {macd_signal} (MACD: {indicators['MACD']:.4f}, 信号: {indicators['MACD_Signal']:.4f})")
        
        # 布林带
        if 'BB_Position' in indicators:
            bb_pos = indicators['BB_Position']
            if bb_pos > 0.8:
                bb_signal = "上轨附近，可能超买"
            elif bb_pos < 0.2:
                bb_signal = "下轨附近，可能超卖"
            else:
                bb_signal = "中轨附近"
            result.append(f"  📊 布林带: {bb_signal}")
    
    return "\n".join(result)

@mcp.tool()
async def analyze_stock_price(symbol: str, interval: str = "1d") -> str:
    """分析股票价格和K线形态
    
    Args:
        symbol: 股票代码 (如: AAPL, 0700.HK, 000001.SS, ^GSPC)
        interval: K线周期 (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 4h, 1d, 1wk, 1mo)
    """
    try:
        if interval not in stock_analyzer.supported_intervals:
            supported = ", ".join(stock_analyzer.supported_intervals.keys())
            return f"❌ 不支持的K线周期，请使用: {supported}"
            
        is_valid = await stock_analyzer.validate_symbol(symbol)
        if not is_valid:
            return f"❌ 股票代码 {symbol} 无效或无法获取数据，请检查代码格式"
            
        analysis = await stock_analyzer.analyze_stock(symbol, interval)
        return _format_analysis(analysis)
        
    except Exception as e:
        return f"❌ 分析股票失败: {str(e)}"

@mcp.tool()
async def search_stock_symbols(keyword: str) -> str:
    """搜索股票代码"""
    try:
        if not keyword or len(keyword.strip()) < 2:
            return "❌ 请输入至少2个字符进行搜索"
            
        symbols = await stock_analyzer.search_symbols(keyword.strip())
        
        if not symbols:
            if any('\u4e00' <= char <= '\u9fff' for char in keyword):
                return f"❌ 中文搜索 '{keyword}' 失败，请尝试使用英文或股票代码搜索"
            else:
                return f"❌ 未找到与 '{keyword}' 相关的股票"
            
        result = [f"🔍 **搜索 '{keyword}' 的结果:**", ""]
        
        for i, symbol_info in enumerate(symbols, 1):
            result.append(f"{i}. **{symbol_info['symbol']}** - {symbol_info['name']}")
            result.append(f"   交易所: {symbol_info.get('exchange', '未知')} | 类型: {symbol_info.get('type', '未知')}")
            result.append("")
            
        result.append("💡 **使用示例:**")
        result.append(f'analyze_stock_price(symbol="{symbols[0]["symbol"]}", interval="1d")')
        
        return "\n".join(result)
        
    except Exception as e:
        return f"❌ 搜索股票失败: {str(e)}"

@mcp.tool()
async def get_stock_examples() -> str:
    """获取股票代码示例"""
    result = ["📋 **股票代码示例:**", ""]
    
    for market, examples in stock_analyzer.market_examples.items():
        market_name = {
            "US": "🇺🇸 美股",
            "HK": "🇭🇰 港股", 
            "CN_SH": "🇨🇳 沪市",
            "CN_SZ": "🇨🇳 深市",
            "INDEX": "📊 指数"
        }.get(market, market)
        
        result.append(f"**{market_name}:**")
        for i in range(0, len(examples), 5):
            result.append("  " + ", ".join(examples[i:i+5]))
        result.append("")
    
    # 添加时间周期说明
    result.extend([
        "⏰ **支持的时间周期:**",
        "  - 分钟级: 1m, 2m, 5m, 15m, 30m, 60m, 90m",
        "  - 小时级: 1h, 4h",
        "  - 日级及以上: 1d, 1wk, 1mo",
        "",
        "💡 **使用说明:**",
        "1. 使用 search_stock_symbols('公司名') 搜索股票代码",
        "2. 使用 analyze_stock_price('代码', '周期') 分析股票",
        "",
        "**示例:**",
        'analyze_stock_price("AAPL", "15m")  # 苹果15分钟线',
        'analyze_stock_price("0700.HK", "30m")  # 腾讯30分钟线',
        'analyze_stock_price("^GSPC", "1h")  # 标普5001小时线'
    ])
    
    return "\n".join(result)

@mcp.tool()
async def get_supported_intervals() -> str:
    """获取支持的时间周期列表"""
    result = ["⏰ **支持的时间周期:**", ""]
    
    # 按类别分组显示
    categories = {
        "分钟级周期": ["1m", "2m", "5m", "15m", "30m", "60m", "90m"],
        "小时级周期": ["1h", "4h"],
        "日级及以上周期": ["1d", "1wk", "1mo"]
    }
    
    for category, intervals in categories.items():
        result.append(f"**{category}:**")
        result.append("  " + ", ".join(intervals))
        result.append("")
    
    result.extend([
        "💡 **周期选择建议:**",
        "  - 超短线交易: 1m, 5m, 15m",
        "  - 短线交易: 30m, 60m, 1h",
        "  - 中线交易: 4h, 1d",
        "  - 长线投资: 1wk, 1mo",
        "",
        "**示例:**",
        'analyze_stock_price("AAPL", "15m")  # 15分钟短线分析',
        'analyze_stock_price("TSLA", "1h")   # 1小时趋势分析',
        'analyze_stock_price("MSFT", "1d")   # 日线长期分析'
    ])
    
    return "\n".join(result)

@mcp.tool()
async def get_candlestick_patterns_info() -> str:
    """获取K线形态说明"""
    result = ["🕯️ **K线形态完全指南:**", ""]
    
    # 单K线形态说明
    result.append("## 📊 单K线形态")
    single_descriptions = {
        "光头光脚阳线": "没有上下影线，开盘价即最低价，收盘价即最高价，表示强烈的看涨信号",
        "光脚阳线": "没有下影线，表示买方力量强劲，但上方有压力",
        "光头阳线": "没有上影线，收盘价即最高价，表示买方完全控制局面",
        "带上下影线的阳线": "有上下影线，表示多空双方有争夺，但最终买方获胜",
        "光头光脚阴线": "没有上下影线，开盘价即最高价，收盘价即最低价，表示强烈的看跌信号",
        "光脚阴线": "没有下影线，表示卖方力量强劲，开盘后价格一路下跌",
        "光头阴线": "没有上影线，开盘价即最高价，表示卖方完全控制局面",
        "带上下影线的阴线": "有上下影线，表示多空双方有争夺，但最终卖方获胜",
        "十字线": "开盘收盘价接近，表示市场犹豫不决，可能预示反转",
        "T字线": "卖方打压后买方收复失地，出现在底部时看涨信号更强",
        "倒T字线": "买方推高后卖方打压回落，出现在顶部时看跌信号更强",
        "一字线": "开盘即涨停或跌停，表示极强的买盘或卖盘力量",
        "锤头线": "出现在下跌趋势中，长下影线表示买方力量开始增强",
        "上吊线": "出现在上涨趋势中，长下影线表示卖方力量开始增强",
        "倒锤头线": "出现在下跌趋势中，长上影线表示买方尝试反攻",
        "射击之星": "出现在上涨趋势中，长上影线表示上方压力巨大"
    }
    
    for pattern, desc in single_descriptions.items():
        emoji = "🟢" if "阳" in pattern or "涨" in desc else "🔴" if "阴" in pattern or "跌" in desc else "🟡"
        result.append(f"{emoji} **{pattern}**: {desc}")
    
    result.append("\n## 📊 双K线组合")
    double_descriptions = {
        "乌云盖顶组合": "第二根阴线开盘高于前一根高点，收盘低于前一根中点，预示上涨趋势可能结束",
        "旭日东升组合": "第二根阳线开盘低于前一根低点，收盘高于前一根中点，预示下跌趋势可能结束",
        "抱线组合": "阳线或阴线完全吞没前一根K线，强烈反转信号",
        "孕线组合": "小实体在大实体内，出现在趋势中可能反转",
        "插入线组合": "阳线插入到前一根阴线实体内部，显示买方力量增强",
        "跳空组合": "K线之间出现跳空缺口，显示强劲的买卖力量",
        "双飞乌鸦组合": "连续两根阴线，第二根开盘高于第一根但收盘更低，预示上涨乏力"
    }
    
    for pattern, desc in double_descriptions.items():
        emoji = "🟢" if "旭日" in pattern or "阳" in desc else "🔴" if "乌云" in pattern or "阴" in desc or "乌鸦" in pattern else "🟡"
        result.append(f"{emoji} **{pattern}**: {desc}")
    
    result.append("\n## 📊 多K线组合")
    multi_descriptions = {
        "黄昏之星": "三根K线组合，出现在上涨趋势顶部，强烈看跌反转信号",
        "红三兵": "连续三根实体逐渐增长的阳线，显示强劲的买方力量",
        "多方炮": "两阳夹一阴形态，显示洗盘后继续上涨的强势信号",
        "上升三法": "大阳线后跟随小阴线，再出现创新高的大阳线，上升中继形态",
        "早晨之星": "三根K线组合，出现在下跌趋势底部，强烈看涨反转信号",
        "黑三鸦": "连续三根实体逐渐增长的阴线，显示强劲的卖方力量",
        "空方炮": "两阴夹一阳形态，显示反弹后继续下跌的弱势信号",
        "下降三法": "大阴线后跟随小阳线，再出现创新低的大阴线，下降中继形态"
    }
    
    for pattern, desc in multi_descriptions.items():
        emoji = "🟢" if "红" in pattern or "多方" in pattern or "早晨" in pattern or "上升" in pattern else "🔴" if "黑" in pattern or "空方" in pattern or "黄昏" in pattern or "下降" in pattern else "🟡"
        result.append(f"{emoji} **{pattern}**: {desc}")
    
    return "\n".join(result)

if __name__ == "__main__":
    mcp.run(transport="stdio")
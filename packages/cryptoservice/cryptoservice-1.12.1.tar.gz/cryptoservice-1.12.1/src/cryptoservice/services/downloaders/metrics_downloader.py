"""市场指标数据下载器.

专门处理资金费率、持仓量(当日)、多空比例（当日）等市场指标数据的下载。
"""

import asyncio
import logging
from datetime import datetime

from binance import AsyncClient

from cryptoservice.exceptions import MarketDataFetchError
from cryptoservice.models import Freq, FundingRate, LongShortRatio, OpenInterest
from cryptoservice.storage.database import Database as AsyncMarketDB

from .base_downloader import BaseDownloader

logger = logging.getLogger(__name__)


class MetricsDownloader(BaseDownloader):
    """市场指标数据下载器."""

    def __init__(self, client: AsyncClient, request_delay: float = 0.5):
        """初始化市场指标数据下载器.

        Args:
            client: API 客户端实例.
            request_delay: 请求之间的基础延迟（秒）.
        """
        super().__init__(client, request_delay)
        self.db: AsyncMarketDB | None = None

    async def download_funding_rate_batch(
        self,
        symbols: list[str],
        start_time: str,
        end_time: str,
        db_path: str,
        request_delay: float = 0.5,
        max_workers: int = 5,
    ) -> None:
        """批量异步下载资金费率数据."""
        try:
            logger.info("💰 批量下载资金费率数据")

            if self.db is None:
                self.db = AsyncMarketDB(db_path)
            await self.db.initialize()

            all_funding_rates = []
            semaphore = asyncio.Semaphore(max_workers)

            async def process_symbol(symbol: str):
                async with semaphore:
                    try:
                        logger.debug(f"获取 {symbol} 资金费率")
                        funding_rates = await self.download_funding_rate(
                            symbol=symbol,
                            start_time=start_time,
                            end_time=end_time,
                            limit=1000,
                        )
                        if funding_rates:
                            all_funding_rates.extend(funding_rates)
                            logger.debug(f"✅ {symbol}: {len(funding_rates)} 条记录")
                    except Exception as e:
                        logger.warning(f"❌ {symbol}: {e}")
                        self._record_failed_download(
                            symbol,
                            str(e),
                            {"data_type": "funding_rate", "start_time": start_time, "end_time": end_time},
                        )

            tasks = [process_symbol(symbol) for symbol in symbols]
            await asyncio.gather(*tasks)

            # 批量存储
            if all_funding_rates and self.db:
                await self.db.insert_funding_rates(all_funding_rates)
                logger.info(f"✅ 存储了 {len(all_funding_rates)} 条资金费率记录")

            logger.info(f"💰 资金费率数据下载完成: {len(all_funding_rates)} 条记录")

        except Exception as e:
            logger.error(f"批量下载资金费率失败: {e}")
            raise MarketDataFetchError(f"批量下载资金费率失败: {e}") from e

    async def download_open_interest_batch(
        self,
        symbols: list[str],
        start_time: str,
        end_time: str,
        db_path: str,
        interval: Freq = Freq.m5,
        request_delay: float = 0.5,
        max_workers: int = 5,
    ) -> None:
        """批量异步下载持仓量数据."""
        try:
            logger.info("📊 批量下载持仓量数据")

            if self.db is None:
                self.db = AsyncMarketDB(db_path)
            await self.db.initialize()

            all_open_interests = []
            semaphore = asyncio.Semaphore(max_workers)

            async def process_symbol(symbol: str):
                async with semaphore:
                    try:
                        logger.debug(f"获取 {symbol} 持仓量")
                        open_interests = await self.download_open_interest(
                            symbol=symbol,
                            period=interval.value,
                            start_time=start_time,
                            end_time=end_time,
                            limit=500,
                        )
                        if open_interests:
                            all_open_interests.extend(open_interests)
                            logger.debug(f"✅ {symbol}: {len(open_interests)} 条记录")
                    except Exception as e:
                        logger.warning(f"❌ {symbol}: {e}")
                        self._record_failed_download(
                            symbol,
                            str(e),
                            {"data_type": "open_interest", "start_time": start_time, "end_time": end_time},
                        )

            tasks = [process_symbol(symbol) for symbol in symbols]
            await asyncio.gather(*tasks)

            # 批量存储
            if all_open_interests and self.db:
                await self.db.insert_open_interests(all_open_interests)
                logger.info(f"✅ 存储了 {len(all_open_interests)} 条持仓量记录")

            logger.info(f"📊 持仓量数据下载完成: {len(all_open_interests)} 条记录")

        except Exception as e:
            logger.error(f"批量下载持仓量失败: {e}")
            raise MarketDataFetchError(f"批量下载持仓量失败: {e}") from e

    async def download_long_short_ratio_batch(
        self,
        symbols: list[str],
        start_time: str,
        end_time: str,
        db_path: str,
        period: str = "5m",
        ratio_type: str = "account",
        request_delay: float = 0.5,
        max_workers: int = 5,
    ) -> None:
        """批量异步下载多空比例数据."""
        try:
            logger.info(f"📊 批量下载多空比例数据 (类型: {ratio_type})")

            if self.db is None:
                self.db = AsyncMarketDB(db_path)
            await self.db.initialize()

            all_long_short_ratios = []
            semaphore = asyncio.Semaphore(max_workers)

            async def process_symbol(symbol: str):
                async with semaphore:
                    try:
                        logger.debug(f"获取 {symbol} 多空比例")
                        long_short_ratios = await self.download_long_short_ratio(
                            symbol=symbol,
                            period=period,
                            ratio_type=ratio_type,
                            start_time=start_time,
                            end_time=end_time,
                            limit=500,
                        )
                        if long_short_ratios:
                            all_long_short_ratios.extend(long_short_ratios)
                            logger.debug(f"✅ {symbol}: {len(long_short_ratios)} 条记录")
                    except Exception as e:
                        logger.warning(f"❌ {symbol}: {e}")
                        self._record_failed_download(
                            symbol,
                            str(e),
                            {
                                "data_type": "long_short_ratio",
                                "ratio_type": ratio_type,
                                "start_time": start_time,
                                "end_time": end_time,
                            },
                        )

            tasks = [process_symbol(symbol) for symbol in symbols]
            await asyncio.gather(*tasks)

            # 批量存储
            if all_long_short_ratios and self.db:
                await self.db.insert_long_short_ratios(all_long_short_ratios)
                logger.info(f"✅ 存储了 {len(all_long_short_ratios)} 条多空比例记录")

            logger.info(f"📊 多空比例数据下载完成: {len(all_long_short_ratios)} 条记录")

        except Exception as e:
            logger.error(f"批量下载多空比例失败: {e}")
            raise MarketDataFetchError(f"批量下载多空比例失败: {e}") from e

    async def download_funding_rate(
        self,
        symbol: str,
        start_time: str | None = None,
        end_time: str | None = None,
        limit: int = 100,
    ) -> list[FundingRate]:
        """异步下载单个交易对的资金费率数据."""
        try:

            async def request_func():
                params = {"symbol": symbol, "limit": limit}
                if start_time:
                    params["startTime"] = self._date_to_timestamp_start(start_time)
                if end_time:
                    params["endTime"] = self._date_to_timestamp_end(end_time)
                return await self.client.futures_funding_rate(**params)

            data = await self._handle_async_request_with_retry(request_func)

            if not data:
                return []

            return [FundingRate.from_binance_response(item) for item in data]

        except Exception as e:
            logger.error(f"获取资金费率失败 {symbol}: {e}")
            raise MarketDataFetchError(f"获取资金费率失败: {e}") from e

    async def download_open_interest(
        self,
        symbol: str,
        period: str = "5m",
        start_time: str | None = None,
        end_time: str | None = None,
        limit: int = 500,
    ) -> list[OpenInterest]:
        """异步下载单个交易对的持仓量数据."""
        try:

            async def request_func():
                params = {"symbol": symbol, "period": period, "limit": min(limit, 500)}
                if start_time:
                    params["startTime"] = self._date_to_timestamp_start(start_time)
                if end_time:
                    params["endTime"] = self._date_to_timestamp_end(end_time)
                return await self.client.futures_open_interest_hist(**params)

            data = await self._handle_async_request_with_retry(request_func)

            if not data:
                return []

            return [OpenInterest.from_binance_response(item) for item in data]

        except Exception as e:
            logger.error(f"获取持仓量失败 {symbol}: {e}")
            raise MarketDataFetchError(f"获取持仓量失败: {e}") from e

    async def download_long_short_ratio(
        self,
        symbol: str,
        period: str = "5m",
        ratio_type: str = "account",
        start_time: str | None = None,
        end_time: str | None = None,
        limit: int = 500,
    ) -> list[LongShortRatio]:
        """异步下载单个交易对的多空比例数据."""
        try:

            async def request_func():
                params = {"symbol": symbol, "period": period, "limit": min(limit, 500)}
                if start_time:
                    params["startTime"] = self._date_to_timestamp_start(start_time)
                if end_time:
                    params["endTime"] = self._date_to_timestamp_end(end_time)

                # 根据ratio_type选择API端点
                if ratio_type == "account":
                    return await self.client.futures_top_longshort_account_ratio(**params)
                elif ratio_type == "position":
                    return await self.client.futures_top_longshort_position_ratio(**params)
                elif ratio_type == "global":
                    return await self.client.futures_global_longshort_ratio(**params)
                elif ratio_type == "taker":
                    return await self.client.futures_taker_longshort_ratio(**params)
                else:
                    raise ValueError(f"不支持的ratio_type: {ratio_type}")

            data = await self._handle_async_request_with_retry(request_func)

            if not data:
                return []

            return [LongShortRatio.from_binance_response(item, ratio_type) for item in data]

        except Exception as e:
            logger.error(f"获取多空比例失败 {symbol}: {e}")
            raise MarketDataFetchError(f"获取多空比例失败: {e}") from e

    def _date_to_timestamp_start(self, date: str) -> str:
        """将日期字符串转换为当天开始的时间戳."""
        timestamp = int(datetime.strptime(f"{date} 00:00:00", "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
        return str(timestamp)

    def _date_to_timestamp_end(self, date: str) -> str:
        """将日期字符串转换为当天结束的时间戳."""
        timestamp = int(datetime.strptime(f"{date} 23:59:59", "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
        return str(timestamp)

    def download(self, *args, **kwargs):
        """实现基类的抽象方法."""
        # 这里可以根据参数决定调用哪个具体的下载方法
        if "funding_rate" in kwargs:
            return self.download_funding_rate_batch(*args, **kwargs)
        elif "open_interest" in kwargs:
            return self.download_open_interest_batch(*args, **kwargs)
        elif "long_short_ratio" in kwargs:
            return self.download_long_short_ratio_batch(*args, **kwargs)
        else:
            raise ValueError("请指定要下载的数据类型")

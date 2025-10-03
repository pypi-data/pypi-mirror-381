# Copyright (c) vnquant. All rights reserved.
import pandas as pd
import requests
from datetime import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import sys
# sys.path.insert(0,'/Users/phamdinhkhanh/Documents/vnquant')
from vnquant import configs
from vnquant.data.loader.proto import DataLoadProto
from vnquant.log import logger
from vnquant.utils import utils

URL_VND = configs.URL_VND
API_VNDIRECT = configs.API_VNDIRECT
URL_CAFE = configs.URL_CAFE
HEADERS = configs.HEADERS
REGEX_PATTERN_PRICE_CHANGE_CAFE = configs.REGEX_PATTERN_PRICE_CHANGE_CAFE
STOCK_COLUMNS_CAFEF = configs.STOCK_COLUMNS_CAFEF
STOCK_COLUMNS_CAFEF_FINAL = configs.STOCK_COLUMNS_CAFEF_FINAL

class DataLoaderCAFE(DataLoadProto):
    def __init__(self, symbols, start, end, include_adjusted=False, *arg, **karg):
        self.symbols = symbols
        self.start = start
        self.end = end
        self.include_adjusted = include_adjusted
        super(DataLoaderCAFE, self).__init__(symbols, start, end)

    def download(self):
        stock_datas = []
        symbols = self.pre_process_symbols()
        logger.info('Start downloading data symbols {} from CAFEF, start: {}, end: {}!'.format(symbols, self.start, self.end))

        for symbol in symbols:
            stock_datas.append(self.download_one(symbol))

        data = pd.concat(stock_datas, axis=1)
        data = data.sort_index(ascending=False)
        return data

    def download_one(self, symbol):
        start_date = utils.convert_text_dateformat(self.start, origin_type = '%d/%m/%Y', new_type = '%Y-%m-%d')
        end_date = utils.convert_text_dateformat(self.end, origin_type = '%d/%m/%Y', new_type = '%Y-%m-%d')
        delta = datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')
        params = {
            "Symbol": symbol, # symbol of stock
            "StartDate": start_date, # start date
            "EndDate": end_date, # end date
            "PageIndex": 1, # page number
            "PageSize":delta.days + 1 # the size of page
        }
        # Note: We set the size of page equal to the number of days from start_date and end_date
        # and page equal to 1, so that we can get a full data in the time interval from start_date and end_date
        res = requests.get(URL_CAFE, params=params)
        data = res.json()['Data']['Data']
        if not data:
            logger.error(f"Data of the symbol {symbol} is not available")
            return None
        data = pd.DataFrame(data)
        data[['code']] = symbol
        stock_data = data[['code', 'Ngay',
                           'GiaDongCua', 'GiaMoCua', 'GiaCaoNhat', 'GiaThapNhat', 'GiaDieuChinh', 'ThayDoi',
                           'KhoiLuongKhopLenh', 'GiaTriKhopLenh', 'KLThoaThuan', 'GtThoaThuan']].copy()

        stock_data.columns = STOCK_COLUMNS_CAFEF

        stock_change = stock_data['change_str'].str.extract(REGEX_PATTERN_PRICE_CHANGE_CAFE, expand=True)
        stock_change.columns = ['change', 'percent_change']
        stock_data = pd.concat([stock_data, stock_change], axis=1)
        stock_data = stock_data[STOCK_COLUMNS_CAFEF_FINAL]

        list_numeric_columns = [
            'close', 'open', 'high', 'low', 'adjust_price',
            'change', 'percent_change',
            'volume_match', 'value_match', 'volume_reconcile', 'value_reconcile'
        ]
        
        stock_data = stock_data.set_index('date')
        stock_data[list_numeric_columns] = stock_data[list_numeric_columns].astype(float)
        stock_data.index = list(map(lambda x: datetime.strptime(x, '%d/%m/%Y'), stock_data.index))
        stock_data.index.name = 'date'
        
        # Filter data to requested date range (CAFE API sometimes returns extra current day data)
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')
        
        # Count records before filtering
        original_count = len(stock_data)
        
        # Filter to requested date range
        date_mask = (stock_data.index >= start_dt) & (stock_data.index <= end_dt)
        stock_data = stock_data[date_mask]
        
        # Log filtering results
        filtered_count = len(stock_data)
        if filtered_count != original_count:
            logger.info(f'Symbol {symbol}: Filtered {original_count - filtered_count} records outside date range {start_date} to {end_date}')
            logger.info(f'Symbol {symbol}: Kept {filtered_count} records within requested date range')
        
        stock_data = stock_data.sort_index(ascending=False)
        stock_data.fillna(method='ffill', inplace=True)
        stock_data['total_volume'] = stock_data.volume_match + stock_data.volume_reconcile
        stock_data['total_value'] = stock_data.value_match + stock_data.value_reconcile

        # Calculate adjusted prices if requested
        if self.include_adjusted:
            try:
                # Handle division by zero and validate data quality
                close_safe = stock_data['close'].copy()
                adjust_safe = stock_data['adjust_price'].copy()
                
                # Identify problematic rows
                zero_close_mask = (close_safe == 0.0) | (close_safe.isna())
                zero_adjust_mask = (adjust_safe == 0.0) | (adjust_safe.isna())
                
                if zero_close_mask.any():
                    problem_dates = stock_data[zero_close_mask].index.tolist()
                    logger.warning(f'Symbol {symbol}: Found {zero_close_mask.sum()} rows with zero/null close prices on dates: {problem_dates}')
                    
                    # For rows where close=0 but adjust_price exists, use adjust_price as close
                    # This handles cases where current day data is incomplete
                    close_safe = close_safe.mask(zero_close_mask & ~zero_adjust_mask, adjust_safe)
                    
                    # For rows where both are zero/null, replace close with 1 to avoid division by zero
                    close_safe = close_safe.replace(0.0, 1.0).fillna(1.0)
                
                # Calculate adjustment factor with enhanced validation
                adjustment_factor = adjust_safe / close_safe
                
                # Validate adjustment factors - flag unreasonable values
                unreasonable_mask = (adjustment_factor > 10.0) | (adjustment_factor < 0.1)
                if unreasonable_mask.any():
                    problem_dates = stock_data[unreasonable_mask].index.tolist()
                    problem_factors = adjustment_factor[unreasonable_mask].tolist()
                    logger.warning(f'Symbol {symbol}: Found {unreasonable_mask.sum()} rows with unreasonable adjustment factors on dates {problem_dates}: {problem_factors}')
                    
                    # For unreasonable factors, use 1.0 (no adjustment) as fallback
                    adjustment_factor = adjustment_factor.mask(unreasonable_mask, 1.0)
                    logger.info(f'Symbol {symbol}: Reset unreasonable adjustment factors to 1.0 (no adjustment)')
                
                # Calculate adjusted OHLC prices
                stock_data['adjusted_open'] = (stock_data['open'] * adjustment_factor).round(2)
                stock_data['adjusted_high'] = (stock_data['high'] * adjustment_factor).round(2)
                stock_data['adjusted_low'] = (stock_data['low'] * adjustment_factor).round(2)
                stock_data['adjusted_close'] = adjust_safe.round(2)
                stock_data['adjustment_factor'] = adjustment_factor.round(6)
                
                logger.info(f'Successfully calculated adjusted OHLC prices for symbol {symbol}')
                
            except Exception as e:
                logger.warning(f'Failed to calculate adjusted prices for {symbol}: {e}. Proceeding without adjusted data.')

        # Create multiple columns
        iterables = [stock_data.columns.tolist(), [symbol]]
        mulindex = pd.MultiIndex.from_product(iterables, names=['Attributes', 'Symbols'])
        stock_data.columns = mulindex

        logger.info('data {} from {} to {} have already cloned!' \
                     .format(symbol,
                             utils.convert_text_dateformat(self.start, origin_type = '%d/%m/%Y', new_type = '%Y-%m-%d'),
                             utils.convert_text_dateformat(self.end, origin_type='%d/%m/%Y', new_type='%Y-%m-%d')))
        return stock_data
    
# if __name__ == "__main__":  
#     loader2 = DataLoaderCAFE(symbols=["VND"], start="2017-01-10", end="2019-02-15")
#     print(loader2.download())

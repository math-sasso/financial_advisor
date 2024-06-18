from pydantic import BaseModel
from typing import List, Optional, Type
from enum import Enum


from pydantic import BaseModel
# from datetime import datetime

# class DateStr(BaseModel):
#     regex = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{2})$'
    
#     @classmethod
#     def validate(cls, value):
#         value = super().validate(value)
#         try:
#             datetime.strptime(value, '%m/%d/%y')
#         except ValueError:
#             raise ValueError('Date must be in the format MM/DD/YY')
#         return value
    
    

class AnalystRating(str, Enum):
    HOLD = 'Hold'
    BUY = 'Buy'
    SELL = 'Sell'

class RiskLevel(str, Enum):
    LOW=  'Low'
    MEDIUM=  'Medium'
    HIGH=  'High'

    
class ClientTargetAllocation(BaseModel):
    client: str
    symbol: str
    name: str
    sector: str # TODO: create an enum here with valid options
    quantity: int
    buy_price: float
    current_price: float
    market_value: float
    purchase_date: str
    dividend_yield: float
    pe_ratio: float
    week_52_high: float
    week_52_low: float
    analist_rating: AnalystRating
    target_price: float
    risk_level: RiskLevel
from pydantic import BaseModel,field_validator
from typing import List, Optional, Type

# Define Pydantic models
class FinancialAdvisorClient(BaseModel):
    client: Optional[str]
    target_portfolio: str
    asset_class: str
    target_allocation: float

    @field_validator('target_allocation')
    def target_allocation_must_be_percentage(cls, v):
        if not 0 <= v <= 100:
            raise ValueError('target_allocation must be between 0 and 100')
        return v
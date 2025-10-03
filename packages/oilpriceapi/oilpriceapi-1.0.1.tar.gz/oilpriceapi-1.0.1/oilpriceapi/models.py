"""
OilPriceAPI Data Models

Pydantic models for API responses.
"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict, field_validator


class Price(BaseModel):
    """Single price data point."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    commodity: str = Field(description="Commodity code (e.g., BRENT_CRUDE_USD)")
    value: float = Field(description="Current price value")
    currency: str = Field(description="Currency code")
    unit: str = Field(description="Unit of measurement")
    timestamp: datetime = Field(description="Price timestamp")
    change: Optional[float] = Field(default=None, description="Price change amount")
    change_percent: Optional[float] = Field(default=None, alias="change_percentage", description="Percentage change")
    previous_close: Optional[float] = Field(default=None, description="Previous closing price")
    open: Optional[float] = Field(default=None, description="Opening price")
    high: Optional[float] = Field(default=None, description="Daily high")
    low: Optional[float] = Field(default=None, description="Daily low")
    volume: Optional[int] = Field(default=None, description="Trading volume")
    
    @field_validator('timestamp', mode='before')
    @classmethod
    def parse_timestamp(cls, v):
        """Parse timestamp from various formats."""
        if isinstance(v, str):
            try:
                return datetime.fromisoformat(v.replace('Z', '+00:00'))
            except ValueError:
                # Try other common formats
                from dateutil import parser
                return parser.parse(v)
        return v
    
    @property
    def is_up(self) -> bool:
        """Check if price is up."""
        return self.change is not None and self.change > 0
    
    @property
    def is_down(self) -> bool:
        """Check if price is down."""
        return self.change is not None and self.change < 0
    
    def __str__(self) -> str:
        """String representation."""
        change_str = ""
        if self.change_percent is not None:
            arrow = "↑" if self.is_up else "↓" if self.is_down else "→"
            change_str = f" {arrow} {abs(self.change_percent):.2f}%"
        return f"{self.commodity}: {self.currency}{self.value:.2f}{change_str}"


class PriceResponse(BaseModel):
    """Response from current price endpoint."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    success: bool = Field(default=True)
    data: Price
    timestamp: datetime = Field(description="Response timestamp")
    

class MultiplePricesResponse(BaseModel):
    """Response with multiple prices."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    success: bool = Field(default=True)
    data: List[Price]
    timestamp: datetime
    count: int = Field(description="Number of prices returned")


class HistoricalPrice(BaseModel):
    """Historical price data point."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    date: datetime = Field(alias="created_at")
    commodity: str = Field(alias="commodity_name")
    value: float = Field(alias="price")
    currency: str = Field(default="USD")
    unit: str = Field(alias="unit_of_measure")
    type_name: Optional[str] = Field(default="spot_price")
    
    @field_validator('date', mode='before')
    @classmethod
    def parse_date(cls, v):
        """Parse date from various formats."""
        if isinstance(v, str):
            try:
                return datetime.fromisoformat(v.replace('Z', '+00:00'))
            except ValueError:
                from dateutil import parser
                return parser.parse(v)
        return v


class HistoricalResponse(BaseModel):
    """Response from historical data endpoint."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    success: bool = Field(default=True)
    data: List[HistoricalPrice]
    meta: Optional['PaginationMeta'] = None
    

class PaginationMeta(BaseModel):
    """Pagination metadata."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    page: int = Field(description="Current page number")
    per_page: int = Field(description="Items per page")
    total: int = Field(description="Total number of items")
    total_pages: int = Field(description="Total number of pages")
    has_next: bool = Field(description="Has next page")
    has_prev: bool = Field(description="Has previous page")
    

# Update forward reference
HistoricalResponse.model_rebuild()


class Commodity(BaseModel):
    """Commodity information."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    code: str = Field(description="Commodity code")
    name: str = Field(description="Commodity name")
    category: str = Field(description="Category (oil, gas, refined)")
    unit: str = Field(description="Unit of measurement")
    currency: str = Field(description="Default currency")
    description: Optional[str] = Field(default=None)
    

class CommodityListResponse(BaseModel):
    """Response with available commodities."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    success: bool = Field(default=True)
    data: List[Commodity]
    count: int


class ApiStatus(BaseModel):
    """API status information."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    status: str = Field(description="API status (operational, degraded, down)")
    version: str = Field(description="API version")
    timestamp: datetime
    uptime: Optional[float] = Field(default=None, description="Uptime percentage")
    response_time: Optional[float] = Field(default=None, description="Average response time (ms)")


class UsageStats(BaseModel):
    """API usage statistics."""
    
    model_config = ConfigDict(populate_by_name=True)
    
    requests_today: int = Field(description="Requests made today")
    requests_this_month: int = Field(description="Requests this month")
    limit_daily: Optional[int] = Field(default=None, description="Daily request limit")
    limit_monthly: int = Field(description="Monthly request limit")
    remaining_today: Optional[int] = Field(default=None)
    remaining_this_month: int
    reset_at: datetime = Field(description="When limits reset")
    plan: str = Field(description="Current plan name")

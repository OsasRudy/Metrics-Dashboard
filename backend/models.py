from typing import List
from pydantic import BaseModel


class Metrics(BaseModel):
    total_orders: int
    total_monthly_orders: int
    total_orders_in_progress: int
    revenue: str
    recent_orders: List

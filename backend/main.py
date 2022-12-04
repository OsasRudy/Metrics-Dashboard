import airtable
from typing import List
from models import Metrics

from fastapi import FastAPI

app = FastAPI()

db: List[Metrics] = [
    Metrics(
        total_orders=airtable.total_orders,
        total_monthly_orders=airtable.total_monthly_orders,
        total_orders_in_progress=airtable.orders_in_progress,
        revenue=airtable.orders_revenue,
        recent_orders=airtable.display_recent_orders
    )
]


@app.get("/api")
def read_root():
    return db


@app.get("/dashboard")
async def get_total_orders():
    return db

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

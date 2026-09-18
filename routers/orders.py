from fastapi import APIRouter
from schemas.models import Order, OrderResponse


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("", response_model=OrderResponse)
def order_process(order: Order):
    return order


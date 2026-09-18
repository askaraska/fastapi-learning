from fastapi import APIRouter
from schemas.models import Product, ProductResponse

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/search")
def search_product(category: str):
    return {
        "category": category,
        "message": "Searching products"
    }    


@router.get("/filter")
def filter_products(category: str, price: int):
    return {
        "category": category,
        "price": price
    }

@router.get("/{product_id}")
def get_productid(product_id: int):
    return {

        "product_id": product_id,
        "message": "Product found"
    }


@router.post("", response_model=ProductResponse)
def create_product(product: Product):
    # return{
    #     "message": "Product created successfully",
    #     "product": product
    # }
    return product
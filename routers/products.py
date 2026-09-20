from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.product import Product as ProductDB
from schemas.models import Product, ProductResponse

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/db-test")
def database_test(db: Session = Depends(get_db)):
    return{
        "message": "Database connection is working"
    }

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

# @router.get("/{product_id}")
# def get_productid(product_id: int):
#     return {

#         "product_id": product_id,
#         "message": "Product found"
#     }


# @router.post("", response_model=ProductResponse)
# def create_product(product: Product):
#     # return{
#     #     "message": "Product created successfully",
#     #     "product": product
#     # }
#     return product

@router.post("", response_model=ProductResponse)
def create_product(product: Product, db: Session = Depends(get_db)):

    db_product = ProductDB(
        name=product.name,
        price=product.price,
        category=product.category,
        description=product.description
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

@router.get("", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    products = db.query(ProductDB).all()

    return products

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):

    product = db.query(ProductDB).filter(
        ProductDB.id == product_id
    ).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product: Product,
    db: Session = Depends(get_db)
):
    db_product = db.query(ProductDB).filter(
        ProductDB.id == product_id
    ).first()    

    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db_product.name = product.name
    db_product.price = product.price
    db_product.category = product.category
    db_product.description = product.description

    db.commit()
    db.refresh(db_product)

    return db_product


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(ProductDB).filter(ProductDB.id == product_id).first()

    if not db_product:
        raise HTTPException(
            status_code=404, 
            detail="Product not found"
        )

    db.delete(db_product)
    db.commit()

    return{
        "message": "Product deleted successfully"
    }
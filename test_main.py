import pytest
from fastapi.testclient import TestClient

from main import app
from database import get_db
from test_database import override_get_db, TestSessionLocal
from models.product import Product as ProductDB

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture
def test_product():
    db = TestSessionLocal()

    product = ProductDB(
        name="Fixture Laptop",
        price=50000,
        category="Electronics",
        description="Fixture product"
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    product_id = product.id

    db.close()

    return product_id

def test_home():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Welcome to my FastAPI learning journey",
        "name": "Sulthan"
    }


def test_about():
    response = client.get("/about")

    assert response.status_code == 200

    assert response.json() == {
        "name": "Sulthan",
        "role": "Python Developer"
    }

def test_search():
    #GET /search?name=Sulthan
    response = client.get("/search?name=Sulthan")

    assert response.status_code == 200

    assert response.json() == {
        "search_name": "Sulthan"
    }


def test_search_without_name():
    response = client.get("/search")

    assert response.status_code == 200

    assert response.json() == {
        "search_name": None
    }


def test_get_user():
    response = client.get("/users/101")

    assert response.status_code == 200

    assert response.json() == {
        "user_id": 101
    }


def test_get_user_invalid_id():
    response = client.get("/users/abc")

    assert response.status_code == 422

def test_create_product():
    product_data = {
        "name": "Test Laptop",
        "price": 50000,
        "category": "Electronics",
        "description": "Test product"
    }

    response = client.post("/products", json=product_data)

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Test Laptop"
    assert data["price"] == 50000
    assert data["category"] == "Electronics"
    assert data["description"] == "Test product"

def test_create_product_invalid_price():
    product_data = {
        "name": "Invalid Product",
        "price": 0,
        "category": "Test",
        "description": "Invalid price"
    }

    response = client.post(
        "/products",
        json=product_data
    )

    assert response.status_code == 422    

def test_create_product_negative_price():
    product_data = {
        "name": "Invalid Laptop",
        "price": -100,
        "category": "Electronics",
        "description": "Negative price"
    }

    response = client.post("/products", json=product_data)

    assert response.status_code == 422


def test_create_product_missing_name():
    product_data = {
        "price": 50000,
        "category": "Electronics",
        "description": "Missing name"
    }

    response = client.post(
        "/products",
        json=product_data
    )

    assert response.status_code == 422

def test_create_product_missing_category():
    product_data = {
        "name": "Test Laptop",
        "price": 50000
    }

    response = client.post(
        "/products",
        json=product_data
    )

    assert response.status_code == 422

def test_create_product_invalid_price_type():
    product_data = {
        "name": "Test Laptop",
        "price": "very expensive",
        "category": "Electronics"
    }

    response = client.post(
        "/products",
        json=product_data
    )

    assert response.status_code == 422    

def test_get_products():
    response = client.get("/products")

    assert response.status_code == 200

    assert isinstance(response.json(), list)

def test_get_product(test_product):
    response = client.get(f"/products/{test_product}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == test_product

def test_get_product_not_found():
    response = client.get("/products/999999")

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Product not found"
    }    

def test_update_product(test_product):
    product_data = {
        "name": "Updated Laptop",
        "price": 60000,
        "category": "Electronics",
        "description": "Updated test product"
    }

    response = client.put(
        f"/products/{test_product}",
        json=product_data
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == test_product
    assert data["name"] == "Updated Laptop"
    assert data["price"] == 60000
    assert data["category"] == "Electronics"   


def test_update_product_not_found():
    product_data = {
        "name": "Updated Product",
        "price": 1000,
        "category": "Test",
        "description": "Test"
    }

    response = client.put(
        "/products/999999",
        json=product_data
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Product not found"
    }

def test_delete_product(test_product):
    response = client.delete(
        f"/products/{test_product}"
    )

    assert response.status_code == 200

    assert response.json() == {
        "message": "Product deleted successfully"
    }


def test_deleted_product_not_found(test_product):
    delete_response = client.delete(
        f"/products/{test_product}"
    )

    assert delete_response.status_code == 200

    response = client.get(
        f"/products/{test_product}"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Product not found"
    }

def test_error_test():
    response = client.get("/products/error-test")

    assert response.status_code == 400

    assert response.json() == {
        "detail": "This is a test error"
    }    

def test_custom_error():
    response = client.get("/products/custom-error")

    assert response.status_code == 200

    assert response.json() == {
        "success": False,
        "error": "CUSTOM_ERROR",
        "message": "This is a custom error response"
    }
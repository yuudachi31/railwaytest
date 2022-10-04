from fastapi import APIRouter
import time
from db.productJson import product_list

router = APIRouter(
    prefix='/products',
    tags=['products']
)


@router.get('/')
def get_all_products():
    # return products
    # time.sleep(1)
    return product_list


@router.get('/id/{product_id}')
def get_product_by_id(product_id):
    # time.sleep(1)
    return next((product for product in product_list if product['id'] == product_id))


@router.get("/{category}")
def get_product_by_category(category):
    category_list = []
    # time.sleep(1)

    if category.upper() == 'all':
        return product_list

    for product in product_list:
        if product['category'].upper() == category.upper():
            category_list.append(product)
    return category_list

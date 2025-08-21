from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, ValidationError

from app.config import load_config
from app.logger import logger
# from app.models import User, FeedBack, NewUSER
from app.models import Product

config = load_config()

app = FastAPI()

if config.debug:
    app.debug = True
else:
    app.debug = False

fake_db = [
    {"username": "vasya", "user_info": "любит колбасу"},
    {"username": "katya", "user_info": "любит петь"}
]


# @app.get('/user/{username}')
# async def get_user(username: str):
#     for user in  fake_db:
#         if user['username'] == username:
#             return user
#     return {"Erorr":"User not found"}


# @app.get('/users')
# async def get_users(limit: int = 10):
#     return fake_db[:limit]


# @app.post('/user_add')
# async def add_user(user: User):
#     try:
#         fake_db.append(user)
#         return {"status": "Ok"}
#     except:
#         return {"massage": "user not add"} 
      
# feedback_data = []
# @app.post('/add_feedback')
# async def add_feedback(feedback: FeedBack, is_premium: bool=False):
#     feedback_data.append(feedback)
    
#     if is_premium:
#         return {
#             "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён. Ваш отзыв будет рассмотрен в приоритетном порядке."
#         }

#     return {
#         "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
#     }


# @app.get('/feedback')
# async def get_feedback():
#     return feedback_data



# @app.post('/create_new_user')
# async def create_new_user(user: NewUSER):
#     new_user = user
#     return new_user


sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]

print('hellasdow=')
@app.get('/product')
async def get_all_product():
    result = [el for el in sample_products]
    return result

@app.get('/product/{id}')
async def get_product_by_id(id: int):
    result = [el for el in sample_products]
    for el in result:
        if el['product_id'] == id:
            return el
    return {"message": "Product not found((1))"}
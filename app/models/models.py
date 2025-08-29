# вставьте этот код в любой файл, который бы вы могли выполнить
# например это abc.py, который вы запустите в терминале командой python3 abc.py
from datetime import datetime

from pydantic import BaseModel, Field, EmailStr
from typing import Optional





# class Childrens(BaseModel):
#     name: str
#     age: int

# class Contact(Childrens):
#     phone: Optional[str] = None
#     email: Optional[str] = None
#     child:  Optional[Childrens] = None

# class FeedBack(BaseModel):
#     name: str = Field(min_length=2, max_length=50) 
#     message:str = Field(min_length=10, max_length=100)
#     contact: Optional[Contact] = None
   

# # Создаём модель данных, которая обычно располагается в файле models.py
# class User(BaseModel):
#     name: str
#     user_info: Optional[str] = None
        

# class NewUSER(BaseModel):
#     name: str
#     emain: EmailStr
#     age: int
#     is_subscribe: bool = None


class Product(BaseModel):
    prodiuct_id: int 
    name: str
    category: str
    price: int|float
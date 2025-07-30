# вставьте этот код в любой файл, который бы вы могли выполнить
# например это abc.py, который вы запустите в терминале командой python3 abc.py
from datetime import datetime

from pydantic import BaseModel


class FeedBack(BaseModel):
    name:str
    massage:str


# Создаём модель данных, которая обычно располагается в файле models.py
class User(BaseModel):
    name: str 
    user_info: str
        
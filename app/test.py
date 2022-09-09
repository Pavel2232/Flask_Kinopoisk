import jwt

from app.constant import secret, algo, user_dao
from app.dao.user import UserDAO
from app.setup_db import db
from constant import user_service

refresh_token1 = {"refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IlRpbSIsInJvbGUiOiJ1c2VyIiwiZXhwIjoxNjczOTU3OTY1fQ.HsBk1-J5chiZ_X1Ly6NlXmZfZFtCBCxUYhuC1uL_F4s"
    }

refresh_token = refresh_token1.get("refresh_token")

data = jwt.decode(jwt = refresh_token, key= secret, algorithms=[algo])
username = data.get("username")

print(data)
# #
# {
#     "username": "1",
#     "password": "test",
#     "role": "admin"
# }
import jwt
from flask import request,current_app
from flask_restx import abort



def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, current_app.config["PWD_HASH_SALT"], algorithms=current_app.config["PWD_HASH_ITERATIONS"])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            user = jwt.decode(token,current_app.config["PWD_HASH_SALT"], algorithms=current_app.config["PWD_HASH_ITERATIONS"])
            role = user.get("role")
            if role != "Admin":
                abort(400)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


class Config():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://$DB_USER:$DB_PASSWORD@app_postgres_1/$DB_NAME'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PWD_HASH_SALT = b"secret here"
    PWD_HASH_ITERATIONS = 100_000
    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAY = 130
    SECRET = 's3cR$eT'
    ALGO = 'HS256'




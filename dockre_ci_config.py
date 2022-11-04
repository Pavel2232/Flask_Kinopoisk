class Config():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://pavel2232:10203040x@postgres/movie'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PWD_HASH_SALT = b"secret here"
    PWD_HASH_ITERATIONS = 100_000
    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAY = 130
    SECRET = 's3cR$eT'
    ALGO = 'HS256'




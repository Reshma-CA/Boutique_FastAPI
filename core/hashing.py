
from passlib.hash import argon2

class Hasher:
    @staticmethod
    def get_password_hash(password: str) -> str:
        return argon2.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return argon2.verify(plain_password, hashed_password)

# from passlib.context import CryptContext

# # Switch from bcrypt to pbkdf2_sha256 or argon2
# psw_context = CryptContext(schemes=["pbkdf2_sha256", "argon2"], deprecated="auto")

# class Hasher:
#     @staticmethod
#     def get_password_hash(password: str) -> str:
#         return psw_context.hash(password)

#     @staticmethod
#     def verify_password(plain_password: str, hashed_password: str) -> bool:
#         return psw_context.verify(plain_password, hashed_password)




# from passlib.context import CryptContext

# psw_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# class Hasher:
#     @staticmethod
#     def verify_password(plain_password, hashed_password):
#         return psw_context.verify(plain_password, hashed_password)

#     @staticmethod
#     def get_password_hash(password):
#         return psw_context.hash(password)
    

# from passlib.hash import bcrypt

# hashed_password = bcrypt.hash("supersecrets")
# print(hashed_password)

# import logging
# from passlib.context import CryptContext

# logging.basicConfig(level=logging.DEBUG)
# psw_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# class Hasher:
#     @staticmethod
#     def get_password_hash(password):
#         logging.debug(f"Hashing password: {password}")
#         hashed_password = psw_context.hash(password)
#         logging.debug(f"Hashed password: {hashed_password}")
#         return hashed_password

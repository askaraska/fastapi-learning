# from fastapi import HTTPException

from pwdlib import PasswordHash



password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

# # testing
# if __name__ == "__main__":
#     password = "StrongPass123"

#     hashed = hash_password(password)

#     print("Original password:", password)
#     print("Hashed password:", hashed)

#     print(
#         "Correct password:",verify_password(password, hashed)
#     )

#     print(
#         "Wrong password:",verify_password("WrongPassword", hashed)
#     )





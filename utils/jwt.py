from datetime import datetime, timedelta, timezone

import jwt
from jwt.exceptions import InvalidTokenError

from config import SECRET_KEY

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(
    data: dict, expires_delta: timedelta | None = None
):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )    

    to_encode.update({
        "exp": expire
    })    

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# if __name__ == "__main__":
#     token = create_access_token(
#         {
#             "sub": "1"
#         }
#     )

#     print("JWT Token:")
#     print(token)

def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:
            return None

        return payload

    except InvalidTokenError:
        return None

# if __name__ == "__main__":
#     token = create_access_token(
#         {
#             "sub": "1"
#         }
#     )

#     print("JWT Token:")
#     print(token)

#     print("\nDecoded payload:")
#     print(verify_access_token(token))

#     print("\nInvalid token:")
#     print(
#         verify_access_token(
#             "this-is-an-invalid-token"
#         )
#     )
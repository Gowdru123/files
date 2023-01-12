from base64 import standard_b64encode, standard_b64decode
from configs import Config

def str_to_b64(__str: str) -> str:
    str_bytes = __str.encode('ascii')
    bytes_b64 = standard_b64encode(str_bytes)
    b64 = bytes_b64.decode('ascii')
    return b64


def b64_to_str(b64: str) -> str:
    bytes_b64 = b64.encode('ascii')
    bytes_str = standard_b64decode(bytes_b64)
    __str = bytes_str.decode('ascii')
    return __str


async def get_shortlink(link, api: int):
    api_key = user["shortener_api"]
    print(user)
    return f"https://{Config.BASE_SITE}/st?api={api_key}&url={link}" if api else link


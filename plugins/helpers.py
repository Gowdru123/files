from base64 import standard_b64encode, standard_b64decode
from config import Config
from shortzy import Shortzy

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


async def get_short_link(user, link, ):
    api_key = user["shortener_api"]
    print(user)
    base_site = Config.BASE_SITE

    shortzy = Shortzy(api_key, base_site)

    short_link = await shortzy.convert(link)

    return short_link

import aiohttp
import re
from b import *
from c import *
from database.url_db import *
from e import *

# GLOBAL-VAR
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}


# WEB-ZONE

async def request(url):
    async with aiohttp.ClientSession() as s:
        async with s.get(url, headers=header, timeout=20) as r:
            return await r.json()

from f import *

async def get_json(url, api):
    url = f"https://kpslink.in/api?api={api}&url={url}"
    print(url)
    async with aiohttp.ClientSession() as s:
        for i in range(3):
            try:
                async with s.get(url, headers=header, timeout=20) as res:
                    res = await res.json()
                    print(res)
                    return res
            except Exception as e:
                print(e)
        return False


async def shortner(links, api):
    nlist = []
    for i in range(len(links)):
        if re.search(r"ture", links[i]):
            nlist.append(links[i])
            continue
        link = await get_json(links[i], api)
        try:
            link = link["shortenedUrl"]
        except Exception as e:
            print(e)
            link = ""
        nlist.append(link)
    return nlist


# API_ZONE

async def api_checker(api):
    url = f"https://kpslink.in/api?api={api}&link={link}"
    r = await request(link)
    print(r)
    if r["status"] != "error":
        return 1, "sucess"
    return False, "failed"


# TEXT-CHANGER-ZONE
async def link_replacer(c, links, nlinks):
    for i in range(len(links)):
        c = c.replace(links[i], nlinks[i])
    return c


async def username_check(c):
    if re.search('@[^\s]+', c):
        return True
    else:
        return False


async def remove_username(c, username):
    c = re.sub('@[^\s]+', username, c)
    return c


async def link_extractor(c):
    links = re.findall("(?P<url>https?://[^\s]+)", c)
    return links


async def bolder(c):
    return "<b> " + c + "</b>"


# EVENT HANDLERS
async def get_type(e):
    if e.file is None and e.media is None and e.photo is None:
        mtype = "text"
    else:
        mtype = "file"
    return mtype

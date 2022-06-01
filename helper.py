from config import bot,dp
import requests as r
import re
import os
import cgitb
from urllib.parse import urlparse
import asyncio

# show detailed errors
cgitb.enable()

def is_valid(url: str):
	if re.match(r"https://www.instagram.com/tv/",url) or re.match(r"https://www.instagram.com/p/",url) or re.match(r"https://www.instagram.com/reel/",url) :
		req = r.get(url)
		if req.status_code == 200:
			return True
	else:
		return False

def prepare_urls(matches):
	return list({match.replace("\\u0026", "&") for match in matches})

async def send_video(user,viewers,username,description):
	await bot.send_video(user.id,open(f'videos/{user.id}.mp4','rb'),caption="<i>@igviddwdbot</i>",parse_mode='HTML')
	await delete_video(user)

async def delete_video(user):
	if os.path.exists(f"videos/{user.id}.mp4"):
		os.remove(f"videos/{user.id}.mp4")

async def normalize_url(url: str):
	uri = urlparse(url)
	path = uri.path.split("/")
	media_id = path[2]

	normalized_url = f"https://www.instagram.com/p/{media_id}/?{uri.query}"
	return normalized_url
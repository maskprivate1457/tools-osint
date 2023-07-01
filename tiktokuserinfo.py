import requests
import json
import sys
from rich.panel import Panel
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich import print as cetak


url = "https://tiktok-scraper7.p.rapidapi.com/user/info"
username = input('\33[m[\033[93m?\33[m] MASUKKAN USERNAME TIKTOK > \x1b[1;92m')
querystring = {"unique_id":username}
headers = {
	"X-RapidAPI-Key": "1a1537d560mshbad07893adb9308p1f0fb2jsn3484472e8f81",
	"X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
output = response.json()
print("")
print(f"\33[m[\x1b[1;92m+\33[m] ID TIKTOK > \x1b[1;92m{output['data']['user']['id']}")
print(f"\33[m[\x1b[1;92m+\33[m] USERNAME TIKTOK > \x1b[1;92m{output['data']['user']['uniqueId']}")
print(f"\33[m[\x1b[1;92m+\33[m] NICKNAME TIKTOK > \x1b[1;92m{output['data']['user']['nickname']}")
print(f"\33[m[\x1b[1;92m+\33[m] AVATAR THUMB > \x1b[1;92m{output['data']['user']['avatarThumb']}")
print(f"\33[m[\x1b[1;92m+\33[m] AVATAR MEDIUM > \x1b[1;92m{output['data']['user']['avatarMedium']}")
print(f"\33[m[\x1b[1;92m+\33[m] AVATAR LARGER > \x1b[1;92m{output['data']['user']['avatarLarger']}")
print(f"\33[m[\x1b[1;92m+\33[m] SIGNATURE > \x1b[1;92m{output['data']['user']['signature']}")
print(f"\33[m[\x1b[1;92m+\33[m] VERIFIED > \x1b[1;92m{output['data']['user']['verified']}")
print(f"\33[m[\x1b[1;92m+\33[m] UID > \x1b[1;92m{output['data']['user']['secUid']}")
print(f"\33[m[\x1b[1;92m+\33[m] SECRET > \x1b[1;92m{output['data']['user']['secret']}")
print(f"\33[m[\x1b[1;92m+\33[m] FTC > \x1b[1;92m{output['data']['user']['ftc']}")
print(f"\33[m[\x1b[1;92m+\33[m] RELATION > \x1b[1;92m{output['data']['user']['relation']}")
print(f"\33[m[\x1b[1;92m+\33[m] OPEN FAVORITE > \x1b[1;92m{output['data']['user']['openFavorite']}")
print(f"\33[m[\x1b[1;92m+\33[m] KOMEN SETTING > \x1b[1;92m{output['data']['user']['commentSetting']}")
print(f"\33[m[\x1b[1;92m+\33[m] DUET SETTING > \x1b[1;92m{output['data']['user']['duetSetting']}")
print(f"\33[m[\x1b[1;92m+\33[m] STITCH SETTING > \x1b[1;92m{output['data']['user']['stitchSetting']}")
print(f"\33[m[\x1b[1;92m+\33[m] PRIVATE ACCOUNT > \x1b[1;92m{output['data']['user']['privateAccount']}")
print(f"\33[m[\x1b[1;92m+\33[m] AD VIRTUAL > \x1b[1;92m{output['data']['user']['isADVirtual']}")
print(f"\33[m[\x1b[1;92m+\33[m] AGE > \x1b[1;92m{output['data']['user']['isUnderAge18']}")
print(f"\33[m[\x1b[1;92m+\33[m] INS ID > \x1b[1;92m{output['data']['user']['ins_id']}")
print(f"\33[m[\x1b[1;92m+\33[m] TWITTER ID > \x1b[1;92m{output['data']['user']['twitter_id']}")
print(f"\33[m[\x1b[1;92m+\33[m] JUDUL YOUTUBE CHANNEL > \x1b[1;92m{output['data']['user']['youtube_channel_title']}")
print(f"\33[m[\x1b[1;92m+\33[m] ID YOUTUBE CHANNEL > \x1b[1;92m{output['data']['user']['youtube_channel_id']}")
print(f"\33[m[\x1b[1;92m+\33[m] JUMLAH FOLLOWING > \x1b[1;92m{output['data']['stats']['followingCount']}")
print(f"\33[m[\x1b[1;92m+\33[m] JUMLAH FOLLOWERS > \x1b[1;92m{output['data']['stats']['followerCount']}")
print(f"\33[m[\x1b[1;92m+\33[m] HEART COUNT > \x1b[1;92m{output['data']['stats']['heartCount']}")
print(f"\33[m[\x1b[1;92m+\33[m] JUMLAH VIDEO > \x1b[1;92m{output['data']['stats']['videoCount']}")
print(f"\33[m[\x1b[1;92m+\33[m] DIGGCOUNT > \x1b[1;92m{output['data']['stats']['diggCount']}")
print(f"\33[m[\x1b[1;92m+\33[m] ID TIKTOK > \x1b[1;92m{output['data']['stats']['heart']}")
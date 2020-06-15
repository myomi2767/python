from pprint import pprint
import requests

key = 'AIzaSyCWSLMap3Wx1SN_C0ouEDe0pdcSbbxmTUM'
# string interpolation
search = input("검색어를 입력해 주세요 : ")
q = f'q={search}'
my_type = 'type=video'
part = 'part=snippet'
url = f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{q}&maxResults=20'

response = requests.get(url)
datas = response.json()
# 채널명, 영상 제목
for data in datas['items'][:10]:
    print(data['snippet']['title'], end=' 채널명 ')
    print(data['snippet']['channelTitle'])

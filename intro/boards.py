### 특정 유저의 게시글 출력하기

# > 제시된 url을 통해 게시글 정보를 받아와 userId가 4인 유저가 작성한 모든 게시글의 제목을 출력하시오.

import requests
url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url).json()

for i in response:
    if i['userId'] == 4 :
        print(i['title'])


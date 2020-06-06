### 상승장? 하락장?

# > 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 '상승장', 그렇지 않을 경우 '하락장' 문자열을 출력하시오

# | Key Name      | Description                     |
# | ------------- | ------------------------------- |
# | opening_price | 최근 24시간 내 시작 거래금액    |
# | closing_price | 최근 24시간 내 마지막 거래 금액 |
# | min_price     | 최근 24시간 내 최저 거래금액    |
# | max_price     | 최근 24시간 내 최고 거래금액    |

import requests

def btc(params):
    url = f'https://api.bithumb.com/public/ticker/btc?status={params}'
    response = requests.get(url).json()
    data = response['data']
    cost = int(data['opening_price']) + (int(data['max_price']) - int(data['min_price']))
    if cost >= int(data['max_price']) :
        print('상승장')
    else :
        print('하락장')

params = input('종목번호를 입력하세요 : ')
btc(params)

#강사님 풀이
# url = 'https://api.bithumb.com/public/ticker/btc'
# response = requests.get(url).json()['data']

# fluctuation = int(data['max_price']) - int(data['min_price'])
# if fluctuation + int(data['opening_price']) >= int(data['max_price'])
#     print('상승장')
# else :
#     print('하락장')



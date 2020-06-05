from lt import lottos

pick = lottos.lotto(1000)
print(pick)

# 1. 만약 4등 한적이 있으면
# 2. 4등 몇번 했습니다.
# 3. 4등 한 적 없으면, 실패 출력

if pick['4th'] >= 1:
    print(f'4등 {pick["4th"]}번 했습니다.')
else:
    print('실패')

# lotto('str')

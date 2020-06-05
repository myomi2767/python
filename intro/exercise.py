import random
# 1. 로또번호 추첨하는데 5번 반복해서
for i in range(5):
    print(sorted(random.sample(range(1,46), 6)))

print("*"*30)
lotto = [sorted(random.sample(range(1,46), 6)) for i in range(5)]
print(lotto)
# 2. 음식점 이름, 전화번호인 딕셔너리
food = {
    '자장면' : '010-2433-4422',
    '짬뽕' : '010-1234-3333',
    '탕수육' : '010-1111-2222',
}
# 2-1. 그 중에서 무작위 음식점 하나 뽑아서
pick = random.choice(list(food.keys()))
print(pick)
# 2-2. 가게이름이랑 전화번호 출력 
print('가게이름은', pick)
print('전화번호는', food[pick])

# f-string
print(f'가게이름은 {pick}, 전화번호는 {food[pick]}')
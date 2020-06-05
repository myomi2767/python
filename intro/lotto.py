import random
#print(dir(random)) #dir 이라는 내장함수로 random을 부른다.
#dir를 사용해서 메소드 뭐있는지 찾아볼 수 있다.

#choice를 써보자
number = random.choice(range(10))
#print(number)

# list에서 무작위로 '뽑아보자.
arr = [100,40,30,50]
pick = random.choice(arr)
#print(pick)

# dictionary에도 써보자
mask = {
    '100' : '삼성',
    '40' : '역삼',
    '30' : '선릉',
    '50' : '영등포'
}
#print(mask[str(pick)])


#sample
lotto = random.sample(range(1,46),6)
print(sorted(lotto))

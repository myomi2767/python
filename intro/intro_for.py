# 반복문 종류 2개
# 1. While

#n=0
#while n < 3 :
#    print(n)
#    n += 1

# 0 1 2

#n=0
#while n<3:
#    n += 1
#    print(n)
#print(n)
#출력결과 : 1 2 3 3

#2. for
#number = list(range(3,10,2))
#print(number)

#for num in range(10):
#    print(num)


# 2-1. list for
#number = [10,9,8,7,6,5,4,3,2,1,0]
#for num in number:
#    print
number = ['삼성', '역삼', '선릉', '일산']
# 2-2. idx로 접근하고 싶어요
#for i in range(len(number)):
#    print(number[i])


# 2-3. enumerate
#for idx, i in enumerate(number):
#    print(idx,i)

# 3. dictionary
mask = {
    '삼성' : 100,
    '역삼' : '50개',
    '선릉' : True
}

for i in mask : 
    print(i) 
print("*"*30)

for i in mask.keys():
    print(i)
print("*"*30)

for i in mask.values():
    print(i)
print("*"*30)

for key, val in mask.items():
    print(key) # key값
    print(val) # value값
    print(mask[key]) # key값으로 접근한 value값

print("*"*50)

for idx, i in enumerate(mask):
    print(idx,i)
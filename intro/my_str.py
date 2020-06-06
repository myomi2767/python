### 모음 제거하기

# 다음 문장의 모음을 제거하여 출력하세요.

my_str = "Life is too short, you need pyhton"
# for char in my_str :
#     print(char)

new_str = my_str.split(' ')
# print(new_str)
# print(new_str[0][0])

new_str = my_str.replace('Life', 'Time')
# print(new_str)

vowels = ['a', 'e', 'i', 'o', 'u']
# for char in vowels:
#     if char in my_str:
#         my_str = my_str.replace(char,'')

# print(my_str)

result = ''
for char in my_str:
    if char not in vowels:
        result += char


# print(result)


print(my_str.find('i')) # 없으면 -1
print(my_str.index('i')) # 없으면 오류


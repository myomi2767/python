### 과일 개수 골라내기

# 장바구니에 아래와 같은 과일이 들어 있고 과일 판별 리스트가 있습니다. 현재 장바구니에는 과일이 몇 개이고, 과일이 아닌 것은 몇 개인지 출력하시오.

# 못품.....(2중 for문은 의미 없음)
# basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# fruit = 0
# notFruit = 0
# for key, val in basket_items.items() :
#     if key == fruits
#         fruit += val
#     elif key != ((for i in fruits) : i) :
#         notFruit += val

# print(f'과일은 {fruit}개 이고, 과일이 아닌 것은 {notFruit}개 입니다.')

# 강사님 풀이
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

fruit_count = 0
not_fruit_count = 0
for key, val in basket_items.items() :
    if key in fruits :
        fruit_count += val
    else :
        not_fruit_count += val

print(f'과일은 {fruit_count}개 이고, 과일이 아닌 것은 {not_fruit_count}개 입니다.')


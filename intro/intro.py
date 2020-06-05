print("hello world")

#저장, 조건, 반복

#1. 저장
#int? str? bool?
number = 10
string = "string"
boolean = True 

print(number, string, boolean)

#2. 리스트 저장
#파이썬에서는 배열같은 개념인 리스트가 있다.
arr = [number, string, boolean]
arr_2 = [10, "10", True, number]
print(arr_2)

#2-1. 인덱스로 접근하기
print(arr_2[0], arr_2[1], arr[2])

#2-2. 자료형 출력하기
print(type(arr_2[0]), type(arr_2[1]))

#3. dictionary //중괄호로 감싼다.
mask = {
    '삼성' : 100,
    '역삼' : 50,
    '선릉' : 30,
    '영등포' : 10
}
print(mask)
print(mask['삼성']) #이렇게 key갑을 지정해주면 value 값만 나오게 된다.
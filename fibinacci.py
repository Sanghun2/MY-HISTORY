# 1. 수를 입력받아서 저장
# 2. 횟수를 체크할 글로벌 변수
# 3. 0이 return 될때 0글로벌 변수에 0의 횟수를 +1
# 4. 1이 return 될 때 1글로벌 변수에 1의 횟수를 +1
# 마지막에 최종 0의 횟수와 1의 횟수를 출력

num = int(input("숫자를 입력하세요 : "))

count_0 = 0
count_1 = 0

def fibonacci(n):
    
    global count_0
    global count_1
    


    if n == 0:
        count_0 =  count_0 + 1
        return 0

    elif (n == 1):
        count_1 = count_1 + 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(num)
print("0의 횟수는 : ", count_0)
print("1의 횟수는 : ", count_1)
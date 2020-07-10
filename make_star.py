# 별찍기 (for, range, input 사용)
# 1. 입력을 받는다
# 입력한 수 만큼 별을 더해서 출력한다.
# 2. 출력할 때 마다 2씩 줄어들게 하고, 빈칸이 1씩 증가시켜서 더한다.
# 3. 출력되는 값의 갯수가 2이하이면 2씩 증가하면서 다시 출력한다.

space = " "
star = "*"


num = int(input("숫자를 입력하세요 : "))

def Making_Star(n):
     
    star_line = ""
    global num_of_space
    global num_of_star
    added_space = ""
    num_of_space = 0
    num_of_star = n #나중에 n은 증가할 때 멈춤 조건
    
    while num_of_star >= 1:
        
        for i in range(num_of_star):
            star_line += star
        added_space = space * num_of_space
        star_line = added_space + star_line
        print(star_line)
        num_of_star -= 2 # 조건변화
        num_of_space += 1 # 공백의 길이
        star_line = ""
        added_space = ""
        
        

    # 현재 짝수면 num_of_space == 0, 홀수면 num_of_space == -1
        num_of_star = num_of_star + 4 # 짝수면 4, 홀수면 3        
        num_of_space -= 1

        i = 0        

        while i <= n: # i가 처음수와 같아지거나 커지게 되면 종료한다.
            for i in range(num_of_space):
                star_line += star # star_line을 만든다.
            added_space = space * num_of_space
            star_line = added_space + star_line # added_space와 star_line을 더해서 출력한다.
            print(star_line)
            star_line = ""
            added_space = ""
            num_of_space -= 1                         
            num_of_star += 2 # 출력이 끝나면 빈칸을 1줄이고, 별의 갯수를 2늘린다. 
            i += 1
        


        


Making_Star(num)
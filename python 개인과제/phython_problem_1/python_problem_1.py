num=0

ice_n = input('부를 숫자의 개수를 입력하세요(1,2,3 만 입력가능) :')


while True: #
    if ice_n.isdigit(): #조건1 정수를 입력
        if ice_n == '1' or ice_n =='2' or ice_n =='3':
            break
        else:  #1,2,3을 입력하지 않은 경우 
            ice_n = input('1,2,3 만 입력가능 :')
    else: # 정수를 입력하지 않은 경우
        ice_n = input('정수만 입력가능 :')

ice_n= int(ice_n)
for num in range(ice_n):
    num = num+1
    print ('playerA:',(num))

   
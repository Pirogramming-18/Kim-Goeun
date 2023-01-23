#함수 이름은 변경 가능합니다.
studentlist= []

##############  menu 1
def Menu1(name, mid_score, final_score) :
    #사전에 학생 정보 저장하는 코딩
    studentlist.append([name,mid_score,final_score])

##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    for i in range(len(studentlist)):
        score = float((studentlist[i][1]+studentlist[i][2])/2)
        grade=""
        if score >= 90:
            grade="A"

        elif score >= 80:
            grade="B"

        elif score >= 70:
            grade ="C"

        else:
            grade ="D"
        studentlist[i].append(grade)    

##############  menu 3
def Menu3() :
    print("---------------------------")
    print("name   mid_score   final_score  grade")
    print("---------------------------")

    for studentlist
        name = studentlist['name']
        mid = studentlist['mid_score']
        final = studentlist['final_score']
        grade = studentlist['grade']
        print(f'{name}\t{mid}\t{final}\t{grade}')

##############  menu 4
def Menu4():
    #학생 정보 삭제하는 코딩
    for i in range(len(studentList)):
        if name == studentList[i][0] :
          del studentList[i]
          break
        ?

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        n, m, f = input('정보를 입력하세요').split(n,m,f)

        Menu1(n,m,f)
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 

    elif choice == "2" :
        break
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력

    elif choice == "3" :
        break
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4" :
        break
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        print("Exit porgram!")
        break
    

    else :
        #"Wrong number. Choose again." 출력
         print("Wrong number. Choose again.")



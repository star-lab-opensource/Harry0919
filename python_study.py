def first_class_number(month, day):

    def day_of_year(month, day): #몇번째 일 인지 구하는 거
        month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        day_total=0
    
        for i in range(1,month):
            day_total+=month_days[i]

        day_total+=day

        return(day_total)

    
    def weekday_2025(month, day): #요일 구하는 거

        base_day=3

        past_day=day_of_year(month, day)
        weekday_result= (base_day+past_day-1)%7

        if weekday_result==0:
            weekday_result=7

        return weekday_result


    def week_of_number(month, day):
        day_of_number=day_of_year(month, day)
        day_of_week=weekday_2025(month, day)
   

        thursday=day_of_number+(4-day_of_week)

        week=1+(thursday-1)//7

        return week
    
    week=week_of_number(month, day)
    class_number=((week-1)%9)+1
    return class_number



def my_class_order(month, day):

    class_list=[1,2,3,4,5,6,7,8,9]

    if my_class >= first_class_number(month, day):
        return my_class-first_class_number(month, day)+1
    if my_class < first_class_number(month, day):
        return (len(class_list)-first_class_number(month, day)+1)+my_class






month, day=map(int, input("몇월 몇일 인가요? :").split())
my_class=int(input("당신의 반은 몇반 입니까? :"))
go_class = int(input("급식실로 간 반: "))

ahead_class = my_class + 1

if go_class == ahead_class:
    print("출발하세요")
else:
    print("순서를 기다리세요")

print("첫번째로 밥먹는반은:",first_class_number(month,day),"반 입니다.")
print("당신의 반은",my_class_order(month,day),"번 째 입니다")



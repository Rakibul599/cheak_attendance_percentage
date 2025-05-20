import pandas as pd

studentinfo=pd.read_excel('demo.xlsx')


column_length = len(studentinfo.columns)
total_rows = len(studentinfo)-1

n=int(input("Please enter the number of Students:"))
if(0<n and total_rows>=n):

    n=n+1
    res={}

    for i in range(1,n):
        total_pr=0
        name=studentinfo.iloc[i, 2]
        id=studentinfo.iloc[i, 1]
        for j in range(column_length):
            value = studentinfo.iloc[i, j]
            # print(value,i,j)
            if not pd.isna(value):
                if value=="P":
                    total_pr=total_pr+1
        total_percentage=(total_pr/20)*100
        mark=0
        if(total_percentage>=70):
            mark=5
        elif(total_percentage>=60):
            mark=4
        elif(total_percentage>=45):
            mark=3
        elif(total_percentage>=30):
            mark=2 
        else:
            mark=2


    
        res[i] = {
            "name": name,
            "total_percentage":total_percentage,
            "id":id,
            "mark":mark
        }

    idxx=1
    std_count=[]
    count_info={
        "1":{
            "percent":'70%',
            "count":0
        },
        "2":{
            "percent":'60%',
            "count":0
        } ,  
        "3":{
            "percent":'45%',
            "count":0
        },
        "4":{
            "percent":'30%',
            "count":0
        }
    }
    for id,inform in res.items():
        if int(inform['total_percentage']) >=70:
            count_info['1']["count"]=count_info['1']["count"]+1
        elif int(inform['total_percentage']) >=60:
            count_info['2']["count"]=count_info['2']["count"]+1
        elif int(inform['total_percentage']) >=45:
            count_info['3']["count"]=count_info['3']["count"]+1
        elif int(inform['total_percentage']) >=30:
            count_info['4']["count"]=count_info['4']["count"]+1

  
    print("Calculated Attendance Percentage:")
    print(f"{'No.':<4} {'Name':<45} {'ID':<10} {'Percentage':<12} {'Mark':<5}")
    for idx, (id, infor) in enumerate(res.items(), start=1):
        percent=f"{int(infor['total_percentage'])}%"
        print(f"{idx:<4} {infor['name']:<45} {int(infor['id']):<10} {percent:<12} {infor['mark']:<5}")

    print("Attendance Percentage(Student count):")
    print(f"{'No.':<5} {'Percentage':<10} {'count':<5}")
    for i in count_info:
        print(f"{i:<5} {count_info[i]['percent']:<10} {count_info[i]['count']:<5}")

else:
    
        print("Plese enter valid number of student ,total student is:",total_rows)
    
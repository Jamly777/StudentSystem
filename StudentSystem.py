import os
import re

def main():
    flag = True
    while (flag):
        Menu()
        Choose=int(input("请输入菜单中的选项："))
        if Choose == 0:
            flag = False
        elif Choose == 1:
            Insert()
        elif Choose == 2:
            Search()
        elif Choose == 3:
            Delect()
        elif Choose == 4:
            Modify()
        elif Choose == 5:
            Sort()
        elif Choose == 6:
            Total()
        elif Choose == 7:
            Show()
        else:
            print("请重新输入0-7的选项")
def Menu():
    print('''
          -----------------------------------------------
          |                    MENU                     |
          |      1.录入学生信息                         |
          |      2.查找学生信息                         |
          |      3.删除学生信息                         |
          |      4.修改学生信息                         |    
          |      5.排序学生                             |
          |      6.统计                                 |   
          |      7.显示学生信息                         |
          |      0.退出系统                             |      
          |_____________________________________________|
              
    ''')
def Save(student):
    try:
        student_txt=open("student.txt","a")
    except Exception as e:
        student_txt=open("student.txt","w")
    for info in student:
        student_txt.write(str(info)+"\n")
    student_txt.close()
def Insert():
    StudentList=[]
    Flag=True
    while (Flag):
        ID=input("请输入学生ID：")
        if not ID:
            break
        NAME=input("请输入学生名字：")
        if not NAME:
            break
        try:
            English=int(input("请输入英语成绩："))
            Python=int(input("请输入python成绩："))
            C=int(input("请输入C成绩："))
        except:
            print("请输入整数成绩")
            continue
        Studentinfo={"ID":ID,"NAME":NAME,"English":English,"Python":Python,"C":C}
        StudentList.append(Studentinfo)
        YN=input("是否继续添加（y/n）")
        if(YN=="y"):
            pass
        elif(YN=="n"):
            Flag=False
    Save(StudentList)
    print("信息录入完成")

def Search():
    Flag=True
    while(Flag):
        Searchinfo=input("请输入你要查询的字段（ID，NAME）：")
        student_txt=open("student.txt","r")
        studentlist=student_txt.readlines()
        if(Searchinfo=='ID'):
            ID=input("请输入ID：")
            for line in studentlist:
                studentdict={}
                studentdict=eval(line)
                if(studentdict['ID']==ID):
                    print(studentdict)
        if(Searchinfo=='NAME'):
            NAME=input("请输入NAME：")
            for info in studentlist:
                studentdict={}
                studentdict=eval(info)
                if(studentdict['NAME']==NAME):
                    print(studentdict)
        YN = input("是否继续查询（y/n）")
        if (YN == "y"):
            pass
        elif (YN == "n"):
            Flag = False
        student_txt.close()

def Delect():
    Flag=True
    while(Flag):
        student_txt = open("student.txt", "r")
        ID=input("请输入需要删除的学生ID：")
        studentlist=student_txt.readlines()
        student_txt=open("student.txt", "w")
        for info in studentlist:
            studentdict={}
            studentdict=eval(info)
            if(studentdict['ID']==ID):
                break
            else:
                student_txt.write(str(info))
        YN=input("是否继续删除（y/n）")
        if (YN == "y"):
            pass
        elif (YN == "n"):
            Flag = False
        student_txt.close()
def Modify():
    Flag=True
    while(Flag):
        ID=input("请输入需要修改的学生ID：")
        student_txt=open("student.txt","r")
        studentlist=student_txt.readlines()
        for info in studentlist:
            studentdict={}
            studentdict=eval(info)
            if(studentdict['ID']==ID):
                studentdict['NAME']=input("请输入学生姓名：")
                try:
                    studentdict['English']=int(input("请输入学生英语成绩："))
                    studentdict['Python']=int(input("请输入学生Python成绩："))
                    studentdict['C']=int(input("请输入学生C成绩："))
                except:
                    print("请输入整数")
                    continue
                student_txt=open("student.txt","w")
                student_txt.write(str(studentdict)+"\n")
        YN = input("是否继续修改（y/n）")
        if (YN == "y"):
            pass
        elif (YN == "n"):
            Flag = False
        student_txt.close()

def Sort():
    Flag=True
    student_new=[]
    student_txt=open("student.txt","r")
    studentlist=student_txt.readlines()
    for str in studentlist:
        studentdict=dict(eval(str))
        student_new.append(studentdict)
    while(Flag):
        try:
            ChooseNum=int(input("按照英语成绩排序请输入1，按照Python成绩请输入2，按照C成绩请输入3，按照总成绩请输入4："))
        except:
            print("请输入整数")
            continue
        if(ChooseNum==1):
            student_new.sort(key=lambda x: x['English'],reverse=True)
        elif(ChooseNum==2):
            student_new.sort(key=lambda x: x['Python'],reverse=True)
        elif(ChooseNum==3):
            student_new.sort(key=lambda x: x['C'],reverse=True)
        elif(ChooseNum==4):
            student_new.sort(key=lambda x:x['English']+x['Python']+x['C'],reverse=True)
        else:
            print("请输入1-4")
            break
        for line in student_new:
            print(line)
        YN = input("是否继续排序（y/n）")
        if (YN == "y"):
            pass
        elif (YN == "n"):
            Flag = False
        student_txt.close()
def Total():
    student_txt=open("student.txt","r")
    studentlist=student_txt.readlines()
    print("一共有%d学生" % len(studentlist))
def Show():
    try:
        student_txt=open("student.txt","r")
    except:
        print("文件不存在")
    studentlist=student_txt.readlines()
    for line in studentlist:
        print(line)
if __name__== "__main__":
    main()
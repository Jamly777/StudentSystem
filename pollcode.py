import os

def mkdir(path):
    isexits=os.path.exists(path)
    if not isexits:
        os.mkdir(path)
def openfile(filename):
    f=open(filename,"r")
    fileinfo=f.read()
    f.close()
    return fileinfo
def inputbox(infostr,showorder,length):
    instr=input(infostr)
    if len(instr)!=0:
        if showorder==1:
            if str.isdigit(instr):
                if instr==0:
                    print("\033[1,31.40m 输入为零，请重新输入！！ \033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1,31.40m 输入非法，请重新输入！！ \033[0m")
                return "0"
        if showorder==2:
            if str.isalpha(instr):
                if len(instr)!=length:
                    print("\033[1,31.40m 必须输入"+str(length)+"个字母，请重新输入 \033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1,31.40m 输入非法，请重新输入！！ \033[0m")
                return "0"
        if showorder==3:
            if str.isdigit(instr):
                if len(instr)!=length:
                    print("\033[1,31.40m 必须输入" + str(length) + "个字母，请重新输入 \033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1,31.40m 输入非法，请重新输入！！ \033[0m")
                return "0"
    else:
        print("\033[1,31.40m 输入为空，请重新输入！！ \033[0m")
        return "0"
def wfile(sstr,sfile,typeis,smsg):
    def wfile(sstr,sfile,typeis,smsg,datapath):
        mkdir(datapath)
        datafile=datapath+"\\"+sfile
        file=open(datafile,"w")
        wrlist=sstr
        pdata=""
        wdata=""
        for i in range(len(wrlist)):
            wdata=str(wrlist[i].replace('[', "")).replace(']', "")
            wdata=wdata.replace("'","").replace("'","")
            file.write(str(wdata))
            pdata=pdata+wdata
        file.close()
        print("\033[1;31m"+pdata+"\033[0m")
        if typeis !="no":
            tkinter.messagebox.showinfo("提示",smsg+str(len(randstr))+"\n 防伪码文件存放位置："+datafile)
            root.withdraw()


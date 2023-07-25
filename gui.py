import requests
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import tkinter.simpledialog
import time
import json
import openai
import os

def ope():
    os.system("log.txt")
def about():
    tkinter.messagebox.showinfo("关于软件","作者：haloged\nGithub仓库：https://github.com/haloged/get_hitokoto")
def run_1():
    yuan=var.get()
    run_num=tkinter.simpledialog.askinteger(title="请输入运行次数",prompt = "运行次数：")
    if yuan==0:
        with open("log.txt","a") as f:
            f.write("获取源：hitokoto.cn\n抓取次数："+str(run_num)+"\n\n")
        for i in range(run_num):
            hitokoto_jx={"hitokoto":"1"}
            hitokoto_get=requests.get("https://v1.hitokoto.cn")
            hitokoto_jx=json.loads(hitokoto_get.text)
            print(hitokoto_jx["hitokoto"])
            with open("log.txt","a") as f:
                f.write(hitokoto_jx["hitokoto"]+"\n")
            time.sleep(2)
        with open("log.txt","a") as f:
            f.write("\n\n")
        tkinter.messagebox.showinfo("提示","抓取成功！")
    elif yuan==1:
        with open("log.txt","a") as f:
            f.write("获取源：apiup\n抓取次数："+str(run_num)+"\n\n")
        for i in range(run_num):
            apiup_jx={"txt":"1"}
            apiup_get=requests.get("https://apiup.tcxone.eu.org/yiyan.php")
            apiup_jx=json.loads(apiup_get.text)
            print(apiup_jx["txt"])
            with open("log.txt","a") as f:
                f.write(apiup_jx["txt"]+"\n")
            time.sleep(2)
        with open("log.txt","a") as f:
            f.write("\n\n")
        tkinter.messagebox.showinfo("提示","获取成功！")
    elif yuan==2:
        with open("log.txt","a") as f:
            f.write("获取源：韩小韩API\n抓取次数："+str(run_num)+"\n\n")
        for i in range(run_num):
            vvhan_get=requests.get("https://api.vvhan.com/api/ian")
            print(vvhan_get.text)
            with open("log.txt","a") as f:
                f.write(vvhan_get.text+"\n")
            time.sleep(2)
        with open("log.txt","a") as f:
            f.write("\n\n")
        tkinter.messagebox.showinfo("提示","获取成功！")
    elif yuan==3:
        with open("log.txt","a") as f:
            f.write("获取源：ChatGPT\n抓取次数："+str(run_num)+"\n\n")
        gpt_api_token=tkinter.simpledialog.askstring("请输入你的OPENAI API KEY")
        openai.api_key = os.getenv(gpt_api_token)
        response = openai.Completion.create(model="text-davinci-003", prompt="请生成"+run_num+"个关于励志的句子", temperature=0, max_tokens=1000)
        print(response)
        with open("log.txt","a") as f:
            f.write(response)
        with open("log.txt","a") as f:
            f.write("\n\n")
        tkinter.messagebox.showinfo("提示","获取成功！")

root=tk.Tk()
root.title("一言生成器v1.0.0 By Haloged")
root.geometry("500x300")

mainmenu = tk.Menu(root)
menuFile = tk.Menu(mainmenu)  # 菜单分组 menuFile
mainmenu.add_cascade(label="文件",menu=menuFile)
menuFile.add_command(label="打开一言保存文件",command=ope)
menuFile.add_separator()  # 分割线
menuFile.add_command(label="退出",command=root.destroy)

menuEdit = tk.Menu(mainmenu)  # 菜单分组 menuEdit
mainmenu.add_cascade(label="关于",menu=menuEdit)
menuEdit.add_command(label="关于",command=about)
root.config(menu=mainmenu)

logo=tk.Label(root,text="一言生成器",font=("宋体",20))
logo.pack()

br=tk.Label(root,text=" ",font=("宋体",20))
br.pack()

run=tk.Button(root,text="开始抓取",command=run_1)
run.pack()

br1=tk.Label(root,text=" ",font=("宋体",20))
br1.pack()

xz=tk.Label(root,text="抓取源")
xz.pack()

var = tk.IntVar()
rd1 = tk.Radiobutton(root,text="hitokoto.cn",variable=var,value=0)
rd1.pack()

rd2 = tk.Radiobutton(root,text="apiup",variable=var,value=1)
rd2.pack()

rd3 = tk.Radiobutton(root,text="韩小韩API",variable=var,value=2)
rd3.pack()

rd4 = tk.Radiobutton(root,text="ChatGPT(需自行提供API KEY)",variable=var,value=3)
rd4.pack()

root.mainloop()
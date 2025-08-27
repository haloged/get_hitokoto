import requests
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import tkinter.simpledialog
import tkinter.ttk
import time
import json
import openai
import os
import yaml
from configparser import ConfigParser

print('''
   __ __     __                 __
  / // /__ _/ /__  ___ ____ ___/ /
 / _  / _ `/ / _ \/ _ `/ -_) _  / 
/_//_/\_,_/_/\___/\_, /\__/\_,_/  v1.3.0
                 /___/            
''')

def clean_hitokoto():
    os.system("del log.txt")
    tkinter.messagebox.showinfo("提示","删除成功！")

def ope_help_doc():
    os.system("start https://haloged-studio.feishu.cn/wiki/S554wi9cPiQi6yk1zhAcEEBfnjf")

def zdy():
    zdy_url=tkinter.simpledialog.askstring(title="请输入api地址",prompt = "地址")
    zdy_j=tkinter.simpledialog.askstring(title="请输入一言文字所在的json路径",prompt="路径（直接输出输入zjscc）：")
    zdy_cs=tkinter.simpledialog.askinteger(title="请输入运行次数",prompt="次数：")
    if zdy_j=="zjscc":
        with open("log.txt","a") as f:
            f.write("获取源：自定义源"+"\n"+"api地址："+zdy_url+"\n抓取次数："+str(zdy_cs)+"\n\n")
        for i in range(zdy_cs):
            zdy_get=requests.get(zdy_url)
            print(zdy_get.text())
            with open("log.txt","a") as f:
                f.write(zdy_get.text()+"\n")
            time.sleep(2)
        with open("log.txt","a") as f:
            f.write("\n\n")
        tkinter.messagebox.showinfo("提示","抓取成功！")
    else:
        with open("log.txt","a") as f:
            f.write("获取源：自定义源"+"\napi地址："+zdy_url+"\n抓取次数："+str(zdy_cs)+"\n\n")
        for i in range(zdy_cs):
            zdy_jx={zdy_j:"1"}
            zdy_get=requests.get(zdy_url)
            zdy_jx_get=json.loads(zdy_get.text)
            print(zdy_jx_get[zdy_j])
            with open("log.txt","a") as f:
                f.write(zdy_jx_get[zdy_j]+"\n")
            time.sleep(2)
        with open("log.txt","a") as f:
            f.write("\n\n")
        tkinter.messagebox.showinfo("提示","抓取成功！")
    

def ope_configfile():
    tip_config=tkinter.messagebox.askyesno("提示","非专业人士请勿修改，修改前请查看文档")
    if tip_config==True:
        os.system("config.yaml")
    
def jcgx():
    vertion=requests.get("https://tinywebdb.appinventor.space/api?user=haloged&secret=463de003&action=get&tag=bbh")
    vertion_jx=json.loads(vertion.text)
    bbh=vertion_jx["bbh"]
    print("当前最新版本："+bbh)
    if bbh=="1.3.0":
        tkinter.messagebox.showinfo("提示","无更新")
    else:
        tip_vertion=tkinter.messagebox.askyesno("提示","有新版本！\n点击“确定”转到仓库")
        if tip_vertion==True:
            os.system("start https://github.com/haloged/get_hitokoto/releases")

def ope_github():
    os.system("start https://github.com/haloged/get_hitokoto/")

def ope():
    os.system("log.txt")

def about():
    tkinter.messagebox.showinfo("关于软件","作者：haloged\n软件版本：1.3.0\n作者B站：https://space.bilibili.com/518055250\nGithub仓库：https://github.com/haloged/get_hitokoto")

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
            f.write("获取源：光环API\n抓取次数："+str(run_num)+"\n\n")
        for i in range(run_num):
            haloapi_jx={"txt":"1"}
            haloapi_get=requests.get("https://api.haloged.eu.org/")
            print(haloapi_get.text)
            with open("log.txt","a") as f:
                f.write(haloapi_get.text+"\n")
            time.sleep(2)
        with open("log.txt","a") as f:
            f.write("\n\n")
        tkinter.messagebox.showinfo("提示","获取成功！")

    elif yuan==2:
        with open("log.txt","a") as f:
            f.write("获取源：韩小韩API\n抓取次数："+str(run_num)+"\n\n")
        for i in range(run_num):
            vvhan_get=requests.get("https://api.vvhan.com/api/ian/rand")
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
        gpt_api_token=tkinter.simpledialog.askstring(title="请输入你的你的KEY",prompt="请输入你的OPENAI API KEY")
        openai.api_key = os.getenv(gpt_api_token)
        response = openai.Completion.create(model="text-davinci-003", prompt="请生成"+run_num+"个关于励志的句子", temperature=0, max_tokens=1000)
        print(response)
        with open("log.txt","a") as f:
            f.write(response)
        with open("log.txt","a") as f:
            f.write("\n\n")
        tkinter.messagebox.showinfo("提示","获取成功！")

    elif yuan==4:
        with open("log.txt","a") as f:
            f.write("获取源：DeepSeek\n抓取次数："+str(run_num)+"\n\n")
        deepseek_api_token=tkinter.simpledialog.askstring(title="请输入你的你的KEY",prompt="请输入你的DeepSeek API KEY")
        openai.api_key = os.getenv(deepseek_api_token)
        client = openai.OpenAI(api_key=os.getenv(deepseek_api_token), base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": "请生成"+run_num+"个关于励志的句子，直接给出"},
            ],
            stream=False
        )
        print(response.choices[0].message.content)
        with open("log.txt","a") as f:
            f.write(response.choices[0].message.content)
        with open("log.txt","a") as f:
            f.write("\n\n")
        tkinter.messagebox.showinfo("提示","获取成功！")


def save_config(status,lnaguage_c):
    print(status)
    if status=="开":
        update_status=True
    else:
        update_status=False
    if lnaguage_c=="chinese.ini":
        language_st=0
    else:
        language_st=1
    Data={
        "Automatically_check_for_updates": update_status,
        "language": language_st
    }
    with open('./config.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(data=Data, stream=f, allow_unicode=True)
    tip_close=tkinter.messagebox.askyesno("提示","更改成功，重启软件后生效\n点击“确定”立即关闭")
    if tip_close==True:
        root.destroy()
    


def read_language():
    a=0
    language_list=[]
    for item in os.listdir('./language'):
        print(item)
        language_list.append(item)
    return language_list
        

def ope_config():
    with open('./config.yaml', 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    update_status=result['Automatically_check_for_updates']
    language_status=result['language']

    win_config = tk.Toplevel(root)
    win_config.geometry('320x240')
    win_config.title('配置')
    config_logo=tk.Label(win_config,text="配置",font=("宋体",20))
    config_logo.pack()
    update_con=tk.Label(win_config,text="自动更新")
    update_con.pack()
    var = tk.StringVar()

    combobox = tkinter.ttk.Combobox(win_config)
    combobox.pack()
    combobox['value'] =("开","关")
    if update_status==True:
        combobox.current(0)
    else:
        combobox.current(1)
    
    language_con=tk.Label(win_config,text="语言")
    language_con.pack()
    combobox_language = tkinter.ttk.Combobox(win_config)
    combobox_language.pack()
    combobox_language['value'] =read_language()
    if language_status==0:
        combobox_language.current(0)
    elif language_status==1:
        combobox_language.current(1)
    
    btsave=tk.Button(win_config,text='保存',command=lambda:save_config(combobox.get(),combobox_language.get()))
    btsave.pack()

    btClose=tk.Button(win_config,text='关闭',command=win_config.destroy)
    btClose.pack()

def auto_update():
    with open('./config.yaml', 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    update_status=result['Automatically_check_for_updates']
    print(update_status)
    if update_status==True:
        vertion=requests.get("https://tinywebdb.appinventor.space/api?user=haloged&secret=463de003&action=get&tag=bbh")
        vertion_jx=json.loads(vertion.text)
        bbh=vertion_jx["bbh"]
        print("当前最新版本："+bbh)
        if bbh=="1.3.0":
            print("检查更新成功，目前无更新。")
        else:
            tip_vertion=tkinter.messagebox.askyesno("提示","有新版本！\n点击“确定”转到仓库")
            if tip_vertion==True:
                os.system("start https://github.com/haloged/get_hitokoto/releases")
    else:
        print("用户已关闭自动更新") 

root=tk.Tk()
root.title("一言生成器v1.3.0 By Haloged")
root.geometry("500x300")

mainmenu = tk.Menu(root)
menuFile = tk.Menu(mainmenu)  # 菜单分组 menuFile
mainmenu.add_cascade(label="文件",menu=menuFile)
menuFile.add_command(label="配置",command=ope_config)
menuFile.add_command(label="打开一言保存文件",command=ope)
menuFile.add_command(label="清空一言保存文件",command=clean_hitokoto)
menuFile.add_command(label="自定义源",command=zdy)
menuFile.add_separator()  # 分割线
menuFile.add_command(label="退出",command=root.destroy)

menuEdit = tk.Menu(mainmenu)  # 菜单分组 menuEdit
mainmenu.add_cascade(label="更多",menu=menuEdit)
menuEdit.add_command(label="帮助文档",command=ope_help_doc)
menuEdit.add_command(label="Github仓库",command=ope_github)
menuEdit.add_command(label="检查更新",command=jcgx)
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

rd2 = tk.Radiobutton(root,text="光环API",variable=var,value=1)
rd2.pack()

rd3 = tk.Radiobutton(root,text="韩小韩API",variable=var,value=2)
rd3.pack()

rd4 = tk.Radiobutton(root,text="ChatGPT(需自行提供API KEY)",variable=var,value=3)
rd4.pack()

rd5 = tk.Radiobutton(root,text="DeepSeek(需自行提供API KEY)",variable=var,value=4)
rd5.pack()

with open('./config.yaml', 'r', encoding='utf-8') as f:
    result = yaml.load(f.read(), Loader=yaml.FullLoader)
language_status_auto=result['language']
if language_status_auto==1:
    conf = ConfigParser()
    conf.read('./language/english.ini')
    logo.configure(text=conf['nr']['logo'])
    run.configure(text=conf['nr']['run'])
    xz.configure(text=conf['nr']['xz'])
    


auto_update()

root.mainloop()

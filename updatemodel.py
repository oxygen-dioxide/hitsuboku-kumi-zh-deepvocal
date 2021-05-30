import os
import sys
import json
import time

def skreadvalue(file):
    return ord(file.read(1))+ord(file.read(1))*256+ord(file.read(1))*256*256+ord(file.read(1))*256*256*256

def skreadstring(file):
    return str(file.read(skreadvalue(file)),"utf-8")


filename = os.path.split(os.path.abspath(sys.argv[0]))[0]+"\kumi.dvtb"
file=open(filename,"rb")
file.read(27)
#读字典
for i in range(0,6):
    skreadstring(file)
skreadvalue(file)
#读dvcfg
dvcfgs={}
for i in range(0,skreadvalue(file)):
    wavpath=skreadstring(file)
#    try:
    dvcfgfile=open(wavpath+"\\voice.dvcfg")
    dvcfg=eval(dvcfgfile.read())
    for i in dvcfg.keys():
        a=dvcfg[i]
        wavname=wavpath+"\\"+a["wavName"]
        dvcfgupdatetime=time.mktime(time.strptime(a["updateTime"],"%Y-%m-%d %H:%M:%S"))
        wavupdatetime=os.path.getmtime(wavname)
        dvcfg[i]=max(dvcfgupdatetime,wavupdatetime)
    dvcfgfile.close()
#    except:
#        dvcfg={}
    dvcfgs.update(dvcfg)
#读dvmodel目录
deletelist=[]
file.read(5)
modelpath=skreadstring(file)
print("dvmodel目录："+modelpath+"\n")
for i in os.listdir(modelpath):
    sp=i.split('.')
    if(len(sp)>=3 and sp[2]=="DVModel"):
        pitch=sp[0]
        name=sp[1].replace("uppercase","")
        modelupdatetime=os.path.getmtime(modelpath+'\\'+i)
        key=pitch+"->"+name
        if((key in dvcfgs) and (modelupdatetime<dvcfgs[pitch+"->"+name])):
            print(modelpath+'\\'+i)
            deletelist+=[modelpath+'\\'+i]
file.close()
input("即将删除上述文件，是否继续?")
for i in deletelist:
    os.remove(i)
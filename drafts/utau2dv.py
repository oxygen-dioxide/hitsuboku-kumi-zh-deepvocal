#2019/7/17 v1.0
#2019/7/20 v1.1 修复有时候程序无法正常结束，导致dvcfg不完整的bug
import os
import sys
import time

print("utau2dv音源转换器 定制for kumi by oxygendioxide")

#载入dv字典文件
#载入拆音字典文件
temp=open("Symbol list.txt").read().split('\n')
cvvcdict=set()
for i in temp:
    if(i!=''):
        cvvcdict.add(i.split(',')[0])

#载入辅音列表
consonants=set(open("Unvoiced Consonant list.txt").read().split('\n')+open("Voiced Consonant list.txt").read().split('\n'))
consonants.discard('')
#载入元音列表
temp=open("Vowel list.txt").read().split('\n')
vowels=set()
for i in temp:
    if(i!=''):
        vowels.add(i.split(',')[0])

#载入尾音列表
tails=set(open("Tail symbol list.txt").read().split('\n')+['-'])
tails.discard('')

pitches=["A3","D4","A4","D5"]
#载入oto.ini
#oto.ini格式：[文件名]=[别名],[左边界],[固定范围],[右边界],[先行声音],[重叠]
#oto词典的结构：{[别名]:[文件名],[左边界],[固定范围],[右边界],[先行声音],[重叠]}
#时间单位：毫秒
#左边界从wav开头算起，固定范围、先行声音、重叠从左边界算起，右边界从左边界算起,为负数。
otos={}
for pitch in pitches:
    temp=open("oto_{}.ini".format(pitch)).read().split('\n')
    oto={}
    for i in temp:
        i=i.replace('=',',').split(',')
        if len(i)>=7:
            i={i[1]:(i[0],float(i[2]),float(i[3]),float(i[4]),float(i[5]),float(i[6]))}
            oto.update(i)
    otos[pitch]=oto

#写入dvcfg
t=time.gmtime()
t="{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour,t.tm_min,t.tm_sec)

dvcfg=open("voice.dvcfg","w")
dvcfg.write("{\n")
"""
#VC
#connectPoint一定是0.05999999865889549
#endTime:EP
#startTime:SP-0.06
#tailPoint:EP-SP
for pitch in pitches:
    oto=otos[pitch]
    for vowel in vowels:
        if((vowel+' yu')in oto.keys()):
            wavoto=oto[vowel+' yu']
            dvcfg.write(',\n')
            dvcfg.write('   "{}->{}_{}" : '.format(pitch,vowel,"yw")+'{\n')
            dvcfg.write('      "connectPoint" : 0.05999999865889549,\n')
            dvcfg.write('      "endTime" : {:.16f},\n'.format(wavoto[1]/1000-wavoto[3]/1000))
            dvcfg.write('      "pitch" : "{}",\n'.format(pitch))
            dvcfg.write('      "srcType" : "VX",\n')
            dvcfg.write('      "startTime" : {:.16f},\n'.format(wavoto[1]/1000+wavoto[5]/1000-0.06))
            dvcfg.write('      "symbol" : "{}_{}",\n'.format(vowel,"yw"))
            dvcfg.write('      "tailPoint" : {:.16f},\n'.format(wavoto[4]/1000-wavoto[5]/1000+0.06))
            dvcfg.write('      "updateTime" : "{}",\n'.format(t))
            dvcfg.write('      "wavName" : "{}"\n'.format(wavoto[0]))
            dvcfg.write("   }")
        else:
            print(vowel+' yu'+'缺失')
"""


#VT
idict={i:i for i in vowels}
idict.update(
    {"vn":"yuen",
    "in":"yin",
    "i0":"zi",
    "u":"wu",
    "v":"yu",
    "ing":"ying",
    "e0":"ye",
    "ir":"zhi",
    "en0":"yan",
    "ong":"yong",
    "i":"yi",})
for pitch in pitches:
    oto=otos[pitch]
    for vowel in idict:
        vowelo=idict[vowel]
        if((vowelo+'1 -')in oto.keys()):
            wavoto=oto[vowelo+'1 -']
            dvcfg.write(',\n')
            dvcfg.write('   "{}->{}_{}" : '.format(pitch,vowel,"R")+'{\n')
            dvcfg.write('      "connectPoint" : 0.05999999865889549,\n')
            dvcfg.write('      "endTime" : {:.16f},\n'.format(wavoto[1]/1000-wavoto[3]/1000))
            dvcfg.write('      "pitch" : "{}",\n'.format(pitch))
            dvcfg.write('      "srcType" : "VX",\n')
            dvcfg.write('      "startTime" : {:.16f},\n'.format(wavoto[1]/1000+wavoto[5]/1000-0.06))
            dvcfg.write('      "symbol" : "{}_{}",\n'.format(vowel,"R"))
            dvcfg.write('      "tailPoint" : {:.16f},\n'.format(-wavoto[3]/1000-wavoto[5]/1000))
            dvcfg.write('      "updateTime" : "{}",\n'.format(t))
            dvcfg.write('      "wavName" : "{}"\n'.format(wavoto[0]))
            dvcfg.write("   }")
        else:
            print(vowelo+'1 -'+'缺失')

#V-
"""
for vowel in vowels:
    if(("_"+vowel+' L')in oto.keys()):
        wavoto=oto[vowel+' '+consonant]
        dvcfg.write(',\n')
        dvcfg.write('   "{}->{}_{}" : '.format(pitch,vowel,consonant)+'{\n')
        dvcfg.write('      "connectPoint" : 0.05999999865889549,\n')
        dvcfg.write('      "endTime" : {:.16f},\n'.format(wavoto[1]/1000-wavoto[3]/1000))
        dvcfg.write('      "pitch" : "{}",\n'.format(pitch))
        dvcfg.write('      "srcType" : "VX",\n')
        dvcfg.write('      "startTime" : {:.16f},\n'.format(wavoto[1]/1000+wavoto[5]/1000-0.06))
        dvcfg.write('      "symbol" : "{}_{}",\n'.format(vowel,consonant))
        dvcfg.write('      "tailPoint" : {:.16f},\n'.format(-wavoto[3]/1000-wavoto[5]/1000))
        dvcfg.write('      "updateTime" : "{}",\n'.format(t))
        dvcfg.write('      "wavName" : "{}"\n'.format(wavoto[0]))
        dvcfg.write("   }")
    else:
        print("_"+vowel+' L缺失')
"""

dvcfg.write("\n}")
dvcfg.close()
input("转换完成")

A3=open("oto_A3.ini","w")
A4=open("oto_A4.ini","w")
D5=open("oto_D5.ini","w")
for i in open("oto.ini").readlines():
    if("_A3" in i):
        A3.write(i.replace("_A3",""))
    elif("_A4" in i):
        A4.write(i.replace("_A4",""))
    elif("_D5" in i):
        D5.write(i.replace("_D5",""))
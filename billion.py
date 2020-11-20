#exception : ten, eleven, twelve, thirteen, fifteen
#teen
#ty
#special case : depan ada 2,3,5

kata=['','one','two','three','four','five','six','seven','eight','nine']

def num(n:int):
    if n<10 :
        return kata[n]
    elif n>=1_000_000_000:
        return num(n//1_000_000_000)+' billion '+num(n%1_000_000_000)
    elif n>=1_000_000:
        return num(n//1_000_000)+' million ' + num(n%1_000_000)
    elif n>=1_000:
        return num(n//1000) + ' thousand ' + num(n%1000)
    elif n>=100:
        return num(n//100)+ ' hundred ' + num(n%100)
    elif n>=20:
        if n//10 == 2:
            return 'twenty ' + num(n%10)
        elif n//10 == 3:
            return 'thirty ' + num(n%10)
        elif n//10 == 5:
            return 'fifty ' + num(n%10)
        else :
            return num(n//10)+('ty 'if (n//10)!=8 else 'y ') + num(n%10)
    else :
        if n==10:
            return 'ten'
        elif n==11:
            return 'eleven'
        elif n==12:
            return 'twelve'
        elif n==13:
            return 'thirteen'
        elif n==15:
            return 'fifteen'
        else :
            return num(n%10) + 'teen'
        

import os
while True:
    os.system('cls')
    print("        WELCOME to TANAMAN'S ENGLISH CONVERTER        ")
    print("======================================================")
    try:
        bil=int(input("Number\t? "))
        print(f"{bil:,} = {num(bil)}")
    except:
        print("Numbers only la bro aiyah")
    print()
    print("Want to Convert Again [y/n] ? ",end='')
    again=input()
    print()
    if again.lower() == 'n' :
        print("Thank You for Choosing TANAMAN!!! SEE YOU NEXT TIME ^^")
        break
    

        
    

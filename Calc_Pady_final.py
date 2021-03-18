def add(x,y): #Συνάρτηση Πρόσθεσης
    return x+y

def sub(x,y): #Συνάρτηση αφαίρεσης
    return(x-y)

def mul(x,y): #Συνάρτηση Πολλαπλασιασμού
    return(x*y)

def div(x,y): #Συνάρτηση διαίρεσης
    if y!=0:
        zero_flag=1
    else: 
        zero_flag=0

    while not zero_flag:       # ΌΣΟ ΕΙΝΑΙ FALSE=0
        y=float(input("Den ginetai diairesi me diaireti 0. Parakalw dwse allo diaireti."))
        if y!=0:
            zero_flag=1
           
    # y=float(y)    δεν χρειάζεται αυτό     
    return(x/y)

def calculator(): #main συνάρτηση
    choice=input('''Parakalw dialekse tin praksi pou thes na kaneis.\
                  An theleis prosthesi grapse'add',afairesi 'sub',\
                  pollaplasiasmo 'mul' kai gia diairesi'div :''')

    while True:
        try:
            a = float(input("Δώστε μας τον πρώτο αριθμό: "))
        except ValueError:
            print("No valid float! Please try again ...")
            continue
        else:
            break
    while True:
        try:
            b = float(input("Δώστε μας τo δεύτερο αριθμό: "))
        except ValueError:
            print("No valid float! Please try again ...")
            continue
        else:
            break
    
    if choice=="add":
        apotelesma=add(a,b)
    elif choice=="div":
        apotelesma=div(a,b)
    elif choice=="mul":
        apotelesma=mul(a,b)
    else:
        apotelesma=div(a,b)

    print("To apotelesma tis praksis %s einai: %.2f" %(choice,apotelesma))

if __name__=='__calculator()__':
    calculator()

calculator()    

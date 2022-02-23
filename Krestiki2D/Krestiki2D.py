# сделать двумерный массив
print ("Возврат хода - буква R")
setka=int(input('введи размер желаемого поля: '))
fulldlina=len(str(setka**2))
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False 
     
def vvod_XO(bukva_,n):
    x=input('следующий ход игрока' + ' '+ bukva_ +', выберите номер: ')

    if x.upper()=='R' :
        if  len(arraysteps)!=0:
            stepp=arraysteps[len(arraysteps)-1]# последний ход
            arraysetka[stepp-1]=stepp
            arraysteps.pop(len(arraysteps)-1)
    if is_integer(x) :
        x=int(x)
        try:
            if not(x<=n**2 and x>0 ):
                raise BaseException("введи допустимое значение")
            if not(x in arraysetka):
                raise BaseException("поле занято")
            arraysetka[x-1]=bukva_
            arraysteps.append(x)
        except BaseException as ve:
          print(ve)
          vvod_XO(bukva_,n)    
        

def ResearchOfSize(current_element):    
    global fulldlina
    dlina=len(str(current_element))
    return fulldlina-dlina


def vuvod_stroka(setka_,k): 
    stroka='|'
    maxlensymbol=len(str(setka_**2))
    for i in range(k,k+setka_):
        stroka+=str(arraysetka[i])
        stroka+=' '*ResearchOfSize(arraysetka[i])
        stroka+='|'
    return stroka

def ToConsoleArray(setka_):    
    t=0
    for i in range(setka_):
        stroka='|'
        for k in range(setka_):
            stroka+=str(arraysetka[i][k]) +' '*ResearchOfSize(arraysetka[i][k])
            stroka+='|'
        print(stroka)

def askwin(win_combinations):   
    for i in range(len(win_combinations)-1):
        if win_combinations[i]!=win_combinations[i+1]:
            return False
    return True

def win(n):
    k=0
    Temp=True
    # проверка по строкам
    for mass_stroka in arraysetka:
        for i in range(len(mass_stroka)-1):
            if mass_stroka[i]!=mass_stroka[i+1]:
               Temp=False
            else:
                Temp=True  
    if Temp:
        return True
        # проверка по столбцам
    k=0
    Temp=True
    for i in range(n-1):
        if arraysetka[i][k]!=arraysetka[i+1][k]:
            Temp=False
        else:
            Temp=True
        k+=1
    if Temp:
        return True
     # проверка по диагоналям
    k=0
    for i in range(n-1):
        if arraysetka[i][k]!=arraysetka[i+1][k+1]:
                Temp=False
        else:
            Temp=True
        k+=1
    if Temp:
        return True
    Temp=True
    k=n-1
    for i in range(n-1):
        if arraysetka[i][k]!=arraysetka[i+1][k-1]:
            Temp=False
        else:
            Temp=True
        k+=1
    if Temp:
        return True
    return False

def GetSymbol():    
   return words[len(arraysteps)%2] 
    

arraysetka=[]
arraysteps=[]
current=1
for i in range(setka):
    mass=[]
    for k in range(setka):
        mass.append(current)
        current+=1
    arraysetka.append(mass)
ToConsoleArray(setka)
words = ("X", "O")
while True:
    vvod_XO(GetSymbol(),setka)
    ToConsoleArray(setka)    
    if win(setka):
       print('Win!')
       break

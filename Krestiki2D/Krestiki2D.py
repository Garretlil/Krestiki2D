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
massive=[] 
current2=1
def vvod_XO(bukva_,n):
    x=input('следующий ход игрока' + ' '+ bukva_ +', выберите номер: ')
    
    if x.upper()=='R' :
        if  len(arraysteps)!=0:
            stepp=arraysteps[len(arraysteps)-1]# последний ход
            current2=1
            for i in range(setka):
                mass=[]
                for k in range(setka):
                    mass.append(current2)
                    if massive[i][k]==stepp:
                        arraysetka[i][k]=stepp
                        break
                    current2+=1
                massive.append(mass)
            arraysteps.pop(len(arraysteps)-1)
     # готово
    if is_integer(x) :
        x=int(x)
        try:
            if not(x<=n**2 and x>0 ):
                raise BaseException("введи допустимое значение")
            
            if x in arraysteps:
                raise BaseException("поле занято")            
            current=1
            for i in range(setka):
                for k in range(setka):
                    if x==current:
                        arraysetka[i][k]=bukva_
                    current+=1
                      
            arraysteps.append(x)
        except BaseException as ve:
          print(ve)
          vvod_XO(bukva_,n)    
        

def ResearchOfSize(current_element):    
    global fulldlina
    dlina=len(str(current_element))
    return fulldlina-dlina

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

def win(setka_):

    # проверка по строкам  
    # проверка по столбцам
 
    Astolbec=[]
    Astroka=[]
    ADiagDown=[]
    ADiagUp=[]
    for i in range(setka_):
       Astolbec.clear()
       Astroka.clear()
       for j in range(setka_):
             Astolbec.append(arraysetka[j][i])
             Astroka.append(arraysetka[i][j])
       ADiagUp.append(arraysetka[i][j-i])      
       ADiagDown.append(arraysetka[i][i])
       if askwin(Astolbec) or askwin(Astroka): return True
    if askwin(ADiagDown) or askwin(ADiagUp): return True
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

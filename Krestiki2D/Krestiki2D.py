# сделать двумерный массив
print ("Возврат хода - буква R")
setka=int(input('введи размер желаемого поля: '))
fulldlina=2*len(str(setka))+1
 
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False 
massive=[] 
current2=1
def vvod_XO(bukva_,setka_):
    temp=input('следующий ход игрока' + bukva_+'  , выберите номер в формате [*,*]: ')
    if len(temp)==1:
        x=temp
        if x.upper()=='R' :
            if  len(arraysteps)!=0:
                stepp=arraysteps[len(arraysteps)-1]# последний ход
                arraysetka[stepp[0]][stepp[1]]=""
                arraysteps.pop(len(arraysteps)-1)
    else: 
        x,y = map(str, temp.split(" "))
        # готово
        if is_integer(x) :
            x=int(x)
            y=int(y)
            try:
   
                if  (y>setka-1 and y<0 ) or (x>setka-1 and x>0 ):
                    raise BaseException("введи допустимое значение")
            
                #if not is_integer(arraysetka[x][y]):
                #    raise BaseException("поле занято")            
            
                arraysetka[x][y]=bukva_                      
                arraysteps.append([x,y])
            except BaseException as ve:
              print(ve)
              vvod_XO(bukva_,setka_)    
        

def ResearchOfSize(x,y,z):    
    global fulldlina
    dlina=len(str(x)+str(y))
    return fulldlina-dlina-z

def ToConsoleArray(setka_):    
    t=0
    for i in range(setka_):
        stroka='|'
        for k in range(setka_):
            if arraysetka[i][k]!="":
               stroka+=arraysetka[i][k] + " "*ResearchOfSize(i,k,0)
            else:
               stroka+=str(i)+","+str(k) + " "*ResearchOfSize(i,k,1)
            stroka+='|'
        print(stroka)

def askwin(win_combinations):   
    for i in range(len(win_combinations)-1):
        if win_combinations[i]!=win_combinations[i+1] or win_combinations[i]=="" or win_combinations[i+1]=="": 
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
        mass.append("")
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

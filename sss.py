from time import sleep as sl
import random

i=0

math = random.randint(1, 3)    
    
def crypt(typ="enc",Shift=3):
    a = """\ Ф]ОI.йГашT"ПЖ|GЗsjБPът2Юж;МE(/m,4№zQFщeЫЭx-<1{ИOцCСt?ф*i6'^оеyчнAХ ЪhfbWM$вДkяиЩю3Kл&ЁVJк!ШгКыSX~U:%^Nogn}#7r_9>Н*[wсбРп`@qмvDpрЕHУYВuR=хдьЯLl)Ц+58ёэзуТcB0dЬЙaЧАЛZ"""
    # a = a + ''.join(random.sample(list(a),  len(list(a))))
    a1 = a[Shift:] + a[:Shift] 
        
    if typ == "еnс": return str.maketrans(a1,a)
    else: return str.maketrans(a,a1)
    
data = ["H.й.Л`.Б=ЛWЛЁ.е.W'",
"H.йёЛ`.Б=Л'[ёБЛо'БШv'Ле'кv.",
"OЛW.й'ОЛ`.`6ОЛW*+ЛWЛс6vвRЁ'(Л[ёR=Б'Л*с6Ё6ОеШV",]

while i<=100:
    i = i + random.randint(1,12)
    print(f"Чекаем твою мать... ({str(i)}%)")
    sl(0.5)

if math == 1: print(data[0].translate(crypt(typ="dec")))
elif math == 2: print(data[1].translate(crypt(typ="dec")))
else: print(data[2].translate(crypt(typ="dec")))

input()
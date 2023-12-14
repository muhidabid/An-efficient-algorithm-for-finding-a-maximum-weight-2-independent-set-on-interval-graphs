import random
from random import randrange
import pandas as pd

should_continue_for_a=True
should_continue_for_b=True

checking_a=[]
checking_b=[]
checking_duplicate=[]
checking_w=[]
final_list=[]
list_i = []

for i in range (1,6501):
    temp={}
    temp['c']=i
    list_i.append(i)
    number1=0
    number2=0
    
    while should_continue_for_a:
        number1=random.uniform(1, 10000)
        if number1 not in checking_duplicate:
            checking_a.append(number1)
            checking_duplicate.append(number1)
            temp['a']=number1
            should_continue_for_a=False


    while should_continue_for_b:
        number2=random.uniform(number1,20000)
        if number2 not in checking_duplicate:
            checking_b.append(number2)
            checking_duplicate.append(number2)
            temp['b']=number2
            should_continue_for_b=False

    weight=randrange(20)
    checking_w.append(weight)
    temp['w']=weight

    should_continue_for_a=True
    should_continue_for_b=True
    final_list.append(temp)

print(final_list)
dict = {'i': list_i, 'a': checking_a, 'b': checking_b,'w':checking_w}
df = pd.DataFrame(dict)
df.to_csv('large_6500.csv', index=False)
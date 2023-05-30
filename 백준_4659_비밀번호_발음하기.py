import sys
import re

vowel = ['a','e','i','o','u'] #모음
# consonant =
word = []
while True :
    w = str(sys.stdin.readline()) 
    w = w.rstrip()
    if w == 'end' : break
    word.append(w) 

for password in word : 
    ifv = False
    v = 0
    c = 0
    temp = None

    for p in password :
        
        if p == temp : #연속해 두 번 왔는지 검사
            if not(p == 'e' or p =='o') :
                ifv = False
                break
        
        if p in vowel : 
            v +=1
            c = 0
            ifv = True
        else : 
            c +=1
            v = 0
        
        if v==3 or c==3 : #모음 혹은 자음이 3개 연속으로 오면
            ifv = False
            break

        temp = p



    if ifv :
        print(f'<{password}> is acceptable.')
    else : 
       print(f'<{password}> is not acceptable.') 
    
    
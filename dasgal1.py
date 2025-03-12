number=input("onoonii ehleliin too boloh bvhel too=")
for num in number: #жагсаалтын тоонуудыг давтах
    if num <100:
        bonus_point +=5 #100-с бага бол 5 оноо нэмнэ
    elif 100<=num <=1000:
        bonus_point += num *0.2
    else:
        bonus_point += num *0.1
print(bonus_point)

# 별찍기

for i in range(0, 5):
    star = ''
    for j in range(0, i+1):
        star = star + '*'
    print(star)
    
    
    
for i in range(5, 0, -1):
    star = ''
    for j in range(0, i):
        star = star + '*'
    print(star)

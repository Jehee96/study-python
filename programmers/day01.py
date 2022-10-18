# 두 수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/120802
def s120802(num1, num2):
    return num1 + num2

print(s120802(2, 3)) # 5
print(s120802(100, 2)) # 102

# 두 수의 차
# https://school.programmers.co.kr/learn/courses/30/lessons/120803
def s120803(num1, num2):
    return num1 - num2

print(s120803(2, 3)) # -1
print(s120803(100, 2)) # 98

# 두 수의 곱
# https://school.programmers.co.kr/learn/courses/30/lessons/120804
def s120804(num1, num2):
    return num1 * num2

print(s120804(3, 4)) # 12
print(s120804(27, 19)) # 513

# 몫 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120805
def s120805(num1, num2):
    return num1 // num2

print(s120805(10, 5)) # 2
print(s120805(7, 2))  # 3

# 두 수의 나눗셈
# https://school.programmers.co.kr/learn/courses/30/lessons/120806
def s120806(num1, num2):
    return int(num1 * 1000 / num2)

print(s120806(3, 2)) # 1500
print(s120806(7, 3)) # 2333
print(s120806(1, 16)) # 62

# 숫자 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120807
def s120807(num1, num2):
    answer = 1
    if num1 != num2:
        answer = -1
    return answer

print(s120807(2, 3)) # -1
print(s120807(11, 11)) # 1
print(s120807(7, 99)) # -1

# 분수의 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/120808
def s120808(denum1, num1, denum2, num2):
    val1, val2 = (denum1 * num2) + (denum2 * num1), num1 * num2
    tmp1, tmp2 = val1, val2
    
    while (tmp1 > 0):
        tmp1, tmp2 = tmp2 % tmp1, tmp1
    
    gcd = tmp2
    #     math.gcd(val1, val2)
    
    return [int(val1 / gcd), int(val2 / gcd)]
    #      [val1//gcd, val2//gcd]

print(s120808(1, 2, 3, 4)) # [5, 4]
print(s120808(9, 2, 1, 3)) # [29, 6]
    
# 배열 두배 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120809
def s120809(numbers):
    for i, v in enumerate(numbers):
        numbers[i] = numbers[i] * 2
    return numbers
    #      [num*2 for num in numbers]

print(s120809([1, 2, 3, 4, 5]))           # [2, 4, 6, 8, 10]
print(s120809([1, 2, 100, -99, 1, 2, 3])) # [2, 4, 200, -198, 2, 4, 6]

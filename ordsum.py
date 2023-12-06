def solution(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1) #The length of num1/num2 represented in 10's place, 100's place, etc.
    for i in num1:
        #Find the number in each "digit" place for num1:
        n1 += (ord(i) - ord("0")) * m1 
        m1 = m1//10
    for i in num2:
        #Find the number in each "digit" place for num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2//10
    return str(n1 + n2)

num1 = '555'
num2 = '999'
print(solution(num1, num2))

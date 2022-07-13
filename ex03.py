#type() => 자료형 리턴

#참이나 거짓을 나타내는 true, false 두 상수를 갖는다.
a = 1
b = a < 10
print(b,type(b))

#True->1, False->0
a = True + False
print(a, type(a))

print(1 == True)
print(0 == True)
print(0 == False)

#특이한 케이스
b1 = True #1
b2 = False #0

print(b1 + 10)
print(b2 + 10)
print(True + True)
print(True - 2)
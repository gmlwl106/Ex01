#대입문
a = 1
b = a + 1
print(a, b)

#대입문 오류
#1 + 3 = a

#세미콜론으로 구분
e = 3.5; f = 5.3
print(e, f)

#여러 변수를 한번에 대입
g,h = 3.5,5.3
print(g,h)

#여러 개를 같은 값으로 대입
x=y=z=10
print(x,y,z)

#값 교환하기
e,f=f,e
print(e,f)

#오류
#a = (b = c+d)

#변수에 새로운 값이 할당되면 기존의 값을 잃어버리고 새로운 값으로 치환된다.
a = 1
print(type(a))
a = 'hello'
print(type(a))

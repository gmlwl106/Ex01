#정수형

a = 101
print(a, type(a))
print(isinstance(a, int))

#2진수 8진수 16진수 표현 가능
b = 0b010 #2진수
c = 0o101 #8진수
d = 0x101 #16진수
print(b,c, d)

#10진수 -> 2진수, 8진수, 16진수
print(bin(5))
print(oct(65))
print(hex(257))
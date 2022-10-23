a = float(input('Введіть значення a:'))
b = float(input('Введіть значення b:'))
c = float(input('Введіть значення c:'))
sqrt = b**2 - 4*a*c
print('Дискримінант =',sqrt)
x1 = ((- b + sqrt**0.5)/2*a)
x2 = ((- b - sqrt**0.5)/2*a)
print(x1,x2)

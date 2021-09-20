
alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alpha=list(alpha)
s=int(input("Введите число: 1-шифровка, 0-расшифровка: "))
c=input("Введите строку: ")
n=int(input("Число - кол-во сдвигов: "))
c=list(c)
c_len=len(c)
l=33
res=''
res_1=''
if s == 1:
    for k in range(0, c_len):
        for i in range(0, len(alpha)):
            if c[k]==alpha[i]:
                res+=(alpha[(i+n)%l])
   
else:
    for k in range(0, c_len):
        for i in range(0, len(alpha)):
            if c[k]==alpha[i]:
                res+=(alpha[(i-n)%l])
print(res)
        




    
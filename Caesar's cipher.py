alpha = list( 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
space=list(' ')
res=''
check=''
while True: #проверка, что вводится число
    n=input("Число - кол-во сдвигов: ")
    try:
        val=int(n)
        break
    except ValueError:
        print("Введено некорректное число! Попробуйте еще раз ")
n=int(n)
while True: #проверка фразы на наличие неправильных символов
    phrase=input("Введите строку: ")
    phrase=list(phrase)
    ph_len=len(phrase)
    union=list(set(alpha+space)) #объединение элементов из алфавита и пробела
    check=list(set(phrase)-set(union))
    if check == list(''):
       for k in range(0, ph_len): 
             if phrase[k] == ' ':
                 res+=' '
             for i in range(0, len(alpha)):
                if phrase[k]==alpha[i]:
                  res+=alpha[(i+n)%33]
       print(res)
       break     
    else:
        print("Введена некоректная строка! Попробуйте еще раз")







    
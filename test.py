import os    #модуль os обеспечивает взаимодействие с операционной системой

sayt = input()

if 'https://' in sayt:          #оператор in - если заданные данные присутствуют в sayt, действие выполняется  
    os.system('start ' + sayt)  #метод system
    print('if')
elif 'www.' in sayt:
    sayt = 'https://' + sayt
    os.system('start ' + sayt)
    print('elif')
else:
    sayt = 'https://www.' + sayt
    os.system('start ' + sayt)
    print('else')


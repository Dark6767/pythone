import warnings

def Addition(value_one,value_two):
    return value_one+value_two
def subtraction(value_one,value_two):
    return value_one-value_two
def multiplication(value_one,value_two):
    return value_one*value_two
def division(value_one,value_two):
    if value_two==0:
        return warnings.warn('Деление на ноль запрещено в данной рельности')
    return value_one/value_two
def exponentiation(value_one,value_two):
    if value_two<0 and value_one==0:
        return warnings.warn('Деление на ноль запрещено в данной рельности')
    return value_one**value_two

a=int(input('Введите первое значение'))
b=int(input('Введите второе значение'))
print('сложение',Addition(a,b))
print('вычитание',subtraction(a,b))
print('деление',division(a,b))
print('возведение в степень',exponentiation(a,b))
print('умножение',multiplication(a,b))

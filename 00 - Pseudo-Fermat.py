import time

input('Демонстрируем соотношение наподобие теоремы Ферма -> Enter!')

s = chr(8308)
e = '\n'

a, b, c, d = 2682440, 15365639, 18796760, 20615673
print(e)
print(str(a)+s+' + '+str(b)+s+' + '+str(c)+s+' =', a**4+b**4+c**4, '=? '+str(d)+s)
print('Считаем -------------> '+str(d)+s+' =', d**4)
print(e)
print('Компьютер проверяет равенство: ' + str(a)+s+' + '+str(b)+s+' + '+str(c)+s+' = '+str(d)+s)
print('Результат:', a**4+b**4+c**4 == d**4)
print(e)
print('Насладитесь, а мы заканчиваем через 10 секунд!')
time.sleep(10)

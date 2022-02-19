#Простейший вариант проверки четности числа
#Плюсы: простой
#Минусы: не очень эффективен
def isEven(value):
	if (value % 2) == 0:
		return True
	return False

#Эффективный вариант проверки честности числа
#Плюсы: эффективный
#Минусы: нет
def isEven2(value):
	if (value & 1) == 0:
		return True
	return False

#Второй вариант (isEven2) быстрее первого, за счет использования бинарной операции "И". Битовые операции быстрее арифметических.
print(isEven(66))
print(isEven2(66))

print(isEven(65))
print(isEven2(65))
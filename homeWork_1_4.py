# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
summ = int(input("Введите кол-во журавликов: "))
# p = 0
# k = 0
# s = 0
num_1 = (summ // 3) * 2 // 4
num_2 = (summ // 3) * 2
num_3 = (summ // 3) * 2 // 4
print(num_1, num_2, num_3)

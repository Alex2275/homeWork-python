# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

P = int(input("Введите произведение чисел: "))
S = int(input("Введите сумму чисел: "))

for x in range(P + 1):
    if x * (S - x) == P:
        y = S - x
        print(x, y)
        break

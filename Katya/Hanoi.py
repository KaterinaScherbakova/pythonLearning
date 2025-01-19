# Вот код, который будет расписывать все шаги. В аргументах функции hanoi указывается три башни А, В, С и число.
# Если число равняется одному, то логично, что потребуется только один шаг перемещения.
# Если число оказывается не равным 1, то функция вызывает сама себя, но уменьшив число на один так как одна операция уже произошла и меняет местами башни,
# после чего печатает новый результат. После снова проверяет не равно ли 1, если нет, то цикл повторяется.
# перемещаем с первого диска на последний

def move(n, start, finish):
    if n <= 0:
        return
    temp = 6 - start - finish # Вспомогательный колышек, найденный через сумму номеров столбиков (1 столб + 2 + 3ий = 6)
    move(n - 1, start, temp) # переносим диск с первого стержня на временный
    print("Перенести диск", n, "со стержня", start, "на стержень", finish)
    move(n - 1, temp, finish) # с временного на целевой
move(3, 1, 3)

print("Testddd")
v = 2065
print(v)
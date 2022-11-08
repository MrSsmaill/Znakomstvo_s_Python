# Задан список чисел.
# Необходимо создать список, содержащий те его элементы, значения которых больше предыдущего.


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 66]


def res(src: list) -> list:
    result = []
    for i in range(1, len(src)):
        if src[i] > src[i - 1]:
            result.append(src[i])
    return result


print(res(src))

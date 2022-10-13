
# Функция формирующая консенсус-стороку
def DnaRows(data: list) -> str:
    '''

    В данной функции мы рассматриваем каждый элемент списка по отдельности.
    Определяем кол-во вхождений элемента в строке (Count).
    Если Count >= 1, добавляем элемент в consensus_str
    '''
    consensus_str = []

    for str_0 in data[0]:
        Count = str_0.count(str_0[0])
        if Count >= 1:
            consensus_str.append(str_0[0])


    for str_1 in data[1]:
        Count = str_1.count(str_1[0])
        if Count >= 1:
            consensus_str.append(str_1[0])


    for str_2 in data[2]:
        Count = str_2.count(str_2[0])
        if Count >= 1:
            consensus_str.append(str_2[0])


    for str_3 in data[3]:
        Count = str_3.count(str_3[0])
        if Count >= 1:
            consensus_str.append(str_3[0])


    result = consensus_str[0], consensus_str[1], consensus_str[2], consensus_str[3]
    return "".join(result)



if __name__ == '__main__':
    print(DnaRows(["ACTA", "CCTA", "TTCA", "AACA"]))




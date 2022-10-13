from random import choice, randint


#Класс, который производит быструю сортировку
def quicksort(data: list):
    if len(data) <= 1:
        return data
    else:
        sup_element = choice(data) # Произвольный выбор опорного элемента
    left = [n for n in data if n < sup_element] # Формируем левую часть
    equals = [sup_element] * data.count(sup_element) # Находим эквивалент
    right = [n for n in data if n > sup_element] # Формируем правую часть
    return quicksort(left) + equals + quicksort(right)



if __name__ == '__main__':
    print(quicksort([randint(0, 10**6) for _ in range(13, 26)]))

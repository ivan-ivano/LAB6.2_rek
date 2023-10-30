import random


def generate_list(b, k, i=0):
    if i >= k:
        return b
    else:
        b.append(random.randint(-40, 50))
        generate_list(b, k, i + 1)
    return b


def search_min_element_index(lst, min_index=-1, i=0):
    if i >= len(lst):
        return min_index
    else:
        if lst[i] % 2 == 0:
            if min_index < 0:
                min_index = i
            else:
                if lst[i] < lst[min_index]:
                    min_index = i
        return search_min_element_index(lst, min_index, i + 1)


def replace_elements(lst, n):
    lst[0], lst[n] = lst[n], lst[0]
    return lst


if __name__ == '__main__':
    n = int(input('Введіть кількість елементів списку: '))
    a = generate_list([], n)
    min_index = search_min_element_index(a)
    print(a)
    try:
        print('Найменший парний елемент:', a[min_index])
        print(replace_elements(a, min_index))
    except TypeError:
        print('Немає парних елементів')

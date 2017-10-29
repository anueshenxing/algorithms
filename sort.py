# coding=utf-8


def quick_sort(need_to_sort):
    greater = []
    less = []
    if len(need_to_sort) <= 1:
        return need_to_sort

    current_item = need_to_sort.pop()
    for element in need_to_sort:
        if element <= current_item:
            less.append(element)
        else:
            greater.append(element)
    return quick_sort(less) + [current_item] + quick_sort(greater)


if __name__ == '__main__':
    pass

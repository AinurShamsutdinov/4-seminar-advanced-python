#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

#params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
#print(params)


def key_params(**kwargs):
    res_dict = dict()
    for key, value in kwargs.items():
        if not isinstance(value, int) and not isinstance(value, float) and value is not None:
            res_dict[str(value)] = key
        else:
            res_dict[value] = key
    return res_dict


def print_table(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


res_dict = key_params(a=1, aa=None, b='hello', c=[1, 2, 3], d={}, jopa=3.4)
print_table(a=1, aa=None, b='hello', c=[1, 2, 3], d={}, jopa=3.4)
print(res_dict)

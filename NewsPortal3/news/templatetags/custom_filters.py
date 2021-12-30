from django import template

register = template.Library()

# заменяет слова "жесть", "афигенно", "круто" на слово "здорово" (для рабочего примера: первая стать, 10 слово)
@register.filter(name='Censor')
def Censor(value, arg):
    value = value.replace("чувак", "ПАРЕНЬ")
    value = value.replace("шпора", "ШПАРГАЛКА")
    value = value.replace("офигенно", "ЗДОРОВО")
    return value


@register.filter(name='Censor1')
def Censor1(value, arg):  # первый аргумент здесь это то значение, к которому надо применить фильтр,
    # второй аргумент — это аргумент фильтра, т. е. примерно следующее будет в шаблоне value|multiply:arg
    if ("чувак" in value) or ("шпора" in value) or ("офигенно" in value):
        arg = 'ВНИМАНИЕ! В тексте используется нежелательная лексика, применена цензура (замена слов)'
        return arg   # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон
    else:
        return value
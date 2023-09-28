from django import template

register = template.Library()


@register.filter(name='cut')
def remove_chars(value, arg):
    print("Arg", arg)
    print("Value:", value)
    for character in arg:
        print(character)
        value = value.replace(character, "")
    return value

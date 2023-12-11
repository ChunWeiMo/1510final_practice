def foo(a: int, b: int) -> int:
    return a + b


def main():
    print(foo(4.5, 'a'))


if __name__ == "__main__":
    # main()
    my_fruity_tuple = ("apple", "banana", "cherry")
    my_fruity_iterator_object = iter(my_fruity_tuple)
    print(my_fruity_iterator_object)
    print(next(my_fruity_iterator_object))
    print(next(my_fruity_iterator_object))
    print(next(my_fruity_iterator_object))

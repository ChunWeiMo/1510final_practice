def append_to(element, to=[]):
    to.append(element)
    return to


def main():
    my_list = append_to('python')
    print(my_list)
    my_other_list = append_to('is better than java')
    print(my_other_list)


if __name__ == "__main__":
    main()
    print(1/0 if False else 'bar')
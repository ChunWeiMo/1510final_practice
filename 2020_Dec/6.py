def do_something(l1: list, l2: list) -> list:
    result = []
    i1 = 0
    i2 = 0
    while i1 != len(l1) and i2 != len(l2):
        if l1[i1] <= l2[i2]:
            result.append(l1[i1])
            i1 += 1
        else:
            result.append(l2[i2])
            i2 += 1
    return result

def main():
    some_names = ['Amy', 'Bob', 'Chloe', 'David', 'Emerald']
    more_names = ['Jacky', 'Jae', 'James', 'Janelle', 'Jasmine', 'Jason']
    lots_of_names = do_something(more_names, some_names)
    print(lots_of_names)

if __name__ == '__main__':
    main()
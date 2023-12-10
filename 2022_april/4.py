def print_something(size):
    numbers = list(range(1,size+1))
    
    for number in numbers:
        pass
    
    for number  in numbers:
        print(number, end=' ')
        for other_number in numbers:
            print('\t' + str(number * other_number), end=' ')
        print()

print_something(4)
    
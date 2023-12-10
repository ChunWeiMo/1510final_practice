def sum_of_evens(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        if n % 2 == 0:
            print(n)
            return n + sum_of_evens(n-1)
        else:
            return sum_of_evens(n-1)
        
if __name__ == '__main__':
    print(sum_of_evens(7))
    print(sum_of_evens(10))

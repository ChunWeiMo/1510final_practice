def foo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return foo(n - 1) + foo(n - 2)
    
def main():
    for number in range(1, 6):
        print(foo(number))

if __name__ == "__main__":
    main()
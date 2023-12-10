def phi(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + phi(x, y - 1)
def main():
    print(phi(7, 5))
    
if __name__ == "__main__":
    main()
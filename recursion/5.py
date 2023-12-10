def mu(numlist):
    n = len(numlist)
    if n == 1:
        return numlist[0]
    else:
        temp = mu(numlist[0:n-1])
        if numlist[n-1] > temp:
            return numlist[n-1]
        else:
            return temp
def main():
    number_list = [8, 6, 7, 5, 3, 0, 9, 1, 4, 2]
    print(mu(number_list))

if __name__ == "__main__":
    main()
    
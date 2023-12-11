def f(x):
    x = 2 * x
    return x


def main():
    x = 1
    x = f(x + 1) + f(x + 2)
    print(x)


if __name__ == "__main__":
    main()

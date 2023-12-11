def get_login_name(first, last, id_number):
    set1 = first[0:3]
    set2 = last[0:3]
    set3 = id_number[-2:]
    login_name = f"{set2}{set1}{set3}"
    return login_name


def main():
    id = get_login_name("Cornelius", "Overlander", "A00123579")
    print(id)


if __name__ == "__main__":
    main()
    print(-4 % 1 == 0)
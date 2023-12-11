def generator(value):
    def calculator(candidate):
        return candidate % value == 0
    return calculator


def collection(count):
    return [generator(i + 1) for i in range(count)]


def main():
    some_numbers = {-5, -4, -3, -2, -1}
    some_functions = collection(3)
    results = {}
    for entry in some_numbers:
        print(f'entry: {entry}, {hash(entry)}')
        values = []
        for function in some_functions:
            values.append(function(entry))
        results[entry] = values
    print(results)


if __name__ == "__main__":
    main()

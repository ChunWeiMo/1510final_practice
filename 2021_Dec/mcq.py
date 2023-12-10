# myset = set([1, 2, 3], [1, 3, 2], [2, 3, 1], [3, 2, 1], [2, 1, 3], [3, 1, 2])
myset = set([1, 2, 3])
print(myset)

a = {1: "a", 2: 'n', 3: (3, 4, 5)}
myset = set(a.values())
print(myset)

global_variable = 'global_variable'


def outer(outer_parameter='outer_parameter'):
    local_variable_in_outer = 'local_variable_in_outer'
    global_variable = 'GLOBAL_VARIABLE'

    def inner():
        print(global_variable, outer_parameter, local_variable_in_outer)
    return inner()


def main():
    outer()
    print(global_variable)


if __name__ == "__main__":
    main()

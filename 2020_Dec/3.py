def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print('Move a disc from peg', from_peg, 'to peg', to_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)


def main():
    # Set up some initial values.
    number_of_discs = 2
    starting_peg = 1
    destination_peg = 3
    temp_peg = 2
    move_discs(number_of_discs, starting_peg, destination_peg, temp_peg)
    print('All the pegs are moved!')


if __name__ == "__main__":
    main()

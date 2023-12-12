def caesar(filename: str, shift: int):
    try:
        with open(filename) as file_object:
            file_str = file_object.read()
    except FileNotFoundError:
        print(f'File does not exist.')
    else:
        shift_file_str = ''
        for character in file_str:
            shift_character = ord(character) + shift
            shift_file_str += chr(shift_character)
        with open(filename+'_shifted', 'w') as file_object:
            file_object.write(shift_file_str)
            
def main():
    caesar('caeser.txt', 1)
    

if __name__ == '__main__':
    main()

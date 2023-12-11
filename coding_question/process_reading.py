def process_readings(file_name):
    try:
        with open(file_name) as file_object:
            file = file_object.readlines()
    except FileNotFoundError:
        print(f'{file_name} does not exist.')
        print(f'Program stops')
    else:
        sum_of_integer = 0
        for integer in file:
            sum_of_integer += int(integer)
    
        with open(file_name, 'a') as file_object:
            file_object.write(str(sum_of_integer))
        
def main():
    process_readings('process_reading.txt')
    
if __name__ == '__main__':
    main()
        
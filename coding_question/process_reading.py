def process_readings(file_name):
    try:
        with open(file_name) as file_object:
            integer_list = file_object.readlines()
    except FileNotFoundError:
        print(f'{file_name} does not exist.')
    else:
        sum_of_integer = sum_of_integers(integer_list)
        with open(file_name, 'a') as file_object:
            file_object.write(str(sum_of_integer))
            
    
        
def sum_of_integers(integer_list):
    sum_of_integer = 0
    for integer in integer_list:
        sum_of_integer += int(integer)
    return sum_of_integer


def main():
    process_readings('process_reading.txt')
    
if __name__ == '__main__':
    main()
        
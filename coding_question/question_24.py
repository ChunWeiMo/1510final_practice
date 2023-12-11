def question_24():
    sum_of_multiples_of_3_or_5 = 0
    list_of_multiples_of_3_or_5 = []
    for number in range(1, 100):
        if number % 3 == 0 or number % 5 == 0:
            sum_of_multiples_of_3_or_5 += number
            list_of_multiples_of_3_or_5.append(number)
    print(list_of_multiples_of_3_or_5)
    return sum_of_multiples_of_3_or_5

def main():
    print(question_24())
    
if __name__ == '__main__':
    main()

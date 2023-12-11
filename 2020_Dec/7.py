def a_function():
    total = 0.0
    try:
        infile = open('sales_data.txt', 'r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
        print(format(total, ',.2f'))
    except IOError:
        print('An error occurred trying to read the file')
    except ValueError:
        print('Non-numeric data found in the file')
    except:
        print('An error occurred.')

def main():
    a_function()

if __name__ == "__main__":
    main()
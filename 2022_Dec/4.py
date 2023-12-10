def main():
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    weekend = enumerate(days)[5:]
    print(type(weekend))
    for day in weekend:
        print(day[0], day[1])

if __name__ == "__main__":
    main()
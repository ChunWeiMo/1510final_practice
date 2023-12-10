def make_priority_queue():
    queue = []
    
    def enequeue(new_value, pop):
        print(queue)
        queue.append(new_value)
        queue.sort()
        if pop:
            return queue.pop(0)
        else:
            return queue[0]
    return enequeue

def main():
    test_queue = make_priority_queue()
    print(test_queue("Juan", False))
    print(test_queue("Jack", True))
    print(test_queue("Joe", True))
    print(test_queue("Jesper", False))
    print(test_queue("Jerry", True))
    print(test_queue("Josh", True))
    
if __name__ == "__main__":
    main()
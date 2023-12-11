def observe_birds(observations_file):
    birds_observed = set()
    for line in observations_file:
        bird = line.strip()
        birds_observed.add(bird)
    return birds_observed


def main():
    with open('observations.txt') as observations_file:
        print(observe_birds(observations_file))


if __name__ == '__main__':
    main()

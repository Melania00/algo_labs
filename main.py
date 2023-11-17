from beers import Beer


def main():
    employees = {
        1: [1],
        2: [1, 4],
        3: [1],
        4: [1, 2, 4],
        5: [1, 2],
        6: [2],
        7: [1, 2, 3],
        8: [2, 3, 4],
        9: [3, 4],
        10: [3, 4]
    }

    beer_manager = Beer(employees)
    beer_manager.run_algorithm()


if __name__ == "__main__":
    main()

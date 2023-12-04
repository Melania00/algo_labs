class Beer:
    def __init__(self, employees):
        self.employees = employees
        self.popular_beer = None

    def find_popular_beer(self):
        beer_count = {1: 0, 2: 0, 3: 0, 4: 0}

        for emp, beers in self.employees.items():
            for beer in beers:
                beer_count[beer] += 1

        self.popular_beer = max(beer_count, key=beer_count.get)
        print(f"Type of beer that company needs to buy: {self.popular_beer}")
        return self.popular_beer

    def remove_satisfied_employees(self):
        remaining_employees = {emp: beers for emp, beers in self.employees.items() if self.popular_beer not in beers}
        self.employees = remaining_employees
        return self.employees

    def run_algorithm(self):
        while len(self.employees) > 0:
            self.find_popular_beer()
            self.remove_satisfied_employees()

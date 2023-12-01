def day16_task1():
    flow_rates = {}
    neighbours = {}
    with open("dummy_input.txt", "r") as f:
        for line in f.readlines():
            stripped = line.strip()
            first, second = stripped.split("; ")

            valve_name = first[6:8]
            valve_rate = int(first[18:].split('=')[1])
            valve_neighs = list(map(lambda valve: valve.strip(), second[22:].split(', ')))
            flow_rates[valve_name] = valve_rate
            neighbours[valve_name] = valve_neighs

        # try greedy: 
        # - calculate each time the best target
        # - mark the target as visited and add to flow
        # - calculate the remaining time and current flow
        time = 30
        current_pressure = 0
        start = 'AA'
        opened = {}

def get_best_valve()

def day16_task2(search_range, file_name):
    pass


if __name__ == '__main__':
    day16_task1()
    # day16_task2()
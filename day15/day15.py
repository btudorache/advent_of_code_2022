def day15_task1():
    pairs = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            stripped = line.strip()
            first, second = stripped.split(": ")

            sensor_x, sensor_y = first[10:].split(", ")
            sensor_x_int, sensor_y_int = int(sensor_x.split("=")[1]), int(sensor_y.split("=")[1])

            beacon_x, beacon_y = second[21:].split(", ")
            beacon_x_int, beacon_y_int = int(beacon_x.split("=")[1]), int(beacon_y.split("=")[1])
            pairs.append([(sensor_x_int, sensor_y_int), (beacon_x_int, beacon_y_int)])

    target_y = 2000000
    positions = [0 for _ in range(10000000)]
    num_positions = 0

    for sensor_coords, beacon_coords in pairs:
        sensor_x, sensor_y = sensor_coords
        beacon_x, beacon_y = beacon_coords
        manhattan_dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        if abs(sensor_y - target_y) <= manhattan_dist:
            diff = abs(manhattan_dist - abs(target_y - sensor_y))
            for i in range(sensor_x - diff, sensor_x + diff):
                if positions[i] == 0:
                    positions[i] = 1
                    num_positions += 1

    print(num_positions)

def day15_task2():
    pairs = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            stripped = line.strip()
            first, second = stripped.split(": ")

            sensor_x, sensor_y = first[10:].split(", ")
            sensor_x_int, sensor_y_int = int(sensor_x.split("=")[1]), int(sensor_y.split("=")[1])

            beacon_x, beacon_y = second[21:].split(", ")
            beacon_x_int, beacon_y_int = int(beacon_x.split("=")[1]), int(beacon_y.split("=")[1])
            pairs.append([(sensor_x_int, sensor_y_int), (beacon_x_int, beacon_y_int)])

    search_range = 20
    positions = [[0 for _ in range(search_range)] for _ in range(search_range)]
    num_positions = 0

    for sensor_coords, beacon_coords in pairs:
        sensor_x, sensor_y = sensor_coords
        beacon_x, beacon_y = beacon_coords
        manhattan_dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        if abs(sensor_y - target_y) <= manhattan_dist:
            diff = abs(manhattan_dist - abs(target_y - sensor_y))
            for i in range(sensor_x - diff, sensor_x + diff):
                if positions[i] == 0:
                    positions[i] = 1
                    num_positions += 1

    print(num_positions)


if __name__ == '__main__':
    day15_task1()
    day15_task2()
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

def day15_task2(search_range, file_name):
    pairs = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            stripped = line.strip()
            first, second = stripped.split(": ")

            sensor_x, sensor_y = first[10:].split(", ")
            sensor_x_int, sensor_y_int = int(sensor_x.split("=")[1]), int(sensor_y.split("=")[1])

            beacon_x, beacon_y = second[21:].split(", ")
            beacon_x_int, beacon_y_int = int(beacon_x.split("=")[1]), int(beacon_y.split("=")[1])
            pairs.append([(sensor_x_int, sensor_y_int), (beacon_x_int, beacon_y_int)])

    # curr_pos = [0 for _ in range(search_range)]
    found_pair = False
    for i in range(search_range):
        if found_pair:
            break

        ranges = []
        for sensor_coords, beacon_coords in pairs:
            sensor_x, sensor_y = sensor_coords
            beacon_x, beacon_y = beacon_coords
            manhattan_dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

            if abs(sensor_y - i) <= manhattan_dist:
                diff = abs(manhattan_dist - abs(i - sensor_y))
                ranges.append((max(sensor_x - diff, 0), min(sensor_x + diff, search_range)))
        
        # overlap ranges
        ranges.sort(key=lambda pair: pair[0])

        _, biggest_end = ranges[0]
        for j in range(1, len(ranges)):
            curr_start, curr_end = ranges[j]
            if curr_start - biggest_end == 2:
                print(i, (biggest_end + 1), (biggest_end + 1) * 4000000 + i)
                found_pair = True
                break
            _ = curr_start
            biggest_end = max(biggest_end, curr_end)
        


if __name__ == '__main__':
    # day15_task1()
    day15_task2(4000000, 'input.txt')
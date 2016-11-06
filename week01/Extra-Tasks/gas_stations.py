def gas_stations(distance, tank_size, stations):
    size = tank_size - stations[0]
    result = []

    for i in range(1, len(stations)):
        diff = stations[i] - stations[i - 1]

        if size < diff:
            result.append(stations[i - 1])
            size = tank_size
            size = size - diff

    result.append(stations[len(stations) - 1])
    return result

print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))

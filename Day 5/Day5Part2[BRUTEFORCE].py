import csv
import re

def get_location(file_path):
    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        seeds = []
        for row in reader:
            if len(row) == 0:  # Skip empty rows
                continue
            if "seeds" in row[0]:
                # This is a really poor bruteforce approach, would like to come back to this in the future
                seeds_info = list(map(int, re.findall(r'\d+', row[0])))
                for i in range(0, len(seeds_info), 2):
                    seeds.extend(range(seeds_info[i], seeds_info[i] + seeds_info[i+1]))
            elif "seed-to-soil map" in row[0]:
                current_map = seed_to_soil_map
            elif "soil-to-fertilizer map" in row[0]:
                current_map = soil_to_fertilizer_map
            elif "fertilizer-to-water map" in row[0]:
                current_map = fertilizer_to_water_map
            elif "water-to-light map" in row[0]:
                current_map = water_to_light_map
            elif "light-to-temperature map" in row[0]:
                current_map = light_to_temperature_map
            elif "temperature-to-humidity map" in row[0]:
                current_map = temperature_to_humidity_map
            elif "humidity-to-location map" in row[0]:
                current_map = humidity_to_location_map
            elif current_map is not None:
                current_map.append(list(map(int, row[0].split())))

    min_location = 9999999999999

    for seed in seeds:
        location = seed
        for mapping in [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]:
            for values in mapping:
                dest_start, source_start, length = values
                if location >= source_start and location < source_start + length:
                    location = dest_start + (location - source_start)
                    break

        # Update the lowest location
        if location < min_location:
            min_location = location

    return min_location

def main():
    file_path = 'input.csv'
    location = get_location(file_path)
    print("min location for part 1:", location)

if __name__ == "__main__":
    main()

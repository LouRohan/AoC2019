import sys
import math

def iterate_fuel(fuel):
    sum = fuel
    fuel_mass = fuel
    while True:
        fuel_mass = max(0, math.floor(fuel_mass / 3) - 2)
        sum += fuel_mass
        if fuel_mass == 0:
            break
    return sum
        

def main():
    f = open("day01.txt")

    # part 1
    sum_part1 = 0
    sum_part2 = 0
    for line in f:
        mass = float(line.rstrip())
        fuel = math.floor(mass / 3) - 2
        sum_part1 += fuel
        sum_part2 += iterate_fuel(fuel)

        


    
    f.close()

    print("Total fuel required for part 1: %s" % (str(sum_part1)))
    print("Total fuel required for part 2: %s" % (str(sum_part2)))

if __name__ == '__main__':
    main()
    
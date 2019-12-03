import sys
import copy


def get_offset(direction):
    offset = [0, 0]                
    if direction == 'U':
        offset[1] = 1
    elif direction == 'D':
        offset[1] = -1
    elif direction == 'L':
        offset[0] = -1
    elif direction == 'R':
        offset[0] = 1
    return offset

def brute_force():
    f = open("day03.txt")

    wires = []
    for line in f:
        wires.append(line.rstrip().split(','))
    f.close()

    pos0 = [0, 0]
    manhattan_dist = 99999999999999
    for course in wires[0]:
        dir0 = course[0]
        steps0 = int(course[1:])
        
        offset0 = get_offset(dir0) 
        for step0 in range(0, steps0):
            pos0[0] += offset0[0]
            pos0[1] += offset0[1]

            # run 2nd wire
            pos1 = [0, 0]
            #print("position: %s %s" % (str(pos0), str(pos1)))
            for course1 in wires[1]:
                dir1 = course1[0]
                steps1 = int(course1[1:])

                offset = get_offset(dir1)               
                for step1 in range(0, steps1):
                    pos1[0] += offset[0]
                    pos1[1] += offset[1]

                    if pos0 == pos1:
                        print("position: %s %s" % (str(pos0), str(pos1)))
                        manhattan_dist = min((pos0[0]) + (pos0[1]), manhattan_dist)

    print("Manhattan distance - part 1: %s" % (str(manhattan_dist)))


def not_dumb_2():
    f = open("day03.txt")

    wires = []
    for line in f:
        wires.append(line.rstrip().split(','))
    f.close()

    wire_positions = []
    for wire in wires:
        positions = []
        pos = [0, 0]
        for course in wire:
            dir = course[0]
            steps = int(course[1:])
        
            offset = get_offset(dir) 
            for step in range(0, steps):
                pos[0] += offset[0]
                pos[1] += offset[1]
                positions.append(copy.deepcopy(pos))

        wire_positions.append(copy.deepcopy(positions))

    print("wire distances: %i, %i" % (len(wire_positions[0]), len(wire_positions[1])))

    min_steps = 999999999999999
    wire_1_steps = 1
    for pos in wire_positions[0]:
        wire_2_steps = -1
        if wire_1_steps < min_steps:
            try:
                wire_2_steps = wire_positions[1].index(pos) + 1
                if (wire_1_steps + wire_2_steps) < min_steps:
                    min_steps = min(wire_1_steps + wire_2_steps, min_steps)
                    print("position: %s, shortest: %i, steps: %i, %i" % (str(pos), min_steps, wire_1_steps, wire_2_steps))
            except ValueError:
                wire_2_steps = -1

        wire_1_steps += 1

    print("Min steps - part 2: %s" % (str(min_steps)))

def not_dumb():
    f = open("day03.txt")

    wires = []
    for line in f:
        wires.append(line.rstrip().split(','))
    f.close()

    wire_positions = []
    for wire in wires:
        positions = []
        pos = [0, 0]
        for course in wire:
            dir = course[0]
            steps = int(course[1:])
        
            offset = get_offset(dir) 
            for step in range(0, steps):
                pos[0] += offset[0]
                pos[1] += offset[1]
                positions.append(copy.deepcopy(pos))

        wire_positions.append(copy.deepcopy(positions))

    print("wire distances: %i, %i" % (len(wire_positions[0]), len(wire_positions[1])))

    manhattan_dist = 99999999999999
    for pos in wire_positions[0]:
        if (abs(pos[0]) + abs(pos[1])) < manhattan_dist:
            if pos in wire_positions[1]:
                manhattan_dist = min(abs(pos[0]) + abs(pos[1]), manhattan_dist)
                print("position: %s, shortest: %i" % (str(pos), manhattan_dist))

    print("Manhattan distance - part 1: %s" % (str(manhattan_dist)))
    #print(str(wire_positions))
    
if __name__ == '__main__':
    #brute_force()
    not_dumb_2()
    
    
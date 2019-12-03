import copy

def main_part1():
    f = open("day02.txt")

    # part 1
    int_program_str = []
    for line in f:
        int_program_str = line.rstrip().split(',')
    f.close()

    int_program = []
    for instr in int_program_str:
        int_program.append(int(instr))
    
    prog = copy.deepcopy(int_program)

    prog[1] = 12
    prog[2] = 2
    
    

    print("part 1 input : %s" % (str(prog)))

    i = 0
    program_len = len(prog)
    while i < program_len:
        opcode = prog[i]

        if opcode == 99:
            #exit
            break

        #print("opcode: %s" % str(opcode))
        a = prog[prog[i+1]]
        b = prog[prog[i+2]]
        output_loc = prog[i+3]

        #if output_loc == 0:
        #    print("instr ptr accessing @0: %s" % str(i))

        if opcode == 1:
            #add
            prog[output_loc] = a + b
        elif opcode == 2:
            #mul
            prog[output_loc] = a * b

        i += 4

    print("part 1 output: %s" % (str(prog)))
    print("part 1 position 0: %s" % (str(prog[0])))



def main_part2():
    f = open("day02.txt")

    # part 1
    int_program_str = []
    for line in f:
        int_program_str = line.rstrip().split(',')
    f.close()

    int_program = []
    for instr in int_program_str:
        int_program.append(int(instr))


    desired_output = 19690720
    print("program : %s" % (str(int_program)))
    
    for noun in range(0, 100):
        for verb in range(0, 100):
            prog = copy.deepcopy(int_program)

            #print("program : %s" % (str(prog)))

            prog[1] = noun
            prog[2] = verb

            i = 0
            program_len = len(prog)
            while i < program_len:
                opcode = prog[i]

                if opcode == 99:
                    #exit
                    break

                #print("opcode: %s" % str(opcode))
                a = prog[prog[i+1]]
                b = prog[prog[i+2]]
                output_loc = prog[i+3]

                #if output_loc == 0:
                #    print("instr ptr accessing @0: %s" % str(i))

                if output_loc >= program_len:
                    print("Invalid memory access with noun: %i verb: %i" % (noun, verb))
                    break

                if opcode == 1:
                    #add
                    prog[output_loc] = a + b
                elif opcode == 2:
                    #mul
                    prog[output_loc] = a * b

                if prog[0] == desired_output:
                    print("Desired output reached with noun: %i verb: %i" % (noun, verb))
                    print("Answer: %i" % (100 * noun + verb))
                    exit(0)

                i += 4

        #print("part 1 output: %s" % (str(prog)))
        #print("part 1 position 0: %s" % (str(prog[0])))


if __name__ == '__main__':
    #main_part1()
    main_part2()
    
import sys
import re

# A significantly more mature answer would `from collections import Counter`

def isValidPwd(i):
    if len(re.findall(r'((\w)\2)', str(i))) > 0:
        increasing = True
        last_char = 0
        for j in str(i):
            if int(j) < last_char:
                increasing = False
                break
            last_char = int(j)
        if increasing:
            return True
    return False

def doTwoMatching(i):
    test = str(i)
    if len(test) != 6:
        return False
    idx = 0
    run = 0
    while idx < 5:
        if test[idx] == test[idx+1]:
            run += 1
        else:
            if run == 1:
                return True
            run = 0
        idx += 1

    return run == 1

def isValidPwd2(i):
    if doTwoMatching(i):
        increasing = True
        last_char = 0
        for j in str(i):
            if int(j) < last_char:
                increasing = False
                break
            last_char = int(j)
        if increasing:
            return True
    return False

def main():
    min = 236491
    max = 713787
  
    valid_pwd_count1 = 0
    valid_pwd_count2 = 0
    i = min
    while i <= max:
        if isValidPwd(i):
            valid_pwd_count1 += 1
        if isValidPwd2(i):
            valid_pwd_count2 += 1
        i = i+1

    print("part 1 passwords that meet criteria: %s" % (str(valid_pwd_count1)))
    print("part 2 passwords that meet criteria: %s" % (str(valid_pwd_count2)))

if __name__ == '__main__':
    main()
    
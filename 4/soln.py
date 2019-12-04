import numpy as np

num1 = 245318
num2 = 765747


counter = 0
for num in range(num1, num2 + 1):
    num = str(num)
    digits = [int(i) for i in num]
    digits = np.array(digits)
    differences = digits[1:] - digits[:-1]
    flag = False
    for i in range(len(differences)):
        double_counter = 0
        d = differences[i]
        if d == 0:
            if i + 1 == len(differences):
                if differences[i - 1] != 0:
                    flag = True
                    break
                else:
                    break
            if differences[i + 1] != 0:
                if i == 0:
                    flag = True
                    break
                if i != 0:
                    if differences[i - 1] != 0:
                        flag = True
                        break

    if all(differences >= 0) and any(differences == 0) and flag:
        #  print(True)
        counter += 1
print(counter)


# Post - cleaner solution
import numpy as np

num1 = 245318
num2 = 765747


# Part 1
counter1 = 0
for num in range(num1, num2 + 1):
    num = str(num)
    digits = [int(i) for i in num]
    digits = np.array(digits)
    differences = digits[1:] - digits[:-1]
    if all(differences >= 0) and any(differences == 0):
        counter1 += 1

# Part 2
counter2 = 0
for num in range(num1, num2 + 1):
    num = str(num)
    digits = [int(i) for i in num]
    digits = np.array(digits)
    differences = digits[1:] - digits[:-1]
    i = 0
    double_flag = False
    while not double_flag and i < len(differences):
        if differences[i] != 0:
            i += 1
            continue
        if i == 0:
            double_flag = differences[i + 1] != 0
        elif i == len(differences) - 1:
            double_flag = differences[i - 1] != 0
        else:
            double_flag = differences[i - 1] != 0 and differences[i + 1] != 0
        i += 1
    if all(differences >= 0) and double_flag:
        counter2 += 1

print(counter1, counter2)

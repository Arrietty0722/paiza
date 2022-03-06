

def mod7(numbers):
    mods = []
    for number in numbers:
        mod = number % 7
        mods.append(mod)
    counter = 0
    for i, mod1 in enumerate(mods):
        if (i - (len(mods) - 1)) > 2:
            break
        mods2 = mods[i+1:]
        for j, mod2 in enumerate(mods2):
            if (j - (len(mods2) - 1)) > 1:
                break
            mods3 = mods2[j+1:]
            for k, mod3 in enumerate(mods3):
                if (k - (len(mods3) - 1)) > 0:
                    break
                sum_mods = mod1 + mod2 + mod3
                result_mod = sum_mods % 7
                if result_mod == 0:
                    counter += 1

    print("mods : ", mods)
    print("counter : ", counter)


def main():
    # input_num = input().rstrip().split(" ")
    input_num = input()
    print(f"in main  input_num : {input_num}")
    values = []
    for _ in range(int(input_num)):
        value = input()
        print(f"input value : {value}")
        values.append(int(value))
    print(f"input values : {values}")

    mod7(values)

if __name__ == "__main__":
    # test_numbers = [1, 3, 5, 7, 9]
    # test_numbers = [10, 4, 14]
    # test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # test_numbers = [10, 4]
    # test_numbers = [10]
    # test_numbers = [2**32 + 3, 2**32 - 1, (2**32) - 3]
    # test_numbers = [2**32 + 3, 2**32 - 1, (2**32) - 7]
    # test_numbers = [2**32 + 3, 2**32 - 1, (2**32)]
    test_numbers = [2**32 + 3, 2**32 - 4, (2**32)-4]
    mod7(test_numbers)
    print(test_numbers)
    print(2**32 + 3)
    print(2**32 - 1)
    print(2**32 - 4)

    input()

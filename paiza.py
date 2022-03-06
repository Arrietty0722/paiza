
# def main():
#     input_line = int(input())

#     for i in range(input_line):
#         s = input().rstrip().split(' ')
#         print("hello = "+s[0]+" , world = "+s[1])


def main():
    line = input().rstrip().split(" ")
    print(line)
    w = int(line[0])
    h = int(line[1])
    img = []
    for i, y in enumerate(range(h)):
        line = input().rstrip().split(" ")
        line = [int(i) for i in line]
        print(line)
        img.append(line)

    print("<< img >>")
    for line in img:
        print(line)

    new_values = []
    new_values.append([0 for _ in range(w + 2)])
    for line in img:
        new_line = [0] + line + [0]
        new_values.append([0 for _ in range(w + 2)])
    new_values.append([0 for _ in range(w + 2)])

    new_h = len(new_values)
    new_w = len(new_values[0])
    num_island = 0
    for y in range(h):
        for x in range(w):
            pix = img[y][x]
            if pix == 1:
                y_value = y+1
                x_value = x+1
                value_up = new_values[y_value - 1][x_value]
                value_left = new_values[y_value][x_value - 1]
                if (value_up == 0) and (value_left == 0):
                    num_island += 1
                    new_values[y_value][x_value] = num_island
                elif (value_up != 0) and (value_left == 0):
                    new_values[y_value][x_value] = value_up
                    # num_island += 1
                elif (value_up == 0) and (value_left != 0):
                    new_values[y_value][x_value] = value_left
                    # num_island += 1
                elif (value_up != 0) and (value_left != 0):
                    if value_up < value_left:
                        update = value_up
                        erase = value_left
                    else:
                        update = value_left
                        erase = value_up
                    new_values[y_value][x_value] = update
                    # num_island += 1
                    num_island -= 1
                    for i in range(new_h):
                        for j in range(new_w):
                            if new_values[i][j] == erase:
                                new_values[i][j] = update
                else:
                    raise Exception

    result = max(num_island, update)
    if result <= 0:
        result = 0
    # result = 0
    # island_ids = [0]
    # for i in range(new_h):
    #     for j in range(new_w):
    #         if new_values[i][j] not in island_ids:
    #             island_ids.append(new_values[i][j])
    #             result += 1

    print(result)
    for line in new_values:
        print(line)


if __name__ == "__main__":
    main()

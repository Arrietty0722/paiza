

def main():
    N, M, L = input()
    command_lines = []
    for _n in range(N):
        command_line = input()
        command_lines.append(command_line)

    param_lines = []
    for _l in range(L):
        param_line = input()
        param_lines.append(param_line)

    for i, param_line in enumerate(param_lines):
        if i == 0:
            continue
        current_line = param_lines[i]
        previous_line = param_lines[i-1]
        diff_line = [c_v - p_v for c_v, p_v in zip(current_line, previous_line)]
        result_idxs = []
        for j, command_line in enumerate(command_lines):
            is_match = True
            for diff_value, command_value in zip(diff_line, command_line):
                if diff_value != command_value:
                    is_match = False
                    break
            if is_match:
                result_idxs.append(j+1)
                break

    for result_idx in result_idxs:
        print(result_idx)
        
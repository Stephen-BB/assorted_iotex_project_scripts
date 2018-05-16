def bool_converter(input_list):
    i = 0
    for element in input_list:
        if element is None:
            input_list[i] = False
        else:
            input_list[i] = True
        i = i + 1
    return input_list


def make_list(input_list):
    i = 0
    output_list = []
    while i < len(input_list):
        if input_list[i]:
            output_list.append(1)
        else:
            output_list.append(0)
        i += 1
    return output_list



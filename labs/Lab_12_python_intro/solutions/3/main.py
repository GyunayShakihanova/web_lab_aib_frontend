input_file = open('input.txt')
input_text = input_file.read()


def maxCount(scan_list):
    max_count_symbol = 0
    for i in scan_list:
        if max_count_symbol < i[1]:
            max_count_symbol = i[1]
    return max_count_symbol


def read_symbols_and_make_hist(input_text_func):
    input_text_func = input_text_func.replace('\n','')
    input_text_func = input_text_func.replace(' ','')
    total_symbols = list()
    symbol_is_in_list = False
    for symbol in input_text_func:
        if len(total_symbols) > 0:
            for check_symbol in total_symbols:
                if check_symbol[0] == symbol:
                    check_symbol[1] += 1
                    symbol_is_in_list = True
                    break
            if not symbol_is_in_list:
                 total_symbols.append([symbol, 1])
            symbol_is_in_list = False
        else:
            total_symbols.append([symbol, 1])
    total_symbols.sort(key = lambda x: x[0])
    max_count_value = maxCount(total_symbols)
    hist = []
    for i in range(max_count_value + 1):
        hist.append(list([' ' for j in range(len(total_symbols))]))
    j = 0
    while j < len(total_symbols):
        hist[max_count_value][j] = total_symbols[j][0]
        k = max_count_value - 1
        o = 0
        while o < total_symbols[j][1]:
            hist[k][j] = '#'
            k -= 1
            o += 1
        j += 1
    return hist


output_file = open('output.txt', 'w')
output_text = read_symbols_and_make_hist(input_text)
for i in output_text:
    for j in i:
        output_file.write(j)
    output_file.write('\n')
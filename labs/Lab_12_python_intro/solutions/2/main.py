input_file = open('input.txt')
input_text = input_file.read().split()
Count_numbers = int(input_text[0])
input_text.pop(0)
input_text = [int (x) for x in input_text]

def Sequence(sum_medians, sub_sequence_length, func_input_text):
    temp_sequence = func_input_text[:sub_sequence_length]
    temp_sequence.sort()
    if len(temp_sequence) % 2 == 1:
        if len(temp_sequence) == 1:
            sum_medians += temp_sequence[0]
        else:
            sum_medians +=  temp_sequence[((len(temp_sequence) + 1) // 2) - 1]
    elif len(temp_sequence) % 2 == 0:
        sum_medians += temp_sequence[(len(temp_sequence) // 2) - 1]
    sub_sequence_length += 1
    if sub_sequence_length > Count_numbers:
        return sum_medians
    else:
        return Sequence(sum_medians, sub_sequence_length, func_input_text)

output_file = open('output.txt', 'w')
output_file.write(str(Sequence(0, 1, input_text)))
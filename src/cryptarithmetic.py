import time

def read_file(file_name):
    word = []
    f = open(file_name, 'r')
    for x in f:
        word.append(x)
    return word

def total_operands(arr):
    operand = []
    total_operands = 0
    for i in range (len(arr)):
        total_operands += 1
        if '+' in arr[i]:
            operand.append(total_operands)
        if arr[i] == '\n':
            total_operands = 0
    return operand

def arr_of_problems(arr, total_operands):
    length = len(total_operands)
    new_arr = [[] for i in range (len(total_operands))]
    j = 0
    for i in range (len(arr)):
        if arr[i] != '':
            new_arr[j].append(arr[i])
        else:
            j += 1
    return new_arr

def convert_words(words, total_operands):
    converted = []
    max_length_of_word = 0
    for i in range (total_operands):
        if len(words[i]) > max_length_of_word:
            max_length_of_word = len(words[i])
        converted.append(words[i].replace(' ', '').strip('+'))
    converted.append(words[total_operands+1])
    return converted, max_length_of_word

def count_unique(words):
    all_words = ''.join(words)
    return len(set(all_words)), list((set(all_words)))

def is_calculated_right(arr_num):
    total = 0
    if arr_num == -999:
        return False
    for i in range (len(arr_num)-1):
        total += int(arr_num[i])
    return total == int(arr_num[i+1])

def is_alphabet_first(words, alph):
    first = [(False) for i in range (len(alph))]
    for i in range (len(words)):
        separated_words = list(words[i])
        j = alph.index(separated_words[0])
        if (first[j] == False):
            first[j] = True
    return first

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def reverse(arr, idx):
    (i, j) = (idx, len(arr)-1)
    while i < j:
        swap(arr, i, j)
        i += 1
        j -= 1

def next_permutation(arr):
    length = len(arr)
    i = length - 1
    while arr[i-1] >= arr[i]:
        i -= 1
        if i == 0:
            return False

    j = length - 1
    while j > i and arr[j] <= arr[i-1]:
        j -= 1
    
    swap(arr, i-1, j)
    reverse(arr, i)
    return True

def permutasi(arr):
    new_arr = []
    sorted_arr = sorted(arr)
    while True:
        new_arr.append(''.join(sorted_arr))
        if not next_permutation(sorted_arr):
            return new_arr

def zero_in_first(arr, first):
    for i in range (len(first)):
        if arr[i] == '0' and first[i] == True:
            return True
    return False

def convert_word_to_number(huruf_uniq, words, huruf_pertama, generated_angka):
    converted = words
    for i in range (len(huruf_uniq)):
        converted = list(map(lambda st: str.replace(st, huruf_uniq[i], str(generated_angka[i])), converted))
    return converted

def possibilities(words, unique_alph, generated_number):
    is_first = is_alphabet_first(words, unique_alph)
    tries = 1
    for i in range (len(generated_number)):
        if not zero_in_first(generated_number[i], is_first):
            converted = convert_word_to_number(unique_alph, words, is_first, generated_number[i])
            if is_calculated_right(converted):
                return converted, tries
            tries += 1

def timer(start, finish):
    duration = finish - start
    temp = time.gmtime(duration)
    clock = time.strftime('%M menit %S detik', temp)
    return clock

def print_result(words, number, max_length_of_word):
    for i in range (len(number) - 1):
        print(words[i], end=' ' * 10)
        if max_length_of_word > len(number[i]):
            diff = max_length_of_word - len(number[i])
            print(' ' * (diff+1), end='')
        if i == len(number) - 2:
            print(number[i] + '+')
        else:
            print(' ' + number[i])

    print(words[i+1], ' ' * 10, words[i+1])
    print(words[i+2], ' ' * 11, number[i+1])


file_name = input('Masukkan nama file: ')
words = read_file('../test/' + file_name)

start = time.time()
operands = total_operands(words)

removed_nl = [words[i].strip('\n') for i in range (len(words))]
new_words = arr_of_problems(removed_nl, operands)

arr_of_numbers = [str(i) for i in list(range(10))]
permutation_result = permutasi(arr_of_numbers)

for i in range (len(operands)):
    if i != 0:
        start = end
        print()

    print('Soal ' + str(i+1))
    converted_words, max_len = convert_words(new_words[i], operands[i])
    total_unique, unique_words = count_unique(converted_words)

    if (total_unique > 10):
        print('Hurufnya kebanyakan :(')
    else:
        result, tries = possibilities(converted_words, unique_words, permutation_result)

        end = time.time()
        print_result(new_words[i], result, max_len)
        print('Waktu eksekusi program:', timer(start, end))
        print('Jumlah total tes yang dilakukan:', tries)
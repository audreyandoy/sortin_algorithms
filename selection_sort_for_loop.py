def sort_by_length(sentence):
    array = sentence.split()
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if len(array[j]) < len(array[min_index]) or len(array[min_index]) == len(array[j]) and array[min_index][0] > array[j][0]:
                min_index = j
        if len(array[min_index]) != len(array[i]):
            array[i], array[min_index] = array[min_index], array[i]
    return array

print(sort_by_length("love great awesome words I"))
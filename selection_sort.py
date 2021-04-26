def sort_by_length(sentence):
    array = sentence.split()
    i = 0
    min_index = i
    while i < len(array) - 1:
        min_index = i
        j = i + 1
        while j < len(array): # find the smallest word for min_index
            if len(array[j]) < len(array[min_index]):
                min_index = j
            elif len(array[min_index]) == len(array[j]) and array[min_index][0] > array[j][0]:
                    min_index = j
            j += 1
        if len(array[min_index]) != len(array[i]):
            temp = array[min_index]
            array[min_index] = array[i]
            array[i] = temp
        i += 1
    return array

print(sort_by_length("love great awesome words I"))
def sort_by_length(sentence):
    array = sentence.split()
    i = 1 # treat first item in array as sorted
    while i < len(array):
        to_insert = array[i]
        j = i
        while j > 0 and len(array[j - 1]) > len(to_insert):
            array[j] = array[j - 1]
            j -= 1
        array[j] = to_insert
        i += 1
    return array

print(sort_by_length("love great awesome words I"))
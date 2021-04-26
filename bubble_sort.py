def sort_by_length(sentence):
    array = sentence.split()
    i = 0
    while i < len(array) - 1:
        j = 0
        while j < (len(array) - i - 1):
            if len(array[j]) > len(array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j + 1] = temp
            j += 1
        i += 1
    return array

print(sort_by_length("I love great awesome words"))
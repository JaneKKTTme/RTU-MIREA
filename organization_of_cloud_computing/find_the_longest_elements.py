def find_the_longest_elements(list_of_elements, alphabet=[], the_longest_elements=[]):
    alphabet = set(map(lambda x : x[0], list_of_elements))
    the_longest_elements = sorted([max(filter(lambda x : i in x, list_of_elements)) for i in alphabet])
    return [(element,len(element)) for element in the_longest_elements]

if __name__ == "__main__":
    print(find_the_longest_elements(["zz", "ccc", "c", "xxxxx", "ccccccccc", "xxx"]))

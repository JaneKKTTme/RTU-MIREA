def calculate_sum(list_of_elements, sum_of_list = 0):
    for element in list_of_elements:
        sum_of_list += element
    return sum_of_list
    
if __name__ == "__main__":
    print(calculate_sum([1, 3, 5, 7, 9, 2, 4, 6, 8]))

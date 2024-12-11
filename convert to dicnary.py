# Function to convert a list of tuples into a dictionary


def convert_to_dict(tuples_list):
    return dict(tuples_list)
list_of_tuples = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
result_dict = convert_to_dict(list_of_tuples)
print("Converted Dictionary:", result_dict)

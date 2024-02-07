# def unique_elements(input_list):
#     unique_list = []
#     for item in input_list:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list

# original_list = [1, 2, 3, 3, 4, 4, 5]
# result_list = unique_elements(original_list)
# print(result_list)   [1, 2, 3, 4, 5]

# def unique_elements(input_list):
#     unique_list = []
#     for item in input_list:
#         if input_list.count(item) == 1:
#             unique_list.append(item)
#     return unique_list

# original_list = [1, 2, 3, 3, 4, 4, 5]
# result_list = unique_elements(original_list)
# print(result_list)  # [1, 2, 5]
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if input_list.count(item) == 1:
            unique_list.append(item)
    return unique_list

#будет выполняться только при запуске test10.py 
if __name__ == "__main__":
    print(unique_elements([1, 2, 3, 3, 4, 4, 5]))

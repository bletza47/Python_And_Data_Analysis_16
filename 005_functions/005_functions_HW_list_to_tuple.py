
# Write a function that accepts a list of numbers
# And returns a tuple with two numbers, amount of odd and even numbers
# Example: input -> [1, 2, 3, 4, 5] output (3, 2)
# Where 3 is amount of Odds and 2 is amount of evens


def list_to_tuple(numbers):
    odd_nums_list = []
    even_nums_list = []
    for nums in numbers:
        if (nums %2 ==0):
            even_nums_list.append(nums)
        else:
            odd_nums_list.append(nums)

    # convert lists to tuples
    odd_nums_tuple = tuple(odd_nums_list) 
    even_nums_tuple = tuple(even_nums_list)

    final= (len(odd_nums_tuple), len(even_nums_tuple))

    return final


my_list = [2,3,5,34,62,63,77,85,90,94]
print(list_to_tuple(my_list))

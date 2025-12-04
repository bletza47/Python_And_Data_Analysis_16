# Write a function that accepts a list of numbers as an argument
# And returns list with squares for each number



# Create the function that takes a takes a list of numbers and create another empty list 
# Use a loop to turn each of its elements into squares
def square_num(numbers):
    square_nums = []
    for element in numbers:
        square_nums.append(element ** 2)

    return square_nums
 
users_list = []

while (True):
    num = input('What is your number? \n'
            'Press 0 to quit! \n'
            '---> ')
             
    if num == '0':
        # print(f"\nOriginal List: {users_list}")
        print(f'Users list {users_list}')
        squared_result = square_num(users_list)
        print(f"Squared List: {squared_result}")
        break  
    users_list.append(int(num))

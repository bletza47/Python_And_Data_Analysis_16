# Create two empty lists (long_names, short_names)
# Iterate through names list and add names that are longer than 5 characters to long_names, and others to short names

"""
names = ['Sarah', 'Jessica', 'Anthony', 'Jack', 'Simon', 'Arthur', 'Maria', 'Samantha']
long_names = []
short_names = []


# Check if the name has more than five characterss and put it in long list otherwise in short list

for each_name in names:
    if len(each_name)>5:
        long_names.append(each_name)
    else:
        short_names.append(each_name)

print(f'The names with more than five chars are: {long_names}. \n The rest of the names have less than five chars: {short_names}')

"""






# # Given a list where each element is a year. Determine whether the given year is a leap year. If the year is a leap year,
# # print YES, otherwise print NO. 
# According to the Gregorian calendar, a year is a leap year if its number is a multiple of 4, but not a multiple of 100 OR if it is a multiple of 400.

"""
years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]
leap_years = []

# We first iterate through the numbers 
for the_year in years_list:
    # We find the years that are divisible by 4 but not 100 and 400 and we add them to the new list
    if (the_year % 4 == 0 and the_year % 100 != 0) or (the_year % 400 == 0):
        leap_years.append(the_year)
            

print(leap_years)

"""




# # Write a program that prompts the user for a string and checks if the string contains only unique characters.
user_input = input('Enter something: ')

if user_input ==



# # Write a program that checks gender for each person.
# # If person is a male, print "This is NAME SURNAME. He is AGE years old"
# # If person is a female, print "This is NAME SURNAME. She is AGE years old"
# people = [
#     ('Jane', 'Smith', 26, 'female'),
#     ('Jack', 'Green', 30, 'male'),
#     ('Maria', 'Gold', 29, 'female'),
#     ('Simon', 'Bloom', 35, 'male'),
# ]


# # FIZZ BUZZ
# # For range of numbers between 1 and 100.
# # If number is divided by 3 without a remainder print number and FIZZ
# # If number is divided by 5 without a remainder print number and BUZZ
# # If number is divided by 5 and by 3 without a remainder print number and FIZZBUZZ

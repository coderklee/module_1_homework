# name = input("What is your name? ")
# age = input("How old are you? ")

# result = "Hello {}! You are {} years old!".format(name,age)
# print(result)

# name = 'Kaleigh'
# age = 35
# location = 'Oceanside'

# result_string = "{} is {} years old and currently lives in {}.".format(name, age, location)
# print(result_string)

# result_again = f"{age} is a great age for {name}!"
# print(result_again)

#find all cubed numbers until the cubed number result is 1000


def print_cubes(a,b):
    for i in range(a,b + 1):
        for j in range(j ** 3, i + 1):
            if (j ** 3 == i):
                print(j ** 3, end=" ")
                break

numbers = list(range(1,1000))
cube_numbers = []
for number in numbers:
    cube = (number)**(3)
    if cube > 1000:
        break
    else:
        print(cube)
        

# for num in range(0,100):
#     if num > 0:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# age = int(input("How old are you? "))

# if age < 18:
#     print('Kid')
# elif age >= 18 and age < 65:
#     print('Adult')
# else:
    # print('Senior')

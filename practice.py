# price = [10, 20, 30, 40]
# total = 0 

# for i in price :
#     total = total + i

# print ("Total : ", total )


# for x in range (5) :
#     for y in range (2) :
#         print (f'({x}, {y})')


# names = [ 'Suvam', 'Sampragya', 'Nirajan', 'ram', 'sam']
# print (f"{names[0:3]}")


# for i in range(5) :
#     number = int(input("Provide five numbers: "))


# number = [1,2,3,4,5]
# max = number[0]
# for numbers in number:
#     if numbers > max:
#         max = numbers
# print ( max )

#remove duplicate in a list

# list = [ 1, 2, 2, 3, 4, 5,5,5,6,6,7,]
# unique = []
# for numbers in list :
#     if numbers not in unique :
#         unique.append(numbers)
# print (unique)

# phone = (input("Enter numbers: "))
# list = {
#     "1" : "one",
#     "2" : "two",
#     "3" : "three",
#     "4" : "four"
# }
# output = ""
# for numbers in phone:
#     output += list.get(numbers, "!") + " "
# print (output)


# data = {"x": 4, "y": 9, "z": 12, "w": 3}
# Use a for loop to print only the keys whose values are even numbers.
# data = {"x": 4, "y": 9, "z": 12, "w": 3} 

# for even, value in data,items():
#     if value % 2 == 0 :
#         print (even, value)

# data = {"x": 4, "y": 9, "z": 12, "w": 3}

# for key, value in data.items():
#     if value % 2 == 0:   # check if value is even
#         print(key, value)

# def square (number):
#     return number * number 


# print (square(4))


import converters
weight = float(input(f"Enter the weight: "))
print(converters.lbs_to_kg(weight))



    






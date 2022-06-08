# # 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# # In the sports_directory, change 'Messi' to 'Andres'
# # Change the value 20 in z to 30

# x = [ [5,2,3], [10,8,9] ] 
# x[1][0]=15
# print(x)

# print("=======================================")


# When we have [] its a list AND {} means its a dictionary
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

# students[1]["last_name"]= "Bryant"

# print(students)
# print("=======================================")



#3.In the sports_directory, change 'Messi' to 'Andres'
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }

# sports_directory['soccer'][0] = "Andres"
# print(sports_directory)
# print("=======================================")



# # 4.Change the value 20 in z to 30
# z = [ {'x': 10, 'y': 20} ]
# z[0]['y']=30
# print(z)
# print("=======================================")





# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:



# students = [
#          {'first_name':  'Michael',  'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]


# shavi1 = 'first_name'
# shavi2 = 'last_name'

# def iterateDictionary(students):
#     for i in range( 0, len(students) ): # (start, end, + or -)
#         print(students[i][shavi1])
#         print(students[i][shavi2])




# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel




# 3. Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

# students = [
#          {'first_name':  'Michael',  'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]


# shavi1 = 'first_name'
# shavi2 = 'last_name'

# def iterateDictionary2(students):
#     for i in range( 0, len(students) ): # (start, end, + or -)
#         print(f"first_name -{students[0]['first_name']}, last_name -{students[0]['last_name']}")
        



# iterateDictionary2(students)






# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }

# sports_directory['soccer'][0] = "Andres"
# print(sports_directory['soccer'])


# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'], # key = locations, value = list
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon'] # key = locations, value = list
}


def printInfo(dictionary): # dictionary == dojo

    """
    For loop that goes through each key, then prints the key name and it's value. 
    The value in this assignment are lists. (Example: ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'])
    
    for each key in dictionary: 
        get each list. 
            Example: dojo['location'] = ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank']
    """
    for key in (dictionary): # key is location/instrucor 
        print(f"Key: {key} ")
        print(f"List: {dictionary[key]} ")
        print(f"Key: {key} \n Length of List :", len(dictionary[key]))

        """
        Second For Loop to take the list we have from using dictionary[key] and printing each value in the list that is in the key's value.

        We use len(dictionary[key]) because that is where the list is stored and we want to loop to the end of that list.

            Then we print the value by using our value of i as the index position in the list. 
                Example: dictionary[key][i] is the same as dojo['locations'][0]

        """
        for i in range(len(dictionary[key])):   
            print(f"Value of {key} at index of {i} : {dictionary[key][i]}")
        

def printInfo(dictionary):
    for key in (dictionary): # key is location/instrucor 
        print(f"Key: {key} ")
        print(f"List: {dictionary[key]} ")
        print(f"Key: {key} \n Length of List :", len(dictionary[key]))
        for i in range(len(dictionary[key])):   
            print(f"Value of {i} : {dictionary[key][i]}")


printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


#   sum = 0

# for x in range(1,500001,2):
#     sum += x

# print(sum)

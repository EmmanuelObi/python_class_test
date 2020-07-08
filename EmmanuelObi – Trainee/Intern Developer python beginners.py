# Extract the colors from the html file provided ‘python_class_test.html’, using regular expression
import re
import random
import numpy
import psycopg2

file = open('python_class_test.html', 'r')
text = file.read()
file.close()


pattern = re.compile(r'<td>(.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)[,](.*?)</td>')
match = pattern.findall(text)
#(match)

# Storing them in a dictionary, using color as key and their frequency as values.
store_house = {}

def myfunc(My_list, store):
    for tup in My_list:
        for color in tup:
            if color in store:
                store[color] += 1

            else:
                store[color] = 1


    print(store)

myfunc(match, store_house)


 #1.) Which color of shirt is the mean color?
#using numpy library

print(numpy.array([store_house[k] for k in store_house]).mean())

# the mean value == 7.916666666666667,  mean color should be orange / red.


 # 2.) Which color is mostly worn throughout the week? 
 #the most worn color == color with most frequency

most_freq = max(store_house, key=store_house.get)  
print(most_freq, store_house[most_freq])
# most frquent color == Blue 


 #3.) Which color is the median?

 #6.) Save the colours and their frequencies in postgresql database
def InsertData(store):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Kolikoman",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO ColorFreq (id, color, Freq) 
                           VALUES (%s,%s,%s) """

        # executemany() to insert multiple rows rows
        result = cursor.executemany(sql_insert_query, store)
        connection.commit()
        print(cursor.rowcount, "data inserted successfully into ColorFreq table")

    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into ColorFreq table {}".format(error))

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

BabyNames = match
InsertData(store_house)

#7.) BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers

My_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

x = int(input("Enter a search number: "))
def SearchListAlgorithm(list, start, end, x):

    if end >= start:
        mid = start + (end - start) // 2
        
        if list[mid] == x:
            return mid
        elif list[mid] > x:
            return SearchListAlgorithm(list, start, mid - 1, x)
        else:
            return SearchListAlgorithm(list, mid + 1, end, x)
    
    else:
        return - 2
        
result = SearchListAlgorithm(My_list, 0, len(My_list) - 1, x)
if result != -2:
    print("Key is present at index " + str(result))
else:
    print("Key is not present in this List. ")


#8.) Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10

#Function to create the random binary string 
def randomBinary(n): 
    
    #  storing the string in variable
    binary = "" 
  
    # Looping to get needed amount 
    for i in range(n): 
          
        temp = str(random.randint(0, 1)) 
  
        binary += temp 
          
    return(binary) 
  
n = 4
generated_binary_string = randomBinary(n) 

converted_binary_string = int(generated_binary_string, 2)

print(converted_binary_string)

# 9.) Write a program to sum the first 50 Fibonacci sequence

# a is the amount to sum
a = 50

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, b + a
        
fib_list = list(fibonacci(a))
the_sum = sum(fib_list)
print(the_sum)



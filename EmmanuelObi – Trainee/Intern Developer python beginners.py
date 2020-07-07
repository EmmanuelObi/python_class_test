# 1.) Extract the colors from the html file provided ‘python_class_test.html’, using regular expression
import re
import random

file = open('python_class_test.html', 'r')
text = file.read()
file.close()


pattern = re.compile(r'<td>(.*?)[,](.*?)</td>')
match = pattern.findall(text)
print(match)


def CountFrequency(my_list): 
  
    # Creating an empty dictionary  
    freq = {} 
    for color in match:
        #for color in line:
        if (color in freq): 
            freq[color] += 1
        else: 
            freq[color] = 1
  
    for key, value in freq.items(): 
        print ("% s : % d"%(key, value)) 
  
# Driver function 
if __name__ == "__main__":  
  
    CountFrequency(match) 

"""
print(re.search(r'<td>(.*?)</td>', text).group())
print(re.search(r'<td>(.*?)[,](.*?)</td>', text).group())

"""

# 7.) BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers
"""
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
"""
# 8.) Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10
"""
# Function to create the random binary string 
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
"""
# 9.) Write a program to sum the first 50 Fibonacci sequence
"""
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
"""
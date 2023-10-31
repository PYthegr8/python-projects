''' Papa Yaw Owusu Nti

    This program defines functions for statistical computations including
    mean,min,max,min_index,max_index and variance on a sample data
    and provides a test function for demonstration 
    
'''

def sum(numbers):
    '''  Calculates the sum of a list of numbers. Accepts one parameter (numbers) and returns its sum as a float '''
# Create a variable to hold the sum
# Initialize the variable to 0.0 (explicitly make it a floating point number).
    sum_numbers = 0.0
# Define a for loop to iterate over the list passed in as the function parameter. 
    for x in numbers:
        # On each iteration, add the current number to the variable holding the sum. 
        sum_numbers+= x
    return sum_numbers

        # Once the loop completes, return the sum.
    
    
def test():
    '''tests the sum function'''
    list1 = [1,2,3,4]
    list2 = sum(list1)
   # print(list2)
    
    
    
# mean(data) - computes the mean of the list of data.

def mean(data):
    '''  Calculates the mean of a list of data. Accepts one parameter (data) and returns its average as a float '''
    mean= sum(data)/len(data)
    return mean
        
# min(data) - computes the min of the list of data.
def min(data):
    '''  Calculates the minimum value of a list of data. Accepts one parameter (data). Initializes 
    the minimum data as 10000. Uses a for lop with an embedded if conditional to iterate through the list 
    to return the smallest data by comparing it to the current min_of_data of the list
     '''
    min_of_data = 10000

    for x in data:
        if x <  min_of_data:
             min_of_data = x
    return min_of_data

    
# max(data) - computes the max of the list of data.
def max(data):
    '''  Calculates the maximum value of a list of data. Accepts one parameter (data). Initializes 
    the maximum data as -200.0  Uses a for lop with an embedded if conditional to iterate through the list 
    to return the largest data by comparing it to the current max_of_data of the list'''
    max_of_data = -200.0

    for y in data:
        if y >  max_of_data:
             max_of_data = y
    return max_of_data


# min_index(data) - computes the index of the min of the list of data.
def min_index(data):
    ''' Computes the index of the minimum value in a list of data. Accepts on parameter	- data (list) and 
        Returns the index of the minimum value .
'''
    min_data = 10000  # For min, set to a large number
    min_index = -1   # Initialize min_index to -1
    
    # Loop over integers from 0 to the size of nums (corresponding to list indices for nums):
    for current_index in range(len(data)):
        # If the value of nums at the current list index is less than min_num:
        if data[current_index] < min_data:
            # Update min_num to be the value of nums at the current list index
            min_data = data[current_index]
            # Update min_index to be the current list index
            min_index = current_index
    return min_index  
         
# max_index(data) - computes the index of the max of the list of data.
def max_index(data):
    ''' Computes the index of the maximum value in a list of data. Accepts on parameter	- data (list) and 
        Returns the index of the maximium value'''
        
    max_data = -10000  # For min, set to a large number
    max_index = -1   # Initialize min_index to -1
    
    # Loop over integers from 0 to the size of nums (corresponding to list indices for nums):
    for current_index in range(len(data)):
        # If the value of nums at the current list index is less than min_num:
        if data[current_index] > max_data:
            # Update min_num to be the value of nums at the current list index
            max_data = data[current_index]
            # Update min_index to be the current list index
            max_index = current_index
    return max_index  



# variance(data) - 
def variance(data):
    '''this function computes the variance of the list of data.'''
    ##Compute the mean of nums 
    mean= sum(data)/len(data)

    #Make a new empty list: squared_nums_minus_means
    squared_data_minus_means = []
    
    #Loop over the values in nums
    for x in data:
        #For each value, append the square of ( the value minus the mean of nums ) to squared_nums_minus_means
        squared_data_minus_means.append((x-mean)**2)
        #Compute the sum of squared_nums_minus_means and divide it by the size of nums minus 1
        var = sum(squared_data_minus_means)/ (len(data)-1)
        #Return the value you just computed   
    return var


	


#Testing the functions defined to make sure they are working properly

sample_data= [1,2,3,4,5]
sample_mean= mean(sample_data)
sample_min = min(sample_data)
sample_max= max(sample_data)
sample_min_index = min_index(sample_data)
sample_max_index= max_index(sample_data)
sample_variance= variance(sample_data)


print(sample_mean)
print(sample_min)
print(sample_max)
print(sample_min_index)
print(sample_max_index)
print(sample_variance)


if __name__ == "__main__":
    test()


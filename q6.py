#fn to calculate average of numbers in a list
def calculateAverage(num_list):
    if len(num_list) == 0:
        return 0
    else:
        return sum(numbers)/len(numbers)

#function to find minimum of numbers in a list
def find_min(num_list):
    if len(num_list) == 0:
        return
    else:
        return min(num_list)

#function to find maximum of numbers in a list
def find_max(num_list):
    if len(num_list) == 0:
        return
    else:
        return max(num_list)

#function to filter out numbers above threshold
def filter_above_threshold(num_list, thresh):
    if len(num_list) == 0:
        return
    
    nums_above_threshold = []  #store nums above threshold
    
    #iterate through numbers list
    for num in num_list:
        if num > thresh:
            nums_above_threshold.append(num)
    return nums_above_threshold

#main program
numbers = [10, 20, 30, 40, 50]

#call fn to calculate average
average = calculateAverage(numbers)
print('Average:', average)

#call fn to calculate minimum
minimum = find_min(numbers)
print('Minimum:', minimum)

#call fn to calculate minimum
maximum = find_max(numbers)
print('Maximum:', maximum)

threshold = int(input('Enter threshold: '))

#call fn to filter numbers above threshold
threshold_list = filter_above_threshold(numbers, threshold)

if threshold_list == None:
    print('List is empty')
else:
    print('Numbers above the threshold ' + str(threshold) + ':', threshold_list)
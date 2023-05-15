#!/usr/bin/env python
# coding: utf-8

# Example1

# In[15]:
#we have two ways to solve
#first one
   # Sort jobs by profit in descending order
def Find_Maximum_profit(Jobs):
    Jobs = sorted(Jobs, key=lambda x: x[2], reverse=True)
    jobs_number = len(Jobs)
    max_profit = 0
    jobs_done = 0
    slots = [False] * jobs_number
    
    for i in range(jobs_number):
        for j in range(min(jobs_number, Jobs[i][1])-1, -1, -1):
            if not slots[j]:
                slots[j] = True
                max_profit += Jobs[i][2]
                jobs_done += 1
                break
    
    return (jobs_done, max_profit)


#To use this function with the example input provided, you can call it like this:


Jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
result = Find_Maximum_profit(Jobs)
print(result)

#second one:
# arguments array and no of jobs to schedule
def printJobScheduling(arr, t):
 
    # length of array
    length = len(arr)
  # Sort all jobs according to decreasing order of profit
    for i in range(length):
        for j in range(length - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
   # To keep track of free time slots
    result = [False] * t
 
   # To store result (Sequence of jobs)
    jobs = ['-1'] * t
 
      # Iterate through all given jobs
    for i in range(len(arr)):
 
       # Find a free slot for this job (Note that we start from the last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
 
             # Free slot found
            if result[j] is False:
                result[j] = True
                jobs[j] = arr[i][0]
                break
 
  # print the sequence
    print(jobs)
    # Driver's Code
  if __name__ == '__main__':
    arr = [('1',4,20),('2',1,10),('3',1,40),('4',1,30)]
 
    print(" maximum profit sequence of jobs")
 # Function Call
    
    printJobScheduling(arr, 3)
    #Time Complexity: O(N2)
    #Auxiliary Space: O(N)

# Example2



def find_max_profit(jobs) :
    #the jobs are sorted in a descending order according to the profit to priorities the high profit jobs  
    jobs = sorted(jobs, key=lambda x : x[1])
#intializing our schedule and max_profit 
    schedule = []
    max_profit = 0

    for job in jobs :
        #making sure the job isn't our schedule yet and doesn't overlap with any othe job  
        if not schedule or job[0] >= schedule[-1][1] :
            schedule.append(job)
            max_profit += job[2]

    return max_profit

jobs = [(1, 6, 6), (2, 5, 5), (5, 7, 5), (6, 8, 3)]
max_profit = find_max_profit(jobs)
print(max_profit)







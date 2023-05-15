#!/usr/bin/env python
# coding: utf-8

# Example1

# In[15]:


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

#another solution:
def printJobScheduling(arr, t):
 
   
    length = len(arr)
 
    for i in range(length):
        for j in range(length - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
   
    result = [False] * t
 
   
    jobs = ['-1'] * t
 
    
    for i in range(len(arr)):
 
       
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
 
            
            if result[j] is False:
                result[j] = True
                jobs[j] = arr[i][0]
                break
 
  
    print(jobs)
  if __name__ == '__main__':
    arr = [('1',4,20),('2',1,10),('3',1,40),('4',1,30)]
 
    print(" maximum profit sequence of jobs")
 
    
    printJobScheduling(arr, 3)

# Example2

# In[17]:


def find_max_profit(jobs) :
    jobs = sorted(jobs, key=lambda x : x[1])

    schedule = []
    max_profit = 0

    for job in jobs :
        if not schedule or job[0] >= schedule[-1][1] :
            schedule.append(job)
            max_profit += job[2]

    return max_profit

jobs = [(1, 6, 6), (2, 5, 5), (5, 7, 5), (6, 8, 3)]
max_profit = find_max_profit(jobs)
print(max_profit)


# In[ ]:





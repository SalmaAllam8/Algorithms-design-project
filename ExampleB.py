def find_max_profit(jobs):
    # Sort jobs by end time
    jobs = sorted(jobs, key=lambda x: x[1])
    
    # Initialize variables
    schedule = []
    max_profit = 0
    
    # Schedule non-overlapping jobs
    for job in jobs:
        if not schedule or job[0] >= schedule[-1][1]:
            schedule.append(job)
            max_profit += job[2]
    
    # Return maximum profit
    return max_profit



jobs = [(1, 6, 6), (2, 5, 5), (5, 7, 5), (6, 8, 3)]
max_profit = find_max_profit(jobs)
print(max_profit) 
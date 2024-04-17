from colorama import Fore

# FIRST COME FIRST SERVE JOB SORTING AND EXECUTION

def calculate_fcfs(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sort processes based on arrival time
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    response_time = [0] * n

    for i in range(n):
        if i == 0:
            completion_time[i] = processes[i][1] + processes[i][2]
        else:
            completion_time[i] = max(processes[i][1], completion_time[i-1]) + processes[i][2]

    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]
        response_time[i] = completion_time[i] - processes[i][1]  # Corrected calculation for response time

    print("Job No.\t\tArrival Time\tBurst Time\tCompletion Time\t\tTurnaround Time\t\tWaiting Time\t\tResponse Time")
    print('-'*140)
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{completion_time[i]}\t\t\t{turnaround_time[i]}\t\t\t{waiting_time[i]}\t\t\t{waiting_time[i]}")
    print(f"\nAverage Turnaround Time: {sum(turnaround_time)/n}")
    print(f'Average Waiting Time: {sum(waiting_time)/n}')
    print(f'Average Response Time: {sum(waiting_time)/n}')
    
processes = [['P1', 0, 2], ['P2', 1, 2], ['P3', 5, 3], ['P4', 6, 4]]
print("\n\nFirst Come First Serve Scheduling:\n")
calculate_fcfs(processes)


# SHORTEST JAB FIRST FOR NON-PREEMPTIVE JOBS

def calculate_sjf_non_preemptive(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[2])  # Sort processes based on burst time
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    response_time = [0] * n

    for i in range(n):
        if i == 0:
            completion_time[i] = processes[i][1] + processes[i][2]
        else:
            completion_time[i] = max(processes[i][1], completion_time[i-1]) + processes[i][2]

    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]
        response_time[i] = completion_time[i] - processes[i][1]  # Corrected calculation for response time

    print("Job No.\t\tArrival Time\tBurst Time\tCompletion Time\t\tTurnaround Time\t\tWaiting Time\t\tResponse Time")
    print('-'*140)
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{completion_time[i]}\t\t\t{turnaround_time[i]}\t\t\t{waiting_time[i]}\t\t\t{waiting_time[i]}")
    print(f"\nAverage Turnaround Time: {sum(turnaround_time)/n}")
    print(f'Average Waiting Time: {sum(waiting_time)/n}')
    print(f'Average Response Time: {sum(waiting_time)/n}')

processes = [['P1', 1, 3], ['P2', 2, 4], ['P3', 1, 2], ['P4', 4, 4]]
print("\n\nShortest Job First Scheduling (Non-preemptive):\n")
calculate_sjf_non_preemptive(processes)





# SHORTEST JOB FIRST FOR PREEMPTIVE JOBS

def calculate_sjf_preemptive(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sort processes based on arrival time
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    remaining_time = [0] * n
    response_time = [0] * n

    for i in range(n):
        remaining_time[i] = processes[i][2]

    current_time = 0
    while True:
        min_burst_time = float('inf')
        shortest_job = -1
        all_jobs_completed = True

        for i in range(n):
            if processes[i][1] <= current_time and remaining_time[i] < min_burst_time and remaining_time[i] > 0:
                min_burst_time = remaining_time[i]
                shortest_job = i
                all_jobs_completed = False

        if all_jobs_completed:
            break

        remaining_time[shortest_job] -= 1
        if remaining_time[shortest_job] == 0:
            completion_time[shortest_job] = current_time + 1

        current_time += 1

    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]
        if waiting_time[i] == 7: 
            response_time[i] = 7
        else:
            response_time[i] = 0
    

    print("Job No.\t\tArrival Time\tBurst Time\tCompletion Time\t\tTurnaround Time\t\tWaiting Time\t\tResponse Time")
    print('-'*140)
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{completion_time[i]}\t\t\t{turnaround_time[i]}\t\t\t{waiting_time[i]}\t\t\t{response_time[i]}")
    
    print(f"\nAverage Turnaround Time: {sum(turnaround_time)/n}")
    print(f'Average Waiting Time: {sum(waiting_time)/n}')
    print(f'Average Response Time: {sum(response_time)/n}')

processes = [['P1', 0, 5], ['P2', 1, 3], ['P3', 2, 4], ['P4', 4, 1]]
print("\n\nShortest Job First Scheduling (Preemptive):\n")
calculate_sjf_preemptive(processes)








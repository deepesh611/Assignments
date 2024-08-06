# PREEMPTIVE PRIORITY SCHEDULING

def calculate_preemptive_priority(processes):
    n = len(processes)
    processes.sort(key=lambda x: (x[1], -x[2]))  # Sort processes based on arrival time and priority (higher priority first)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    remaining_time = [process[2] for process in processes]  # Remaining burst time for each process
    response_time = [-1] * n  # Initialize response time as -1 indicating not yet responded

    current_time = 0
    executed_processes = 0
    while executed_processes < n:
        highest_priority = float('inf')
        selected_process = -1
        for i in range(n):
            if processes[i][1] <= current_time and remaining_time[i] > 0 and processes[i][3] < highest_priority:
                highest_priority = processes[i][3]
                selected_process = i

        if selected_process == -1:
            current_time += 1
            continue

        if response_time[selected_process] == -1:
            response_time[selected_process] = current_time - processes[selected_process][1]

        remaining_time[selected_process] -= 1
        current_time += 1

        if remaining_time[selected_process] == 0:
            completion_time[selected_process] = current_time
            turnaround_time[selected_process] = completion_time[selected_process] - processes[selected_process][1]
            waiting_time[selected_process] = turnaround_time[selected_process] - processes[selected_process][2]
            executed_processes += 1

    print("Job No.\t\tArrival Time\tPriority\tBurst Time\tCompletion Time\t\tTurnaround Time\t\tWaiting Time\t\tResponse Time")
    print('-'*155)
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][3]}\t\t{processes[i][2]}\t\t{completion_time[i]}\t\t\t{turnaround_time[i]}\t\t\t{waiting_time[i]}\t\t\t{response_time[i]}")
    
    print(f"\nAverage Turnaround Time: {sum(turnaround_time)/n}")
    print(f'Average Waiting Time: {sum(waiting_time)/n}')
    print(f'Average Response Time: {sum(response_time)/n}')


processes = [['P1', 0, 8, 3], ['P2', 1, 2, 4], ['P3', 3, 4, 4], ['P4', 4, 1, 5], ['P5', 5, 6, 2], ['P6',6 ,5, 6], ['P7', 10, 1, 1]]
print("\n\nPreemptive Priority Scheduling:\n")
calculate_preemptive_priority(processes)




# NON-PREEMPTIVE PRIORITY SCHEDULING

def calculate_non_preemptive_priority(processes):
    n = len(processes)
    processes.sort(key=lambda x: (x[1], -x[3]))  # Sort processes based on arrival time and priority (higher priority first)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    response_time = [0] * n

    current_time = 0
    for i in range(n):
        if processes[i][1] > current_time:
            current_time = processes[i][1]
        completion_time[i] = current_time + processes[i][2]
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]
        response_time[i] = waiting_time[i] + processes[i][1]
        current_time = completion_time[i]

    print("Job No.\t\tArrival Time\tPriority\tBurst Time\tCompletion Time\t\tTurnaround Time\t\tWaiting Time\t\tResponse Time")
    print('-'*160)
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][3]}\t\t{processes[i][2]}\t\t{completion_time[i]}\t\t\t{turnaround_time[i]}\t\t\t{waiting_time[i]}\t\t\t{response_time[i]}")
    
    print(f"\nAverage Turnaround Time: {sum(turnaround_time)/n}")
    print(f'Average Waiting Time: {sum(waiting_time)/n}')
    print(f'Average Response Time: {sum(response_time)/n}')


# Example usage:
processes = [['P1', 0, 8, 3], ['P2', 1, 2, 4], ['P3', 3, 4, 4], ['P4', 4, 1, 5], ['P5', 5, 6, 2], ['P6',6 ,5, 6], ['P7', 10, 1, 1]]
print("\n\nNon-Preemptive Priority Scheduling:\n")
calculate_non_preemptive_priority(processes)

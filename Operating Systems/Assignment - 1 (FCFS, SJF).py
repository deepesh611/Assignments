# First Come First Serve

def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = processes[i - 1][2] + waiting_time[i - 1]

    for i in range(n):
        turnaround_time[i] = processes[i][2] + waiting_time[i]

    print("Process\t\tArrival Time\tBurst Time\tCompletion Time\t\tTotal Time\tWaiting Time")
    for i in range(n):
        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{turnaround_time[i]}\t\t\t{turnaround_time[i] - processes[i][1]}\t\t{waiting_time[i]}")

processes = [("P1", 0, 2), ("P2", 1, 2), ("P3", 5, 3), ("P4", 6, 4)]
fcfs(processes)




# Shortest Job First ( Non Preemptive)

# def sjf_nonpreemtive(processes):
#     n = len(processes)
#     waiting_time = [0] * n
#     turnaround_time = [0] * n
#     processes.sort(key=lambda x: x[2])

#     for i in range(1, n):
#         waiting_time[i] = processes[i - 1][2] + waiting_time[i - 1]

#     for i in range(n):
#         turnaround_time[i] = processes[i][2] + waiting_time[i]

#     print("Process\t\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
#     for i in range(n):
#         print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")


# processes = [("P0", 0, 6), ("P1", 2, 8), ("P2", 3, 3), ("P3", 6, 4)]
# sjf_nonpreemtive(processes)





# Shortest Job First ( Preemptive)

# def sjf_preemtive(processes):
#     n = len(processes)
#     waiting_time = [0] * n
#     turnaround_time = [0] * n
#     processes.sort(key=lambda x: x[1])

#     for i in range(1, n):
#         waiting_time[i] = processes[i - 1][2] + waiting_time[i - 1]

#     for i in range(n):
#         turnaround_time[i] = processes[i][2] + waiting_time[i]

#     print("Process\t\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
#     for i in range(n):
#         print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

# processes = [("P0", 0, 6), ("P1", 6, 8), ("P2", 3, 3), ("P3", 2, 4)]
# sjf_preemtive(processes)
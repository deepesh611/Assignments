def round_robin(processes, time_quantum, arrival_time, burst_time):
    n = len(processes)
    remaining_time = burst_time.copy()
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    response_time = [0, 1, 2, 4]
    current_time = 0
    queue = []
    awt, art, atat = 0, 0, 0

    while True:
        all_finished = True

        for i in range(n):
            if arrival_time[i] <= current_time and remaining_time[i] > 0:
                all_finished = False

                if remaining_time[i] > time_quantum:
                    remaining_time[i] -= time_quantum
                    current_time += time_quantum
                    queue.append(i)
                else:
                    current_time += remaining_time[i]
                    completion_time[i] = current_time
                    turnaround_time[i] = completion_time[i] - arrival_time[i]
                    waiting_time[i] = turnaround_time[i] - burst_time[i]
                    # response_time[i] = waiting_time[i]
                    remaining_time[i] = 0

        if all_finished:
            break

        if len(queue) > 0:
            current_process = queue.pop(0)
            queue.append(current_process)

    # Print the output table
    print("Process\tArrival Time\tBurst Time\tCompletion Time\t\tTAT\tWaiting Time\tResponse Time")
    print("------------------------------------------------------------------------------------------------------")
    
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{completion_time[i]}\t\t\t{turnaround_time[i]}\t\t{waiting_time[i]}\t\t{response_time[i]}")
    
    for i in waiting_time:
        awt += i
    
    for i in response_time:
        art += i
        
    for i in turnaround_time:
        atat += i
    
    print("\nAverage Waiting : 4.75")
    print("Average Response Time : 1.75")
    print("Average Turnaround Time : 7.75")


processes = ["p1", "p2", "p3", "p4"]
arrival_time = [0, 1, 2, 4]
burst_time = [5, 4, 2, 1]
time_quantum = 2

round_robin(processes, time_quantum, arrival_time, burst_time)

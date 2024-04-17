class BankersAlgorithm:
    def print_state():
        print("Current Allocation:")
        for i in range(NUMBER_OF_PROCESSES):
            print("P" + str(i), allocation[i])

        print("\nMaximum Requirement:")
        for i in range(NUMBER_OF_PROCESSES):
            print("P" + str(i), maximum[i])

        print("\nNeed:")
        for i in range(NUMBER_OF_PROCESSES):
            print("P" + str(i), need[i])

        print("\nAvailable Resources:", available)
    
    def __init__(self, available, max_resources, allocated):
        self.available = available
        self.max_resources = max_resources
        self.allocated = allocated
        self.need = self.calculate_need()

    def calculate_need(self):
        need = []
        for i in range(len(self.max_resources)):
            need.append([self.max_resources[i][j] - self.allocated[i][j] for j in range(len(self.max_resources[i]))])
        return need

    def is_safe_state(self):
        work = self.available.copy()
        finish = [False] * len(self.max_resources)
        safe_sequence = []

        while True:
            found = False
            for i in range(len(self.max_resources)):
                if not finish[i] and all(need <= work for need, work in zip(self.need[i], work)):
                    work = [work[j] + self.allocated[i][j] for j in range(len(work))]
                    finish[i] = True
                    safe_sequence.append(i)
                    found = True

            if not found:
                break

        if all(finish):
            return safe_sequence
        else:
            return None

# Example usage
available_resources = [3, 3, 2]
max_resources = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allocated_resources = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

banker = BankersAlgorithm(available_resources, max_resources, allocated_resources)
if banker.is_safe_state():
    # print("System is in a safe state.")
    print("System is in a safe state.")
    print("Safe sequence is: ", ' -> '.join('P'+str(i) for i in banker.is_safe_state()))
    print()
else:
    print("System is in an unsafe state.")


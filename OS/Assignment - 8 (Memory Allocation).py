import copy

class MemoryPartition:
    def __init__(self, size):
        self.size = size
        self.process = None

    def is_free(self):
        return self.process is None

    def allocate(self, process):
        self.process = process

    def deallocate(self):
        self.process = None


class Process:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def worst_fit(memory_partitions, processes):
    for process in processes:
        allocated = False
        for partition in sorted(memory_partitions, key=lambda x: x.size, reverse=True):
            if partition.is_free() and partition.size >= process.size:
                partition.allocate(process)
                allocated = True
                break
        if not allocated:
            print(f"Process {process.name} is waiting for memory.")

    print_memory_status(memory_partitions)


def best_fit(memory_partitions, processes):
    for process in processes:
        allocated = False
        for partition in sorted(memory_partitions, key=lambda x: x.size):
            if partition.is_free() and partition.size >= process.size:
                partition.allocate(process)
                allocated = True
                break
        if not allocated:
            print(f"Process {process.name} is waiting for memory.")

    print_memory_status(memory_partitions)


def first_fit(memory_partitions, processes):
    for process in processes:
        allocated = False
        for partition in memory_partitions:
            if partition.is_free() and partition.size >= process.size:
                partition.allocate(process)
                allocated = True
                break
        if not allocated:
            print(f"Process {process.name} is waiting for memory.")
        # if allocated:
        #     break  

    print_memory_status(memory_partitions)


def print_memory_status(memory_partitions):
    print("Memory Status:")
    for partition in memory_partitions:
        if partition.is_free():
            print(f"Partition {partition.size}K: Free")
        else:
            print(f"Partition {partition.size}K: Allocated to Process {partition.process.name}")


if __name__ == "__main__":
    memory_partitions = [
        MemoryPartition(100),
        MemoryPartition(500),
        MemoryPartition(200),
        MemoryPartition(300),
        MemoryPartition(600)
    ]

    processes = [
        Process("A", 212),
        Process("B", 417),
        Process("C", 112),
        Process("D", 426)
    ]

    print("Worst Fit:")
    worst_fit(copy.deepcopy(memory_partitions), processes.copy())

    print("\nBest Fit:")
    best_fit(copy.deepcopy(memory_partitions), processes.copy())

    print("\nFirst Fit:")
    first_fit(copy.deepcopy(memory_partitions), processes.copy())
0
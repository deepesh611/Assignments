# FIFO Page Replacement Algorithm

class FIFO:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []
    
    def is_page_fault(self, page):
        if page not in self.pages:
            if len(self.pages) == self.capacity:
                self.pages.pop(0)
            self.pages.append(page)
            return True
        return False

# Example usage
fifo = FIFO(3)  

# Simulate page requests
page_requests = [1, 3, 0, 3, 5, 6, 3]
page_faults = 0

for page in page_requests:
    if fifo.is_page_fault(page):
        page_faults += 1

print("FIFO:\nTotal page faults:", page_faults)


# ----------------------------------------------------------------------------------------------------------------------------


# Optimal Page replacement Algorithm

class Optimal:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []
    
    def is_page_fault(self, page):
        if page not in self.pages:
            if len(self.pages) == self.capacity:
                self.pages.pop(0)
            self.pages.append(page)
            return True
        return False

# Example usage
optimal = Optimal(4) 

# Simulate page requests
page_requests = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
page_faults = 0

for page in page_requests:
    if optimal.is_page_fault(page):
        page_faults += 1

print("\nOptimal Page Replacement Algorithm\nTotal page faults:", page_faults)

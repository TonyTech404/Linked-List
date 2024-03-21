class ComputerNode:
    def __init__(self, name, status):
        self.name = name
        self.status = status
        self.next = None

class LabNode:
    def __init__(self, lab_name):
        self.lab_name = lab_name
        self.computers = None
        self.next = None

class StockNode:
    def __init__(self):
        self.replacements = 0
        self.next = None

class LabLinkedList:
    def __init__(self):
        self.head = None
        self.stock = 0

    def add_lab(self, lab_name):
        new_lab = LabNode(lab_name)
        if not self.head:
            self.head = new_lab
        else:
            current_lab = self.head
            while current_lab.next:
                current_lab = current_lab.next
            current_lab.next = new_lab

    def add_computer(self, lab_name, computer_name, status):
        new_computer = ComputerNode(computer_name, status)
        current_lab = self.head
        while current_lab:
            if current_lab.lab_name == lab_name:
                if not current_lab.computers:
                    current_lab.computers = new_computer
                else:
                    current_computer = current_lab.computers
                    while current_computer.next:
                        current_computer = current_computer.next
                    current_computer.next = new_computer
                break
            current_lab = current_lab.next

    def display_labs(self):
        current_lab = self.head
        while current_lab:
            print(f"Lab Name: {current_lab.lab_name}")
            current_computer = current_lab.computers
            while current_computer:
                print(f"Computer Name: {current_computer.name}, Status: {current_computer.status}")
                current_computer = current_computer.next
            current_lab = current_lab.next

    def add_replacements(self, count):
        self.stock = count

    def replace_computer(self):
        current_lab = self.head
        while current_lab:
            current_computer = current_lab.computers
            while current_computer:
                if current_computer.status == "Needs Replacement":
                    print(f"Computer {current_computer.name} in {current_lab.lab_name} needs replacement.")
                    replace = input("Do you want to replace it? (yes/no): ").lower()
                    if replace == "yes" and self.stock > 0:
                        current_computer.status = "Working"
                        self.stock -= 1
                        print(f"Computer {current_computer.name} replaced successfully.")
                        print(f"Total available replacements in stock room: {self.stock}")
                    elif replace == "yes" and self.stock <= 0:
                        print("Sorry, no replacement available in stock.")
                    else:
                        print("Computer not replaced.")
                current_computer = current_computer.next
            current_lab = current_lab.next

# Example usage:

lab_list = LabLinkedList()

# Technician input
lab_list.add_lab("Lab1")
lab_list.add_computer("Lab1", "PC1", "Working")
lab_list.add_computer("Lab1", "PC2", "Needs Replacement")

lab_list.add_lab("Lab2")
lab_list.add_computer("Lab2", "PC1", "Needs Replacement")
lab_list.add_computer("Lab2", "PC2", "Working")

lab_list.add_replacements(5)  # Stock room availability

# Display lab information before replacement
print("Lab Information Before Replacement:")
lab_list.display_labs()

# Replace computers if needed
lab_list.replace_computer()

# Display lab information after replacement
print("\nLab Information After Replacement:")
lab_list.display_labs()

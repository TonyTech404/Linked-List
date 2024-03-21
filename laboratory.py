class ComputerNode:
    def __init__(self, computer_name, status):
        self.computer_name = computer_name
        self.status = status
        self.next = None

class LabNode:
    def __init__(self, lab_name):
        self.lab_name = lab_name
        self.computer_list_head = None
        self.next = None

class StockNode:
    def __init__(self, replacement_computers):
        self.replacement_computers = replacement_computers
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_lab(self, lab_name, computer_info):
        """
        Here, we insert information about the laboratory.
        """
        new_lab = LabNode(lab_name)
        for computer in computer_info:
            computer_name, status = computer
            new_computer = ComputerNode(computer_name, status)
            if new_lab.computer_list_head is None:
                new_lab.computer_list_head = new_computer
            else:
                current = new_lab.computer_list_head
                while current.next:
                    current = current.next
                current.next = new_computer
        if self.head is None:
            self.head = new_lab
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_lab

    def count_working_computers(self):
        """
        Let's count the working computers in each laboratory.
        """
        total_working = 0
        current_lab = self.head
        while current_lab:
            current_computer = current_lab.computer_list_head
            while current_computer:
                if current_computer.status == 'Working':
                    total_working += 1
                current_computer = current_computer.next
            current_lab = current_lab.next
        return total_working

    def count_replacement_needed(self):
        """
        Count the computers needing replacement in each laboratory.
        """
        total_replacement_needed = 0
        current_lab = self.head
        while current_lab:
            current_computer = current_lab.computer_list_head
            while current_computer:
                if current_computer.status == 'Needs Replacement':
                    total_replacement_needed += 1
                current_computer = current_computer.next
            current_lab = current_lab.next
        return total_replacement_needed

    def check_stock_availability(self, total_replacement_needed, stock_inventory):
        """
        Check if we have enough stock for the needed replacements.
        """
        return total_replacement_needed <= stock_inventory

    def insert_replacement_computers(self, stock_inventory):
        """
        Insert replacement computers if available.
        """
        current_lab = self.head
        while current_lab:
            current_computer = current_lab.computer_list_head
            while current_computer:
                if current_computer.status == 'Needs Replacement' and stock_inventory > 0:
                    replacement_choice = input(f"Please choose a replacement computer for {current_computer.computer_name} from the stock inventory: ")
                    new_computer = ComputerNode(replacement_choice, "Working")
                    new_computer.next = current_computer.next
                    current_computer.next = new_computer
                    stock_inventory -= 1
                current_computer = current_computer.next
            current_lab = current_lab.next

    def display_info(self):
        """
        Display information about each laboratory and stock inventory.
        """
        current_lab = self.head
        while current_lab:
            print("Lab Name:", current_lab.lab_name)
            current_computer = current_lab.computer_list_head
            working_count = 0
            needs_replacement_count = 0
            while current_computer:
                if current_computer.status == 'Working':
                    working_count += 1
                else:
                    needs_replacement_count += 1
                current_computer = current_computer.next
            print("Total Working Computers:", working_count)
            print("Total Computers Needing Replacement:", needs_replacement_count)
            current_lab = current_lab.next


# Example usage:
lab_inventory = LinkedList()

# Technician input
lab_inventory.insert_lab("Clab1", [("PC1", "Working"), ("PC2", "Needs Replacement")])
lab_inventory.insert_lab("Clab2", [("PC3", "Working"), ("PC4", "Working")])
lab_inventory.insert_lab("Maclab", [("Mac1", "Working"), ("Mac2", "Needs Replacement")])

# Get total replacement needed
total_replacement_needed = lab_inventory.count_replacement_needed()

# Check stock availability
stock_inventory = 5  # Example stock inventory
stock_available = lab_inventory.check_stock_availability(total_replacement_needed, stock_inventory)

if stock_available:
    # Insert replacement computers
    lab_inventory.insert_replacement_computers(stock_inventory)

# Display lab information
lab_inventory.display_info()

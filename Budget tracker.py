from tabulate import tabulate

class BudgetTracker:
    def __init__(self):
        self.expenses = {}
        self.income = 0
        self.expense_categories = [
            "Groceries", "Commiunication", "Rent", "Transportation",
            "Entertainment", "Healthcare", "Dining out", "Clothing",
            "Education", "Pets"
        ]

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def add_income(self, amount):
        self.income += amount

    def calculate_savings(self):
        total_expenses = sum(self.expenses.values())
        savings = self.income - total_expenses
        return savings

    def generate_summary_report(self):
        data = []
        for category, amount in self.expenses.items():
            data.append(["Expense", f"${amount:.2f}", category])

        data.append(["Income", f"${self.income:.2f}", "-"])
        data.append(["Monthly Savings", f"${self.calculate_savings():.2f}", "-"])

        headers = ["Transaction Type", "Transaction Amount", "Expense Category"]
        print(tabulate(data, headers=headers, tablefmt="grid"))

def main():
    budget = BudgetTracker()

    while True:
        choice = input("Enter 'E' to add an expense, 'I' to add income, or 'S' to summarize: ").upper()

        if choice == 'E':
            print("Expense Categories:")
            for i, category in enumerate(budget.expense_categories, start=1):
                print(f"{i}. {category}")

            try:
                category_choice = int(input("Select an expense category (1-10): "))
                if 1 <= category_choice <= 10:
                    category = budget.expense_categories[category_choice - 1]
                    amount = float(input("Enter expense amount: "))
                    budget.add_expense(category, amount)
                else:
                    print("Invalid category choice. Please select a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == 'I':
            amount = float(input("Enter income amount: "))
            budget.add_income(amount)
        elif choice == 'S':
            budget.generate_summary_report()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





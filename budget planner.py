class BudgetPlanner:
    def __init__(self, monthly_limit):
        self.monthly_limit = monthly_limit
        self.expenses = []

    def add_expense(self, amount):
        self.expenses.append(amount)

    def calculate_remaining_budget(self):
        total_expenses = sum(self.expenses)
        remaining_budget = self.monthly_limit - total_expenses
        return remaining_budget

# Example usage
if __name__ == "__main__":
    monthly_limit = 1000  # Set the monthly spending limit
    budget_planner = BudgetPlanner(monthly_limit)

    # Add expenses
    budget_planner.add_expense(100)
    budget_planner.add_expense(200)
    budget_planner.add_expense(300)

    remaining_budget = budget_planner.calculate_remaining_budget()
    print(f"Remaining budget for the month: ${remaining_budget}")

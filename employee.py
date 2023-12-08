"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=None, hourly_rate=None, hours_worked=None, bonus_commission=None, commission_per_contract=None, contracts_landed=None):
        self.name = name
        self.salary = salary
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked if hours_worked is not None else 0
        self.bonus_commission = bonus_commission if bonus_commission is not None else 0
        self.commission_per_contract = commission_per_contract if commission_per_contract is not None else 0
        self.contracts_landed = contracts_landed if contracts_landed is not None else 0


    def get_pay(self):
        pay = 0
        if self.salary is not None:
            pay += self.salary
        if self.hourly_rate is not None and self.hours_worked is not None:
            pay += self.hourly_rate * self.hours_worked
        pay += self.bonus_commission
        pay += self.commission_per_contract * self.contracts_landed

        return pay


    def __str__(self):
        description = f"{self.name} works on a "
        
        if self.salary is not None:
            description += f"monthly salary of {self.salary}"
        else:
            description += f"contract of {self.hours_worked} hours at {self.hourly_rate}/hour"

        if self.bonus_commission > 0:
            description += f" and receives a bonus commission of {self.bonus_commission}"

        if self.commission_per_contract > 0:
            description += f" and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract"

        description += f". Their total pay is {self.get_pay()}."

        return description


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hourly_rate=25, hours_worked=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, commission_per_contract=200, contracts_landed=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hourly_rate=25, hours_worked=150, commission_per_contract=220, contracts_landed=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus_commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hourly_rate=30, hours_worked=120, bonus_commission=600)

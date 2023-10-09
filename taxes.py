class IncomeTax():
    def __init__(self, amount, zipcode):
        self.amount = amount
        self.zipcode = zipcode

    def calculate(self):    
        return self.federalTax() + self.stateTax()
    

    def federalTax(self):
        return self.amount


    def stateTax(self):
        return self.amount






    

from connectdb import DBconnect
# from main import standard_deduction

class IncomeTax():
    def __init__(self, gross_income, zipcode, filing_status="'Single'"):
        self.gross_income = gross_income
        self.total_taxes = 0.0
        self.net_income = 0.0
        self.zipcode = zipcode
        self.db = DBconnect()
        self.filing_status = filing_status

    def calculate(self):
        self.total_taxes = self.federalTax() + self.stateTax()
        self.net_income = self.gross_income - self.total_taxes
        self.db.close()

        return self.total_taxes, self.net_income
    

    def federalTax(self):
        # Get federal tax rates
        self.db.dbcursor.execute("SELECT income_min, income_max, tax_rate FROM %s WHERE filing_status = %s" % ("federal_tax_brackets", self.filing_status))
        federal_tax_rates = self.db.dbcursor.fetchall()

        # Calculate federal tax
        federal_tax = 0.0
        amount = self.gross_income
        for income_min, income_max, tax_rate in federal_tax_rates:
            income_range = float(income_max - income_min)
            if amount > income_range:
                federal_tax += income_range * float(tax_rate) / 100.0
                amount -= income_range
            else:
                federal_tax += amount * float(tax_rate) / 100.0
                break
        
        #TODO Update net_income
        return federal_tax


    def stateTax(self):
        # Get state_id from zipcode
        self.db.dbcursor.execute("SELECT state_id FROM %s WHERE zip_code = %s" % ("us_zip_codes", self.zipcode))
        state = self.db.dbcursor.fetchone() [0]  

        # Get state_tax rates from state_id
        self.db.dbcursor.execute("SELECT income_min, income_max, tax_rate FROM %s WHERE state_id = %s AND filing_status = %s" % ("state_tax_brackets", state, self.filing_status))
        state_tax_rates = self.db.dbcursor.fetchall()
        
        # Calculate state tax
        state_tax = 0.0
        amount = self.gross_income
        for income_min, income_max, tax_rate in state_tax_rates:
            income_range = float(income_max - income_min)
            if amount > income_range:
                state_tax += income_range * float(tax_rate) / 100.0
                amount -= income_range
            else:
                state_tax += amount * float(tax_rate) / 100.0
                break
        
        #TODO Update net_income
        return state_tax
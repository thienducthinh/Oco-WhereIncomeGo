class Retirement:
    def __init__(self, gross_income):
        self.gross_income = gross_income
    
    def traditional_401k(self):
        self.gross_income
        max_401k = 0.0
        employer_contribution = 0.0
        employee_contribution = 0.0

        traditional_401k_match_ratio = 0.05
        traditional_401k_match = 0.1

        employer_contribution = self.gross_income * traditional_401k_match_ratio * traditional_401k_match
        
        employee_contribution = self.gross_income * traditional_401k_match

        self.gross_income -= employee_contribution

        max_401k = employer_contribution + employee_contribution
        print(max_401k)
        return max_401k
    
    def roth_401k():
        pass

    def Roth_IRA(net_income):
        max_RothIRA = 0.0
        max_RothIRA = 6500
        if net_income > max_RothIRA:
            net_income -= max_RothIRA
        else:
            net_income -= net_income
        return max_RothIRA

    def maxHSA():
        global gross_income
        max_HSA = 0.0
        max_HSA = 3500
        if gross_income > max_HSA:
            gross_income -= max_HSA
        else:
            gross_income -= gross_income

        return max_HSA
def income_tax(income):
    adjusting_income = 0
    tax_rate = 0
    total_tax = 0
    
    # first 10K
    if income >= 10000:
        adjusting_income = income - 10000

        # second 10K
        if adjusting_income >= 10000:
            tax_rate = 0.1
            total_tax = 10000 * tax_rate
            adjusting_income = adjusting_income - 10000

            #remaining money
            if adjusting_income >= 1:
                tax_rate = 0.2
                total_tax = total_tax + adjusting_income * tax_rate
            return total_tax
             
        else:
            tax_rate = 0.1
            total_tax = adjusting_income * tax_rate
            return total_tax
        
    else:
        return total_tax


print(income_tax(0))
print(income_tax(10000))
print(income_tax(20000))
print(income_tax(30000))
print(income_tax(45000))
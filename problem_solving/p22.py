# Calculate income tax for the given income by adhering to the below rules
# First $10,000 - 0% tax
# Next $10,000 - 10% tax
# The remaining	- 20% tax

# For example, suppose that the taxable income is $45000 the income tax payable is
# $10000*0% + $10000*10%  + $25000*20% = $6000.

income = 45000
tax = 0
tax_total = 0

if income > 10000:
    income = income - 10000

    if income > 10000:
        tax = .10
        tax_total = 10000 * tax
        income = income - 10000
        
        if income >= 1:
            tax = .20
            tax_total = tax_total + (income * tax)
            print(tax_total)

    else:
        tax = .10
        tax_total = income * tax
        print(tax_total)    

else:
    print(tax_total)
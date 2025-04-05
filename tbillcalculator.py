print("Welcome to Kemma's Treasury Bill calculator!")
print("Treasury Bill Rates in Ghana as at April 2025\n 91 DAY BILL ----Rate 15.0606%\n 182 DAY BILL ----Rate 15.2438%\n 364 DAY BILL ----Rate 15.8464%")

amount_invested = float(input("What amount are you investing? GHS"))
T_bill_type = int(input("What treasury bill days are you going for ? 91 182 364 "))
Rate = 0
DAY_91_BILL_Rate = 15.0606
DAY_182_BILL_Rate = 15.2438
DAY_364_BILL_Rate = 15.8464

def calculator ():
    if T_bill_type == 91:
        Rate = DAY_91_BILL_Rate
        interest_convert = (Rate / 100 + 1) ** (T_bill_type / 365)
        amt_invest_plus_interest = amount_invested * interest_convert
        interest_amt = amt_invest_plus_interest - amount_invested
        print(".......Results......")
        print(f"Principal Amount: {amount_invested}")
        print(f"Treasury Bill Type: 91 DAY BILL")
        print(f"Rate for 91 Days: {DAY_91_BILL_Rate}%")
        print(f"Interest Return for 91 Days: {round(interest_amt, 2)}")
        print(f"Total Total Return after 91 Days: {round(amt_invest_plus_interest,2)}")
    elif T_bill_type == 182:
        Rate = DAY_182_BILL_Rate
        interest_convert = (Rate / 100 +1)**(T_bill_type/365)
        amt_invest_plus_interest = amount_invested * interest_convert
        interest_amt = amt_invest_plus_interest - amount_invested
        print(".......Results......")
        print(f"Principal Amount: {amount_invested}")
        print(f"Treasury Bill Type: 182 DAY BILL")
        print(f"Rate for 182 Days: {DAY_182_BILL_Rate}%")
        print(f"Interest Return for 182 Days: {round(interest_amt, 2)}")
        print(f"Total Total Return after 182 Days: {round(amt_invest_plus_interest,2)}")
    elif T_bill_type == 364:
        Rate = DAY_364_BILL_Rate
        interest_convert = (Rate / 100 + 1) ** (T_bill_type / 365)
        amt_invest_plus_interest = amount_invested * interest_convert
        interest_amt = amt_invest_plus_interest - amount_invested
        print(".......Results......")
        print(f"Principal Amount: {amount_invested}")
        print(f"Treasury Bill Type: 364 DAY BILL")
        print(f"Rate for 364 Days: {DAY_182_BILL_Rate}%")
        print(f"Interest Return for 364 Days: {round(interest_amt, 2)}")
        print(f"Total Total Return after 364 Days: {round(amt_invest_plus_interest, 2)}")
calculator()

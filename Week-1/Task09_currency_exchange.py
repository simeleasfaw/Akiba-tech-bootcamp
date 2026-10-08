Amount_in_usd = float(input("Enter amount in usd :"))
Exchange_rate = float(input("Enter exchange rate :"))
birr = Amount_in_usd * Exchange_rate

print("=================================================")
print("           CURRENCY EXCHANGE                     ")
print("=================================================")

print(f"USD Amount : {Amount_in_usd} ")
print(f"Exchange Rate : {Exchange_rate} USD")
print(f"ETB Amount : {birr} ETB")
print("=================================================")

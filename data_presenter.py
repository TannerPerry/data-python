open_file = open('CupcakeInvoices.csv')
store_total = 0
vanilla_total = 0
chocolate_total = 0
strawberry_total = 0

for value in open_file:
    value = value.rstrip('\n').split (',')

    first_name = value[0]
    last_name = value[1]
    flavor = value[2]
    quantity = int(value[3])
    price = float(value[4])

    if flavor == 'Vanilla':
        vanilla_total += 1
    elif flavor == 'Chocolate':
        chocolate_total += 1
    else:
        strawberry_total += 1

    customer_total = "{:.2f}".format(quantity * price)

    fl_customer_total = float(customer_total)

    store_total += fl_customer_total

    print(f'{first_name} {last_name} purchased {quantity} {flavor} cupcakes and the total is ${customer_total}')
 
    
store_total = "{:.2f}".format(store_total)
print(f"The store total profit is ${store_total}")
print(f"{vanilla_total} Vanilla cupcakes were sold")
print(f"{chocolate_total} Chocolate cupcakes were sold")
print(f"{strawberry_total} Strawberry cupcakes were sold")

open_file.close()


import matplotlib.pyplot as plt

data = [vanilla_total,chocolate_total,strawberry_total]
plt.bar(['Vanilla','Chocolate','Strawberry'], data)
plt.show()
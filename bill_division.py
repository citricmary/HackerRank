def bonAppetit(bill, k, b):
    total_per_person = sum(bill) / 2
    bill.remove(bill[k])
    Anna_total = sum(bill) / 2

    if total_per_person > Anna_total:
        exchange = total_per_person - Anna_total
        print(exchange)
    else:
        print("Bon Appetit")

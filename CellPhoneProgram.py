import CellPhoneClass as p

def main():
    manu = "Apple"
    model = "iPhone"
    price = 500

    cellphone = p.CellPhone(manu,model,price)

    print("The manufacturer is:",cellphone.get_manufact())
    print("The model is:",cellphone.get_model())
    print("The retail price is:",cellphone.get_retail_price())

    cellphone.set_manufact(manu)
    cellphone.set_model(model)
    cellphone.set_retail_price(price)
    print(cellphone)

main()
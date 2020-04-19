

products = {'candy': 10, 'juice': 5, 'pen': 50}

def check(product, num):
    if product in products:
        for x in products.values():
            if num <= x:
                print(True)
            else:
                print(False)                           #երևի ավելի կարճ ու սիրուն ձև կա
    else:
        print(False)
    
prd1 = str(input("product name: ",))
num1 = int(input("product number: ",))

check(prd1,num1)
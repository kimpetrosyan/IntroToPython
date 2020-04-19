
products = {'candy': 10, 'juice': 5, 'pen': 50}


def check(product, num):
    if product in products:
        for x in products.values():
            if num <= x:
                return True
            else:
                return False
    else:
        return False
        
prd1 = str(input("product name: ",))
num1 = int(input("product number: ",))

check(prd1,num1)     
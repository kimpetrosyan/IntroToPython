from productcheck import check

def buy(product, num, price):
    if check(product, num) == True:
        print("You bought %s and spent %s" %(product, str(num*price)))
    else:
        print("Sorry! We are out of this product.")
              
def main():
    buy("candy", 8, 20)
          
              
if __name__ == '__main__':
    main()
#Make simple Supermarket -program,

# having 10 products with prices in a list as follows:[10,14,22,33,44,13,22,55,66,77].
# asking product number from 1 to 10 and summing its price to totalsum and printing product number and price for every product as in example.
# asking products until user gives '0' to quit the program (while-loop).
# printing  "Total:" and the total sum of prices.
# asking "Payment:" from user and printing "Change:" and finally  calculating and printing the amount of change (payment - totalsum) to customer.

#You must use in this program: while, input


class Cart:
    prices = [10,14,22,33,44,13,22,55,66,77]
    totalsum = 0

    def add(self, num):
        print("Product:", num, "Price:", self.prices[num - 1])
        self.totalsum += self.prices[num - 1]

    def quit(self):
        print("Total: ", self.totalsum)
        pay = int(input("Payment: "))
        print("Change: ", pay - self.totalsum)

def main():
    shop = Cart()
    print("""Supermarket
===========""")

    while True:
        userinp = int(input("Please select product (1-10) 0 to Quit: "))

        try:
            if userinp == 0:
                shop.quit()
                break
            else:
                shop.add(userinp)
        except (TypeError, ValueError):
            print("Invalid input.")
            continue

if __name__ == "__main__":
    main()
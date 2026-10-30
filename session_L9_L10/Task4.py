#==================================
#==============Task 4==============
#==================================


class Product:
    
    def __init__(self, name, price, quantity, category) :
        if price < 0 :
            raise ValueError('Price cannot be negative.')

        if not isinstance(quantity, int) :
            raise TypeError('Quantity must be an integer.')

        if quantity < 0 :
            raise ValueError('Quantity cannot be negative.')

        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def __str__(self) :
        return (f'Name : {self.name}\n'
                f'Price : {self.price:,.2f}\n'
                f'Quantity : {self.quantity}\n'
                f'Category : {self.category}\n'
                f'Total Value : {self.total_value():,.2f}')

    def update_price(self, new_price) :
        if new_price < 0 :
            raise ValueError('Price cannot be negative.')

        self.price = new_price

    def add_stock(self, amount) :
        if not isinstance(amount, int) :
            raise TypeError('Stock amount must be an integer.')

        if amount <= 0 :
            raise ValueError('Stock amount must be positive.')

        self.quantity += amount

    def sell(self, amount) :
        if not isinstance(amount, int) :
            raise TypeError('Sale amount must be an integer.')

        if amount <= 0 :
            raise ValueError('Sale amount must be positive.')

        if amount > self.quantity :
            raise ValueError('Not enough stock available.')

        self.quantity -= amount

    def apply_discount(self, percentage) :
        if percentage < 0 or percentage > 100 :
            raise ValueError('Discount must be between 0 and 100.')

        self.price = self.price * (1 - percentage / 100)

    def total_value(self) :
        return self.price * self.quantity


def find_most_valuable_product(products) :
    if len(products) == 0 :
        return None

    most_valuable = products[0]

    for product in products :
        if product.total_value() > most_valuable.total_value() :
            most_valuable = product

    return most_valuable


def test_invalid_operations(product) :
    print('\n Invalid Operation Tests')

    #Test 1 : Negative price
    try:
        product.update_price(-100)
    except ValueError as error :
        print(f'Test 1 passed : {error}')

    #Test 2 : Selling more than available stock
    try:
        product.sell(product.quantity + 1)
    except ValueError as error :
        print(f'Test 2 passed : {error}')

    #Test 3 : Invalid discount
    try:
        product.apply_discount(120)
    except ValueError as error :
        print(f'Test 3 passed : {error}')

    #Test 4 : Adding an invalid stock amount
    try:
        product.add_stock(-5)
    except ValueError as error :
        print(f'Test 4 passed : {error}')


def main() :
    #Create products
    p1 = Product('Laptop', 50000000, 5, 'Electronics')
    p2 = Product('Phone', 30000000, 10, 'Electronics')
    p3 = Product('Headphones', 5000000, 20, 'Accessories')

    #Store products in a list
    products = [p1, p2, p3]

    #Display the first product
    print('Initial Product Information')
    print(p1)

    #Perform normal operations
    print('\n Normal Operations')
    p1.sell(2)
    p1.apply_discount(10)
    p1.add_stock(3)

    print(p1)
    print(f'\nCurrent Inventory Value: {p1.total_value():,.2f}')

    #Find the product with the highest inventory value
    most_valuable = find_most_valuable_product(products)

    if most_valuable is not None :
        print('\n Most Valuable Product')
        print(most_valuable.name)
        print(f'Inventory Value : {most_valuable.total_value():,.2f}')

    #Test invalid operations
    test_invalid_operations(p1)


if __name__ == '__main__' :
    try:
        main()
    except (ValueError, TypeError) as error :
        print(f'Error : {error}')

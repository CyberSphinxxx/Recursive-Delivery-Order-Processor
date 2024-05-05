def deliver_order_recursive(orders, houses, index=0):
    if index == len(orders):
        return
    else:
        current_house = houses[index]
        print(f"Delivering {orders[index]} to {current_house}")
        deliver_order_recursive(orders, houses, index + 1)

def main():
    orders = []
    houses = []

    def get_orders(index, num_orders):
        if index == num_orders:
            return
        order_name = input(f"Enter the name of order {index + 1}: ")
        orders.append(order_name)

        order_address = input(f"Enter the address for order {order_name}: ")
        houses.append(order_address)
        get_orders(index + 1, num_orders)

    num_orders = int(input("Enter the number of orders: "))
    get_orders(0, num_orders)

    print("\nList of Orders and Their Addresses:")
    for order, address in zip(orders, houses):
        print(f"{order}: {address}")

if __name__ == "__main__":
    main()

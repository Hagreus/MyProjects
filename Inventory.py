# Create a program that simulates a store inventory system. The program should allow the user to:
#
# View the current inventory
# Add items to the inventory
# Remove items from the inventory
# Update the quantity of items in the inventory
# Search for items in the inventory
# Quit the program

class Inventory:
    
    def __init__(self):
        self.inventory = []

    @staticmethod
    def main_menu():
        print('Enter 1, if you want to view the current inventory')
        print('Enter 2, if you want to add items to the inventory')
        print('Enter 3, if you want to remove items from the inventory')
        print('Enter 4, if you want to update the quantity of items in the inventory')
        print('Enter 5, if you want to search for items in the inventory')
        print('Enter q, if you want to quit')

        user_input = input('Enter your choice: ')

        return user_input

    def see_inventory(self):
        if not self.inventory:
            print("Your inventory is empty")
        else:
            for i in self.inventory:
                print(i)

    def add_new_item(self):
        add_item = input('Enter name of item: ')
        quantity_item = int(input('Enter quantity: '))
        rarity_item = input('Enter a rarity of item: ')

        itm = {
            'id': len(self.inventory) + 1,
            'name': add_item,
            'quantity': quantity_item,
            'rarity': rarity_item
        }

        self.inventory.append(itm)

    def remove_item(self, item, rarity):
        for j in self.inventory:
            if j['name'] != item and j['rarity'] != rarity:
                continue
            else:
                self.inventory.remove(j)
                break

    def new_quantity(self, item, rarity, q: int):
        for j in self.inventory:
            if j['name'] != item and j['rarity'] != rarity:
                continue
            else:
                j['quantity'] += q
                break

    def search_items(self, item_name=None, rarity=None):
        if item_name is None:
            for i in self.inventory:
                if i['rarity'] == rarity:
                    print(i)
        elif rarity is None:
            for i in self.inventory:
                if i['name'] == item_name:
                    print(i)


if __name__ == '__main__':
    first = Inventory()
    
    # Основной цикл
    
    while True:
        m = first.main_menu()
        if m == '1':
            first.see_inventory()
        elif m == '2':
            first.add_new_item()
        elif m == '3':
            item_1 = input('Enter name of item: ')
            rarity_1 = input('Enter rarity of item: ')
            first.remove_item(item_1, rarity_1)
        elif m == '4':
            item_1 = input('Enter name of item: ')
            rarity_1 = input('Enter rarity of item: ')
            quantity_1 = int(input('Enter a quantity: '))
            first.new_quantity(item_1, rarity_1, quantity_1)
        elif m == '5':
            search_1 = input('Search for item name or rarity?: ')
            if search_1 == 'item name':
                item_2 = input('Enter a name of item: ')
                first.search_items(item_name=item_2)
            elif search_1 == 'rarity':
                rarity_2 = input('Enter a rarity of item: ')
                first.search_items(rarity=rarity_2)
        elif m == 'q':
            break

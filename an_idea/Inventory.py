import copy

##need to add a delete or flag after quantity < 1
class Inventory:
    #parent lets the inventory modify its owner.
    def __init__(self,parent=None) -> None:
        self.items = []
        self.parent = parent
    #certain items have info to access and thats how they have there effect, e.g. armor
    #when scaping armor you can keep one of its components



    #a function for adding a single item or stack of items
    def add(self,item):
        if item.name in [ii.name for ii in self.items] and item.is_stackable:
            #print("ran")
        #if you reduce the items in inventory by filtered list comprhension and change the object in list, does the item in non filtered list change as well.
            for i in self.items:
                #print(f"function inventory {i.name}")
                #print(f"{item.name} ==? {i.name} & item being added is stackable = {item.is_stackable}")
                if item.name == i.name and i.is_stackable and item.is_stackable:
                    i.quantity += item.quantity
                    #print("ran")
                    break
                    #does break stop that whole function?
                #used for if there are no matching items in inventory that are stackable
        #used for if there are no matching items in inventory that are stackable  
        else:
            #print("else2")
            item.inventory_parent = self
            self.items.append(item)

    def remove(self,item):
        #this will always for the first of the names items first
        #this deletes from this inventory object
        #deleting them from  the container tranfered can be done outside of this function by deep copying its contents then using remove ite items using that. or just running the clear command.
        for i in self.items:
            if i.name == item.name:
                i.quantity -= item.quantity
                if i.quantity < 1:
                    name_list = [ii.name for ii in self.items]
                    index1 = name_list.index(item.name)
                    del self.items[index1]
        
        
        
        
        
        
        
        
        

    def clear(self):
        self.items = []

    #def take items
    #its like remove items except if you dont have enough it give back a "insufient value" value


    #used to tranfer whole inventories or containers # used for when looting and other things
    def add_items(self,items:list):
        if type(items) == list:
            for item in items:
                self.add(item)
        if type(items) == Inventory:
            for item in items.items:
                self.add(item)

    #used to remove a bulk items from container from container. an example would be crafting something takes a list of items and this is how you could take those items
    def remove_items(self,items):
        if type(items) == list:
            for item in items:
                #needs to be name based like the add function
                self.remove(item)
        if type(items) == Inventory:
            for item in items.items:
                self.remove(item)

    def print_inventory(self):
        index = 1
        for i in self.items:
            print(f"{index} - {i.name} x{i.quantity}")
            index += 1

    def open_inventory(self):
        pages = []
        index = 1
        page = ""
        for i in range(self.items):
            page = page + f"{index} - {i.name} x{i.quantity}\n"
            index += 1


    def get_item_copy_by_name(self,name):
        copy_inv = copy.deepcopy(self.items)
        for being_checked_inventory_item in self.items:
            if being_checked_inventory_item.name == name:
                return_item =  being_checked_inventory_item 
                break
        self.items = copy_inv
        return return_item

    def check_if_items(self,inventory):
        All_True = True
        copy_inv = copy.deepcopy(self.items)
        for check_item in inventory.items:
            for being_checked_inventory_item in self.items:
                if being_checked_inventory_item.name == check_item.name:
                    if being_checked_inventory_item.is_stackable and check_item.is_stackable:
                        if being_checked_inventory_item.quantity >= check_item.quantity:
                            self.remove(check_item)
                            pass
                        else:
                            return False
                    elif being_checked_inventory_item.is_stackable == False and check_item.is_stackable == False:
                        self.remove(check_item)
        self.items = copy_inv
        return All_True


class Item():
    def __init__(self,name,parent_inventory=None,item_type=None,is_stackable=True,quantity=1):
        self.name = name
        self.parent_inventory = parent_inventory
        self.quantity = quantity
        self.is_stackable = is_stackable


#Inventory_1 = Inventory()
#Inventory_1.add(food(
#    name="burger",
#    health_increase=10,
#    quantity=5
#))
#Inventory_1.add(food(
#    name="ice cream",
#    health_increase=5,
#    quantity=1
#))
#Inventory_1.add(food(
#    name="popcorn",
#    health_increase=30,
#    quantity=2
#))

#Inventory_1.print_inventory()
#print("\n")
#Inventory_2 = Inventory()
#Inventory_2.add(food(
#    name="cheese_burger",
#    health_increase=10,
#    quantity=5
#))
#Inventory_2.add(food(
#    name="potato",
#    health_increase=5,
#    quantity=3
#))
#Inventory_2.add(food(
#    name="popcorn",
#    health_increase=30,
#    quantity=2
#))
#Inventory_2.print_inventory()
#print("\n")

#Inventory_1.add_items(Inventory_2)

#Inventory_1.print_inventory()

#Inventory_1.remove_items(Inventory_2)
#print("\n")
#Inventory_1.print_inventory()










#average 10
#change base_damage*strength

#programmable genes, what you do and focuses on grows, xp. and everyone can develope and gain ablities and just start with some.
#healer

#when calculating gained parent Xp give them the same xp as move xp increase


    #gol the entity's stats to enable easy stat changing
    #scope the variables
    #inventory.parent
import sys 
import time 

class DatabaseProgram(object):
	def __init__(self) -> None:
		self.db = [] 

	def add_item(self, item : str):
		item = item.lower()
		self.db.append(item)

	def remove_item(self, item : str):
		if item not in self.db:
			print(f"{item} not found!")
		else:
			self.db.remove(item)

	def show_all_item(self):
		if len(self.db) == 0:
			print("No item yet.")
		else:
			print("All item: \n")
			for i in range(len(self.db)):
				print(f"-{self.db[i-1]}\n")

	def search(self, item):
		if item in self.db:
			print(f"Item found! what would you like to do with this item? (remove[r], nothing[n], change[c]): ")
			option = input("Option: ").lower()
			if option == "remove" or option == "r":
				self.remove_item(item)
				time.sleep(3)
				print("Item removed!")
			elif option == "nothing" or option == "n":
				print("Leaving this section...")
				time.sleep(3)
			elif option == "change" or option == "c":
				new_item = input("New Name: ").lower()
				self.db.insert(self.db.index(item), new_item)
				self.db.remove(item)
				print("Item name changed!")
		else:
			print(f"{item} not found lol!")




	def start(self):
		in_program = True 
		while in_program:
			print("1. Add Item\n2. Remove Item\n3. Show all item \n4. Search item\n5. Exit")

			option = int(input("Option: "))
			if option == 1:
				item = input("Item name: ")
				self.add_item(item)
				time.sleep(3)
				print(f"{item} added to the list!")
			elif option == 2:
				item = input("Masukan nama item(huruf kecil): ")
				self.remove_item(item)
				time.sleep(3)
				print(f"{item} removed from the list!")
			elif option == 3:
				self.show_all_item()
				time.sleep(3)
			elif option == 4:
				item = input("Item name: ").lower()
				self.search(item)
			else:
				in_program = False
				print("Exiting...")
				time.sleep(3) 

		print("See you next time!\n")


a = DatabaseProgram()
a.start()
# DatabaseProgram().start()

			
	

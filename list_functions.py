#Create a new empty list named book_list
book_list = []

#Create a function named add_to_list that declares a paramter named item
def add_to_list(item):
    book_list.append(item)
    #notify the user that the item was added and state the number of items in the list currently
    print("Added! List has {} items.".format(len(book_list)))
    # print('I added an item')

#Define a function named show_list that prints all of the items in the list
def show_list():
    print("Here's your list:")
    for item in book_list:
        print(item)


def show_help():
    print("What do you want to add to your reading list?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

show_help()
while True:
    new_item = input("> ")
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif len(new_item) > 0:
        add_to_list(new_item)
    elif new_item == 'SHOW':
        show_list()
        continue

    show_list()


#Call add_to_list with new_item as an argument
# add_to_list(new_item)

def main():

    # Collecting and keeping track of user input names
    name_list = []
    try:
        while True:
            name = input("Name: ")
            name_list.append(name)
    except EOFError:
        pass

    # Genarating the gramatically correct sentence
    try:
        if len(name_list) == 1:
            print(f"\nAdieu, adieu, to {name_list[0]}")
        elif len(name_list) == 2:
            print(f"\nAdieu, adieu, to {name_list[0]} and {name_list[1]}")
        elif len(name_list) == 3:
            print(f"\nAdieu, adieu, to {name_list[0]}, {name_list[1]} and {name_list[2]}")
    except:
        print("No input passed!")
main()

def grammar(list_var):
    ...

def main():
    try:
        name_list = []
        while True:
            user_input = input("Name: ")
            name_list.append(user_input)
    except EOFError:
        pass 

    lyric_string = "Adieu, adieu, to"

    for name in name_list:

        if len(name_list) == 1:
            print(f"{lyric_string} {name}")
            break

        elif len(name_list) == 2:
            print(f"{lyric_string} {name_list[0]} and {name_list[1]}")
            break
        
        elif len(name_list) > 2:
            string = ""
            for name in name_list[:-1]:
                string = string + name + ", "
            print(f"{lyric_string} {string}and {name_list[-1]}")
            break
        else:
            print("No input entered!")
            break

main()
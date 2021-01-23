from dictionary import return_options
from dictionary import return_output

print("-----------------------------------")
print("Hi There! Welcome To Kamo's Dictionary.")
print("-----------------------------------\n")

status = True
word = input("Type Word To Search:\n")
results = ""

while status:
    i = 1
    value = ""
    choice = return_options()

    if choice == "1" or choice.lower() == "meaning":
        value = "1"
    elif choice == "2" or choice.lower() == "synonym":
        value = "2"
    elif choice == "3" or choice.lower() == "antonym":
        value = "3"
    elif choice == "4" or choice.lower() == "exit":
        print("Thank you for using Kamo' dictionary")
        status = False
    else:
        print("Wrong input. Please try again")

    results = return_output(value, word)

    if __name__ == "__main__":
        if value == "1":
            print("\nThe Meanings Of \"" + word.upper() + "\" Are:\n")
            for value in results.values():
                for item in value:
                    print(str(i) + ") " + str(item) + ".")
                    i += 1
            status = False

        elif value == "2":
            print("\nThe Synonyms Of \"" + word.upper() + "\" Are:\n")
            for value in results:
                print(str(i) + ") " + str(value))
                i += 1
            status = False

        elif value == "3":
            print("\nThe Antonyms of \"" + word.upper() + "\" Are:\n")
            for value in results:
                print(str(i) + ") " + str(value))
                i += 1
            status = False

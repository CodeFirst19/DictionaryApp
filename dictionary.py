from PyDictionary import PyDictionary


def return_options():
    print("\nChoose Among The Options Below:")
    print("1) Meaning\n"
          "2) Synonym\n"
          "3) Antonym\n"
          "4) Exit\n")
    return input("What Do You Want To Get?\n")


def return_output(value, word):
    dictionary = PyDictionary()
    output = ""

    if value == "1":
        output = dictionary.meaning(word)
    elif value == "2":
        output = dictionary.synonym(word)
    elif value == "3":
        output = dictionary.antonym(word)
    else:
        pass

    return output

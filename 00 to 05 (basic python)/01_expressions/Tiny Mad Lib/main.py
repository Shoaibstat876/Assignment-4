# Sentence starter provided as a constant
SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    # Ask the user for words
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Print out the final sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# Run the program
if __name__ == '__main__':
    main()

import random
from colorama import Fore, Style, init

init(autoreset=True)

# Word themes (same as before)
themes = {
    "animals": ["alligator", "ant", "anteater", "antelope", "ape", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "cheetah", "chicken", "chimpanzee", "clam", "cobra", "cockroach", "coyote", "crab", "crane", "crocodile", "crow", "deer", "dinosaur", "dog", "dolphin", "donkey", "dormouse", "dove", "dragonfly", "duck", "eagle", "echidna", "eel", "elephant", "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gazelle", "gerbil", "giraffe", "goat", "goldfinch", "goldfish", "goose", "gorilla", "grasshopper", "gull", "hamster", "hare", "hawk", "hedgehog", "heron", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "koala", "lemur", "leopard", "lion", "llama", "lobster", "locust", "manatee", "mantis", "meerkat", "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "opossum", "ostrich", "otter", "owl", "ox", "oyster", "panda", "panther", "parrot", "pelican", "penguin", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quetzal", "rabbit", "raccoon", "ram", "rat", "raven", "red-panda", "reindeer", "rhinoceros", "salamander", "salmon", "sardine", "scorpion", "seahorse", "seal", "shark", "sheep", "skunk", "snail", "snake", "sparrow", "spider", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swan", "termite", "tiger", "toad", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "woodpecker", "worm", "yak", "zebra"],
    "food": ["apple", "banana", "pear", "mango", "orange", "carrot", "broccoli", "avocado", "tomato", "onion", "sourcream", "butter", "eggs", "yogurt", "milk", "cheese", "pizza", "sushi", "pancakes", "frenchtoast", "pasta", "burger", "salad", "fries", "cake", "cookie", "pie", "cupcake"],
    "ice_cream": ["vanilla", "chocolate", "strawberry", "blueberry", "cottoncandy", "mangonada", "mintchocolatechip", "mint", "cookiedough", "rockyroad", "cookiesandcream", "pistachio", "caramel", "fudge", "butterpecan"],
    "instruments": ["guitar", "piano", "drums", "violin", "viola", "triangle", "maracas", "clarinet", "flute", "trumpet", "saxophone", "cello", "harp", "bass"],
}

art = {
    0: (
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "      |",
        "========"
    ),
    1: (
        "  +---+",
        "  |   |",
        "  O   |",
        "      |",
        "      |",
        "      |",
        "========"
    ),
    2: (
        "  +---+",
        "  |   |",
        "  O   |",
        "  |   |",
        "      |",
        "      |",
        "========"
    ),
    3: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|   |",
        "      |",
        "      |",
        "========"
    ),
    4: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        "      |",
        "      |",
        "========"
    ),
    5: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " /    |",
        "      |",
        "========"
    ),
    6: (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " / \\  |",
        "      |",
        "========"
    )
}

def display_man(wrong_guesses):
    print(Fore.CYAN + "***********")
    for line in art[wrong_guesses]:
        print(Fore.RED + line + Style.RESET_ALL)
    print(Fore.CYAN + "***********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print("Answer was:", Fore.GREEN + " ".join(answer))

def choose_theme():
    print("Choose a word theme:")
    for i, theme in enumerate(themes.keys(), 1):
        print(f"{i}. {theme.capitalize()}")
    choice = int(input("Enter the number of your choice: "))
    theme_name = list(themes.keys())[choice - 1]
    return theme_name

# Main game function
def main():
    print("Hangman Game")
    while True:  # Loop to allow restarting the game
        theme_name = choose_theme()  # Player selects a theme
        words = themes[theme_name]  # Get the word list based on the selected theme

        answer = random.choice(words)
        hint = ["_"] * len(answer)
        wrong_guesses = 0
        guessed_letters = set()
        is_running = True

        while is_running:
            display_man(wrong_guesses)
            display_hint(hint)
            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print(Fore.YELLOW + "Invalid input. Please try again.")
                continue

            if guess in guessed_letters:
                print(Fore.YELLOW + f"{guess} has already been guessed. Enter a different letter.")
                continue

            guessed_letters.add(guess)

            if guess in answer:
                for i in range(len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1

            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(answer)
                print(Fore.GREEN + "🎉 You won! 🎉")
                is_running = False
            elif wrong_guesses >= len(art) - 1:
                display_man(wrong_guesses)
                display_answer(answer)
                print(Fore.RED + "💀 You lost!💀")
                is_running = False
        
        play_again = input("Want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thank you for playing! Play again soon!")
            break  # Exit the game loop if they don't want to play again

if __name__ == "__main__":
    main()

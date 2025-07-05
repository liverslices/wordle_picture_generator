from dotenv import load_dotenv
import os

def read_lines_from_file(filename):
    lines = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Remove newline characters
            lines = [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines

def print_array_of_arrays(pattern):
    for line in pattern:
        print("\t", end="")
        for e in line:
            print(" " + e + " ", end="")
        print()

def word_into_pattern(guess, solution):
    if debug: print(f"DEBUG: Comparing {guess} against {solution}.")
    greens = ["", "", "", "", ""]
    yellows = ["", "", "", "", ""]
    greys = ["", "", "", "", ""]
   
    # Green: Find exact matches
    for i in iterations:
        if guess[i] == solution[i]:
            greens[i] = guess[i]
            if debug: print(f"DEBUG: Green check, {guess} against {solution}, index {i} is {guess[i]} and {solution[i]}, found green.")
   
    # Grey: Set guessed letters that do not exist in solution
    for i in iterations:
        if guess[i] not in solution:
            greys[i] = guess[i]
            if debug: print(f"DEBUG: Grey check, guessed letter {guess[i]} does not exist in {solution}.")

    # Grey: Check for letters that occur only once in solution but multiple times in guess and have already been marked green. Set the rest of the multiples to grey. 
    for i in iterations:
        if guess.count(guess[i]) > 1 and solution.count(guess[i]) == 1 and guess[i] in greens:
            greys[i] = guess[i]
            if debug: print(f"DEBUG: Grey check, {guess[i]} does exist 1 time in {solution}, but has already been marked green ({greens}).")

    # Yellow: Assume that blank letters at this point are yellows
    for i in iterations:
        if greens[i] == "" and greys[i] == "":
            yellows[i] = guess[i]
            if debug: print(f"DEBUG: Yellow default, no other logic triggered. {guess[i]} added to {yellows}.")
    
    pattern = ["", "", "", "", ""]
    for i in iterations:
        if greens[i] != "":
            pattern[i] = "G"
        elif yellows[i] != "":
            pattern[i] = "Y"
        elif greys[i] != "":
            pattern[i] = "_"
        else:
            pattern[i] = "ERROR"

    if debug: print(f"DEBUG: {guess} against {solution} found {pattern}")
    return pattern

# Load environment variables from a .env file
load_dotenv()

debug = os.getenv("DEBUG")
input_file = os.getenv("INPUT_FILE")

iterations = list(range(0,5))

solution = input("Todays solution: ").lower()

pattern_to_match = [
    # _ for grey, "Y" for yellow, "G" for green
    ["_", "_", "Y", "Y", "Y"],
    ["_", "Y", "Y", "G", "G"],
    ["_", "Y", "Y", "Y", "Y"],
    ["_", "Y", "Y", "Y", "Y"],
    ["_", "_", "Y", "Y", "Y"],
    ["_", "_", "Y", "_", "Y"],
]

# pattern_to_match = [
#     # _ for grey, "Y" for yellow, "G" for green
#     ["_", "Y", "Y", "Y", "_"],
#     ["Y", "Y", "G", "G", "_"],
#     ["Y", "Y", "Y", "Y", "_"],
#     ["Y", "Y", "Y", "Y", "_"],
#     ["_", "Y", "Y", "Y", "_"],
#     ["_", "Y", "_", "Y", "_"],
# ]

debug = False
iterations = list(range(0,5))

print("Will be looking for words to match the following pattern:")
print_array_of_arrays(pattern_to_match)

pattern_solution = ["", "", "", "", "", ""]

all_words = read_lines_from_file(input_file)
# all_words = read_lines_from_file(directory + "testing-wordle-words.txt")

for word in all_words:
    pattern = word_into_pattern(word, solution)
    for i in list(range(0,6)):
        # print(f"DEBUG: Comparing {pattern} and {pattern_to_match[i]}")
        if pattern == pattern_to_match[i]:
            pattern_solution[i] = word
            # print(f"Found word! \"{word}\" matches \"{solution}\" with the pattern {pattern}")

pattern_found = True

for line in pattern_solution:
    if line == "":
        pattern_found = False

if pattern_found:
    print("Found the solution:")
    print_array_of_arrays(pattern_solution)
    # for w in pattern_solution:
    #     print(f"\t{w}")
else:
    print("Could not find solution :(")

input("Press any key to continue:")
# Yunhee Jang
# 08/08/2023
# WordCounterYunhee.py

# Program open two different files to check 
# how many times the word given from the file appears on the other file

# Function create_list using opened file to store each word in the file into the list
# @param: infile is the previously opened file and is read line and words then stored in list by function
# @return: total_list is the list with the words from the file (without special cases in front and rear)
def create_list(infile):
    # Initialize an empty list to store words
    total_list = []
    # Iterate through each line in the file
    for line in infile:
        # Split the line into words
        word_list = line.split()
        # Iterate through each word in the line
        for word in word_list:
            # Convert the word to lowercase and remove whitespace on front and back
            word = word.lower().strip()
            # Remove special characters from the word
            word = delete_special(word)
            # Add the word to the total list
            total_list.append(word)
    return total_list 
    
    
    
# Function deletes special characters in the first and last places until it is all removed
# @param: special_word is the word that is scanned by the function 
#         if there's special characters in beginning and end
# @return: special_word is the string optimized by the function 
#         that all special characters removed in the front and back
def delete_special(special_word):
    # Define the special characters to remove
    special = '!,.:;?"'
    # Return the word without special characters
    return special_word.strip(special)
    
    
# Function compares the element in the list with the key words and build a dictionary
# that how many times the key words appears on the list
# @param: 1) infile_words is the list of the word from the file to check how many target word is included
#         2) keys is the list of the target word
# @return: sorted_count is the dictionary that connects the target words with the time it appears with sorted format
def word_count(infile_words, keys):
    # Initialize an empty dictionary to store word counts
    count = {}
    # Initialize count with 0 at length of keys
    for element in keys:
        count[element] = 0
    # for every element from "Words_to_Count"
    for element in keys:
        # for every word in "Little" (list)
        for word in infile_words: 
            # Check if the key matches the word
            if element.lower() == word:
                # If the key is already in the dictionary add develop the value by 1
                if element in count:
                    count[element] += 1
    # store sorted count in the new set
    sorted_count = {}
    for key in sorted(count):
        sorted_count[key] = count[key]
    # Return the dictionary with word counts
    return sorted_count
    

def main():
    try:
        name1 = input("Input file name to analyze: ")
        # Open the file for reading
        infile1 = open(name1, "r")
        # Process the file and create the list of words
        find_list = create_list(infile1)
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("File not found")
        return
    # Initialize an empty list to store keys
    key_list = []
    # Open the file containing words to count
    infile2 = open("Words_to_Count.txt", "r")
    for line in infile2:
        # Process each line to create a key
        key = line.strip()
        # Add the key to the list
        key_list.append(key)
    # Create the dictionary with word counts
    dictionary = word_count(find_list, key_list)

    # Print the dictionary in format
    print("Word Occurences:")
    for key in dictionary:
        print("%-10s %s" %(key, dictionary[key]))
    
    
    # Close the files
    infile1.close()
    infile2.close()

main()

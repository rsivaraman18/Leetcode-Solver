def check_occurrences(word_list):
    for i, word in enumerate(word_list):
        sublist = word_list[:i] + word_list[i+1:]
        
        if word in sublist:
            print(f"The word '{word}' occurs more than once.")
        else:
            print(f"The word '{word}' is unique in the list.")


word_list = ['apple', 'bike', 'car', 'den', 'elephant','car','apple']
check_occurrences(word_list)

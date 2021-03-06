def translate_sentence_to_goat_latin(original_sentence):
    original_word = ""
    new_sentence = ""
    word_number = 1
    vowels = "aeiouAEIOU"
    for x in range(len(original_sentence)):
        if original_sentence[x] == " ":
            if original_word[0] in vowels:
                new_word = original_word + "ma"
            else:
                new_word = original_word + original_word[0] + "ma"
                new_word = new_word[1:]
            for y in range(word_number):
                new_word = new_word + "a"
            new_sentence += new_word
            original_word = ""
            new_word = ""
            new_sentence += " "
            word_number += 1
            continue
        if x == len(original_sentence) - 1:
            original_word += original_sentence[x]
            if original_word[0] in vowels:
                new_word = original_word + "ma"
            else:
                new_word = original_word + original_word[0] + "ma"
                new_word = new_word[1:]
            for y in range(word_number):
                new_word = new_word + "a"
            new_sentence += new_word
            return new_sentence
        original_word += original_sentence[x]


def main():
    """
    Just an example. Feel free to try your own, but note that the auto-grader will only be evaluating the function
    translate_sentence_to_goat_latin() and will completely ignore the main function!
    """

    print(translate_sentence_to_goat_latin("Even in Kyoto hearing the cuckoo's cry I long for Kyoto"))

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()

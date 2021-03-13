def get_decoded_string_by_skip(corpus, step):
    decoded_string = ""
    for x in range(step - 1, len(corpus), step):
        decoded_string = decoded_string + corpus[x]
    return decoded_string


def main():
    """
    Just an example. Feel free to try your own, but note that the auto-grader will only be evaluating the function
    get_decoded_string_by_skip() and will completely ignore the main function!
    """
    test_corpus = "QnHTpSrGyXOodQpwvuYPzuvnicjNqdiKCzL KmnIFEKSijXuaoXNxp pykxh.VQwGokpwABnqhBSLitrXouuzlTIBm"
    test_step = 6

    print(get_decoded_string_by_skip(corpus=test_corpus, step=test_step))

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()

def upper_string(input_string):
    '''
    func that did words upper
    '''
    return input_string.upper()



def capitalize_first_letters(sentence):

    '''
    finctions did first letters words upper
    '''

    sentence = input("Введите строку: ")
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    capitalized_sentence = ' '.join(capitalized_words)
    return capitalized_sentence
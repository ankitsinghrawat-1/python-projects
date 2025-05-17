from word2number import w2n
def word_to_number():
    words = input("Enter a number in words: ")
    number = w2n.word_to_num(words)
    print(f"The number is: {number}")   
word_to_number()
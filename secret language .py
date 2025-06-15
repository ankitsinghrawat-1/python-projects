import random


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


while True:
     ran = random.sample(letters, 3)
     # joined = ''.join(ran)


     ask = input("Do you want to encode or decode or quit the program? (e/d/quit): ").lower()


     if ask == 'quit':
          print('Exiting the program...')
          break
     if ask == 'e':
          text = input("Enter the text to encode: ")
          words = text.split()
          encoded = []
          for word in words:
               if len(word) >=3:
                    ntext = ''.join(ran) + word[1:] + word[0] + ''.join(ran)
                    encoded.append(ntext)
               elif len(word) <= 2:
                    encoded.append(word[::-1])
          print("Encoded text:", " ".join(encoded))

     elif ask == 'd':
          text = input("Enter the text to decode: ")
          words = text.split()
          decoded = []
          for word in words:
               if len(word) >= 9:
                    wtext = word[3:-3]
                    ntext = wtext[-1] + wtext[:-1]
                    decoded.append(ntext)
               elif len(word) <= 2:
                    decoded.append(word[::-1])
          print("Decoded text:", " ".join(decoded))   

     else:
          print("Invalid input. Please try again.")

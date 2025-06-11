import random


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
     'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
ran = random.sample(letters, 3)
joined = ''.join(ran)

   
ask = input("Do you want to encode or decode? (e/d): ").lower()
if ask == 'e':
     print("You chose to encode.")
     tex= input("Enter your text: ")
     text = tex.split()
     print('encoding your text...')

     for words in text:
          if len(words) >= 3:
               print(joined + words + joined)
          elif len(words) <= 2:
               print(''.join(reversed(words)))
elif ask == 'd':
     print("You chose to decode.")
     tex = input("Enter your text: ")
     text = tex.split()
     print('decoding your text...')

     for words in text:
          if len(words) >= 3:
               print(words[3:-3])

          elif len(words) <= 2:
               print(''.join(reversed(words)), end=' ')
          else:
               print('Invalid encoding detected.')
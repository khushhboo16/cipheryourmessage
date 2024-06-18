alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text1, shift1):
  str1 = ""
  for letter in text1:
    e = alphabet.index(letter)
    f = e + shift
    str1+= alphabet[f]
  print(f"The encoded text is {str1}")
def decrypt(shift2,text2):
  str=""
  for letters in text2:
    c=alphabet.index(letters)
    b=c-shift
    d=alphabet[b]
    str=str+d
  print(f"Your decoded word is {str}")



 
if direction=="encode":
  encrypt(text1=text, shift1=shift)
else:
  decrypt(text2=text, shift2=shift)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  encrypted_text = ''

  if shift > len(alphabet):
    shift = shift % len(alphabet)

  if direction == 'decode':
    shift *= -1

  # Get indices of translated text
  letter_indices = []
  for char in text:
    if char not in alphabet:
      letter_indices.append(-1)
    else:
      i = alphabet.index(char)
      i+= shift
      if i > 25:
        i-= 26
      letter_indices.append(i)

  # Create translated message
  for i in letter_indices:
    if i == -1:
      encrypted_text+= text[letter_indices.index(i)]
    else:
      encrypted_text+= alphabet[i]

  # Print output
  print(f"{direction.capitalize()}d text:\n{encrypted_text}\n")

# Main
direction = ''
print('Welcome to Caesar Cipher!\n')

while(direction != 'quit'):
  # Get input
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, 'quit' to quit:\n")
  # Quit
  if direction == 'quit':
    print("Goodbye.")
  # Get input and translate
  elif direction == 'encode' or direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
  # Bad input
  else:
    print("Invalid input.")
    
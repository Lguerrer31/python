def is_pangram(text):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  text = str.lower(text)
  for letter in alphabet:
    if letter not in text:
      return False
  return True
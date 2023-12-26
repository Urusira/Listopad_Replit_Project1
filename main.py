def almost_palindrome(txt, n=0):
  for i in range(len(txt)):
      n += txt[i] != txt[::-1][i]
  return n == 2

almost_palindrome("абвгвбж")
# Если поменять «ж» на «а», получится палиндром «абвгвба».
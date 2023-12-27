def almost_palindrome(txt, n=0):
  for i in range(len(txt)):
      n += txt[i] != txt[::-1][i]
  return n == 2
#мой комментарий оч важен!!!!
#настолько важен, что прям очень важее
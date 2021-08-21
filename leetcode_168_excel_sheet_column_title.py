#def convertToTitle(self, columnNumber: int) -> str:
def convertToTitle(columnNumber):
  s = ""
  Q = columnNumber
  while Q > 0:
    Q,R = divmod(Q-1,26)
    s += chr(65+R)
    
  return s[::-1]

convertToTitle(25)

convertToTitle(676)

convertToTitle(702)

convertToTitle(1000)

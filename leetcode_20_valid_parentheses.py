

def isValid(s: str):
  paran = []
  if len(s) <= 1:
    return False
  else:
    paran.append(s[0])
    for p in s[1:]:
      if p in ['(','{','[']:
        paran.append(p)
      else:
        if p == ')':
          if paran and paran[-1] == '(':
            paran.pop()
          else:
            return False
        if p == '}':
          if paran and paran[-1] == '{':
            paran.pop()
          else:
            return False
        if p == ']':
          if paran and paran[-1] == '[':
            paran.pop()
          else:
            return False
    if not paran:
      return True
    else:
      return False

ps = "(){}}{"
result = 'Not Valid'
if isValid1(ps):
  result = 'Valid'
print(f'The string {ps} is {result}.')


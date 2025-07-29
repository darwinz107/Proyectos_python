import re
def alphanumeric(password: str) -> bool:
    for c in password:
         
         if re.fullmatch('[A-Za-z0-9]+',c) :
              print(c)
         else:
              return False
    return True;     
   
print(alphanumeric("darzam10"));   
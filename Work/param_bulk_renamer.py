string = IN[0]
 
def borra(x):
  return x[IN[4]:]
 
def creaprinc(x):
  return IN[1] + x
 
def creaalfin(x):
  return x + IN[2]
 
 
borrastring = list(map(borra,string))
 
masstring = list(map(creaprinc,borrastring))
 
masmasstring = list(map(creaalfin,masstring))
 
 
 
def primemayus(x):
  return x.title()
 
def todomayus(x):
  return x.upper()
 
 
 
if IN[3] == 1:
  OUT = list(map(primemayus,masmasstring))
 
 
 
elif IN[3] == 2:
  OUT = list(map(todomayus,masmasstring))
 
 
 
else:
  OUT = masmasstring

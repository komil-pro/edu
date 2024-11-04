def pyro(blocks=1000):
  height=0
  while blocks > height:
    height += 1
    blocks -= height
  print("Высота пирамиды:",height) #44

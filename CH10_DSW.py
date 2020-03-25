def hanoi (a,b,c,g):
     g=int(input('please input the number of the layer of the hanoi'))
   if g ==1:
      print(a,"move to",c)
   else:
      hanoi(a,c,b,g-1)
      print(a,"move to",c)
      hanoi(b,a,c,g-1)
      print def hanoi (a,b,c,g) 
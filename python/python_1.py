n=int(input())
i=1
while i<=n:
    space=1
    while space<=n-i:
        print(" ", end="")
        space+=1
    j=1
    while j<=((2*i)-1):
        print("*", end="")
        j+=1
    print()
    i+=1

"""
input : 4
output : 
   *
  ***
 *****
*******
"""
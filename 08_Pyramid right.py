maxi = int(input("Bilangan tertinggi : "))

for bawah in range(maxi):
    for kanan in range(bawah+1):
     print("*",end=' ')
    print("\n")

"""
pyramid left
"""


for bawah in range(maxi):
   print(" ",end=' ')
   for kiri in range(bawah-1):
    print("*")
panjang = input("Panjang : ")
lebar = input("Lebar : ")

p = int(panjang)
l = int(lebar)

"""
BUATLAH KOTAK PERSEGI MENGGUNAKAN BINTANG
Panjang itu kebawah
Lebar itu kesamping
"""
for row in range(0, p): #Turun kebawah
    for col in range(1, l): #Kesamping
        if(row == 0 or row == p-1 or col == 1):
            print("* ",end='')            
        else:
            print("  ",end='')        
    print("*")

# for i in range (0,l):
#     print("*")or 

# for row in range (0,p):
#     print("*"*row)
 
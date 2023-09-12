
f = open("D:\GITH\myfile.txt", "a")

m = input("Masukkan kalimat baru : ")
f.write(f'{m}\n')
f.close()

#membuka file
f = open({a} + "D:\GITH\myfile.txt", "r")
print(f.read())

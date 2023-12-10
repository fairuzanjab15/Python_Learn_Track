total = 0
def sum(nominal):
  global total
  try:
    total += float(nominal)
  except:
    print("Harga harus berupa angka")

while True:
    price = input("Masukkan Harga: ")
    sum(price)
    print("Total Harga : {0}".format(total))100
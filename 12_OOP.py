class Segitiga:
  def __init__(self, alas, tinggi):
    self.alas = alas
    self.tinggi = tinggi

  def get_luas(self):
    return 0.5 * self.alas * self.tinggi

segitiga1 = Segitiga(5, 10)
segitiga2 = Segitiga(10, 10)

print('luas segitiga1:', segitiga1.get_luas())
print('luas segitiga2:', segitiga2.get_luas())    

class Segiempat:
  def __init__(self,panjang,lebar):
    self.panjang = panjang
    self.lebar = lebar

  def get_luasem(self):
    return self.panjang * self.lebar
  
segiempat1 = Segiempat(5,10)

print("Luas segiempat: ", segiempat1.get_luasem())
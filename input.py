#input user
#tanpa casting data yang diinput akan menjadi tipe data string
print("====INPUT MENGHASILKAN DATA STRING===")
data = input("Masukkan data : ")
print("data = ",data,",tipe data ", type(data))
print("\n")
#cara menjadikan data inputan sebagai angka integer
print("====INPUT MENGHASILKAN DATA INTEGER===")
angka = int(input("Masukkan angka : "))
print("data = ",angka,",tipe data ", type(angka))

print("\n")
#bagaimana dengan boolean
#hasil tipe data tetap menghasilkan data true
print("====INPUT MENGHASILKAN DATA BOOLEAN===")
biner = bool(input("Masukkan nilai boolean : "))
print("data = ", biner, " tipe data ", type(biner))
print("\n")

print("====INPUT MENGHASILKAN DATA BOOLEAN YG DI CASTING===")
biner = bool(int(input("Masukkan nilai boolean : ")))
print("data = ", biner, " tipe data ", type(biner))

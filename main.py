#casting
#merubah dari satu tipe ke tipe yang lain
#tipe data int, float, str, bool
print("====INTEGER====")
data_int = 9
print("data ", data_int, ",type = ", type(data_int))

data_float = float(data_int)
print("data ", data_int, ",type = ", type(data_float))
data_string = str(data_int)
data_boolean = bool(data_int)
print("data ", data_string, ",type = ", type(data_string))
print("data ", data_boolean, ",type = ", type(data_boolean))

print("====FLOAT====")
data_float = 9.9
print("data ", data_float, ",type = ", type(data_float))

data_int = int(data_float)
print("data ", data_int, ",type = ", type(data_float))
data_string = str(data_float)
data_boolean = bool(data_float)
print("data ", data_string, ",type = ", type(data_string))
print("data ", data_boolean, ",type = ", type(data_boolean))
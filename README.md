# forward-chaining-main-street-knowledge-base

Sistem ini menggunakan basis pengetahuan untuk memilih restoran bagi pengguna yang sesuai 
dengan batasan diet, preferensi, dan pertimbangan lainnya dari orang tersebut.

Cara pengunaan nya

# KUNCI INFORMASI:
#A - menampung alergi
#GF - bebas gluten
#V - vegan
#VEG - vegetarian
#Harga - "Rendah", "Sedang", atau "Tinggi"
#Style - bisa "Sub", "Pub", "Pizza", "Ethnic", "Mexican"

# mendeskripsikan format argumen pengguna
# (Tidak ada ?, A ?, GF ?, V ?, VEG ?, Harga, Bawa Pulang ?, Alkohol ?, Gaya?)
# (semua nilai kecuali 'Price' dan 'Style' adalah boolean 0 atau 1 ... jika Tidak Ada adalah 1, A, GF, V, VEG diabaikan)

Pengguna menginput kan informasi yang di inginkan 
agar sistem dapat merekomendasikan tempat makan 
yang sessuai dengan informasi yang pengguna inputkan

userInput = [1, 0, 0, 0, 0, "High", 0, 0, "Pub"]

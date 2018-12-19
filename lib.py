users = {} #Variabel Global

def option(): #Variabel Lokal #Marta
	print("Aplikasi pengumpul saran mahasiswa, silahkan login dahulu")
	print("\n1. Untuk login")
	print("\n2. Untuk buat akun")
	print("\n3. Untuk menampilkan saran")
	print("\n4. Untuk keluar program")
	pilihan = int(input("masukan pilihan anda: "))
	return pilihan
	
def newUser(): #Variabel Lokal #Gilang
	global createLogin
	
	createLogin = str(input ("Masukan nama akun :"))
	
	if createLogin in users:
		print("\nLogin name already exist!\n")
	else:
		createPassw = str(input("Masukan Password :"))
		users[createLogin] = createPassw
		print("\nAkun berhasil dibuat\n")
		
def oldUser(): #Variabel Lokal #Abiyoga
	login = str(input("Masukan nama akun :"))
	passw = str(input("Masukan Password : "))
		
	if login in users and users[login] == passw:
		print("\nLogin Berhasil!\n")
		inputSaran()
		print("\n")
	else:
		print("\n====Nama yang anda masukan tidak terdaftar atau password salah!====\n")
		
def inputSaran(): #Variabel Lokal #Iga Esti
	print("\nSelamat datang, {}\n".format(createLogin))
	print("\nMasukkan Saran Anda untuk Universitas Jenderal Achmad Yani")
	
	Saran = str(input("Masukan Saran : "))
	file = open("database.txt","a")
	file.write("Dari :{}\n".format(createLogin))
	file.write("Saran :{}\n".format(Saran))
	file.write("\n")
	
def read(): #Iga Esti
	file =open("database.txt", "r")
	print("\n==Saran untuk Universitas Jenderal Achmad Yani==\n")
	print(file.read())
	print
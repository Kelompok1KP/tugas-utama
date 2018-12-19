import lib #memanggil file lib.py
print ("==============================================================================")

pilihan = 1
while (pilihan < 5):
	pilihan = lib.option()
	print(pilihan)
	if pilihan == 1:
		lib.oldUser()
	elif pilihan == 2:
		lib.newUser()
	elif pilihan == 3:
		lib.read()
	elif pilihan == 4:
		break
	elif pilihan == 5:
		print(" Informatika, Sistem Informasi, TI")
		
	
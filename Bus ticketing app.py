import csv
import matplotlib.pyplot as plt

#Deklarasi list
ltujuan = ['Jakarta','Bandung','Semarang','Yogyakarta']
lnohp = []
lnama = []
lemail = []
lwaktu = ['06.00','13.00','18.30']
running = True
usedKolom = []
usedBaris = []
seat = [["R" for j in range(0,8)] for i in range(0,7)]
seatKolom= {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5,
    'F' : 6,
}


def intro() : #untuk intro
  print("======Selamat datang di Ticketing Bus Online Bogor====== ")
  print('Pilihan Destinasi : \n1.Jakarta \n2.Bandung \n3.Semarang \n4.Yogyakarta')

def data_pemesan(): #untuk meminta detail pemesan dan traveler
  for traveler in range(kursi) :
    if traveler == 0 :
      print(f'\n===Detail Pemesan===')

      nama = input("Nama Lengkap : ")
      while nama.isnumeric() == True :
        print("Nama hanya mengandung alphabet")
        nama= input("Nama Lengkap : ")
      lnama.append(nama)

      nohp = input("No HP : ")
      while nohp.isnumeric() == False :
        print("No HP hanya mengandung angka")
        nohp= input("No HP : ")
      lnohp.append(nohp)

      email = input("Email : ")
      lemail.append(email)
      print("\n")
    else :
      traveler_no = traveler + 1
      print(f'\n===Detail Traveler {traveler_no}===')
      nama= input("Nama Lengkap : ")

      while nama.isnumeric() == True :
        print("Nama hanya mengandung alphabet")
        nama= input("Nama Lengkap : ")
      lnama.append(nama)

      nohp= input("No HP : ")
      while nohp.isnumeric() == False :
        print("No HP hanya mengandung angka")
        nohp= input("No HP : ")
      lnohp.append(nohp)

      email= input("Email : ")
      lemail.append(email)
      print("\n")

def Displayseat(): #Untuk memunculkan visual tempat duduk
    print("       ","|","=============Kaca Depan============","|")
    print("       ","|","  [crew]                  [supir]  ","|")
    print("       ","|","                                   ","|")
    print("       ","|","  A  ","  B  ","  C  ","  D  ","  E  ","  F  ","|")
    for j in range(1,8):
        print("Baris "+str(j),"|",end=" ")
        if j==6:
            for i in range(1,4):
                print(end="      ")
            for i in range(4,7):
                print("[",seat[i][j],"]", end=" ")     
            print("|")
        elif j==7:
            for i in range(1,7):
                print("[",seat[i][j],"]", end=" ")     
            print("|")
        else:
            for i in range(1,7):
                if i==3:
                    print(end="      ")
                else:
                    print("[",seat[i][j],"]", end=" ")     
            print("|")
    
    print("       ","|","                                   ","|")
    print("       ","|","===========Kaca Belakang===========","|")

def pilih_kursi(): #untuk memilih kursi yang tersedia
    barisInput= input("Baris Kursi: ") #Meminta input barisk kursi

    while barisInput.isnumeric() == False : # Error handling input baris
      print("Masukkan angka dari indeks baris")
      barisInput= input("Baris Kursi: ")

    usedBaris.append(barisInput)
    baris = int(barisInput)

    kolomInput = input("Kolom kursi: ") #Meminta input kolom kursi

    while kolomInput.isalpha() == False : # Error handling input kolom
      print("Masukkan huruf indeks kolom")
      kolomInput = input("Kolom kursi: ")

    kolomInput = kolomInput.upper()
    usedKolom.append(kolomInput)
    kolom = seatKolom[kolomInput] # Menggunakan Dictionary untuk konversi kolom huruf menjadi indeks angka

    if kolom==1:
        if baris==6:
            print("Silahkan pilih tempat duduk yang tersedia")
            pilih_kursi()
        else:
            while seat[kolom][baris]=="R":
                seat[kolom][baris]="X"
    elif kolom==2:
        if baris==6:
            print("Silahkan pilih tempat duduk yang tersedia")
            pilih_kursi()
        else:
            while seat[kolom][baris]=="R":
                seat[kolom][baris]="X"
    elif kolom==3:
        if baris==1:
            print("Silahkan pilih tempat duduk yang tersedia")
            pilih_kursi()
        elif baris==2:
            print("Silahkan pilih tempat duduk yang tersedia")
            pilih_kursi()
        elif baris==3:
            print("Silahkan pilih tempat duduk yang tersedia")
            pilih_kursi()
        elif baris==4:
            print("Silahkan pilih tempat duduk yang tersedia")
            pilih_kursi()
        elif baris==5:
            print("Silahkan pilih tempat duduk yang tersedia")
            pilih_kursi()
        elif baris==6:
            print("Silahkan pilih tempat duduk yang tersedia")
            pilih_kursi()
        else:
            while seat[kolom][baris]=="R":
                seat[kolom][baris]="X"
    elif kolom==4:
        while seat[kolom][baris]=="R":
            seat[kolom][baris]="X"
    elif kolom==5:
        while seat[kolom][baris]=="R":
            seat[kolom][baris]="X"
    elif kolom==6:
        while seat[kolom][baris]=="R":
            seat[kolom][baris]="X"

def billing(kursi) : #untuk print ticket
  if tujuan == 1 :
    harga = 120000 *kursi
  elif tujuan == 2 :
    harga = 280000*kursi
  elif tujuan == 3 :
    harga = 220000*kursi
  elif tujuan == 4 :
    harga = 160000*kursi
  print("Rincian Harga")
  print("----------------------------------")
  print(f"Tiket Reguler x{kursi}     {harga}")
  print("----------------------------------")
  print(f"Total :     {harga}\n")

def payment() : #Untuk memilih metode pembayaran dan menyelesaikan pembayaran
  print("Metode Pembayaran :\n1.GO-PAY\n2.Transfer Bank Online")
  payMethod = input("Pilih Metode Pembayaran :" )
  while payMethod != '1' and payMethod != '2' :
    print("Metode pembayaran tidak tersedia, pilih 1 (GO-PAY) atau 2 (Transfer Bank Online) ")
    payMethod = input("Pilih Metode Pembayaran :" )
  if payMethod == '1':
    print("Transfer GO-PAY dari nomor", lnohp[0], ": y/n")
    transfer = input()
    if transfer.lower() =='y' :
      print("Payment Successful!")
      ticket()
      manifest()
    elif transfer.lower() == 'n' :
      print("\nPayment cancelled!")
      print("\nOrder Cancelled!")
    while transfer != 'y' and transfer !='n' :
      print("Transfer GO-PAY dari nomor", lnohp[0], ": y/n")
      transfer = input()
  elif payMethod == '2' :
    norek = input("Masukkan Nomor Rekening Anda :")
    while norek.isnumeric() == False :
      print("Nomor rekening hanya mengandung angka")
      norek = input("Masukkan Nomor Rekening Anda :")
    print("Transfer uang dari rekening", norek, ": y/n")
    transfer = input()
    if transfer.lower() =='y' :
      print("\nPayment Successful!")
      ticket()
      manifest()
    elif transfer.lower() == 'n' :
      print("Payment cancelled!")
      print("\nOrder cancelled!")
    while transfer != 'y' and transfer !='n' :
      print("Transfer uang dari rekening", norek, ": y/n")
      transfer = input()
    
def ticket() : #Untuk print ticket
  for ticket in range(kursi) :
    print("\n---------------------------------------")
    print("|  ", end="")
    print("Ticket #", ticket+1,)
    print("|  ", end="")
    print("Nama :",lnama[ticket])
    print("|  ", end="")
    print("No. HP :",lnohp[ticket])
    print("|  ", end="")
    print("Email :",lemail[ticket])
    print("|  ", end="")
    print("From : Bogor","   To : ",ltujuan[tujuan-1])
    print("|  ", end="")
    print("Tanggal :",tanggal, "   Waktu :",lwaktu[waktu-1])
    print("|  ", end="")
    print("[Reguler] ")
    print("|  ", end="")
    print("Seat :")
    print("| (Kolom,Baris) : (", usedKolom[ticket],",", usedBaris[ticket],")  ") #ini untuk nunjukkin koordinat kursi
    print("---------------------------------------")

def manifest() : # Untuk memasukkan data ke dalam file Manifest.csv
    with open('manifest_1.csv','a', newline ='') as file :
        writer = csv.writer(file, delimiter=',')
        #Format CSV
        #Nama, Destinasi, Waktu, Kolom, Baris
        for i in range(kursi) :
            seat_data = usedKolom[i] + usedBaris[i]
            writer.writerow([lnama[i], ltujuan[tujuan-1], lwaktu[waktu-1], seat_data])



while running == True : #main loop
  intro()
  tujuan = int(input("Pilih Destinasi Tujuan Anda (1, 2, 3 atau 4): "))
  while tujuan != 1 and tujuan != 2 and tujuan != 3 and tujuan != 4 :
    print("Destinasi tidak tersedia, pilih 1, 2, 3 atau 4")
    tujuan = int(input("Pilih Destinasi Tujuan Anda (1 atau 2): "))

  tanggal = input("Tanggal Perjalanan (dd/mm/yyyy) : ")

  print("Jadwal Keberangkatan dari Terminal Bogor :\n1.06.00\n2.13.00\n3.18.30 ")

  waktu = int(input("Pilih waktu keberangkatan :"))

  kursi_req = input("Jumlah kursi : ")
  while kursi_req.isnumeric() == False : #Error handling permintaan kursi
    print("Masukkan angka saja")
    kursi_req = input("Jumlah kursi : ")
  while int(kursi_req) >= 34 : #Error handling permintaan berlebih
    print("Kapasitas bus hanya 34, ubah jumlah pesanan")
    kursi_req = input("Jumlah kursi : ")
  kursi = int(kursi_req)
  for traveler in range(kursi) : #Loop untuk menampilkan dan memilih kursi
    Displayseat()
    pilih_kursi()
  Displayseat()
  data_pemesan()
  billing(kursi)
  payment()
  running = False


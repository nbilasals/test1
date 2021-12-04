awal=int(input( " Masukkan Nilai Awal = "))
akhir=int(input( " Masukkan Nilai Akhir = "))
dec=int(input( " Masukkan Nilai decrement = "))
tgenap=0
tganjil=0
j=dec
for i in range (awal, akhir+1, dec) :
    for j in range (dec, i+1, dec) :
        print (j,end= ' ')
        if j&2==0:
            tgenap+=j
        else:
            tganjil+=j
    print ( " " )
print ( ' Jumlah Bilangan Ganjil : ',tganjil)
print ( ' Jumlah Bilangan Genap : ',tgenap)

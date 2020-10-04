t = int(input("12.ayın harcamasını giriniz"))

mevcut_butce_ort = 5000

a = mevcut_butce_ort

aylikharcamalar = [20000,3000,4000,6000,9000,500,8000,700,500,1000,1000,t]

def ortalama(aylikharcamalar):
    toplam = 0
    for i in aylikharcamalar:
        toplam +=i
    return toplam/12
y = ortalama(aylikharcamalar)

if a-y>0:
    print("devam")
elif a-y<0:
    print("harcama politikaları değerlendirilmeli")
else:
    print("harcamalar bütçeyle eşdeğer")
    
    
    

    

    






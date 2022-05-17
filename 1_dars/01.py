import os
file_name = "Talabalar Ro'yxati"
def file_och():
    if not os.path.exists(file_name):
        file = open(file_name, "x")
        file.close()
file_och()
def menu():
    son = input(""""
=== Talabalar ro'yxati ===
Menyuni tanlang:
1. Ro'yxatdan o'tish
2. Ko'rish
3. O'zgartirish
4. Qidirish
5. O'chirish
6. Chiqish\n""")
    if son.isdigit() and int(son) in range(1,7):
       return int(son)
    else:
        print("Xato kiritildi. Sonlarni 1 dan 5 gacha tanlang!")
        return None
def kiritish():
    file = open(file_name, "a")
    soz = input("Ism familiyangiz: ")
    if soz.strip():
        file.write(f"\n{soz}")
    file.close()
def korish():
    file = open(file_name, "r")
    qatorlar = file.readlines()
    for i in range(0, len(qatorlar)):
      print(f"{i+1}\t{qatorlar[i].strip()}")
    return qatorlar
def ochirish():
    qatorlar = korish()
    print("Qaysi qatorni o'chirmohchisiz?")
    qator = int(input("Qatorni kiriting: ")) -1
    del qatorlar[qator]
    with open(file_name, "w") as file:
        file.write("".join(qatorlar))
    print("Natija")
    korish()
def ozgartirish():
    qatorlar = korish()
    print("Qaysi qatorni o'zgartirmohchisiz?")
    qator = int(input("Qatorni kiriting: ")) - 1
    yangi = input("Yangi so'zni yozing: ")
    qatorlar[qator] = yangi + "\n"
    with open(file_name, "w") as file:
        file.write("".join(qatorlar))
    print("Natija")
    korish()
def qidirish(soz):
    qatorlar = korish()
    with open(file_name) as file:
        for qator_soz in file.readlines():
            if soz in qator_soz:
                return True
        return False
while True:
    tanlov = menu()
    if tanlov == 1:
        kiritish()
    elif tanlov == 2:
        korish()
    elif tanlov == 3:
        ozgartirish()
    elif tanlov == 4:
        soz = input("Qaysi talabani qidirmohchisiz ismi va familiyasini yozing: ")
        if qidirish(soz):
            print("Talaba topildi!")
        else:
            print("Talaba topilmadi")
    elif tanlov == 5:
        ochirish()
    elif tanlov == 6:
        break

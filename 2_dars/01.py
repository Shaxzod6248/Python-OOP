import json
import os


file_name = "Talabalar"
def bazani_oqish():
    if not os.path.exists(file_name):
        return None
    with open(file_name, 'r') as file:
        return json.load(file)


def bazaga_yozish(data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


def kiritish():
    data = bazani_oqish()
    if not data:
        data = []
        id = 0
    else:
        id = int(data[-1]["id"])
    talaba = {
        "id": id +1,
        "ismi": input("Ismingiz: "),
        "sharifi": input("Sharifingiz: "),
        "yoshi": int(input("Yoshingiz: ")),
        "sohasi": input("Sohangiz: ")
    }
    data.append(talaba)
    bazaga_yozish(data)


def korish():
    talabalar = bazani_oqish()
    print(f"{'id'}"
          f"{'ismi'.center(20)}"
          f"{'sharifi'.center(20)}"
          f"{'yoshi'.center(20)}"
          f"{'sohasi'.center(20)}")
    for talaba in talabalar:
        print(f"{str(talaba['id'])}"
              f"{talaba['ismi'].center(20)}"
              f"{talaba['sharifi'].center(20)}"
              f"{str(talaba['yoshi']).center(20)}"
              f"{talaba['sohasi'].center(20)}"
              )


def qidirish():
    talabalar = bazani_oqish()
    print(f"{'id'}"
          f"{'ismi'.center(20)}"
          f"{'sharifi'.center(20)}"
          f"{'yoshi'.center(20)}"
          f"{'sohasi'.center(20)}")
    ism = input("Ismini kiritng:")
    for talaba in talabalar:
        if ism == talaba['ismi']:
            print(f"{str(talaba['id'])}"
                  f"{talaba['ismi'].center(20)}"
                  f"{talaba['sharifi'].center(20)}"
                  f"{str(talaba['yoshi']).center(20)}"
              f"{talaba['sohasi'].center(20)}"
              )
def ochirish():
    data = bazani_oqish()
    uzun = len(data)
    korish()
    qaysi_qator = int(input("O'chirmohchi bo'lgan qatorni kiriting: "))

    for i in range(len(data)):
        if qaysi_qator == data[i]["id"]:
            del data[i]
            break
    if uzun == len(data):
        print("Talaba topilmadi")
    else:
        print("O'chirildi!!!")
    bazaga_yozish(data)



def ozgartirish():

    data = bazani_oqish()
    korish()
    qaysi_qator = int(input("O'zgartirmohchi bo'lgan qatorni kiriting: "))
    ozgardi = input("O'zgartirmohchi bo'lgan ismni yozing: ")

    for i in range(len(data)):
        if qaysi_qator == data[i]["id"]:
            data[i]["ismi"] = ozgardi
            break
    bazaga_yozish(data)




def menu():
    birinchi = True
    while True:
        if birinchi:
            tanlov = input("""
            ===Talabalar ro'yxatiga xush kelibsiz===
            1. Ro'yxatdan o'tish
            2. Ko'rish
            3. Qidirish
            4. O'chirish
            5. O'zgartirish
            6. Chiqish\n""")
            birinchi = False
        else:
            tanlov = input("Xato! qaytadan kiriting: ")
        if tanlov.isdigit() and int(tanlov) in range(1,7):
            return int(tanlov)


if __name__ == "__main__":
    tanlov = menu()
    if tanlov == 1:
        kiritish()
    elif tanlov == 2:
        korish()
    elif tanlov == 3:
        qidirish()
    elif tanlov == 4:
        ochirish()
    elif tanlov == 5:
        ozgartirish()
    elif tanlov == 6:
        print("Siz dasturdan chiqib ketdingiz! Ya'na kutib qolamiz")
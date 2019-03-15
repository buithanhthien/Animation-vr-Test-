name = []
phone_number = []
def create_contact(name, phone_number):
    name = raw_input("Nhap ten nguoi moi: ")
    file = open('contact.txt','rb+')
    file.write(name)
    file.write(" - ")
    phone_number = raw_input("Nhap so dien thoai: ")
    file.writelines(phone_number + "\r\n")
    file.close()

def show_contact():
    file = open('contact.txt', 'r')
    print file.read()
    file.close()

print "Ban muon lam gi?\n"
print "1.Hien ra danh sach."
print "2.Them nguoi."
print "'exit' de thoat!\n"

choose = ''

while 1:
    choose = raw_input("Ban chon: ")
    if choose == 'exit':
        break
    elif choose == '2':
        create_contact(name,phone_number)
    else:
        show_contact()

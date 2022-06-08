from unicodedata import decimal
print ("คุณต้องการคำณวณรูปทรงได")
print ("1. สี่เหลี่ยมผืนผ้า")
print ("2. สามเหลี่ยม")
choice = input("กรุณาระบุตัวเลือก(1/2): ")

print("คุณต้องการให้ผลลัพธ์ออกมาเป็นหน่วยใด")
print("1. เซนติเมตร")
print("2. เมตร")
unit = input("กรุณาระบุตัวเลือก(1/2): ")

if choice == '1':
    length = float(input("กรุณาระบุความยาวของสี่เหลี่ยมผืนผ้าในหน่วยเซนติเมตร: "))
    width = float(input("กรุณาระบุความกว้างของสี่เหลี่ยมผืนผ้าในหน่วยเซนติเมตร: "))
    if unit == '1':
        area = float(length * width)
        print("พื้นที่สี่เลี่ยมผืนผ้าของคุณคือ: ", round(area, 2), "ตารางเซนติเมตร")
    elif unit == '2':
        area = float(length * width)
        uc = area / 100
        print("พื้นที่สี่เลี่ยมผืนผ้าของคุณคือ: ", round(uc, 2), "ตารางเมตร")
    else:
        print("Invalid Input")
elif choice == '2':
    base = float(input("กรุณาระบุความยาวฐานของสามเหลี่ยมของคุณในหน่วยเซนติเมตร : "))
    height = float(input("กรุณาระบุความสูงของสามเหลี่ยมของคุณในหน่วยเซนติเมตร : "))
    if unit == '1':
        area = 0.5 * base * height
        print("พื้นที่ของสามเหลี่ยมของคุณคือ: ", round(area, 2), "ตารางเซนติเมตร")
    elif unit == '2':
        area = 0.5 * base * height
        uc = area / 100
        print("พื้นที่ของสามเหลี่ยมของคุณคือ: ", round(uc , 2), "ตารางเมตร")
    else:
        print("Invalid Input")

else:
    print("Invalid Input")
 

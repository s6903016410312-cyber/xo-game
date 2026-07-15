def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "หารด้วยศูนย์ไม่ได้"
    return a / b


def run_calculator():
    print("===== Calculator =====")

    while True:
        print("\n1. บวก")
        print("2. ลบ")
        print("3. คูณ")
        print("4. หาร")
        print("5. ออก")

        choice = input("เลือกเมนู : ")

        if choice == "5":
            break

        try:
            a = float(input("ตัวเลขที่ 1 : "))
            b = float(input("ตัวเลขที่ 2 : "))
        except ValueError:
            print("กรุณาใส่ตัวเลข")
            continue

        if choice == "1":
            print("ผลลัพธ์ =", add(a, b))

        elif choice == "2":
            print("ผลลัพธ์ =", subtract(a, b))

        elif choice == "3":
            print("ผลลัพธ์ =", multiply(a, b))

        elif choice == "4":
            print("ผลลัพธ์ =", divide(a, b))

        else:
            print("เมนูไม่ถูกต้อง")
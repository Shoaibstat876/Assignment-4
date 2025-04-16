from encoder import generate_qr
from decoder import decode_qr

def menu():
    while True:
        print("\n📌 QR Code Encoder / Decoder Menu")
        print("1. Generate QR Code")
        print("2. Decode QR Code")
        print("3. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            data = input("Enter data to encode: ")
            filename = input("Enter filename (default: qr_code.png): ") or "qr_code.png"
            generate_qr(data, filename)

        elif choice == "2":
            image_path = input("Enter path of QR code image: ")
            decode_qr(image_path)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()

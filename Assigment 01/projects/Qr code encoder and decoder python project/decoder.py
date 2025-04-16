import cv2

def decode_qr(image_path):
    detector = cv2.QRCodeDetector()
    img = cv2.imread(image_path)
    data, bbox, _ = detector.detectAndDecode(img)
    
    if data:
        print("Decoded Data:", data)
    else:
        print("No QR code found in the image.")

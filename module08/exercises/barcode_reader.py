import os
import cv2
from pyzbar.pyzbar import decode
from pathlib import Path

def iterate_images(directory: Path):
    image_extensions = (".png", ".jpg")
    res = list()
    for item in directory.iterdir():
        if item.is_file() and item.suffix in image_extensions:
            res.append(item)
    return res

def read_barcode(image:Path):
    absolute_path = str(image.absolute())
    img = cv2.imread(absolute_path)
    detectedBarcodes = decode(img)

    barcodes_data = list()
    if len(detectedBarcodes) < 1:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
        barcodes_data = list()
        for barcode in detectedBarcodes:
            if barcode.data:
                barcodes_data.append(barcode.data.decode("UTF-8"))
    return " or ".join(barcodes_data)

def assign_codes_to_clients(clients_filename):
    with open(clients_filename, "r") as fs:
        clients = fs.readlines()
    
    images = iterate_images(Path("images/"))

    with open("barcodes_for_clients.txt", "w") as file:
        file.write("Client name" + "    " + "Barcode" + "\n")    
        for i, path in enumerate(images):
            barcode = read_barcode(path)
            try:
                client = clients[i]
            except IndexError:
                print("There are more barcodes than users")
                break
            file.write(client + "    " + barcode + "\n")

if __name__ == "__main__":
    assign_codes_to_clients("clients.txt")
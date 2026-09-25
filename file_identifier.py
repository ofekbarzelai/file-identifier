import os

FILE_SIGNATURES = {
    "4D5A": "PE",
    "89504E470D0A1A0A": "PNG",
    "FFD8FF": "JPG",
    "255044462D": "PDF"
}

def main():
    while True:
        option = int(input("Please choose an option from the menu\n1. Check files in a folder\n2. check a file\n"))
        
        if option == 1 or option == 2:
            path = input("Please Enter the path\n")
            if os.path.exists(path):
                print("Path exist.")
                handle_option(path, option)
            print("Invalid path. Please try again")

        else:
            print("Invalid choose. Please try again")

def handle_option(path, option):
    if option == 1:
        files = os.listdir(path)
        for file in files:
            handle_file(f"{path}\\{file}")
    else:
        handle_file(path)

def handle_file(file_path):
    first_bytes = get_bytes(file_path)
    file_format = check_format(first_bytes)
    print(f"Path: {file_path}\nFormat: {file_format}\n")

def get_bytes(path):
    with open(path, 'rb') as file:
        data = file.read(8)
        first_bytes = data.hex().upper()
    return first_bytes

def check_format(first_bytes):
    for signature, file_format in FILE_SIGNATURES.items():
        if first_bytes.startswith(signature):
            return file_format

if __name__ == "__main__":
    main()
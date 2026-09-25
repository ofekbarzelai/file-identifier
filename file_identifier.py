import os

FILE_SIGNATURES = {
    "4D5A": "PE",
    "89504E470D0A1A0A": "PNG",
    "FFD8FF": "JPG",
    "255044462D": "PDF"
}

bytes_to_read = 0

def main():
    calc_max_bytes()
    while True:
        print("Please choose an option from the menu\n1. Check files in a folder\n2. Check a file\n3. Exit")
        try:
            option = int(input("Your option: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue
        if option == 1 or option == 2:
            path = input("Please Enter the path:\n")
            if os.path.exists(path):
                if (option == 1 and os.path.isdir(path)) or (option == 2 and os.path.isfile(path)):
                    handle_option(path, option)
                else:
                    print("Invalid path choice. Please try again.")
            else:
                print("Invalid path. Please try again.")
        elif option == 3:
            exit()
        else:
            print("Invalid choice. Please try again.")

def calc_max_bytes():
    global bytes_to_read
    for signature, file_format in FILE_SIGNATURES.items():
        if len(signature) // 2 > bytes_to_read:
            bytes_to_read = len(signature) // 2
        
def handle_option(path, option):
    if option == 1:
        try:
            files = os.listdir(path)
        except PermissionError:
            print(f"You don't have permission for {path}.\n")
            return
        for file in files:
            full_path = os.path.join(path, file)
            if os.path.isdir(full_path):
                handle_option(full_path, 1)
            else:
                handle_file(full_path)
    else:
        handle_file(path)

def handle_file(file_path):
    try:
        first_bytes = get_bytes(file_path)
    except PermissionError:
        print(f"You don't have permission for {file_path}.\n")
        return
    file_format = check_format(first_bytes)
    print(f"Path: {file_path}\nFormat: {file_format}\n")

def get_bytes(path):
    with open(path, 'rb') as file:
        data = file.read(bytes_to_read)
        first_bytes = data.hex().upper()
    return first_bytes

def check_format(first_bytes):
    for signature, file_format in FILE_SIGNATURES.items():
        if first_bytes.startswith(signature):
            return file_format
    return "Unknown"

if __name__ == "__main__":
    main()
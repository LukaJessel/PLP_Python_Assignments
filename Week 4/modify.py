def modify_file(old_file_path, new_file_path):
    try:
        # Open the old file for reading
        with open(old_file_path, 'r') as old_file:
            content = old_file.readlines()

        # Modify the content as needed (example: convert to uppercase)
        modified_content = [line.upper() for line in content]

        # Open the new file for writing
        with open(new_file_path, 'w') as new_file:
            new_file.writelines(modified_content)

        print("File modified successfully and saved to", new_file_path)

    except FileNotFoundError:
        print("The file", old_file_path, "does not exist.")

    except PermissionError:
        print("Permission denied when trying to access the file", old_file_path)

    except Exception as e:
        print("An error occurred:", str(e))

def main():
    old_file_path = input("Enter the filename to read from: ")
    new_file_path = input("Enter the filename to save the modified content: ")

    modify_file(old_file_path, new_file_path)

if __name__ == "__main__":
    main()
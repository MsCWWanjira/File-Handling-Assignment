# File Creation
try:
    # Open the file in write mode to create a new file
    with open("my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("This is line 1.\n")
        file.write("12345\n")  # Writing a mix of string and number
        file.write("Another line of text.\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    # Open the file in read mode
    with open("my_file.txt", "r") as file:
        # Read the contents of the file
        content = file.read()
        # Display the contents on the console
        print("Contents of my_file.txt:")
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File reading process completed.")

# File Appending
try:
    # Open the file in append mode to add additional content
    with open("my_file.txt", "a") as file:
        # Append three more lines of text to the file
        file.write("Appending line 1.\n")
        file.write("Appending line 2.\n")
        file.write("Appending line 3.\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File appending process completed.")
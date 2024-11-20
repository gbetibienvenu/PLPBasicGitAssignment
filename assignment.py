def read_and_modify_file():
    # Ask the user for the filename
    input_file = input("Enter the name of the file to read (or create): ")

    try:
        # Try to open and read the input file
        with open(input_file, 'r') as file:
            content = file.readlines()
        print(f"File '{input_file}' exists. Reading content...")

    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist. Creating it now...")
        # Create the file with some default content
        default_content = ["This is a newly created file.\n"]
        with open(input_file, 'w') as file:
            file.writelines(default_content)
        content = default_content
        print(f"File '{input_file}' created with default content.")
    
    except PermissionError:
        print(f"Error: You don't have permission to read or write '{input_file}'.")
        return  # Exit the function if permission is denied

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return  # Exit the function if another unexpected error occurs

    # Modify the content (e.g., adding line numbers)
    modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]
    
    # Write the modified content to a new file
    output_file = "modified_" + input_file
    try:
        with open(output_file, 'w') as file:
            file.writelines(modified_content)
        print(f"Modified content successfully written to '{output_file}'.")
    except Exception as e:
        print(f"Failed to write to '{output_file}': {e}")


# Run the program
if __name__ == "__main__":
    read_and_modify_file()

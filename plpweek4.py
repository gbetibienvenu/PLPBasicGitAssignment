def read_and_write_file():
    # Ask the user for the filename
    input_filename = input("Please enter the filename to read from: ")
    output_filename = input("Please enter the filename to write to: ")

    try:
        # Attempt to open the file for reading
        with open(input_filename, 'r') as infile:
            # Read the contents of the file
            content = infile.read()
            print("File read successfully!")
        
        # Modify the content (for demonstration, converting to uppercase)
        modified_content = content.upper()

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"Modified content written to {output_filename} successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: An error occurred while handling the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()

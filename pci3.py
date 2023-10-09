def read_and_write_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        # Process the content (convert to uppercase) here
        processed_content = content.upper()

        # Write the processed content back to the file
        with open(filename, 'w') as file:
            file.write(processed_content)

        print(f"File '{filename}' processed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    filename = "sample.txt"
    read_and_write_file(filename)

if __name__ == "__main__":
    main()




#unconditionally in the with open(filename, 'w') as file block.
# To avoid this issue,  make use of a temporary variable to store uppercase 
# content and write it to the file only if no exceptions occur
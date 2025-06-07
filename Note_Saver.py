def save_note():
    filename = "notes.txt"
    
    try:
        note = input("Write a note: ")
        
        # Try to open the file in append mode
        file = open(filename, "a")
        file.write(note + "\n")
        print("Note saved successfully!")

    except Exception as e:
        print("Something went wrong:", e)

    finally:
        try:
            file.close()
            print("File closed.")
        except NameError:
            # If 'file' was never created due to an error
            print("No file to close.")

# Run the note-saver
save_note()

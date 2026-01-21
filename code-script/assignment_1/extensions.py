def get_mime_type(filename):

    # Remove extra spaces and convert to lowercase
    filename = filename.strip().lower()

    # Check if there's no dot in the filename
    if '.' not in filename:
        return 'application/octet-stream'

    # Get the extension
    ext = filename.split(".")[-1]

    # Check the extension and return the corresponding MIME type
    if ext == 'gif':
        return 'image/gif'
    elif ext in ['jpg', 'jpeg']:
        return 'image/jpeg'
    elif ext == 'png':
        return 'image/png'
    elif ext == 'pdf':
        return 'application/pdf'
    elif ext == 'txt':
        return 'text/plain'
    elif ext == 'zip':
        return 'application/zip'
    else:
        return 'application/octet-stream'

def main():

    # ask the user for the file name and print the MIME type
    name = input("File name: ")
    print(get_mime_type(name))

main()
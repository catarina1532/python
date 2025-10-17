#get input from the user
file_name = input("File name: ").strip().lower()
#.strip() removes any whitespace and .lower() converts the string to lowercase making it case insensitive

#if the file name ends with a certain extension, print the corresponding media type
#.endswith() checks if the string ends with the suffix
if file_name.endswith('.gif'):
    print('image/gif')
elif file_name.endswith((".jpg", ".jpeg")):
    print('image/jpeg')
elif file_name.endswith('.png'):
    print('image/png')
elif file_name.endswith('.pdf'):
    print('application/pdf')
elif file_name.endswith('.txt'):
    print('text/plain')
elif file_name.endswith('.zip'):
    print('application/zip')
#each elif checks another extension and prints the corresponding media type
else:
    print('application/octet-stream')
#if none of the above conditions are true, print "application/octet-stream" (generic fallback type)
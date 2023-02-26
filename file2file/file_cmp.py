import filecmp

file1= r"C:\Users\nales\OneDrive\Desktop\DATA\file_1.csv"
file2= r"C:\Users\nales\OneDrive\Desktop\file_2.csv"
print(file1)
differences = filecmp.cmp(file1,file2)

if differences:
    print("files are different")
    diff_generator = filecmp.cmp(file1, file2, shallow=False)
    for line in diff_generator:
        print(line)
else:
    print("Files are the same")
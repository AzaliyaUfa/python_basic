import os

file_dir = os.path.join(os.getcwd(), "resources", "my_file.txt")
reverse_file_dir = os.path.join(os.getcwd(), "resources", "my_reverse_file.txt")

if not os.path.exists(file_dir):
    os.mkdir(os.path.join(os.getcwd(), "resources"))
    my_file = open(file_dir, 'x')
    my_file.write("line 1\nline 2\nline 3")
    my_file.close()

my_file = open(file_dir)
my_file_data = "".join(my_file.readlines())
my_file.close()

if os.path.exists(reverse_file_dir):
    os.remove(reverse_file_dir)

reverse_file = open(reverse_file_dir, 'x').write(my_file_data[::-1])

print("original file:\n" + my_file_data)
print("reversed file:\n" + my_file_data[::-1])

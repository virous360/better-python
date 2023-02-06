import sys,os
# file verification before proccessing 
#=========================================
print("="*64)
path = os.getcwd()
file_name = sys.argv[-1]
if file_name == __file__:
    file_name = input("Error : No file specified while running the script,\nplease input file name : ")
if not file_name.endswith(".bpy"):
    print(f"Error : file {file_name} doesn't end with the bpy extention...")
    print("Finished...")
#=========================================

#read file
with open(file_name,"r") as file:
    lines = file.readlines()

for line_value in lines:
    first_letter = line_value.split(" ",1).pop(0)
    print(line_value,'"',first_letter,'"')#
    if first_letter == "var":
        exec(line_value[4:])
filename1 = input ("enter Source file name ") 
with open(filename1, 'r') as file1: 
   lines = file1.readlines()
filename2 = input ("enter destination file name ") 
with open(filename2, 'w') as file2:
   for i in range(len(lines)): 
     if i % 2 == 0: 
          file2.write(lines[i])
print(f"\nOdd lines copied to '{filename2}'.")
print("\nContent of the source file:") 
with open(filename1, 'r') as file1:
   print(file1.read())
print("\n Content of the destination file:") 
with open(filename2, 'r') as file2:
   print(file2.read())

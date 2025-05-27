#Write into the file
with open("sample.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

#Append
with open("sample.txt", "a+") as f:
    f.write("Fourth line\n")
    f.write("Fifth line\n")
    f.seek(0)
    print("\nContent in sample file is:")
    print(f.read())


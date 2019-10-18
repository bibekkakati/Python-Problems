"""
    A floppy disk shows f bytes free, u bytes used. If you delete a file of size s bytes and create a new file of size n bytes, how many free bytes will be in the floppy disk ?
"""

free = int(input("Free bytes- \n"))
used = int(input("Used bytes- \n"))
delSize = int(input("Deleted file size in bytes- \n"))
newFile = int(input("New file size in bytes- \n"))

totalBytes = free + used
used =  used - delSize
used = used + newFile
free = totalBytes - used

print("free bytes ",free)

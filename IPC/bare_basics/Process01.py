import multiprocessing.shared_memory as sharedmem
import time

# Creating a memory segment with 256 bytes of size
memseg = sharedmem.SharedMemory(name="memseg_01", create=True, size=256)

message = "Hello, I am process 01 sending a message"

while True:
    # This condition checks if the "other end" read the message, which will
    # introduce 1 to address 0 if it had.
    if memseg.buf[0] == 1:
        data = message.encode() # this encodes to utf-8 as default
        memseg.buf[1:len(data)+1] = data
        memseg.buf[0] = 0
    time.sleep(1)

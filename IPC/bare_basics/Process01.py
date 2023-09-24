import multiprocessing.shared_memory as sharedmem
import time

# Creating a memory segment with 256 bytes of size
try:
    memseg = sharedmem.SharedMemory(name="memseg_01", create=True, size=256)
except FileExistsError:
    memseg = sharedmem.SharedMemory(name="memseg_01")

counter = 0

while True:
    # This condition checks if the "other end" read the message, which will
    # introduce 1 to address 0 if it had.
    
    if memseg.buf[0] == 1:
        counter += 1
        message = f"Hello, I am process 01 sending a message for the {counter} time via IPC"
        data = message.encode() # this encodes to utf-8 as default
        memseg.buf[1:len(data)+1] = data
        memseg.buf[0] = 0
    time.sleep(1)

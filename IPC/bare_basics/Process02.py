import multiprocessing.shared_memory as sharedmem
import time

# Creating a memory segment with 256 bytes of size
# Note that this one uses the shared memory but does not create it
memseg = sharedmem.SharedMemory(name="memseg_01")

while True:
    
    if memseg.buf[0] == 0:
        data = memseg.buf.tobytes().decode()
        print("Got from Process 01: ", data)

        time.sleep(3)
        # Mark as readed
        memseg.buf[0] = 1
    time.sleep(1)

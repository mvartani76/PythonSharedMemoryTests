from multiprocessing import shared_memory
import time
import sys


shm_a = shared_memory.SharedMemory(name="memtest", create=True, size=1)
print(shm_a)

a = shm_a.buf[0]
print(a)

print(shm_a.name)

a = 10
shm_a.buf[0] = 10

try:
	for i in range(40):
		print("i = " + str(i) + ", a = " + str(shm_a.buf[0]))
		time.sleep(1)
except KeyboardInterrupt:
	shm_a.close()
	shm_a.unlink()
	sys.exit()
shm_a.close()
shm_a.unlink()

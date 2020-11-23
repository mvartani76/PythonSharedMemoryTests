from multiprocessing import shared_memory
import time
import sys

shm_b = shared_memory.SharedMemory(name="memtest")
print(shm_b)

b = shm_b.buf[0]
print(b)

#b = 20
#shm_b.buf = b
try:
	for i in range(40):
		print("i =  " + str(i) + ", b = " + str(shm_b.buf[0]))
		if i == 20:
			shm_b.buf[0] = 20
		time.sleep(1)
except KeyboardInterrupt:
	shm_b.close()
	shm_b.unlink()
	sys.exit()
shm_b.close()
shm_b.unlink()

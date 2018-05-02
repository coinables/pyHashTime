import hashlib
import time

startHash = "some_super_secret_entropy"
startTime = time.time()
print("Calibrating, please wait this will take just a minute")
for i in range(10000000):
    # process 10 million hashes and time how long it takes the CPU
    x = startHash
    startHash = hashlib.sha256(x.encode()).hexdigest()

timeAfter = time.time()
changeTime = timeAfter - startTime

# print(startHash)
print("it took your CPU ",changeTime," seconds to process 10 million hashes")
minutes = float(input("how long do you want the hashing to take in minutes?"))

findMillionPerMinuteRate = 60 / changeTime
howManyMillion = minutes * findMillionPerMinuteRate
if howManyMillion >= 100:
    numberType = "Billion"
    calcAmount = howManyMillion / 100
    print(calcAmount," ",numberType," hashes to lock for ", minutes," minutes")
else:
    numberType = "Million"
    calcAmount = howManyMillion * 10
    print(calcAmount," ",numberType," hashes to lock for ", minutes," minutes")



import numpy as np
with open('Day6/data_day6.txt') as f:
    data = np.array([int(x) for x in f.read().split(',')])



freq = np.zeros(max(data)+2, dtype=np.int64)
for fish in range(data.size):
    freq[data[fish]] += 1
print(freq)



# freq1 = freq.copy()
# freqyoung = np.array([0, 0])
# n = 80
# #print(0, freq1, freqyoung)
# for i in range(n):
#     freq1 = np.roll(freq1,-1)
#     newbies = freq1[-1]
#     freq1[-1] += freqyoung[0]
#     freqyoung[0] = freqyoung[1]
#     freqyoung[1] = newbies
#     #print(i+1, freq1, freqyoung, np.sum(freq1) + np.sum(freqyoung))

    
# print(np.sum(freq1)+np.sum(freqyoung))



freq1 = freq.copy()
freqyoung = np.array([0, 0], dtype=np.int64)
n = 256
#print(0, freq1, freqyoung)
for i in range(n):
    freq1 = np.roll(freq1,-1)
    print(freq1)
    newbies = freq1[-1]
    freq1[-1] += freqyoung[0]
    freqyoung[0] = freqyoung[1]
    freqyoung[1] = newbies
    #print(i+1, freq1, freqyoung, np.sum(freq1) + np.sum(freqyoung))

    
print(np.sum(freq1)+np.sum(freqyoung))

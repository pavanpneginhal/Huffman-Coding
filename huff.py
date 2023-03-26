from heapq import heappush, heappop, heapify
from collections import defaultdict
from bitarray import bitarray
import time

text = "Kaizoku ni orewa naru"




freq_lib = defaultdict(int)    # generate a default library
for ch in text:                # count each letter and record into the frequency library 
    freq_lib[ch] += 1
    
print(freq_lib)



heap = [[fq, [sym, ""]] 
for sym, fq in freq_lib.items()]  # '' is for entering the huffman code later
print(heap)

heapify(heap) # transform the list into a heap tree structure
print(heap)

while len(heap) > 1:
    right = heappop(heap)  # heappop - Pop and return the smallest item from the heap
    print('right = ', right)
    left = heappop(heap)
    print('left = ', left)

    for pair in left[1:]:  
        pair[1] = '0' + pair[1]   # add zero to all the right edge
    for pair in right[1:]:  
        pair[1] = '1' + pair[1]   # add one to all the left edge
    heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])  # add values onto the heap. Eg. h = []; heappush(h, (5, 'write code')) --> h = [(5, 'write code')]

huffman_list = right[1:] + left[1:]
print(huffman_list)
huffman_dict = {a[0]:bitarray(str(a[1])) for a in huffman_list}
print(huffman_dict)

encoded_text = bitarray()
encoded_text.encode(huffman_dict, text)
print("ENC",encoded_text)

padding = 8 - (len(encoded_text) % 8)




with open('compressed_file.bin', 'wb') as w:
    encoded_text.tofile(w)

# start = time.time()

# end =  time.time()

# print("start time is:",start)
# print("end time is:",end)
# print("total time is:",end - start)


#Decoding

decoded_text = bitarray()

with open('compressed_file.bin', 'rb') as r:
    decoded_text.fromfile(r)
    
decoded_text = decoded_text[:-padding] # remove padding
    
decoded_text = decoded_text.decode(huffman_dict) 
decoded_text = ''.join(decoded_text)

print(decoded_text)


# with open('uncompress.bin', 'w') as w:
#     w.write(text)
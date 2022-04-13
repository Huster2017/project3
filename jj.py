import cv2,socket,pickle

data1 = "frame_data"
data2 = "BN"
print("data1 is: "+data1)
print("data2 is: "+data2)
a = pickle.dumps(data1)
b = pickle.dumps(data2)

print("encode data1: ")
print(a)
print("encode data2: ")
print(b)


c = a+b
print("Sum of 2 data: ")
print(c)
i = len(c)
info = c[i-12:]
print("get data2 from sum_data: ")
print(pickle.loads(info))
print("get data1 from sum_data: ")
f  = c[:i]
print(pickle.loads(f))

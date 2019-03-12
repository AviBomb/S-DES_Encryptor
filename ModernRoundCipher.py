# Read Fuction helps us take in the input of the user for the Grammer to be followed by the encoder
# Parameters To Function :
# 1) n - is the number of terms to be read into the array
# 2) k - is true when the data to be entered is palain text (ie: comprising of 1's and 0's)
# 3) r - is true when the reduction of the data takes place (ie: permutations operation) the maximum value to be allowed is number_of_terms(n)+2 
# 4) u - is true when the expansion of the data takes place (ie: expand and permutations operation) the values to be allowed can be reapeated 2 times

def read(n,k=0,r=0,u=0): 
	x = input('Enter the sequece : ')
	y=x.split()
	arr=[]
	for i in y:
		arr.append(int(i))
	if(len(arr)!=n):
		print("The number of terms is incorrect re-enter data.")
		return(arr,0)
	if(k==1):
		for j in arr:
			if(j>1 or j<0):
				print("The plain text should only be in 1's and 0's re-enter data.")
				return(arr,0)
	if(k==0):
		if(r==1):
			for j in arr:
				if(j>n+2 or j<=0):
					print("Some of the terms might out of range re-enter data.")
					return(arr,0)
		if(r==0):
			for j in arr:
				if(j>n or j<=0):
					print("Some of the terms might out of range re-enter data.")
					return(arr,0)
		arr1=[]
		if(u==0):
			for k in arr:
				if k not in arr1:
					arr1.append(k)
			if(len(arr1)!=n):
				print("Some of the terms have be repeated re-enter data.")
				return(arr,0)
		arr2=[]
		if(u==1):
			for l in arr:
				ct=0
				for k in arr:
					if (l==k):
						ct=ct+1
				if(ct > 2):
					print("Some of the terms have be repeated more than twice re-enter data.")
					return(arr,0)
				if(ct < 2):
					print("Some of the terms may not belong to the sequence re-enter data.")
					return(arr,0)	
	return(arr,1)

def read_matrix (n=4):
	main_list = []
	for i in range(n):
		temp_list = []
		for j in range(n):
			temp_list.append(input("Element {0}:{1}: ".format(i,j)))
		main_list.append(temp_list)
	main_list1 = []
	for row in main_list:
		temp_list = []
		for l in row:
			if (l==''):
				print("Some of the elements are missing re-enter data.")
				return(main_list,0)
			else:
				temp_list.append(int(l))
		main_list1.append(temp_list)
	for row in main_list1:
		for k in row:
			if (k<0 or k>4):
				print("Some of the terms might out of range re-enter data.")
				return(main_list,0)	
	return(main_list,1)

def left_shift(arr):
	arr1=[]
	ct=0;
	temp=0;
	for i in arr:
		if(ct==0):
			temp=i
			ct=ct+1
		else:
			arr1.append(i)
	arr1.append(temp)
	return(arr1)

def binary_generator(a,b):
	arr=[]
	if(a==0):
		arr.append(0)
		arr.append(0)
	if(a==1):
		arr.append(0)
		arr.append(1)
	if(a==2):
		arr.append(1)
		arr.append(0)
	if(a==3):
		arr.append(1)
		arr.append(1)		
	if(b==0):
		arr.append(0)
		arr.append(0)
	if(b==1):
		arr.append(0)
		arr.append(1)
	if(b==2):
		arr.append(1)
		arr.append(0)
	if(b==3):
		arr.append(1)
		arr.append(1)
	return (arr)

def generate_new(arr,arr1):
	arr2=[]
	for i in arr:
		ct=1;
		for j in arr1:
			if(ct==i):
				arr2.append(j)
				ct=ct+1
			else:
				ct=ct+1
	return(arr2)

def exor(arr,arr1):
	arr2=[]
	for i in range(0,len(arr)):
		if((arr[i] and not arr1[i]) or (not arr[i] and arr1[i])):
			arr2.append(1)
		else:
			arr2.append(0)
	return(arr2)

def row_col(arr):	
	if(arr[0]==0 and arr[3]==0):
		row=0
	if(arr[0]==0 and arr[3]==1):
		row=1
	if(arr[0]==1 and arr[3]==0):
		row=2
	if(arr[0]==1 and arr[3]==1):
		row=3
	if(arr[1]==0 and arr[2]==0):
		col=0
	if(arr[1]==0 and arr[2]==1):
		col=1
	if(arr[1]==1 and arr[2]==0):
		col=2
	if(arr[1]==1 and arr[2]==1):
		col=3
	return (row,col)

#Start Reading Of Parameters
print ("Enter P10 Pattern : ")
p10=[]
k=0
while (k==0):
	p10,k=read(10)
print (p10)
print ("Enter (Reduction) Permutations Pattern (P8) : ")
p8=[]
k=0
while (k==0):
	p8,k=read(8,0,1,0)
print (p8)
print ("Enter Key : ")
mk=[]
k=0
while (k==0):
	mk,k=read(10,1,0,0)
print (mk)
print ("Enter IP Pattern : ")
ip=[]
k=0
while (k==0):
	ip,k=read(8)
print (ip)
print ("Enter IP Inverse Pattern : ")
ip1=[]
k=0
while (k==0):
	ip1,k=read(8)
print (ip1)
print ("Enter Exand and Permutations Pattern (E/P) : ")
ep=[]
k=0
while (k==0):
	ep,k=read(8,0,0,1)
print (ep)
print ("Enter S0 Matrix : ")
s0=[]
k=0
while (k==0):
	s0,k=read_matrix()
print (s0)
print ("Enter S1 Matrix : ")
s1=[]
k=0
while (k==0):
	s1,k=read_matrix()
print (s1)
print ("Enter P4 Pattern : ")
p4=[]
k=0
while (k==0):
	p4,k=read(4)
print (p4)
print ("Enter Plain Text : ")
pt=[]
k=0
while (k==0):
	pt,k=read(8,1,0,0)
print (pt)
#End Of Reading of Parameters

#Generating Of Key 1
arr=[]
arr=generate_new(p10,mk)
print (arr)
arr1=[]
arr2=[]
for i in range (0,5):
	arr1.append(arr[i])
arr1=left_shift(arr1)
for i in range (5,10):
	arr2.append(arr[i])
arr2=left_shift(arr2)
arr=[]
for i in range (0,5):
	arr.append(arr1[i])
for i in range (0,5):	
	arr.append(arr2[i])
print (arr)
k1=[]
k1=generate_new(p8,arr)
print (k1)
#End of Key 1 Generating

#Generating Of Key 2
arr1=left_shift(arr1)
arr1=left_shift(arr1)
arr2=left_shift(arr2)
arr2=left_shift(arr2)
arr=[]
for i in range (0,5):
	arr.append(arr1[i])
for i in range (0,5):	
	arr.append(arr2[i])
print (arr)
k2=[]
k2=generate_new(p8,arr)
print (k2)
#End of Key 2 Generating

arr=[]
arr=generate_new(ip,pt)
arr1=[]
arr2=[]
for i in range (0,4):
	arr1.append(arr[i])
print (arr1)
for i in range (4,8):
	arr2.append(arr[i])
print (arr2)	
arr5=[]
arr5=generate_new(ep,arr2)
arr6=[]
arr6=exor(arr5,k1)
print (arr)
arr3=[]
arr4=[]
for i in range (0,4):
	arr3.append(arr6[i])
for i in range (4,8):
	arr4.append(arr6[i])

row,col=row_col(arr3)
temp=int(s0[row][col])
print (temp)
row,col=row_col(arr4)
temp1=int(s1[row][col])
print(temp1)
arr7=[]
arr7=binary_generator(temp,temp1)
print (arr7)
arr8=[]
arr8=generate_new(p4,arr7)
print (arr8)
arr9=[]
arr9=exor(arr8,arr1)
print(arr9)


arr5=[]
arr5=generate_new(ep,arr9)
arr6=[]
arr6=exor(arr5,k2)
print (arr)
arr3=[]
arr4=[]
for i in range (0,4):
	arr3.append(arr6[i])
for i in range (4,8):
	arr4.append(arr6[i])

row,col=row_col(arr3)
temp=int(s0[row][col])
print (temp)
row,col=row_col(arr4)
temp1=int(s1[row][col])
print(temp1)
arr7=[]
arr7=binary_generator(temp,temp1)
print (arr7)
arr8=[]
arr8=generate_new(p4,arr7)
print (arr8)
arr10=[]
arr10=exor(arr8,arr2)
print(arr10)

arr=[]
for i in range (0,4):
	arr.append(arr10[i])
for i in range (0,4):
	arr.append(arr9[i])
arr_final=[]	
arr_final=arr5=generate_new(ip1,arr)
print(arr_final)
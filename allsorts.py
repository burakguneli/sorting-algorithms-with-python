import random
import time
import copy
import sys
sys.setrecursionlimit(10000)
size2 = 10000
span = 1000000
threshold = 20

# Insertion Sort
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum

# Selection Sort
def selection_sort(A):
	for i in range (0, len(A) - 1):
		minIndex = i
		for j in range (i+1, len(A)):
			if A[j] < A[minIndex]:
				minIndex = j
		if minIndex != i:
			A[i], A[minIndex] = A[minIndex], A[i]

# Bubble Sort
def bubble_sort1(A):
	for i in range (0, len(A) - 1):
		for j in range (0, len(A) - i - 1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]

def bubble_sort2(A):
	for i in range (0, len(A) - 1):
		done = True
		for j in range (0, len(A) - i - 1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
				done = False
		if done:
			return

# Merge Sort
def merge_sort(A):
	merge_sort2(A, 0, len(A)-1)

def merge_sort2(A, first, last):
	if last-first < threshold and first < last:
		quick_selection(A, first, last)
	elif first < last:
		middle = (first + last)//2
		merge_sort2(A, first, middle)
		merge_sort2(A, middle+1, last)
		merge(A, first, middle, last)

def merge(A, first, middle, last):
	L = A[first:middle]
	R = A[middle:last+1]
	L.append(999999999)
	R.append(999999999)
	i = j = 0

	for k in range (first, last+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1

# Quick Sort
def quick_sort(A):
	quick_sort2(A, 0, len(A)-1)

def quick_sort2(A, low, hi):
	if hi-low < threshold and low < hi:
		quick_selection(A, low, hi)
	elif low < hi:
		p = partition(A, low, hi)
		quick_sort2(A, low, p - 1)
		quick_sort2(A, p + 1, hi)

def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]])
	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]:
		return mid
	return hi

def partition(A, low, hi):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low

	for i in range(low, hi+1):
		if A[i] < pivotValue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]

	return (border)

def quick_selection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]

# Heap Sort
def heapsort(a):
    heapify(a, len(a))
    end = len(a)-1
    while end > 0:
        a[end], a[0] = a[0], a[end]
        end -= 1
        sift_down(a, 0, end)

def heapify(a, count):
    start = int((count-2)/2)
    while start >= 0:
        sift_down(a, start, count-1)
        start -= 1

def sift_down(a, start, end):
    root = start
    while (root*2+1) <= end:
        child = root * 2 + 1
        swap = root
        if a[swap] < a[child]:
            swap = child
        if (child + 1) <= end and a[swap] < a[child+1]:
            swap = child+1
        if swap != root:
            a[root], a[swap] = a[swap], a[root]
            root = swap
        else:
            return

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#Test part
#RANDOM ARRAY --------------------
print("")
start_time = time.time()
print("Random\n---------------------------------")

w = [random.randint(0, span) for a in range(0, size2)]
insertion_sort3(w)
print("Insertion Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
w = [random.randint(0, span) for a in range(0, size2)]
selection_sort(w)
print("Selection Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
w = [random.randint(0, span) for a in range(0, size2)]
bubble_sort2(w)
print("Bubble Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
w = [random.randint(0, span) for a in range(0, size2)]
merge_sort(w)
print("Merge Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
w = [random.randint(0, span) for a in range(0, size2)]
quick_sort(w)
print("Quick Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
w = [random.randint(0, span) for a in range(0, size2)]
heapsort(w)
print("Heap Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

#ALREADY SORTED ------------------------
start_time = time.time()
print("\nAlready Sorted\n---------------------------------")

w = [a for a in range(0, size2)]
insertion_sort3(w)
print("Insertion Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
selection_sort(w)
print("Selection Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
bubble_sort2(w)
print("Bubble Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
merge_sort(w)
print("Merge Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
quick_sort(w)
print("Quick Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
heapsort(w)
print("Heap Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

#REVERSE SORTED ---------------------------------
start_time = time.time()
print("\nReverse Sorted\n---------------------------------")

w = [a for a in range(0, size2)]
w.reverse()
insertion_sort3(w)
print("Insertion Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
w = [a for a in range(0, size2)]
w.reverse()
selection_sort(w)
print("Selection Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
w = [a for a in range(0, size2)]
w.reverse()
bubble_sort2(w)
print("Bubble Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
w = [a for a in range(0, size2)]
w.reverse()
merge_sort(w)
print("Merge Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
w = [a for a in range(0, size2)]
w.reverse()
quick_sort(w)
print("Quick Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))

start_time = time.time()
w = [a for a in range(0, size2)]
w.reverse()
heapsort(w)
print("Heap Sort(size="+ str(size2)+"): ", round(time.time() - start_time, 11))
print("")

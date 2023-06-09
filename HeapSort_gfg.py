#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        if 2 * i + 1 >= n:
            return

        c = 2 * i + 1
        
        if c + 1 < n and arr[c + 1] > arr[c]:
            c += 1
        if arr[i] < arr[c]:
            arr[i], arr[c] = arr[c], arr[i]
            
        self.heapify(arr, n, c)
        
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
        return arr
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        heap = self.buildHeap(arr, n)
        for i in range(len(heap) - 1, -1, -1):
            max_ = heap[0]
            temp = heap[i]
            heap[i] = max_
            heap[0] = temp
            self.heapify(heap, i, 0)
        return heap

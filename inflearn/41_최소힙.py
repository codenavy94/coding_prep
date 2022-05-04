import sys
sys.stdin = open('input.txt', 'r')

# 최소힙 리스트로 구현해보기 (단점: 시간이 오래 걸림)

def up_heap(heap:list):
    c = len(heap)-1
    while c > 0:
        p = (c-1)//2
        if heap[c] <= heap[p]:
            heap[c], heap[p] = heap[p], heap[c]
        c = p
    return heap
    
def down_heap(heap:list):
    idx = 0
    while idx < (len(heap)-1)//2:
        left = idx*2+1
        right = idx*2+2
        if heap[left] <= heap[right]:
            heap[idx], heap[left] = heap[left], heap[idx]
            idx = left
        else:
            heap[idx], heap[right] = heap[right], heap[idx]
            idx = right
    return heap

heap = []
while True:
    a = int(input())
    if a == -1:
        break
    elif a == 0:
        res = heap.pop(0)
        print(res)
        if heap:
            last = heap.pop()
            heap.insert(0, last)
            heap = down_heap(heap)
    else:
        heap.append(a)
        heap = up_heap(heap)
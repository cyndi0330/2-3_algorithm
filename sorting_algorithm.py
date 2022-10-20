from collections import deque

def bubble(A):
    for i in range(1, len(A)):
        for j in range(len(A) - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

    return A


def insertion(A):
    for j in range(2, len(A)):
        key = A[j]
        i = j-1
        while i > 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key

    return A


def selection(A):
    for i in range(1, len(A)-1):
        key = i
        for j in range(i+1, len(A)):
            if A[key] > A[j]:
                key = j
            temp = key
            key = j
            j = temp

    return A


def merge(A):
    stack = [[0, len(A)]]
    idx = 0
    while idx < len(stack):
        l, r = stack[idx]
        if r - l > 2:
            stack.append([l, (l + r) // 2])
            stack.append([(l + r) // 2, r])
        idx += 1

    while stack:
        l, r = stack.pop()
        c = (l + r) // 2

        tmp_l = A[l:c] + [2 ** 32 - 1]
        tmp_r = A[c:r] + [2 ** 32 - 1]

        p = l
        lp, rp = 0, 0
        while p < r:
            if tmp_l[lp] > tmp_r[rp]:
                A[p] = tmp_r[rp]
                rp += 1
            else:
                A[p] = tmp_l[lp]
                lp += 1
            p += 1

    return A

import time
def quick(A):
    queue = deque()
    queue.append([0, len(A) - 1])

    while queue:
        l, r = queue.popleft()
        if l < r:
            i, j = l, l - 1
            while i < r:
                if A[i] < A[r]:
                    j += 1
                    A[i], A[j] = A[j], A[i]
                i += 1
            A[r], A[j + 1] = A[j + 1], A[r]
            queue.append([l, j])
            queue.append([j + 2, r])

    return A

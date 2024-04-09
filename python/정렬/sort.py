from random import randint

def bubble_sort(arr: list[int], reverse=False):
  for i in range(len(arr)):
    swapped = False
    for j in range(len(arr) - i - 1):
      if not (arr[j] > arr[j + 1] and not reverse or arr[j] < arr[j + 1] and reverse):
        continue
      arr[j], arr[j + 1] = arr[j + 1], arr[j]
      swapped = True
    if not swapped:
      break
  return arr


def selection_sort(arr: list[int], reverse=False):
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if not (arr[i] > arr[j] and not reverse or arr[i] < arr[j] and reverse):
        continue
      arr[i], arr[j] = arr[j], arr[i]
  return arr

def insertion_sort(arr: list[int], reverse=False):
  for i in range(1, len(arr)):
    key_val = arr[i]
    for j in range(i - 1, -1, -1):
      if key_val < arr[j] and not reverse or key_val > arr[j] and reverse:
        arr[j + 1] = arr[j]
        continue
      arr[j + 1] = key_val
      break
    else:
      arr[0] = key_val
  return arr

def quick_sort(arr, reverse=False):
  stack = [(0, len(arr) - 1)]

  def partition(arr, low, high):
    randind = randint(low, high)
    arr[high], arr[randind] = arr[randind], arr[high]
    pivot = arr[high]
    i = low

    for j in range(low, high):
      if arr[j] > pivot and not reverse or arr[j] < pivot and reverse:
        continue
      arr[i], arr[j] = arr[j], arr[i]
      i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i
  
  while len(stack):
    low, high = stack.pop()
    if low >= high:
      continue
    pi = partition(arr, low, high)
    stack.append((low, pi - 1))
    stack.append((pi + 1, high))

  return arr
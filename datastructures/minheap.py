from typing import Any


# Static helper functions

def parent(i: int) -> int:
    return (i - 1) // 2

def lchild(i: int) -> int:
    return (i * 2) + 1

def rchild(i: int) -> int:
    return (i * 2) + 2

def has_lchild(i: int, array) -> bool:
    return lchild(i) < len(array)

def has_rchild(i: int, array) -> bool:
    return rchild(i) < len(array)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


class MinHeap:

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return str(self.array)

    # Bubbles an item at an index up into its appropriate place in the heap.
    def bubble_up(self, index):
        if index <= 0:
            return

        item = self.array[index]
        parent_index = parent(index)
        parent_item = self.array[parent_index]

        if parent_item > item:
            swap(self.array, index, parent_index)
            self.bubble_up(parent_index)

    # Adds an item to the heap.
    def push(self, item):
        self.array.append(item)
        self.bubble_up(len(self.array)-1)


    # Heapify maintains the Min Heap invariant by recursively checking that
    # the parent value is less than or equal to both its children.
    def heapify(self, parent_index: int):

        # If we don't have a left child, we won't have any children, so we're done
        if not has_lchild(parent_index, self.array):
            return

        # We at least know we have a left child at this point, so cache some vars
        parent_item = self.array[parent_index]
        lchild_index = lchild(parent_index)
        lchild_item = self.array[lchild_index]

        # We've got a left child, but no right child
        if not has_rchild(parent_index, self.array):
            # Just check if the parent should swap with left child, then we're done
            if parent_item > lchild_item:
                swap(self.array, parent_index, lchild_index)
            return

        # We've got both children
        rchild_index = rchild(parent_index)
        rchild_item = self.array[rchild_index]

        # See if we should swap down at all
        if parent_item > lchild_item or parent_item > rchild_item:

            # If so, swap with the minimum of the two
            if lchild_item <= rchild_item:
                # left child was smaller, so swap with it and recursively heapify
                swap(self.array, parent_index, lchild_index)
                self.heapify(lchild_index)
            else:
                # right child was smaller, so swap with it and recursively heapify
                swap(self.array, parent_index, rchild_index)
                self.heapify(rchild_index)


    # Pops the top item off the top of the heap.
    # Runs heapify() to maintain the Min Heap invariant.
    def pop(self) -> (Any, bool):
        ok = True

        # Edge case, heap is empty
        if len(self.array) == 0:
            return None, not ok

        # Save off the item to return
        item = self.array[0]

        # Swap the last element into the root's location,
        # remove the last element then heapify
        swap(self.array, 0, len(self.array) - 1)
        del self.array[-1]

        # If we've got either an empty or single-item heap left, we're done
        if len(self.array) > 1:
            self.heapify(0)

        return item, ok

    # Updates a value in our heap, while maintaining the Min Heap invariant
    def update(self, index: int, item) -> bool:

        if index >= len(self.array):
            return False

        old_val = self.array[index]
        self.array[index] = item

        # If we're changing the value to something less, we need to check
        # we didn't being smaller than our parent, by bubbling up.
        if item < old_val:
            self.bubble_up(index)

        # If we're changing the value to something greater, we need to check
        # we didn't become larger than either of our children, by heapifying.
        if item > old_val:
            self.heapify(index)

        return True

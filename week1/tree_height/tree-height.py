# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
 

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.pointer = [0] * self.n
                

        def compute_height(self):
                # Replace this code with a faster implementation
                def height(i):
                        parent = self.parent[i]
                        if parent==-1:
                                return 1

                        if self.pointer[i]:
                                return self.pointer[i]

                        self.pointer[i] = 1 + height(parent)
                        return self.pointer[i]
                max_height = 0
                for i in range(self.n):
                        if max_height<height(i):
                                max_height = height(i)
                return max_height

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()

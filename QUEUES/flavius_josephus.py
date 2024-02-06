from collections import deque


""" 
    Since writing our own queue implementation
    with python lists is quite cumbersome we'll
    use dequeue from collections to solve the 
    famous Flaviuos-Josephus problem.
    
    Given n soldiers and k (k-1 steps if k=3 i=1
    then soldier i=3 is executed) write a function
    that returns the position of the only survivor.
"""

def survivor(n: int, k: int) -> int:
    soldiers = deque(i+1 for i in range(n))

    steps = 1
    while len(soldiers) > 1:
        chosen = soldiers.popleft()

        if steps != k:
            soldiers.append(chosen)
        else:
            steps = 0 

        steps += 1
    
    return soldiers.popleft()

if __name__ == "__main__":
    print("Flavious-Josephus 41-3: ", survivor(41, 3))


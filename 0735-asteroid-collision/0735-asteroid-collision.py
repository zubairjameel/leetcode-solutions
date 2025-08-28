from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            destroyed = False
            while stack and a < 0 < stack[-1]:
                if abs(a) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(a) == stack[-1]:
                    stack.pop()
                destroyed = True
                break
            if not destroyed:
                stack.append(a)
        return stack

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []   # stack stores indices
        max_area = 0
        heights.append(0)   # dummy bar to empty stack at the end

        for i, curr in enumerate(heights):
            # If top > curr → we need to pop and calculate area
            while stack and heights[stack[-1]] > curr:
                height = heights[stack.pop()]  # height is the popped value

                # Width calculation:
                # If stack is empty, width = i (all bars before this index are >= popped height)
                if not stack:
                    width = i
                else:
                    # Otherwise, width = (i - stack[-1] - 1)
                    # Meaning rectangle extends between current index and new top
                    width = i - stack[-1] - 1

                # Area = height × width
                area = height * width
                max_area = max(max_area, area)

            # If top <= curr → just push index into stack
            stack.append(i)

        return max_area

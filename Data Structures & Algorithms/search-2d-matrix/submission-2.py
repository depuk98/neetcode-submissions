class Solution:
    def binser(self, i, target):
        low, high = 0, len(i) - 1
        while low <= high:
            mid = (low + high) // 2
            if i[mid] == target:
                return True
            elif i[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target <= i[-1]:
                return self.binser(i, target)
        return False
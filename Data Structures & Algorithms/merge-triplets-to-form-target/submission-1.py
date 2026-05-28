class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # brute force
        x,y,z = False, False, False
        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue
            if trip[0] == target[0]:
                x = True
            if trip[1] == target[1]:
                y = True
            if trip[2] == target[2]:
                z = True
            if x and y and z:
                return True
        return False
            
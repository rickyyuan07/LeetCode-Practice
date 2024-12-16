class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        ax1, ax2 = min(ax1, ax2), max(ax1, ax2)
        ay1, ay2 = min(ay1, ay2), max(ay1, ay2)
        bx1, bx2 = min(bx1, bx2), max(bx1, bx2)
        by1, by2 = min(by1, by2), max(by1, by2)

        ans = (ax2-ax1) * (ay2-ay1) + (bx2-bx1) * (by2-by1)
        x_overlap = min(ax2, bx2) - max(ax1, bx1)
        y_overlap = min(ay2, by2) - max(ay1, by1)
        if x_overlap > 0 and y_overlap > 0:
            ans -= x_overlap * y_overlap
        
        return ans
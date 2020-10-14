class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if D <= F or C <= E or B >= H or A >= G:
            return (D-B) * (C-A) + (H-F) * (G-E)
        
        left = max(E, A)
        right = min(C, G)
        up = min(H, D)
        down = max(F, B)
        return (D-B) * (C-A) + (H-F) * (G-E) - (up-down) * (right-left)

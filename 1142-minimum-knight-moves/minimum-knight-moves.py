class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        offsets = [(1, 2), (2, 1), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1)]

        # Bidirectional BFS
        origin_deq = deque([(0, 0, 0)]) # x, y, step
        origin_dct = {(0, 0): 0}

        dest_deq = deque([(x, y, 0)])
        dest_dct = {(x, y): 0}

        while dest_deq and origin_deq:
            origin_x, origin_y, origin_s = origin_deq.popleft()
            if (origin_x, origin_y) in dest_dct:
                return origin_s + dest_dct[(origin_x, origin_y)]

            dest_x, dest_y, dest_s = dest_deq.popleft()
            if (dest_x, dest_y) in origin_dct:
                return dest_s + origin_dct[(dest_x, dest_y)]

            for off_x, off_y in offsets:
                new_origin_x, new_origin_y = origin_x + off_x, origin_y + off_y
                if (new_origin_x, new_origin_y) not in origin_dct:
                    origin_dct[(new_origin_x, new_origin_y)] = origin_s + 1
                    origin_deq.append((new_origin_x, new_origin_y, origin_s+1))

                new_dest_x, new_dest_y = dest_x + off_x, dest_y + off_y
                if (new_dest_x, new_dest_y) not in dest_dct:
                    dest_dct[(new_dest_x, new_dest_y)] = dest_s + 1
                    dest_deq.append((new_dest_x, new_dest_y, dest_s+1))
            
        return 0
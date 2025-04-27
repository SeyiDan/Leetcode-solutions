class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
    
        merged = []
        for interval in intervals:
            # If merged is empty or current interval doesn't overlap with previous
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is overlap, so we merge with the previous interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

class Solution:
   def minWindow(self, s: str, t: str) -> str:
       
       t_counts = Counter(t)
       w_counts = Counter()
       
       min_low, min_high = 0, len(s)
       low = 0
       
       for high in range(len(s)):
           w_counts[s[high]] += 1
           
           while all(t_counts[ch] <= w_counts[ch] for ch in t_counts):
               if high - low < min_high - min_low:
                   min_low, min_high = low, high
               if s[low] in t_counts:
                   w_counts[s[low]] -= 1
               low += 1
               
       return s[min_low : min_high + 1] if min_high < len(s) else ""
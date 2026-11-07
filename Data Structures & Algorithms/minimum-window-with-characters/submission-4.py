class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need_counts = Counter(t)
        window = {}
        need = len(need_counts)
        have = 0

        best_l, best_len = 0, float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            if c in need_counts:
                window[c] = window.get(c, 0) + 1
                if window[c] == need_counts[c]:
                    have += 1

            while have == need:
                if r - l + 1 < best_len:
                    best_l, best_len = l, r - l + 1

                left_char = s[l]
                if left_char in need_counts:
                    window[left_char] -= 1
                    if window[left_char] < need_counts[left_char]:
                        have -= 1
                l += 1

        return s[best_l:best_l + best_len] if best_len != float("inf") else ""
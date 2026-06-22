class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def compare(cnt1, cnt2):
            for k,v in cnt1.items():
                if k not in cnt2 or cnt2[k] < v:
                    return False
            return True
        t_cnt = Counter(t)
        cur = defaultdict(int)
        cur_len = math.inf
        res = ""

        l = 0
        if len(s) < len(t):
            return ""
        if s == t:
            return s
        for i in range(len(t)):
            cur[s[i]] += 1
        if compare(t_cnt,cur):
            return s[l:len(t)]
        for r in range(len(t),len(s)):
            cur[s[r]] += 1
            if s[r] in t_cnt:
                if compare(t_cnt, cur):
                    while s[l] not in t_cnt or t_cnt[s[l]] < cur[s[l]]:
                        cur[s[l]] -= 1
                        l += 1
                    if r-l+1 < cur_len:
                        res = s[l:r+1]
                        cur_len = r-l+1
            
        return res
           

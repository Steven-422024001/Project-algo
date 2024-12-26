class Arrays:
    def kadane_algorithm(self, arr):
        """
        Kadane's Algorithm: Menemukan subarray dengan jumlah maksimum.
        """
        max_current = max_global = arr[0]
        for i in range(1, len(arr)):
            max_current = max(arr[i], max_current + arr[i])
            if max_current > max_global:
                max_global = max_current
        return max_global

    def floyd_algorithm(self, arr):
        """
        Floyd's Algorithm: Deteksi loop dalam linked list (diimplementasikan dengan array).
        """
        slow = fast = 0
        while fast < len(arr) and arr[fast] < len(arr):
            slow = arr[slow]
            fast = arr[arr[fast]]
            if slow == fast:
                return True
        return False

    def kmp_algorithm(self, text, pattern):
        """
        KMP Algorithm: Mencari posisi kemunculan pertama pola dalam teks.
        """
        def build_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = build_lps(pattern)
        i = j = 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            if j == len(pattern):
                return i - j
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    def quick_select(self, arr, k):
        """
        Quick Select: Menemukan elemen ke-k terkecil dalam array.
        """
        if len(arr) == 1:
            return arr[0]
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        if k <= len(left):
            return self.quick_select(left, k)
        elif k == len(left) + 1:
            return pivot
        else:
            return self.quick_select(right, k - len(left) - 1)

    def boyer_moore_majority(self, arr):
        """
        Boyer-Moore Majority Vote: Mencari elemen mayoritas dalam array.
        """
        candidate, count = None, 0
        for num in arr:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
class Sorting:
    def insertion_sort(self, arr):
        """
        Insertion Sort: Memasukkan elemen pada posisi yang benar secara bertahap.
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def selection_sort(self, arr):
        """
        Selection Sort: Memilih elemen terkecil di setiap iterasi dan menukarnya ke posisi yang benar.
        """
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def heap_sort(self, arr):
        """
        Heap Sort: Membuat heap dan menggunakan heap untuk menyortir elemen.
        """
        import heapq
        heapq.heapify(arr)  # Mengubah array menjadi heap
        return [heapq.heappop(arr) for _ in range(len(arr))]

    def merge_sort(self, arr):
        """
        Merge Sort: Membagi array menjadi dua bagian dan menggabungkannya dalam urutan terurut.
        """
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

        return arr

    def quick_sort(self, arr):
        """
        Quick Sort: Memilih pivot dan memisahkan elemen lebih kecil atau besar dari pivot.
        """
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

    def counting_sort(self, arr):
        """
        Counting Sort: Menghitung frekuensi elemen dan menyusun array berdasarkan jumlah tersebut.
        """
        if not arr:
            return arr
        max_val = max(arr)
        count = [0] * (max_val + 1)

        for num in arr:
            count[num] += 1

        sorted_arr = []
        for i, freq in enumerate(count):
            sorted_arr.extend([i] * freq)

        return sorted_arr

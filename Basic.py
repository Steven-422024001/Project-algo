class Basic:
    def huffman_coding(self, data):
        """
        Huffman Coding: Menghasilkan kode biner untuk setiap karakter berdasarkan frekuensi.
        """
        # Contoh sederhana: karakter yang sering muncul diberi kode lebih pendek.
        from collections import Counter
        freq = Counter(data)
        return {char: bin(i)[2:] for i, char in enumerate(freq)}

    def euclids_algorithm(self, a, b):
        """
        Euclid's Algorithm: Mencari FPB (GCD) dari dua angka.
        """
        while b != 0:
            a, b = b, a % b
        return a

    def union_find(self, n, edges):
        """
        Union-Find: Menentukan jumlah kelompok (komponen) dalam sebuah graf.
        """
        parent = list(range(n))

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        for u, v in edges:
            parent[find(u)] = find(v)

        return len(set(find(i) for i in range(n)))

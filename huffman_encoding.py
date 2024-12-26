import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)


    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def build_huffman_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}

    if node:
        if node.char is not None:
            code_map[node.char] = prefix
        build_huffman_codes(node.left, prefix + "0", code_map)
        build_huffman_codes(node.right, prefix + "1", code_map)

    return code_map

def huffman_encode(text):
    if not text:
        return "", {}

    root = build_huffman_tree(text)
    huffman_codes = build_huffman_codes(root)

    encoded_text = ''.join(huffman_codes[char] for char in text)

    print(len(huffman_codes), len(encoded_text))
    for char, code in sorted(huffman_codes.items()):
        print(f"'{char}': {code}")
    print(encoded_text)

    return encoded_text, huffman_codes


text = "Errare humanum est."
huffman_encode(text)

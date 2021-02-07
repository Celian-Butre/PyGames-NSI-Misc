import time
from compressionHuffman import CompressionHuffman
from compression8bit import Compression8bit

def compareCompressions(file):
    t0 = time.time()
    text8bit = Compression8bit(file)
    text8bit.compress()
    t1 = time.time()
    text8bit.decompress()
    t2 = time.time()
    text8bit.compress()
    t3 = time.time()
    print("8bit compression without a pre-existing encoding table took ", t1-t0, " seconds")
    print("8bit compression with a pre-existing encoding table took ", t3-t2, " seconds")
    print("8bit decompression took ", t2-t1, " seconds")
    print("An 8bit compressed text takes up ", len(text8bit.compressedText), " bytes")
    
    
    t0 = time.time()
    textHuffman = CompressionHuffman(file)
    textHuffman.compress()
    t1 = time.time()
    textHuffman.decompress()
    t2 = time.time()
    textHuffman.compress()
    t3 = time.time()
    print("Huffman compression without a pre-existing encoding table took ", t1-t0, " seconds")
    print("Huffman compression with a pre-existing encoding table took ", t3-t2, " seconds")
    print("Huffman decompression took ", t2-t1, " seconds")
    print("A Huffman compressed text takes up ", len(textHuffman.compressedText), " bytes")
    
if __name__ == '__main__':
    compareCompressions("longerRandomText.txt")
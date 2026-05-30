import bz2
import zstandard as zstd


def compress_bz2(data: bytes) -> bytes:
    return bz2.compress(data)


def decompress_bz2(data: bytes) -> bytes:
    return bz2.decompress(data)


def compress_zstd(data: bytes) -> bytes:
    compressor = zstd.ZstdCompressor()
    return compressor.compress(data)


def decompress_zstd(data: bytes) -> bytes:
    decompressor = zstd.ZstdDecompressor()
    return decompressor.decompress(data)

import os
import time
import tarfile
import io

from .utils import get_algorithm_from_extension
from .algorithms import compress_bz2, decompress_bz2, compress_zstd, decompress_zstd


def compress(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError(f"Источник не найден: {source}")

    algo = get_algorithm_from_extension(destination)
    if algo is None:
        raise ValueError("Недопустимое расширение")

    print(f"Архивация: {source} -> {destination}")
    start = time.time()

    # Если директория — сначала упаковываем в tar
    if os.path.isdir(source):
        data = make_tar(source)
    else:
        with open(source, 'rb') as f:
            data = f.read()

    # Сжимаем данные
    if algo == 'bz2':
        compressed = compress_bz2(data)
    else:
        compressed = compress_zstd(data)

    with open(destination, 'wb') as f:
        f.write(compressed)

    period = time.time() - start
    size = os.path.getsize(destination)
    print(f"Готово, Время: {period:.3f} сек")


def decompress(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError(f"Архив не найден: {source}")

    algo = get_algorithm_from_extension(source)
    if algo is None:
        raise ValueError("Недопустимое расширение архива")

    print(f"Распаковка: {source} -> {destination}")
    start = time.time()

    # Читаем сжатые данные из файла
    with open(source, 'rb') as f:
        compressed = f.read()

    # Распаковываем
    if algo == 'bz2':
        data = decompress_bz2(compressed)
    else:
        data = decompress_zstd(compressed)

    # Проверяем: внутри tar (директория) ил файл
    buffer = io.BytesIO(data)
    if tarfile.is_tarfile(buffer):
        os.makedirs(destination, exist_ok=True)
        buffer.seek(0)
        with tarfile.open(fileobj=buffer, mode='r') as tar:
            tar.extractall(path=destination)
    else:
        if os.path.isdir(destination):
            base_name = os.path.basename(source)[:-4]  # убираем .zst или .bz2
            destination = os.path.join(destination, base_name)
        with open(destination, 'wb') as f:
            f.write(data)

    period = time.time() - start
    print(f"Готово, Время: {period:.3f} сек")


def make_tar(source):
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode='w') as tar:
        tar.add(source, arcname=os.path.basename(source))
    return buffer.getvalue()

import argparse
from .compress import compress, decompress


def main():
    parser = argparse.ArgumentParser(
        description='Утилита архиватор/распаковщик',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  # Архивация файла с bz2:
  python archiver.py compress file.txt archive.bz2

  # Архивация файла с zstd:
  python archiver.py compress file.txt archive.zst

  # Архивация директории с bz2:
  python archiver.py compress my_folder/ backup.bz2

  # Архивация директории с zstd:
  python archiver.py compress my_folder/ backup.zst

  # Распаковка bz2:
  python archiver.py decompress archive.bz2 output/

  # Распаковка zstd:
  python archiver.py decompress archive.zst output/
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Команда')

    # Подкоманда compress
    compress_parser = subparsers.add_parser(
        'compress',
        help='Архивировать файл или директорию'
    )
    compress_parser.add_argument(
        'source',
        help='Путь к файлу или директории для архивации'
    )
    compress_parser.add_argument(
        'destination',
        help='Путь к создаваемому архиву'
    )

    # Подкоманда decompress
    decompress_parser = subparsers.add_parser(
        'decompress',
        help='Распаковать архив'
    )
    decompress_parser.add_argument(
        'source',
        help='Путь к архиву'
    )
    decompress_parser.add_argument(
        'destination',
        help='Путь куда распаковать'
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    try:
        if args.command == 'compress':
            compress(args.source, args.destination)
        elif args.command == 'decompress':
            decompress(args.source, args.destination)
    except Exception as e:
        print(f"Ошибка: {e}")
        exit(1)

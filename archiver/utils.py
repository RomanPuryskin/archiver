def get_algorithm_from_extension(filepath: str):

    if filepath.endswith('.zst'):
        return 'zstd'
    elif filepath.endswith('.bz2'):
        return 'bz2'
    else:
        return None

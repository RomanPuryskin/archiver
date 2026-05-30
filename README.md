# Утилита для архивации/распаковки


## Требования

- Python 3.14+

## Использование

### Общий синтаксис

```
python -m archiver <команда> <источник> <назначение>
```

## Примеры запуска

### Архивация файла

```bash
python -m archiver compress test_bz2.txt archive1.bz2

python -m archiver compress test_zst.txt archive2.zst
```

### Архивация директории

```bash
python -m archiver compress my_dir/ dir_archive1.bz2

python -m archiver compress my_dir/ dir_archive2.zst
```

### Распаковка

```bash
python -m archiver decompress archive2.zst test_zst_result.txt

python -m archiver decompress archive1.bz2 test_bz2_result.txt
```
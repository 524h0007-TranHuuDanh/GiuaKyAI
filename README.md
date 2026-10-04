# Sokoban AI

## Moi truong
- Python 3.11+
- pygame 2.5.2

## Cai dat
```bash
pip install -r requirements.txt
```

## Chay chuong trinh
```bash
python main.py
```

## Kieu du lieu thong nhat
- Vi tri: tuple `(x, y)`
- `boxes`, `goals`, `walls`: set cac tuple
- Khong dung `frozenset`
- Khong dung `row_lengths`

## GUI
GUI chi dung cac hinh ve co ban cua Pygame, khong load anh.

Single mode:
- Chon map
- Chay UCS hoac A*
- Prev / Next de xem tung buoc
- Reset ve buoc dau

Competitive mode:
- Chon va xem cac map 2 agent

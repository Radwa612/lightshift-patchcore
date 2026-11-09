from src.config import DATA_ROOT, CATEGORIES

for c in CATEGORIES:
    tr = len(list((DATA_ROOT / c / 'train' / 'good').glob('*.png')))
    te = len(list((DATA_ROOT / c / 'test').glob('*/*.png')))
    gt = len(list((DATA_ROOT / c / 'ground_truth').glob('*/*.png')))
    print(f'{c:10s} train/good={tr:4d}  test={te:4d}  masks={gt:4d}')
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_ROOT = ROOT / 'data' / 'mvtec_ad'
RESULTS = ROOT / 'results'
MODELS = ROOT / 'models'

CATEGORIES = ['carpet', 'leather', 'tile', 'bottle', 'screw']
IMG_SIZE = 224
BACKBONE = 'wide_resnet50_2'   # Change to 'resnet18' if running slowly on CPU
LAYERS = ('layer2', 'layer3')
SEED = 0
ALPHA = 0.05
"""用原始 Hello Kitty 图生成所有 PWA 图标"""
from PIL import Image
import os

OUT = '/workspace/memo-app/icons'
SRC = os.path.join(OUT, 'hellokitty-memo.jpg')

src = Image.open(SRC).convert('RGBA')
print(f"原图尺寸: {src.size}")

def make_icon(size, name=None):
    if name is None:
        name = f'icon-{size}.png'
    w, h = src.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    cropped = src.crop((left, top, left + side, top + side))
    img = cropped.resize((size, size), Image.LANCZOS)
    img.save(os.path.join(OUT, name))

# PWA 图标
for sz in [16, 32, 48, 72, 96, 120, 144, 152, 167, 180, 192, 256, 512]:
    make_icon(sz)

# Apple Touch Icons
for sz in [57, 60, 72, 76, 114, 120, 144, 152, 167, 180]:
    make_icon(sz, f'apple-touch-icon-{sz}.png')

# 主图标
make_icon(180, 'apple-touch-icon.png')
make_icon(16, 'favicon-16.png')
make_icon(32, 'favicon-32.png')
make_icon(1024, 'icon-master.png')

print(f"✅ 生成完成，{len(os.listdir(OUT))} 个文件")
for f in sorted(os.listdir(OUT)):
    print(f"  {f}")
from PilLite import Image
import nbtlib
from schema import schem_schematic, schem_te, schem_schematic_file


def rgb32to16(rgb):
    r = int(((rgb & 0x00FF0000) >> 16) / 255 * 15)
    g = int(((rgb & 0x0000FF00) >> 8) / 255 * 15)
    b = int(((rgb & 0x000000FF) >> 0) / 255 * 15)
    return (r << 8) + (g << 4) + b


def rgb32to16ex(rgb):
    r = int(((rgb & 0xFF000000) >> 24) / 255 * 15)
    g = int(((rgb & 0x00FF0000) >> 16) / 255 * 15)
    b = int(((rgb & 0x0000FF00) >> 8) / 255 * 15)
    return (r << 8) + (g << 4) + b


def generate_nbt(img: Image, transparent=False):
    (width, length) = img.size
    blocks = bytearray()
    data = bytearray()
    addblocks_raw = bytearray()
    te = list()
    for l in range(length):
        for w in range(width):
            pixel = img.get_pixel((w, l))
            color_code = rgb32to16ex(pixel) if transparent else rgb32to16(pixel)
            if not transparent or pixel & 0xff == 255:
                blocks.append(0x7F)
                data.append(0x0B)
                addblocks_raw.append(3)
                te.append(schem_te({
                    'id': 'terraqueous:type.colored',
                    'rgb16': color_code,
                    'x': w,
                    'y': 0,
                    'z': l
                }))
            else:
                blocks.append(0)
                data.append(0)
                addblocks_raw.append(0)
    addblocks = bytearray()
    for i in range(0, len(addblocks_raw), 2):
        addblocks.append(addblocks_raw[i] + (addblocks_raw[i + 1] << 4) if len(addblocks_raw) - i >= 2 else 3)
    te_list = nbtlib.List(te)
    nbt = schem_schematic({
        'Height': 1,
        'Length': length,
        'Width': width,
        'Materials': 'Alpha',
        'TileEntities': te_list,
        'AddBlocks': addblocks,
        'Blocks': blocks,
        'Data': data
    })
    return schem_schematic_file({'Schematic': nbt})

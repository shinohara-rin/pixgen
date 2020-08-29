import nbtlib
from nbtlib.tag import Int, Short, String, ByteArray, List, Compound

schem_schematic_file = nbtlib.schema("file", {
    "Schematic": Compound
})

schem_schematic = nbtlib.schema("schematic", {
    'Height': Short,
    'Length': Short,
    'Width': Short,
    'Materials': String,
    'TileEntities': List[Compound],
    'AddBlocks': ByteArray,
    'Blocks': ByteArray,
    'Data': ByteArray
}, strict=True)

schem_te = nbtlib.schema("tileEntities", {
    'id': String,
    'rgb16': Short,
    'x': Int,
    'y': Int,
    'z': Int,
}, strict=True)

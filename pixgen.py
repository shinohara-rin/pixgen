import argparse
import nbtlib
import utils
from PilLite import Image

parser = argparse.ArgumentParser(description="Generate schematic file from image")
parser.add_argument('-i', '--input', dest='image', help="image to convert from")
parser.add_argument('-o', '--output', dest='output', help="save schematic file to")
parser.add_argument('-t', '--transparent', action='store_true', dest='transparent', help='use this if input has alpha '
                                                                                         'transparency')
args = parser.parse_args()
image = Image.open(args.image)

nbt = utils.generate_nbt(image, args.transparent)
file = nbtlib.File(nbt, gzipped=True)
file.save(args.output+'.schematic')

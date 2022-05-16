import pathlib
from PIL import Image
import os
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


if __name__ == '__main__':

    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--path1', type=str, help=('Path to the real images'))
    parser.add_argument('--path2', type=str, help=('Path to generated images'))

    args = parser.parse_args()
    path1 = args.path1
    path2 = args.path2
    suffix = 'png'

    path1 = pathlib.Path(path1)
    files1 = list(path1.glob('*.%s' % suffix))

    path2 = pathlib.Path(path2)
    files2 = list(path2.glob('*.%s' % suffix))

    for i in range(len(files1)):
        img_png1 = Image.open(files1[i])
        img_png1 = img_png1.convert('RGB')
        img_png1.save(str(files1[i].parent) + "/" + files1[i].name[:-4] + '.jpg')
        os.remove(files1[i])

    for i in range(len(files2)):
        img_png2 = Image.open(files2[i])
        img_png2 = img_png2.convert('RGB')
        img_png2.save(str(files2[i].parent) + "/" + files2[i].name[:-4] + '.jpg')
        os.remove(files2[i])
import glob
import os
import copy
import palom
import argparse
from natsort import natsorted
import re
import sys

# Make the object
psr = argparse.ArgumentParser(
    description='Piecewise alignment for layers of mosaics',
    epilog = 'You need to activate your conda environment for Palom before using ME'
)

psr.add_argument('-f', '--folderPath', required=True, help=r'Path to the directory where your image files are stored (example: /home/labishimoto/workspace/palom_data)')
psr.add_argument('-r', '--refName', required=True, help=r'File name for reference image  (example: H11-05390_DNA1_Pan-CK_aSMA.ome.tif)')
psr.add_argument('-o', '--outputName', default='merge_palom_result', help=r'File name for output image (default: merge_palom_result)')

args = psr.parse_args()


# Set folder path
folder_path = os.path.normpath(args.folderPath)

# Set reference image path
ref_path = os.path.normpath(os.path.join(folder_path,args.refName))

# Set output image path
oput_path = os.path.normpath(os.path.join(folder_path,args.outputName + ".ome.tif"))


# get file path list (except reference file) and channel name list
filepath_list = natsorted(glob.glob(os.path.join(folder_path,'*.ome.tif')))
chName_list = []

for fpath in filepath_list:
    fname = os.path.basename(fpath).split('.',1)[0]
    chName = re.sub('.*?DNA', 'DNA', fname, 1, flags=re.IGNORECASE).split('_')
    chName_list.append(copy.deepcopy(chName))


if ref_path in filepath_list:
    filepath_list.remove(ref_path)


# reference image
c1r = palom.reader.OmePyramidReader(ref_path)

LEVEL = 0
THUMBNAIL_LEVEL = c1r.get_thumbnail_level_of_size(2000)

# make NULL list
c2r_list = []
c21l_list = []
c2m_list = []

for i in range(len(filepath_list)):
    c2r = palom.reader.OmePyramidReader(filepath_list[i])
    c2r_list.append(copy.deepcopy(c2r))
    c21l = palom.align.Aligner(
        ref_img=c1r.read_level_channels(LEVEL, 0),
        moving_img=c2r_list[i].read_level_channels(LEVEL, 0),
        ref_thumbnail=c1r.read_level_channels(THUMBNAIL_LEVEL, 0).compute(),
        moving_thumbnail=c2r_list[i].read_level_channels(THUMBNAIL_LEVEL, 0).compute(),
        ref_thumbnail_down_factor=c1r.level_downsamples[THUMBNAIL_LEVEL] / c1r.level_downsamples[LEVEL],
        moving_thumbnail_down_factor=c2r_list[i].level_downsamples[THUMBNAIL_LEVEL] / c2r_list[i].level_downsamples[LEVEL]
        )
    c21l.coarse_register_affine(n_keypoints=4000)
    c21l.compute_shifts()
    c21l.constrain_shifts()
    c21l_list.append(copy.deepcopy(c21l))
    c2m = palom.align.block_affine_transformed_moving_img(
        ref_img=c1r.read_level_channels(LEVEL, 0),
        moving_img=c2r_list[i].pyramid[LEVEL],
        mxs=c21l_list[i].block_affine_matrices_da
        )
    c2m_list.append(copy.deepcopy(c2m))


# write the registered images to a pyramidal ome-tiff
palom.pyramid.write_pyramid(
    mosaics=palom.pyramid.normalize_mosaics([
        c1r.pyramid[LEVEL],
        *c2m_list
    ]),
    output_path=oput_path,
    pixel_size=c1r.pixel_size*c1r.level_downsamples[LEVEL],
    #downscale_factor=2,
    channel_names=chName_list
)


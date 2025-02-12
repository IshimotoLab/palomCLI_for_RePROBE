# palomCLI

description

## How to use

### Step1

Create your `palom` environment for `RePROBE`.

1. Create conda environment and install `palom` according to the [instruction](https://github.com/labsyspharm/palom).

1. Copy `palomCLI.py` to your `palom` environment.

    ```sh
    cp palomCLI.py /PathToYourConda/envs/palom/lib/python3.10/site-packages/palom/cli/palomCLI.py
    ```

    You have to change the path according to your installed python version.

1. Activate your `palom` environment and install `natsort`.

    ```sh
    conda activate palom
    pip install natsort
    ```

1. Now you can use palom with one-liner!

    Check the details with the help commands.

    ```sh
    (palom) username:~$ palom --help
    usage: palom [-h] -f FOLDERPATH -r REFNAME [-o OUTPUTNAME]

    Piecewise alignment for layers of mosaics

    options:
      -h, --help            show this help message and exit
      -f FOLDERPATH, --folderPath FOLDERPATH
                            Path to the directory where your image  files are
                            stored (example:
                            /home/labishimoto/workspace/palom_data)
      -r REFNAME, --refName REFNAME
                            File name for reference image (example:
                            H11-05390_DNA1_Pan-CK_aSMA.ome.tif)
      -o OUTPUTNAME, --outputName OUTPUTNAME
                            File name for output image (default:
                            merge_palom_result)

    You need to activate your conda environment for Palom before using ME
    ```

### Step2

1. Create your image directory containing `OME-TIFF` format files.

    Example directory;

    ```sh
    username:~$ ls /path/to/your/imageDir
    sample1_DNA1_Pan-CK_aSMA.ome.tif
    sample1_DNA2_CD45_EpCAM_PDPN.ome.tif
    sample1_DNA3_CD31_CD68.ome.tif
    sample1_DNA4_CD3_CD4_CD8.ome.tif
    sample1_DNA5_CD16.ome.tif
    ```

    > You must change file names according to naming conventions.  
    > **`sample name`**_**`channel names`**.ome.tif

    - `sample name`: Do not include underscores or spaces.
    - `channel names`: List of multiple channnel name.
        - The first channel is always DNA channel. (e.g. DAPI, Hoechst)  
            If the DNA channel is not in the first channel, you must arrange the channel order.
        - The name of the DNA channel must be `DNA` + cycle number. (e.g. DNA1)
        - Do not use underscores or spaces in each channel name.
        - Each channel name is separated by an underscore.
    - `sample name` and `channel name` are separated by an underscore.

2. Usage

    ```sh
    conda activate palom
    palom -f /path/to/your/imageDir -r sample1_DNA1_Pan-CK_aSMA.ome.tif
    ```

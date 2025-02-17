# palomCLI for RePROBE

Image registration tool for **RePROBE** (**Re**petitive **P**rimary antibody **R**eplacement and **O**verlaying images from a **B**road range of fluorescence imaging **E**quipment). This tool is based on [labsyspharm/palom](https://github.com/labsyspharm/palom).

## How to use

### Step1

Create your `palom` environment for `RePROBE`.

1. Create conda environment and install `palom` according to the [instruction](https://github.com/labsyspharm/palom).

2. Copy `palomCLI4RePROBE.py` to your PC.

3. Activate your `palom` environment and install `natsort`.

    ```sh
    conda activate palom
    pip install natsort
    ```

4. Now you can use palom with one-liner!

    Check the details with the help commands.

    ```sh
    (palom) username:~$ palomCLI4RePROBE.py --help
    usage: palom [-h] -f FOLDERPATH -r REFNAME [-o OUTPUTNAME]

    Piecewise alignment for layers of mosaics

    options:
      -h, --help            show this help message and exit
      -f FOLDERPATH, --folderPath FOLDERPATH
                            Path to the directory where your image  files are
                            stored (example:
                            /home/ishimotolab/workspace/palom_data)
      -r REFNAME, --refName REFNAME
                            File name for reference image (example:
                            samplename_DNA1_Pan-CK_aSMA.ome.tif)
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
    palomCLI4RePROBE.py -f /path/to/your/imageDir -r sample1_DNA1_Pan-CK_aSMA.ome.tif
    ```

## Citation

Please cite the following paper when using `RePROBE` system in your research:

> Semba, T., Ishimoto, T. Spatial analysis by current multiplexed imaging technologies for the molecular characterisation of cancer tissues. Br J Cancer 131, 1737–1747 (2024). https://doi.org/10.1038/s41416-024-02882-6

# palomCLI

## How to use

1. Copy `palomCLI.py` to your conda environment of palom.

    ```sh
    cp palomCLI.py /PathToYourConda/envs/YourPalomEnvName/lib/python3.10/site-packages/palom/cli/palomCLI.py
    ```

    You have to change the path according to your installed python version.

1. Activate your `palom` environment.

    ```sh
    conda activate palom
    ```

1. Now you can use palom with one-liner!

    Check the details with the help commands.

    ```sh
    (palom) username ~ % palom --help
    usage: palom [-h] -f FOLDERPATH -r REFNAME [-o OUTPUTNAME]

    Piecewise alignment for layers of mosaics

    options:
      -h, --help            show this help message and exit
      -f FOLDERPATH, --folderPath FOLDERPATH
                            Path to the directory where your image  files are
                            stored (exsample:
                            /home/labishimoto/workspace/palom_data)
      -r REFNAME, --refName REFNAME
                            File name for reference image (exsample:
                            H11-05390_DNA1_Pan-CK_aSMA.ome.tif)
      -o OUTPUTNAME, --outputName OUTPUTNAME
                            File name for output image (default:
                            merge_palom_result)

    You need to activate your conda environment for Palom before using ME
    ```

1. Usage

    ```sh
    conda activate palom3
    palom -f /path/to/your/image/directory -r referenceImage.ome.tif
    ```

import gdown
import argparse
import os

cnvrg_workdir = os.environ.get("CNVRG_WORKDIR", "/cnvrg")

parser = argparse.ArgumentParser()

parser.add_argument(
    "--dir_url",
    type=str,
    action="store",
    dest="dir_url",
    default="https://drive.google.com/drive/folders/1AsTXq6uPPnqKiko2LoFVwYNHzhqa8mi9",
    help="Google drive directory link with Training.csv and Testing.csv",
)

FLAGS = parser.parse_args()
print("start to download file from {FLAGS.dir_url}")
gdown.download_folder(
    url=FLAGS.dir_url, output="output/", quiet=True, use_cookies=False
)
ls_dir = os.listdir("output/")
print("download completed, file has been saved to {ls_dir}")

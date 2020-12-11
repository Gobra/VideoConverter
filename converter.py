import sys
import os
import subprocess
from argparse import ArgumentParser

def main():
    # args parser
    parser = ArgumentParser()
    parser.add_argument('-args', '--args', default='-c:v h264', help='ffmpeg arguments for conversion')
    parser.add_argument('folder', help='folder to process files from')
    args = parser.parse_args(sys.argv[1:])

    # find files
    exts = [".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", \
        ".m2ts", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", \
        ".rm", ".swf", ".vob", ".wmv"]
    videoFiles = [os.path.join(args.folder, file) for file in os.listdir(args.folder) if file.endswith(tuple(exts))]

    # process results
    for video in videoFiles:
        base = os.path.splitext(os.path.basename(video))[0]
        output = os.path.join(args.folder, "Output", base + "_x264.mp4")
        command = "ffmpeg {} -i {} {}".format(args.args, video, output)
        done = subprocess.run(command, shell=True)
        if 0 == done.returncode:
            print("{} - OK".format(video))
        else:
            print("{} - FAILED".format(video))

if __name__ == '__main__':
    main()
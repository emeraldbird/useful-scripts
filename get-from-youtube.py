#!/usr/bin/python3

import argparse
from pytube.streams import Stream
from pytube import Playlist, YouTube

parser = argparse.ArgumentParser()
parser.add_argument('--playlist', type=str)
parser.add_argument('--video', type=str)
parser.add_argument('--dir', '-d', type=str)
args = parser.parse_args()


if args.playlist:
    print(args.playlist)
    playlist = Playlist(args.playlist)
    for video in playlist.videos:
        video.streams.get_highest_resolution().download(output_path=args.dir)

if args.video:
    YouTube(args.video).streams.get_highest_resolution().download(output_path=args.dir)

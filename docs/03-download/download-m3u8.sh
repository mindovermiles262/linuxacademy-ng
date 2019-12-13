#!/bin/bash
#
# Downloads video file from m3u8 playlist url
#
# Example
# $ ./download-m3u8.sh http://linuxacademy.org/playlist.m3u8
#
# $ ./download-m3u8.sh https://video-cdn.linuxacademy.com/vods3/_definst_/smil:box/cdnstore/modules/google-cloud-certified-professional-cloud-architect-1547152447664/gcparch_intro_1557514438.smil/playlist.m3u8

ffmpeg -i "$1" -c copy  -bsf:a aac_adtstoasc output_file.mp4


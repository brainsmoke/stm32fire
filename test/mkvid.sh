#!/bin/bash

./fire_stdout | python3 virtsave.py mov 1600

ffmpeg -r 160 -i mov/frame%04d.png -c:v libx264 -r 60 -pix_fmt yuv420p animation.mp4


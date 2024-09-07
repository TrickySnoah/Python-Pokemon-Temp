
# THIS FILE DOES NOT DIRECTLY CORRELATE TO THE MAIN .PY FILES. THIS PROGRAM
# JUST SHOWS HOW TO SCALE THINGS TO THE USER'S SCREEN

originalResolutionWidth = 1920
originalResolutionHeight = 1020

originalImageWidth = 50
originalImageHeight = 60

newResolutionWidth = 960
newResolutionHeight = 510

newImageWidthRatio = originalImageWidth / originalResolutionWidth
newImageHeightRatio = originalImageHeight / originalResolutionHeight

newImageWidth = newImageWidthRatio * newResolutionWidth
newImageHeight = newImageHeightRatio * newResolutionHeight

print(f"original: w {originalImageWidth} h {originalImageHeight}")
print(f"new: w {newImageWidth} h {newImageHeight}")

import pyautogui

# get the resolution of the user's screen
resolution = pyautogui.size()
reso_width = resolution[0]; reso_height = resolution[1]
print(f"w {reso_width} \nh {reso_height}")
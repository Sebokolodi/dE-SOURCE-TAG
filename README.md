# pyDDI 

This tool is for identifying regions in an image that require direction-dependent calibration. It does this mainly based on an image rather than the sky model. It returns a Tigger sky model with locations of the directions of interest in terms of ra and dec (in degrees), note that this sky model should never be used for anything else other than reference location. The user can supply the actual sky model in which the tool will tag the sources that corresponds to the above directions.

This tool does the following:

1. It searches for high intensity pixels given the user provided limit.   
2. For computation purposes, pixels separated by less than some user-specified radius are grouped together, and for a given group a position and intensity of the brightest pixel are returned.  
3. Pixels from step 2 are then evaluated further. The local variance around these pixels is computed and those with variance above a user-specified threshold are considered.  
4. If the user provides a PSF image, a region taken from the PSF is correlated with region around each pixels from step 3. This step seems to eliminate spurious pixels quite well and thus, we highly recommend this step.
5. Lastly, a user can simply take the output sky model and use the positions for their own purposes. Alternatively, a user may provide a sky model to be cross-matched with this output sky model, and the sources that are near the directions are tagged as 'dE'. 


Implementation: ./dd-source-identification.py  -h 

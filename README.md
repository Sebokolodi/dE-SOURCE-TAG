# pyddi

### Description 

This tool is designed to identify regions in an image that require direction-dependent calibration. 
 
### Installation


### The Technique:

This tool carries out the following steps:

1. It searches for pixels in an image/sources in the sky model with high signal-to-noise ratio.   
2. For computation purposes, pixels separated by a few beams are grouped. The position and intensity of the brightest pixel is returned for each group.  
3. Computes the local variance around pixels from 2 or sources from 1, and selects those with high local variance.   
4. If the user provides a PSF image, the PSF is correlated with each source/region. those with high correlation factor are selected.
5. Lastly, the tool writes out a Tigger model containing the source/pixel positions that made it through step 3 or 4. 

    5.1 However, a user can supply an actual sky model and the tool will cross match with above model, and tag sources in this former model as 'dE'.
  
    5.2 Or, alternatively, a user can specify whether they want their actual sky model to be used for the identification rather than pixels from an image, in which case, the sources in the sky model will be updated with tags 'dE'. 
    
    5.3 If a sky model is not supplied, source a model with positions will be returned. This model should not be used for anything except the positions.

### Implementation  

Implementation: pyddi  -h 

Test 1:

    pyddi -i examples/test/kat7restored.fits -c examples/test/kat7restored.gaul -p examples/test/kat7psf.fits -usec -o test-output-1 
 
 Test 2: Without a catalog
 
    pyddi -i examples/test/kat7restored.fits -p examples/test/kat7psf.fits -o test-output-2
  
  Test 3: Without the PSF
  
    pyddi -i examples/test/kat7restored.fits -o test-output-3
    
  Test 4: Changing some useful thresholds
  
    pyddi -i examples/test/kat7restored.fits -p examples/test/kat7psf.fits -vth 10 -cth 0.7 -gpix 50  -o test-output-4 
    
  
 
 
 
 


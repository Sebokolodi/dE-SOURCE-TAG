# dE-SOURCE-TAG

This tool is for identifying regions in an image that require direction-dependent calibration. It does this mainly based on an image rather than the sky model. It returns a Tigger sky model with locations of the directions of interest in terms of ra and dec (in degrees), note that this sky model should never be used for anything else other than reference location. The user can supply the actual sky model in which the tool will tag the sources that corresponds to the above directions.

This tool does the following:

1. It searches for high intensity pixels given the user provided limit.   
2. For computation purposes, pixels separated by less than some user-specified radius are grouped together, and for a given group a position and intensity of the brightest pixels are returned.  
3. Pixels from step 2, are then evaluated further. The local variance around these pixels is computed and those with variance above a user-specified threshold are considered.  
4. If the user provides a PSF image, a region taken from the PSF is correlated with region around each pixels from step 3. This step seems to eliminate spurious pixels quite well and thus, we highly recommend this step.
5. Lastly, a user can simple take the output sky model and use the positions for their own purposes. Alternatively, a user may provide a sky model to be cross-matched with this output sky model, and the sources that are near the directions are tagged as 'dE'. 


Implementation: ./dd-source-identification.py  -h 


  -h, --help            show this help message and exit   
  -i IMAGE, --img IMAGE     
                        Image of interest. Required.    
                        
  -p PSF_IMAGE, --psf PSF_IMAGE       
                        The psf image. Default=None.      
  -c CATALOG, --cat CATALOG     
                        Sky model as LSM/txt. Default=None. Must be in Tigger   
                        format: "#format:name, ra_d, dec_d, i"      
  -fth FLUX_THRESHOLD, --flux-thresh FLUX_THRESHOLD     
                        Flux threshold. Regions in an image with flux > fth *     
                        noise are considered. Default=5     
  -vth VARIANCE_THRESHOLD, --variance-thresh VARIANCE_THRESHOLD     
                        Local variance threshold. Sources with varinace > vth   
                        * noise are considered. Defautl=5.      
  -vsize VARIANCE_SIZE, --var-size VARIANCE_SIZE      
                        The size of the region to compute the local variance.   
                        E.g vsize=10, gives a region of size = 10 *   
                        resolution. The resolution is in pixels. Default=10   
  -cth CORRELATION_THRESHOLD, --correlation-thresh CORRELATION_THRESHOLD      
                        Correlation threshold. Sources with correlation factor    
                        > cth are considered. Default=0.5   
  -csize CORRELATION_SIZE, --corr-size CORRELATION_SIZE   
                        The size of the region to compute correlation. see    
                        vsize. Default=5    
  -gpix GROUP_PIXELS, --group-pix GROUP_PIXELS    
                        The size of the region to group the pixels, in terms    
                        of psf-size. The psf is in degrees. e.g gpix=20, gives    
                        20xpsf. Default=20    
  -o OUTPUT_PREFIX, --outpref OUTPUT_PREFIX   
                        The prefix for the output file containing directions    
                        in RA, DEC both in degrees, and peak flux of the    
                        pixels. Default=None    

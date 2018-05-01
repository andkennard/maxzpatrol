import pims
from tifffile import TiffWriter


images = pims.Bioformats('testImages/testStack_xyzct.tif')
images.bundle_axes='zcyx'
images.iter_axes = 't'
with TiffWriter('out/testOut_xyzt_imagej.tif',imagej=True) as writer:
    for image in images:
        writer.save(image)
print(images.sizes)

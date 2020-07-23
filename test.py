import os
import segyio
import numpy as np

filename = 'small.sgy'
with segyio.open(filename) as segyfile:

    # Memory map file for faster reading (especially if file is big...)
    segyfile.mmap()

    # Print binary header info
    print(segyfile.bin)
    print(segyfile.bin[segyio.BinField.Traces])

    # Read headerword inline for trace 10
    print(segyfile.header[10][segyio.TraceField.INLINE_3D])

    # Print inline and crossline axis
    print(segyfile.xlines)
    print(segyfile.ilines)

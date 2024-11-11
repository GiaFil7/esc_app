# Import
import os
from PySide6.QtCore import QDir, QRect
from PySide6.QtGui import QImage, QImageReader
from PySide6 import QtSvg
from PySide6.QtSvgWidgets import QSvgWidget


# Paths
source_path = "E:\\Desktop\\source"
destination_path = "E:\\Desktop\\destination"

# Clip
crop_left   = 230
crop_top    = 97
crop_width  = 133
crop_height = 133

# Files List
qdir = QDir( source_path )
qdir.setSorting( QDir.LocaleAware )
qdir.setFilter( QDir.Files | QDir.NoSymLinks | QDir.NoDotAndDotDot )
qdir.setNameFilters( [ "*.svg","*.png"] )
files = qdir.entryInfoList()

# Loop Items
for i in range( 0, len( files ) ):
    # Paths
    image_path = os.path.normpath( files[i].filePath() )
    save_path = os.path.join( destination_path, os.path.basename( image_path ) )

    # Image
    qreader = QImageReader( image_path )
    if qreader.canRead() == True:
        qreader.setClipRect( QRect( crop_left, crop_top, crop_width, crop_height ) )
        qimage = qreader.read()
        qimage.save( save_path )
        del qimage
    del qreader

print( "Task End" )
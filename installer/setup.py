# -*- coding: utf-8 -*-
## @package setup
# Setup file used to build the Installers

from distutils.core import setup
from gmapcatcher.mapConst import *
import os
import pyproj
import sys
from glob import glob

pyProjData = pyproj.pyproj_datadir
sys.path.append( pyProjData)  # not sure if this is necessary, but it is needed for msvcr90.dll

if os.name == "posix":
    ico = "images/map.png"
    setup(
        name = NAME,
        description = 'Offline Map Viewer',
        version = VERSION,
        url = WEB_ADDRESS,
        data_files = [('share/doc/mapcatcher', ['README', 'changelog']),
                    ('share/applications', ['gmapcatcher.desktop']),
                    ('share/man/man1',
                        ['man/mapcatcher.1.gz', 'man/mapdownloader.1.gz']),
                    ('share/pixmaps', ['images/mapcatcher.png']),
                    ('share/pixmaps/gmapcatcher',
                    map(lambda(thestr): "images/" + thestr, os.listdir('images')))
        ],
        scripts = ['mapcatcher', 'mapdownloader'],
        packages = ['gmapcatcher', 'gmapcatcher.mapServers',
                    'gmapcatcher.tilesRepo', 'gmapcatcher.widgets',
                    'gmapcatcher.gpxpy', 'gmapcatcher.gps']
    )
else:
    import matplotlib
    import py2exe
    matplotlib.use('TkAgg')
    import matplotlib.backends.backend_tkagg
    DLL_EXCLUDES = [ 
                 'KERNELBASE.dll',
                 'MSIMG32.dll',
                 'NSI.dll',
                 'USP10.dll',
                 'DNSAPI.dll',
                 'API-MS-Win-Core-SysInfo-L1-1-0.dll',
                 'API-MS-Win-Core-Misc-L1-1-0.dll',
                 'API-MS-Win-Core-IO-L1-1-0.dll',
                 'API-MS-Win-Core-File-L1-1-0.dll',
                 'API-MS-Win-Core-Debug-L1-1-0.dll',
                 'API-MS-Win-Core-Handle-L1-1-0.dll',
                 'API-MS-Win-Core-Localization-L1-1-0.dll',
                 'API-MS-Win-Core-Profile-L1-1-0.dll',
                 'API-MS-Win-Core-Heap-L1-1-0.dll',
                 'API-MS-Win-Core-Synch-L1-1-0.dll',
                 'API-MS-Win-Core-String-L1-1-0.dll',
                 'API-MS-Win-Core-DelayLoad-L1-1-0.dll',
                 'API-MS-Win-Core-LibraryLoader-L1-1-0.dll',
                 'API-MS-Win-Core-ErrorHandling-L1-1-0.dll',
                 'API-MS-Win-Core-ProcessThreads-L1-1-0.dll',
                 'API-MS-Win-Core-ProcessEnvironment-L1-1-0.dll',
                 'API-MS-Win-Core-LocalRegistry-L1-1-0.dll',
                 'MSVCP90.dll',
                 'api-ms-win-core-registry-l1-1-0.dll',
                 'api-ms-win-core-string-obsolete-l1-1-0.dll',
                 'api-ms-win-security-base-l1-1-0.dll',
                 'api-ms-win-core-localization-obsolete-l1-2-0.dll',
                 'api-ms-win-core-libraryloader-l1-2-1.dll',
                 'api-ms-win-crt-private-l1-1-0.dll',
                 'api-ms-win-core-processthreads-l1-1-1.dll',
                 'api-ms-win-core-heap-l2-1-0.dll',
                 'api-ms-win-core-delayload-l1-1-1.dll',
                 'api-ms-win-crt-string-l1-1-0.dll',
                 'api-ms-win-core-synch-l1-2-1.dll',
                 'api-ms-win-core-libraryloader-l1-2-0.dll',
                 'api-ms-win-core-realtime-l1-1-0.dll',
                 'api-ms-win-crt-runtime-l1-1-0.dll',
                 'api-ms-win-core-interlocked-l1-1-0.dll',
                 'api-ms-win-security-activedirectoryclient-l1-1-0.dll',
                 'w9xpopen.exe'] # is not excluded for some reasion
    setup(
        name = NAME,
        description = 'Offline Map Viewer',
        version = VERSION,
        url = WEB_ADDRESS,
        console = ['download.py'],
        windows = [{
            'script': 'maps.py',
            'icon_resources': [(1, "images\maps.ico")],
        }],
        options = {
            'py2exe': {
                'packages':'encodings',
                'includes': 'matplotlib.backends.backend_tkagg, cairo, pango, pangocairo, atk, gobject, gio', 
                'dll_excludes': DLL_EXCLUDES,
                #'py2exe': { "includes" : ["matplotlib.backends.backend_tkagg"] }
            }
        },
        # opts = {
        #     'py2exe': { "includes" : ["matplotlib.backends.backend_tkagg"] }
        #     },
        data_files = matplotlib.get_py2exe_datafiles() + [ "README.md", "changelog.md",
                    ( "pyproj", glob( os.path.join( pyProjData, "*" ))) ]
    )

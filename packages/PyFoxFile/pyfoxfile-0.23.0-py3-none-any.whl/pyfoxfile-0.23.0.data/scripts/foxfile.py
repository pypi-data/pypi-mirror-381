#!python
# -*- coding: utf-8 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2018-2024 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2018-2024 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2018-2024 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: foxfile.py - Last Update: 10/1/2025 Ver. 0.23.0 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals, generators, with_statement, nested_scopes
import os
import sys
import argparse
import pyfoxfile
import binascii

# Conditional import and signal handling for Unix-like systems
if os.name != 'nt':  # Not Windows
    import signal
    if hasattr(signal, 'SIGPIPE'):
        def handler(signum, frame):
            pyfoxfile.VerbosePrintOut(
                "Received SIGPIPE, exiting gracefully.", "info")
            sys.exit(0)
            signal.signal(signal.SIGPIPE, handler)

rarfile_support = pyfoxfile.rarfile_support
py7zr_support = pyfoxfile.py7zr_support

if(sys.version[0] == "2"):
    try:
        from io import StringIO, BytesIO
    except ImportError:
        try:
            from cStringIO import StringIO
            from cStringIO import StringIO as BytesIO
        except ImportError:
            from StringIO import StringIO
            from StringIO import StringIO as BytesIO
elif(sys.version[0] >= "3"):
    from io import StringIO, BytesIO
else:
    teststringio = 0
    if(teststringio <= 0):
        try:
            from cStringIO import StringIO as BytesIO
            teststringio = 1
        except ImportError:
            teststringio = 0
    if(teststringio <= 0):
        try:
            from StringIO import StringIO as BytesIO
            teststringio = 2
        except ImportError:
            teststringio = 0
    if(teststringio <= 0):
        try:
            from io import BytesIO
            teststringio = 3
        except ImportError:
            teststringio = 0

__project__ = pyfoxfile.__project__
__program_name__ = pyfoxfile.__program_name__
__file_format_name__ = pyfoxfile.__file_format_name__
__file_format_magic__ = pyfoxfile.__file_format_magic__
__file_format_len__ = pyfoxfile.__file_format_len__
__file_format_hex__ = pyfoxfile.__file_format_hex__
__file_format_delimiter__ = pyfoxfile.__file_format_delimiter__
__file_format_dict__ = pyfoxfile.__file_format_dict__
__file_format_default__ = pyfoxfile.__file_format_default__
__file_format_multi_dict__ = pyfoxfile.__file_format_multi_dict__
__use_new_style__ = pyfoxfile.__use_new_style__
__use_advanced_list__ = pyfoxfile.__use_advanced_list__
__use_alt_inode__ = pyfoxfile.__use_alt_inode__
__project_url__ = pyfoxfile.__project_url__
__version_info__ = pyfoxfile.__version_info__
__version_date_info__ = pyfoxfile.__version_date_info__
__version_date__ = pyfoxfile.__version_date__
__version_date_plusrc__ = pyfoxfile.__version_date_plusrc__
__version__ = pyfoxfile.__version__

# Initialize the argument parser
argparser = argparse.ArgumentParser(
    description="Manipulate archive files.", conflict_handler="resolve", add_help=True)

# Version information
argparser.add_argument("-V", "--version", action="version",
                       version=__program_name__ + " " + __version__)
# Input and output specifications
argparser.add_argument(
    "-i", "--input", nargs="+", help="Specify the file(s) to concatenate or the archive file to extract.", required=True)
argparser.add_argument("-o", "--output", default=None,
                       help="Specify the name for the extracted or output archive files.")
# Operations
argparser.add_argument("-c", "--create", action="store_true",
                       help="Perform only the concatenation operation.")
argparser.add_argument("-e", "--extract", action="store_true",
                       help="Perform only the extraction operation.")
argparser.add_argument("-t", "--convert", action="store_true",
                       help="Convert a tar/zip/rar/7zip file to a archive file.")
argparser.add_argument("-r", "--repack", action="store_true",
                       help="Re-concatenate files, fixing checksum errors if any.")
# File manipulation options
argparser.add_argument(
    "-F", "--format", default="auto", help="Specify the format to use.")
argparser.add_argument(
    "-D", "--delimiter", default=__file_format_dict__['format_delimiter'], help="Specify the delimiter to use.")
argparser.add_argument(
    "-m", "--formatver", default=__file_format_dict__['format_ver'], help="Specify the format version.")
argparser.add_argument("-l", "--list", action="store_true",
                       help="List files included in the archive file.")
# Compression options
argparser.add_argument("-P", "--compression", default="auto",
                       help="Specify the compression method to use for concatenation.")
argparser.add_argument("-L", "--level", default=None,
                       help="Specify the compression level for concatenation.")
argparser.add_argument("-W", "--wholefile", action="store_true",
                       help="Whole file compression method to use for concatenation.")
# Checksum and validation
argparser.add_argument("-v", "--validate", action="store_true",
                       help="Validate archive file checksums.")
argparser.add_argument("-C", "--checksum", default="crc32",
                       help="Specify the type of checksum to use. The default is crc32.")
argparser.add_argument("-s", "--skipchecksum", action="store_true",
                       help="Skip the checksum check of files.")
# Permissions and metadata
argparser.add_argument("-p", "--preserve", action="store_false",
                       help="Do not preserve permissions and timestamps of files.")
# Miscellaneous
argparser.add_argument("-d", "--verbose", action="store_true",
                       help="Enable verbose mode to display various debugging information.")
argparser.add_argument("-T", "--text", action="store_true",
                       help="Read file locations from a text file.")
# Parse the arguments
getargs = argparser.parse_args()

fname = getargs.format
if(getargs.format=="auto"):
    fnamedict = __file_format_multi_dict__
    __file_format_default__ = getargs.format
else:
    fnamemagic = fname
    fnamelen = len(fname)
    fnamehex = binascii.hexlify(fname.encode("UTF-8")).decode("UTF-8")
    __file_format_default__ = fnamemagic
    fnamesty = __use_new_style__
    fnamelst = __use_advanced_list__
    fnameino = __use_alt_inode__
    fnamedict = {'format_name': fname, 'format_magic': fnamemagic, 'format_len': fnamelen, 'format_hex': fnamehex,
                 'format_delimiter': getargs.delimiter, 'format_ver': getargs.formatver, 'new_style': fnamesty, 'use_advanced_list': fnamelst, 'use_alt_inode': fnameino}

# Determine the primary action based on user input
actions = ['create', 'extract', 'list', 'repack', 'validate']
active_action = next(
    (action for action in actions if getattr(getargs, action)), None)
input_file = getargs.input[0]

# Execute the appropriate functions based on determined actions and arguments
if active_action:
    if active_action == 'create':
        if getargs.convert:
            checkcompressfile = pyfoxfile.CheckCompressionSubType(
                input_file, fnamedict, True)
            if((pyfoxfile.IsNestedDict(fnamedict) and checkcompressfile in fnamedict) or (pyfoxfile.IsSingleDict(fnamedict) and checkcompressfile==fnamedict['format_magic'])):
                tmpout = pyfoxfile.RePackFoxFile(input_file, getargs.output, getargs.compression, getargs.wholefile, getargs.level, pyfoxfile.compressionlistalt, False, 0, 0, 0, [getargs.checksum, getargs.checksum, getargs.checksum, getargs.checksum], getargs.skipchecksum, [], {}, fnamedict, getargs.verbose, False)
            else:
                tmpout = pyfoxfile.PackFoxFileFromInFile(
                    input_file, getargs.output, __file_format_default__, getargs.compression, getargs.wholefile, getargs.level, pyfoxfile.compressionlistalt, [getargs.checksum, getargs.checksum, getargs.checksum, getargs.checksum], [], {}, fnamedict, getargs.verbose, False)
            if(not tmpout):
                sys.exit(1)
        else:
            pyfoxfile.PackFoxFile(getargs.input, getargs.output, getargs.text, __file_format_default__, getargs.compression, getargs.wholefile, getargs.level, pyfoxfile.compressionlistalt, False, [getargs.checksum, getargs.checksum, getargs.checksum, getargs.checksum], [], {}, fnamedict, getargs.verbose, False)
    elif active_action == 'repack':
        if getargs.convert:
            checkcompressfile = pyfoxfile.CheckCompressionSubType(
                input_file, fnamedict, True)
            if((pyfoxfile.IsNestedDict(fnamedict) and checkcompressfile in fnamedict) or (pyfoxfile.IsSingleDict(fnamedict) and checkcompressfile==fnamedict['format_magic'])):
                pyfoxfile.RePackFoxFile(input_file, getargs.output, getargs.compression, getargs.wholefile, getargs.level, pyfoxfile.compressionlistalt,
                                            False, 0, 0, 0, [getargs.checksum, getargs.checksum, getargs.checksum, getargs.checksum], getargs.skipchecksum, [], {}, fnamedict, getargs.verbose, False)
            else:
                pyfoxfile.PackFoxFileFromInFile(input_file, getargs.output, __file_format_default__, getargs.compression, getargs.wholefile, getargs.level, pyfoxfile.compressionlistalt, [getargs.checksum, getargs.checksum, getargs.checksum, getargs.checksum], [], {}, fnamedict, getargs.verbose, False)
            if(not tmpout):
                sys.exit(1)
        else:
            pyfoxfile.RePackFoxFile(input_file, getargs.output, getargs.compression, getargs.wholefile, getargs.level, pyfoxfile.compressionlistalt,
                                        False, 0, 0, 0, [getargs.checksum, getargs.checksum, getargs.checksum, getargs.checksum], getargs.skipchecksum, [], {}, fnamedict, getargs.verbose, False)
    elif active_action == 'extract':
        if getargs.convert:
            checkcompressfile = pyfoxfile.CheckCompressionSubType(
                input_file, fnamedict, True)
            tempout = BytesIO()
            if((pyfoxfile.IsNestedDict(fnamedict) and checkcompressfile in fnamedict) or (pyfoxfile.IsSingleDict(fnamedict) and checkcompressfile==fnamedict['format_magic'])):
                tmpout = pyfoxfile.RePackFoxFile(input_file, tempout, getargs.compression, getargs.wholefile, getargs.level, pyfoxfile.compressionlistalt, False, 0, 0, 0, [getargs.checksum, getargs.checksum, getargs.checksum, getargs.checksum], getargs.skipchecksum, [], {}, fnamedict, False, False)
            else:
                tmpout = pyfoxfile.PackFoxFileFromInFile(
                    input_file, tempout, __file_format_default__, getargs.compression, getargs.wholefile, getargs.level, pyfoxfile.compressionlistalt, [getargs.checksum, getargs.checksum, getargs.checksum, getargs.checksum], [], {}, fnamedict, False, False)
            if(not tmpout):
                sys.exit(1)
            input_file = tempout
        pyfoxfile.UnPackFoxFile(input_file, getargs.output, False, 0, 0, 0, getargs.skipchecksum,
                                    fnamedict, getargs.verbose, getargs.preserve, getargs.preserve, False, False)
    elif active_action == 'list':
        if getargs.convert:
            checkcompressfile = pyfoxfile.CheckCompressionSubType(
                input_file, fnamedict, True)
            if((pyfoxfile.IsNestedDict(fnamedict) and checkcompressfile in fnamedict) or (pyfoxfile.IsSingleDict(fnamedict) and checkcompressfile==fnamedict['format_magic'])):
                tmpout = pyfoxfile.FoxFileListFiles(input_file, "auto", 0, 0, 0, getargs.skipchecksum, fnamedict, False, getargs.verbose, False, False)
            else:
                tmpout = pyfoxfile.InFileListFiles(input_file, getargs.verbose, fnamedict, False, False, False)
            if(not tmpout):
                sys.exit(1)
        else:
            pyfoxfile.FoxFileListFiles(input_file, "auto", 0, 0, getargs.skipchecksum, fnamedict, False, getargs.verbose, False, False)
    elif active_action == 'validate':
        if getargs.convert:
            checkcompressfile = pyfoxfile.CheckCompressionSubType(
                input_file, fnamedict, True)
            tempout = BytesIO()
            if((pyfoxfile.IsNestedDict(fnamedict) and checkcompressfile in fnamedict) or (pyfoxfile.IsSingleDict(fnamedict) and checkcompressfile==fnamedict['format_magic'])):
                tmpout = pyfoxfile.RePackFoxFile(input_file, tempout, getargs.compression, getargs.wholefile, getargs.level, pyfoxfile.compressionlistalt, False, 0, 0, 0, [getargs.checksum, getargs.checksum, getargs.checksum, getargs.checksum], getargs.skipchecksum, [], {}, fnamedict, False, False, False)
            else:
                tmpout = pyfoxfile.PackFoxFileFromInFile(
                    input_file, tempout, __file_format_default__, getargs.compression, getargs.wholefile, getargs.level, pyfoxfile.compressionlistalt, [getargs.checksum, getargs.checksum, getargs.checksum, getargs.checksum], [], {}, fnamedict, False, False)
            input_file = tempout
            if(not tmpout):
                sys.exit(1)
        fvalid = pyfoxfile.FoxFileValidate(
            input_file, "auto", 0, fnamedict, False, getargs.verbose, False)
        if(not getargs.verbose):
            import sys
            import logging
            logging.basicConfig(format="%(message)s",
                                stream=sys.stdout, level=logging.DEBUG)
        if(fvalid):
            pyfoxfile.VerbosePrintOut("File is valid: \n" + str(input_file))
        else:
            pyfoxfile.VerbosePrintOut("File is invalid: \n" + str(input_file))

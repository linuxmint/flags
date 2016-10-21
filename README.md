
SOURCE FLAGS
------------

These flags originate from https://github.com/linuxmint/iso-country-flags-svg-collection.

They are built over there (make -j4 svgs) and that clips them (rounds them).

They are then optimized with scour as follows and placed in src/:

scour -i file.svg -o newfile.svg --enable-viewboxing --enable-id-stripping --enable-comment-stripping --shorten-ids --indent=none; done;

BUILD PROCESS
-------------

make-flags.py requires:

 - scour
 - svg-utils (https://github.com/btel/svg_utils)

This script applies a shadow (located in src/*/back.svg) and an effect (located in src/*/fore.svg) to the flags in src/ and builds a resulting set in flags/

REQUIREMENTS
------------

The finalized set is part of the source package so requirements are only necessary if you want to modify the flags.

In Linux Mint you can install them as follows:

apt install python-scour python-wheel python-wheel-common python3-wheel python-pip libxml2-dev libxslt-dev

pip install svgutils --user

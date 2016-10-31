#!/usr/bin/env python2
#coding=utf-8

from svgutils.compose import *

FLAG_SETS = ["iso-4x3"]

for flag_set in FLAG_SETS:

    os.system("mkdir -p flags/%s-svg" % flag_set)
    os.system("rm -f flags/%s-svg/*" % flag_set)

    for file in sorted(os.listdir("src/%s/svg" % flag_set)):

        # apply back and force on the flag
        back = "src/%s/back.svg" % flag_set
        fore = "src/%s/fore.svg" % flag_set
        flag = "src/%s/svg/%s" % (flag_set, file)
        if file.endswith(".svg"):
            figure = Figure( "1280", "960", SVG(back), SVG(flag), SVG(fore))

        destination = "flags/%s-svg/%s" % (flag_set, file)
        figure.save(destination)

        tmp = "flags/%s-svg/tmp.svg" % (flag_set)

        # compress
        os.system("scour -i %s -o %s --enable-viewboxing --enable-id-stripping --enable-comment-stripping --shorten-ids --indent=none" % (destination, tmp))
        os.rename(tmp, destination)

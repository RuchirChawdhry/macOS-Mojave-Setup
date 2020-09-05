#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess as sp


class Fonts:
    FONTS = [
        "source-code-pro",
        "source-sans-pro",
        "source-serif-pro",
        "roboto",
        "roboto-mono",
        "roboto-slab",
        "open-sans",
        "open-sans-condensed",
        "lato",
        "ibm-plex",
        "ibm-plex-mono",
        "ibm-plex-sans",
        "georgia",
        "ibm-plex-sans-condensed",
        "fira-mono",
        "fira-sans",
        "fira-code",
        "times-new-roman",
        "great-vibes",
        "grand-hotel",
        "montserrat",
        "hack",
        "simple-line-icons",
        "old-standard-tt",
        "ibm-plex-serif",
        "inconsolata",
        "impact",
        "bebas-neue",
        "arial",
        "arial-black",
        "alex-brush",
        "alegreya",
        "alegreya-sans",
        "aguafina-script",
        "libre-baskerville",
        "lobster",
        "material-icons",
        "raleway",
        "rajdhani",
        "raleway-dots",
        "merriweather",
        "merriweather-sans",
        "redhat",
        "pacifico",
    ]

    def get_noto_casks(self):
        cmd = ["brew", "search", "font-noto", "--casks"]
        noto = sp.run(cmd, capture_output=True).stdout.decode().splitlines()[1:]
        return noto

    def install(self):
        self.FONTS += self.get_noto_casks()
        for font in self.FONTS:
            sp.run(["brew", "cask", "install", font])

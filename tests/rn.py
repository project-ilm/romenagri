# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Tiny driver around the compiled Romenagri filters.  Always bytes in, bytes out; locale-independent.

    old, mid, new = rn.old, rn.mid, rn.new   # Tools for the unpatched build, for the build with the Sanskrit characters only (patch 0001),
                                             # and for the patched build (patches 0001, 0002 and 0003: the Sanskrit characters, the guards and the nukta layer)
    new.u2a("ॐ")                     # Unicode text -> ACII bytes        (uni2acii)
    new.a2u(b"\\xa0")                 # ACII bytes -> Unicode text        (acii2uni)
    new.u2a(text, form="nfd")        # the same with the form of the nukta layer (-f asis|nfc|nfd; only the new build has the flag)
    new.a2u(data, form="nfc")
    new.a2r(b"...")                  # ACII -> Romenagri                 (acii2rmn)
    new.r2a(b"...")                  # Romenagri -> ACII                 (rmn2acii), returns (returncode, bytes)
    new.a2h(b"...")                  # ACII -> "saral" Latin             (acii2hin)
    new.run3(prog, data, args=(), env={})   # (returncode, stdout, stderr) with options and environment variables

The environment variables ROMENAGRI_NUKTA_FORM and ROMENAGRI_NUKTA_WARN are removed from the environment of every call, so that a setting of
the person who runs the tests cannot change a result; a test that wants one passes it in env.
"""
import os
import subprocess

import config


class Tools:
    def __init__(self, d):
        self.d = d

    def run3(self, prog, data, timeout=120, args=(), env=None):
        e = {k: v for k, v in os.environ.items() if not k.startswith("ROMENAGRI_NUKTA_")}
        e.update(env or {})
        p = subprocess.run([os.path.join(self.d, prog)] + list(args), input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, env=e)
        return p.returncode, p.stdout, p.stderr

    def run(self, prog, data, timeout=120, args=(), env=None):
        rc, out, _ = self.run3(prog, data, timeout, args, env)
        return rc, out

    def u2a(self, text, form=None):
        return self.run("uni2acii", b"\xff\xfe" + text.encode("utf-16-le"), args=("-f", form) if form else ())[1]

    def a2u(self, data, form=None):
        return self.run("acii2uni", data, args=("-f", form) if form else ())[1].decode("utf-16", "replace").replace("\r\n", "\n")

    def a2r(self, data):
        return self.run("acii2rmn", data)[1]

    def r2a(self, data):
        return self.run("rmn2acii", data)

    def a2cf(self, data):
        return self.run("acii2cf", data)[1]

    def a2h(self, data):
        return self.run("acii2hin", data)[1]


old = Tools(config.OLD)
mid = Tools(config.MID)
new = Tools(config.NEW)

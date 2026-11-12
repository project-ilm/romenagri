# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Adds the missing Sanskrit characters to Romenagri / ACII.

    python3 -I tools/apply_sanskrit.py <pristine Romenagri directory>

Edits (byte-exact; acii.h, unicode.h and aciihin.h keep their CRLF line ends and their raw 8-bit data):
  unicode.h   +12 rows   (Unicode <-> ACII byte), UNI_LEN 73 -> 85
  acii.h      +12 rows, avagraha string "_3" -> "_s", ACII_LEN 84 -> 96
  aciihin.h   +12 rows   (one-way "saral" Latin rendering), ACII_HIN_LEN 75 -> 87
  acii2hin.c  literal 75 -> ACII_HIN_LEN
  rmn2acii.c  new parser branches (same recursive-descent structure) for _li _lee _ree _om _vd _vua _vna _vga _vca
  all five    copyright line 1993-2026, and one entry in the file's "Modifications" log

The script is the exact, reproducible form of patches/0001-add-missing-sanskrit-characters.patch (which also adds
TRANSLITERATION.md).  Run it once on a pristine tree: every edit asserts that its anchor occurs exactly once, so a second run, or
a run on an already patched or on a changed upstream tree, stops with an AssertionError instead of damaging anything.

Patch 0002, the guards against the underscore (TRANSLITERATION.md, section 14.7), comes after this one: patches/0002-apply-underscore-guards.patch,
or tools/apply_guards.py for the edits to rmn2acii.c alone.
"""
import os
import re
import sys

d = sys.argv[1]
MOD_DATE = "19-Oct-2026"

# (code point, ACII byte, Romenagri string, saral string, Unicode name)
NEW = [
    (0x090C, 0x81, "_li",   "lri",  "VOCALIC L"),
    (0x0961, 0x82, "_lee",  "lri",  "VOCALIC LL"),
    (0x0960, 0x83, "_ree",  "ri",   "VOCALIC RR"),
    (0x0962, 0x84, "^_li",  "^lri", "VOWEL SIGN VOCALIC L"),
    (0x0963, 0x85, "^_lee", "^lri", "VOWEL SIGN VOCALIC LL"),
    (0x0944, 0x86, "^_ree", "^ri",  "VOWEL SIGN VOCALIC RR"),
    (0x0965, 0x87, "_vd",   "||",   "DOUBLE DANDA"),
    (0x0951, 0x88, "_vua",  "",     "STRESS SIGN UDATTA"),
    (0x0952, 0x89, "_vna",  "",     "STRESS SIGN ANUDATTA"),
    (0x0953, 0x8A, "_vga",  "",     "GRAVE ACCENT"),
    (0x0954, 0x8B, "_vca",  "",     "ACUTE ACCENT"),
    (0x0950, 0x8C, "_om",   "om",   "OM"),
]
assert len(NEW) == 12

CRLF = b"\r\n"


def rd(n):
    return open(os.path.join(d, n), "rb").read()


def wr(n, data):
    open(os.path.join(d, n), "wb").write(data)


def sub1(data, old, new):
    assert data.count(old) == 1, (old, data.count(old))
    return data.replace(old, new)


# ---------------------------------------------------------------- unicode.h
u = rd("unicode.h")
u = sub1(u, b"#define UNI_LEN 73", b"#define UNI_LEN 85")
body = b""
for i, (cp, byte, rmn, hin, name) in enumerate(NEW):
    sep = "," if i < len(NEW) - 1 else ""
    body += ("    {%d, %d, '\\x%02X'}%s //U+%04X %s" % (cp & 255, cp >> 8, byte, sep, cp, name)).encode() + CRLF
old = b"{49, 9, '\xD0'}" + CRLF + CRLF + b"  };"
new = (b"{49, 9, '\xD0'}," + CRLF + CRLF
       + b"    //Sanskrit additions. 0x81-0x8C continue the ACII extension block that starts with U+0979 at 0x80." + CRLF
       + b"    //OM is deliberately not at 0xA0, its slot in iscii_map.csv: uni2acii writes an unmapped U+00A0 (no-break space) as 0xA0. See TRANSLITERATION.md." + CRLF
       + body + CRLF + b"  };")
u = sub1(u, old, new)
wr("unicode.h", u)

# ---------------------------------------------------------------- acii.h
a = rd("acii.h")
a = sub1(a, b"#define ACII_LEN 84", b"#define ACII_LEN 96")
body = (b'{"_s","\\xEB"}, //Avagraha. Was "_3": a digit never reaches the rmn2acii parser. "_s" is the branch level2c already had.' + CRLF
        + b"/* Sanskrit additions (see TRANSLITERATION.md). Strings use only [a-z_]; a leading '^' marks the dependent (matra) form. */" + CRLF)
for i, (cp, byte, rmn, hin, name) in enumerate(NEW):
    sep = "," if i < len(NEW) - 1 else ""
    pad = " " * max(1, 8 - len(rmn))
    body += ('{"%s",%s"\\x%02X"}%s //U+%04X %s' % (rmn, pad, byte, sep, cp, name)).encode() + CRLF
a = sub1(a, b'{"_3","\xEB"} //Avagraha' + CRLF + b"};", body + b"};")
wr("acii.h", a)

# ---------------------------------------------------------------- aciihin.h
h = rd("aciihin.h")
h = sub1(h, b"#define ACII_HIN_LEN 75", b"#define ACII_HIN_LEN 87")
body = (b'    {"shra", "\xD5\xE8\xCF"},' + CRLF
        + b"    /* Sanskrit additions: one-way and lossy like the rest of this table (length is dropped, accents vanish) */" + CRLF)
for i, (cp, byte, rmn, hin, name) in enumerate(NEW):
    sep = "," if i < len(NEW) - 1 else ""
    body += ('    {"%s", "\\x%02X"}%s //U+%04X %s' % (hin, byte, sep, cp, name)).encode() + CRLF
h = sub1(h, b'    {"shra", "\xD5\xE8\xCF"}' + CRLF + b"  };", body + b"  };")
wr("aciihin.h", h)

# ---------------------------------------------------------------- acii2hin.c
c = rd("acii2hin.c")
c = sub1(c, b"for (j = 0; j < 75; j++)", b"for (j = 0; j < ACII_HIN_LEN; j++)")
wr("acii2hin.c", c)

# ---------------------------------------------------------------- rmn2acii.c  (explicit tabs: the file mixes tabs and spaces)
r = rd("rmn2acii.c").decode("ascii")
T = "\t"


def sub1s(s, old, new):
    assert s.count(old) == 1, (old, s.count(old))
    return s.replace(old, new)


# helper, right after lookup()
r = sub1s(r, """  return NULL; // returning NULL here causes seg fault. TBD - fix architecture
}
""", """  return NULL; // returning NULL here causes seg fault. TBD - fix architecture
}

/* A vowel that has an independent byte and a dependent (matra) byte and is written the same way
   in Romenagri.  After a consonant the parser has just emitted a halant; that halant is replaced
   by the matra byte (consonant + "_ri" is consonant + sign RI) -- the 'push-pop' of "_ri". */
static void
vocalic (char *indep, char *dep)
{
  if (strlen (msg) > 0 && msg[strlen (msg) - 1] == *lookup ("^"))
    {
      msg[strlen (msg) - 1] = '\\0';
      strcat (msg, lookup (dep));
    }
  else
    strcat (msg, lookup (indep));
}
""")

# matra(): the '_' branch learns _li, _lee, _ree; everything else keeps the old meaning ("^_ri", 3 chars)
r = sub1s(r, "    case '_':" + T * 3 + "/*redundant */\n"
             '      strcat (msg, lookup ("^_ri"));\n      tok += 3;\n      level1 (tok);\n      break;\n',
          "    case '_':" + T * 3 + "/*redundant */\n"
          """      if (tok[1] == 'l' && tok[2] == 'i')
        {
          strcat (msg, lookup ("^_li"));
          tok += 3;
        }
      else if (tok[1] == 'l' && tok[2] == 'e' && tok[3] == 'e')
        {
          strcat (msg, lookup ("^_lee"));
          tok += 4;
        }
      else if (tok[1] == 'r' && tok[2] == 'e' && tok[3] == 'e')
        {
          strcat (msg, lookup ("^_ree"));
          tok += 4;
        }
      else
        {
          strcat (msg, lookup ("^_ri"));
          tok += 3;
        }
      level1 (tok);
      break;
""")

# level2c(): "_o" + 'm' = OM
old = (T + "case 'u':\n" + T + '  strcat (msg, lookup ("_ou"));\n' + T + "  tok++;\n" + T + "  level1 (tok);\n" + T + "  break;\n")
r = sub1s(r, old, old
          + T + "case 'm':" + T * 3 + "/* _om: OM */\n"
          + T + '  strcat (msg, lookup ("_om"));\n' + T + "  tok++;\n" + T + "  level1 (tok);\n" + T + "  break;\n")

# level2c(): "_r" + "ee" = vocalic RR
old = (T + "case 'r':\n" + T + '  level2b (++tok, "_rr");\n' + T + "  break;\n")
r = sub1s(r, old, old
          + T + "case 'e':" + T * 3 + "/* _ree: vocalic RR, or its sign after a consonant */\n"
          + T + "  if (tok[1] == 'e')\n" + T + "    {\n"
          + T + '      vocalic ("_ree", "^_ree");\n' + T + "      tok += 2;\n" + T + "      level1 (tok);\n" + T + "    }\n"
          + T + "  else\n" + T + "    {\n"
          + T + "      strcat (msg, c2s (tok[0]));\n" + T + "      level1 (++tok);\n" + T + "    }\n"
          + T + "  break;\n")

# level2c(): new families '_l' (vocalic L) and '_v' (Vedic accents, double danda), before the final default
old = """    default:
      strcat (msg, c2s (tok[0]));
      level1 (++tok);
    }
  return 1;
}

int
level1 (char *tok)"""
new = """    case 'l':            /* _li: vocalic L, _lee: vocalic LL (or their signs after a consonant) */
      if (tok[1] == 'i')
        {
          vocalic ("_li", "^_li");
          tok += 2;
          level1 (tok);
        }
      else if (tok[1] == 'e' && tok[2] == 'e')
        {
          vocalic ("_lee", "^_lee");
          tok += 3;
          level1 (tok);
        }
      else
        {
          strcat (msg, c2s (tok[0]));
          level1 (++tok);
        }
      break;
    case 'v':            /* _v? family: the double danda and the Vedic accents */
      tok++;
      switch (tok[0])
        {
        case 'd':
          strcat (msg, lookup ("_vd"));
          tok++;
          level1 (tok);
          break;
        case 'u':            /* accents are written like the nukta: an explicit 'a' follows, then level2a */
          strcat (msg, lookup ("_vua"));
          level2a (++tok);
          break;
        case 'n':
          strcat (msg, lookup ("_vna"));
          level2a (++tok);
          break;
        case 'g':
          strcat (msg, lookup ("_vga"));
          level2a (++tok);
          break;
        case 'c':
          strcat (msg, lookup ("_vca"));
          level2a (++tok);
          break;
        default:
          strcat (msg, "v");
          level1 (tok);
        };
      break;
""" + old
r = sub1s(r, old, new)
wr("rmn2acii.c", r.encode("ascii"))

# ---------------------------------------------------------------- copyright line (1993-2026) and "Modifications" logs
MODLOG = {
    "unicode.h": ["Added 12 Sanskrit characters to the Unicode<->ACII table:",
                  "ACII bytes 0x81-0x8C, see TRANSLITERATION.md,"],
    "acii.h": ["Added 12 Sanskrit characters to the ACII<->Romenagri table;",
               "avagraha string changed from _3 to _s, see TRANSLITERATION.md,"],
    "aciihin.h": ["Added 12 Sanskrit characters to the saral table,"],
    "acii2hin.c": ["Table length is ACII_HIN_LEN instead of the literal 75,"],
    "rmn2acii.c": ["Parser branches for _li _lee _ree _om _vd _vua _vna _vga _vca,",
                   "new helper vocalic(), see TRANSLITERATION.md,"],
}
TEMPLATE = ["\tdd-mmm-yyyy, Nature of modification,",
            "                        Name of modifier <alias>,",
            "\t\t\temail adress of modifier"]
COPYRIGHT = re.compile(rb"Copyright \(C\) [0-9, -]+ Abhishek Choudhary")
for name, what in MODLOG.items():
    data = rd(name)
    assert len(COPYRIGHT.findall(data)) == 1, (name, "copyright line")
    data = COPYRIGHT.sub(b"Copyright (C) 1993-2026 Abhishek Choudhary", data)
    eol = b"\r\n" if b"\r\n" in data else b"\n"
    anchor = eol.join(t.encode() for t in TEMPLATE) + eol + eol
    lines = ["\t%s, %s" % (MOD_DATE, what[0])] + ["\t              " + w for w in what[1:]]
    lines += ["                        Abhishek Choudhary <obonac> (prepared with Claude),",
              "                        a.choudhary@ieee.org"]
    entry = eol.join(l.encode() for l in lines) + eol + eol
    assert data.count(anchor) == 1, (name, data.count(anchor))
    wr(name, data.replace(anchor, anchor + entry))

print("patched", d)

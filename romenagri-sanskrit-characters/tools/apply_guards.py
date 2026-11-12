# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Applies the twelve guards of TRANSLITERATION.md, section 14.7, to rmn2acii.c.

    python3 -I tools/apply_guards.py <Romenagri directory that already has patches/0001 applied>

Eleven branches of the parser jump over, or keep as plain text, a character that they have not looked at (section 14.6).  When that
character is an underscore it is swallowed, and the pairing of `__` is lost; when it is the end of the string the parser reads past it.
Each guard is a test in front of one such branch: if the next character is an underscore or the end of the string, the branch is not
taken, and the letter is written as plain text, which is what the parser does with any other unknown letter.  No new function with
a state and no new state is needed; the one helper, no_partner(), is the test itself.

    level1   case 'c'              the letter c that has no 'h' after it
    level2b  the 'v' branch        the stem that has no "vr" after it
    level2c  cases e y o n r j     "_e", "_y", "_o", "_n", "_r", "_j" with nothing after them
    matra    cases e o             "e" and "o" with nothing after them
    matra    case '_'              "^_" that has an underscore or the end of the string in one of the two places where "_ri" has "ri"

The script is the exact, reproducible form of patches/0002-apply-underscore-guards.patch (which also changes TRANSLITERATION.md).  Every
edit asserts that its anchor occurs exactly once, so a second run, or a run on a tree without patch 0001, stops with an AssertionError
instead of damaging anything.
"""
import os
import sys

d = sys.argv[1]
MOD_DATE = "26-Oct-2026"
T = "\t"

path = os.path.join(d, "rmn2acii.c")
r = open(path, "rb").read().decode("ascii")
assert "no_partner" not in r, "the guards are already applied"
assert "vocalic" in r, "patch 0001 (the Sanskrit characters) is not applied"


def sub1(s, old, new):
    assert s.count(old) == 1, (old, s.count(old))
    return s.replace(old, new)


def guard(indent, what):
    """the test that goes in front of a branch: a letter with no partner is plain text, and the cursor moves past that one letter only"""
    p = " " * indent
    return (p + "if (no_partner (tok[1]))" + T + "/* " + what + " */\n"
            + p + "  {\n"
            + p + "    strcat (msg, c2s (tok[0]));\n"
            + p + "    level1 (++tok);\n"
            + p + "    break;\n"
            + p + "  }\n")


# ---- the helper, right after vocalic()
r = sub1(r, """  else
    strcat (msg, lookup (indep));
}
""", """  else
    strcat (msg, lookup (indep));
}

/* The guards of TRANSLITERATION.md, section 14.7.  The branches below that jump over, or keep as plain text, the character after
   their letter without looking at it (the 'h' of "ch", the 'r' of "vra", the second 'e' of "_ee", the 'n' of "_yna", the two
   letters of "_ri" ...) must not take an underscore, which belongs to the next unit or to a "__" pair, nor step over the end of
   the string.  no_partner() is true for those two characters; a letter that is followed by one of them has no partner. */
static int
no_partner (char next)
{
  return next == '_' || next == '\\0';
}
""")

# ---- matra(): e, _ (the two letters of "_ri"), o
r = sub1(r, """    case 'e':
      strcat (msg, lookup ("^ee"));
""", "    case 'e':\n" + guard(6, "an 'e' with no second 'e'") + """      strcat (msg, lookup ("^ee"));
""")
r = sub1(r, """      else
        {
          strcat (msg, lookup ("^_ri"));
          tok += 3;
        }
""", """      else if (no_partner (tok[1]) || no_partner (tok[2]))	/* "_ri" with an underscore or the end where "ri" should be: */
        {
        }						/* the underscore is read again, as the start of the next unit */
      else
        {
          strcat (msg, lookup ("^_ri"));
          tok += 3;
        }
""")
r = sub1(r, "    case 'o':\n      tok++;\n      switch (tok[0])\n" + T + "{\n" + T + "case 'o':\n" + T + '  strcat (msg, lookup ("^oo"));\n',
         "    case 'o':\n" + guard(6, "an 'o' with nothing after it") + "      tok++;\n      switch (tok[0])\n" + T + "{\n" + T + "case 'o':\n" + T + '  strcat (msg, lookup ("^oo"));\n')

# ---- level2b(): the 'v' of "lvra"
r = sub1(r, "  else if (tok[0] == 'v')" + T + "/*lvra-case */",
         "  else if (tok[0] == 'v' && !no_partner (tok[1]))" + T + "/*lvra-case */")

# ---- level2c(): e, y, o, n, r, j
r = sub1(r, """    case 'e':
      strcat (msg, lookup ("_ee"));
""", "    case 'e':\n" + guard(6, "'_e' with no second 'e'") + """      strcat (msg, lookup ("_ee"));
""")
r = sub1(r, """    case 'y':
      strcat (msg, lookup ("_yna"));
""", "    case 'y':\n" + guard(6, "'_y' with no 'n'") + """      strcat (msg, lookup ("_yna"));
""")
for letter, anchor, what in (
        ("o", "case 'o':\n" + T + '  strcat (msg, lookup ("_oo"));\n', "'_o' with nothing after it"),
        ("n", "case 'a':\n" + T + '  strcat (msg, lookup ("_na"));\n', "'_n' with nothing after it"),
        ("r", "case 'i':/*_ri*/\n", "'_r' with nothing after it"),
        ("j", "/*case 'a':\n", "'_j' with nothing after it")):
    old = "    case '%s':\n      tok++;\n      switch (tok[0])\n" % letter + T + "{\n" + T + anchor
    r = sub1(r, old, "    case '%s':\n" % letter + guard(6, what) + old[len("    case '%s':\n" % letter):])

# ---- level1(): the 'c' of "ch"
r = sub1(r, """    case 'c':
      tok++;
      level2b (++tok, "ch");
""", "    case 'c':\n" + guard(6, "a 'c' with no 'h' after it") + """      tok++;
      level2b (++tok, "ch");
""")

# ---- the "Modifications" log
anchor = ("\tdd-mmm-yyyy, Nature of modification,\n"
          "                        Name of modifier <alias>,\n"
          "\t\t\temail adress of modifier\n\n")
entry = ("\t%s, Guards: a letter that needs a partner is plain text when an underscore or the end follows\n"
         "\t              (level1 c, level2b v, level2c e y o n r j, matra e o _), new helper no_partner(),\n"
         "\t              see TRANSLITERATION.md, section 14.7,\n"
         "                        Abhishek Choudhary <obonac> (prepared with Claude),\n"
         "                        a.choudhary@ieee.org\n\n") % MOD_DATE
r = sub1(r, anchor, anchor + entry)

open(path, "wb").write(r.encode("ascii"))
print("guards applied to", path)

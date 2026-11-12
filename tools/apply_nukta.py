# Copyright (C) 1993-2026 Abhishek Choudhary
# SPDX-License-Identifier: GPL-2.0-or-later
# This file is part of the Romenagri Transliteration System; see the file COPYING.
"""Applies the nukta layer of TRANSLITERATION.md, section 15, to uni2acii.c, acii2uni.c and the Makefile, and creates nukta.h.

    python3 -I tools/apply_nukta.py <Romenagri directory that already has patches/0001 and patches/0002 applied>

ACII writes a letter with a nukta as two bytes (the consonant, then E9).  Unicode has eleven letters that are such a pair in one code point.
Two of them have a row in unicode.h (U+0929 and U+0931); nine have none, and uni2acii wrote the low byte of their code point for them
(U+095C became a backslash).  The layer has three parts:

    the rule      uni2acii writes a code point that unicode.h has no row for and that nukta.h lists as the byte of its consonant and E9.
                  Always: it is how the sound of the modified consonant is there as a consonant and a nukta when the parser maps the
                  consonants (level 1), before a halant, an adjunct consonant or a vowel sign is attached (level 2)
    the form      what the two converters write for the family, as one code point or as two: the Unicode layer, kept apart from the
                  rule.  asis (the default: what they always wrote), nfc or nfd, chosen by -f, by ROMENAGRI_NUKTA_FORM, by -DNUKTA_FORM
                  or, in a program that includes nukta.h, by nukta_set_form()
    the warning   uni2acii -w (or ROMENAGRI_NUKTA_WARN=1) reports each code point that it writes as its low byte (the low byte of U+00E9
                  is the nukta byte); off by default

With the default form nothing that was converted before is converted differently, except the nine letters that uni2acii wrote as a low
byte.  No table of unicode.h changes, and the parser (rmn2acii.c) is not touched.  The script is the exact, reproducible form of
patches/0003-add-nukta-layer.patch (which also changes TRANSLITERATION.md).  Every edit asserts that its anchor occurs exactly once, and the
code that the two converters lose is checked by its SHA-256, so a second run, or a run on a tree without patches 0001 and 0002, stops with an
AssertionError instead of damaging anything.
"""
import hashlib
import os
import sys

d = sys.argv[1]
MOD_DATE = "05-Nov-2026"        # the entry of the Makefile
T = "\t"
END_MODS = "End of modifications.\n*/\n"
OLD_COPY = "Copyright (C) 2003,2004,2005,2006 Abhishek Choudhary"
NEW_COPY = "Copyright (C) 1993-2026 Abhishek Choudhary"
ANCHOR_MOD = T + "19-Jan-2006, Added the modifications section,\n"


def read(name):
    return open(os.path.join(d, name), "rb").read().decode("latin-1")


def write(name, text):
    open(os.path.join(d, name), "wb").write(text.encode("latin-1"))


def sub1(s, old, new):
    assert s.count(old) == 1, (old, s.count(old))
    return s.replace(old, new)


assert not os.path.exists(os.path.join(d, "nukta.h")), "the nukta layer is already applied"
assert "no_partner" in read("rmn2acii.c") and "vocalic" in read("rmn2acii.c"), "patches 0001 and 0002 are not applied"

# ---------------------------------------------------------------- nukta.h: the licence of unicode.h, then this
NUKTA_H = r'''/*
Modifications: (Please maintain reverse chronological order)

	dd-mmm-yyyy, Nature of modification,
                        Name of modifier <alias>,
			email adress of modifier

	08-Nov-2026, Reworked: the forms (asis, nfc, nfd), the options -f and -w, the environment variables, nukta_set_form();
	              a nukta letter is a consonant and a nukta in every form; NUKTA_REBUILD is gone, section 15.6,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

	05-Nov-2026, Created: the table and the helper of the nukta layer of uni2acii and acii2uni,
	              see TRANSLITERATION.md, section 15,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

End of modifications.
*/

/* The nukta layer.  Include this file after unicode.h.

   The rule.  ACII writes a letter with a nukta as two bytes: the consonant, then NUKTA_BYTE.  Unicode has eleven letters that are such
   a pair in one code point, and gave a code point of its own to some letters with a nukta and not to others.  The layer does not follow
   that: a letter with a nukta is a consonant and a nukta, however it arrives.  So uni2acii writes a code point that unicode.h has no
   row for and that is listed here (the eight of U+0958 to U+095F, and U+0934) as the byte of its consonant, then NUKTA_BYTE.  This is
   not an option.  It is how the sound of the modified consonant is found before a halant, an adjunct consonant or a vowel sign is
   attached to it (in the parser: level1 before level2).  Two of the eleven have a row of their own in unicode.h (U+0929 and U+0931,
   with the bytes C7 and D0); of the other nine uni2acii used to write the low byte (U+095C, for example, became a backslash).

   The form.  What the converters write for the letters of this family, as one code point or as two, is the form.  The form is the
   Unicode layer, and is kept apart from the rule.  There are three:
     asis  (the default) what the converters always wrote: a row of unicode.h is used as it is (C7 is U+0929, and U+0929 is C7); a
           consonant and a nukta that arrive as two code points, or as two bytes, stay two
     nfc   as Unicode's normalisation form NFC: where NFC composes a consonant and a nukta (U+0928, U+0930 or U+0933 and U+093C) they are
           one code point (acii2uni), or the one byte that unicode.h has for the letter (uni2acii: C7 and D0); the eight letters that
           NFC leaves decomposed (the composition exclusions, U+0958 to U+095F) stay a consonant and a nukta
     nfd   as NFD: all eleven letters are a consonant and a nukta, in both converters (C7 and D0 as well)
   The form is chosen, the last of these winning, by the macro NUKTA_FORM when a converter is compiled (cc -DNUKTA_FORM=NUKTA_NFD), by the
   environment variable ROMENAGRI_NUKTA_FORM, and by the flag -f.  A program that includes this file sets nukta_form, or calls
   nukta_set_form(), before it converts.

   The warning.  uni2acii writes the low byte of a code point that unicode.h has no row for.  Every converter of this kind does, and the
   low byte of U+00E9 (an e with an acute accent) is the nukta byte.  With the flag -w, or ROMENAGRI_NUKTA_WARN=1, uni2acii reports each
   such code point once, on stderr.  Nothing is reported by default, and the bytes written are the same.

   tests/test_nukta.py compares this table with Python's unicodedata.
*/

#ifndef __NUKTA_H__
#define __NUKTA_H__

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#ifdef __cplusplus
extern "C"
{
#endif


#define NUKTA_BYTE 0xE9		/* the ACII byte of U+093C DEVANAGARI SIGN NUKTA: its row in unicode.h */
#define NUKTA_SIGN_LOW 0x3C	/* U+093C as the two bytes of a UTF-16LE code unit */
#define NUKTA_SIGN_HIGH 0x09

#define NUKTA_ASIS 0		/* the forms */
#define NUKTA_NFC 1
#define NUKTA_NFD 2

#ifdef NUKTA_REBUILD
#error "NUKTA_REBUILD is gone: choose the form with NUKTA_FORM (NUKTA_ASIS, NUKTA_NFC or NUKTA_NFD); see TRANSLITERATION.md, section 15.6"
#endif

#ifndef NUKTA_FORM
#define NUKTA_FORM NUKTA_ASIS
#endif

#if NUKTA_FORM < 0 || NUKTA_FORM > 2
#error "NUKTA_FORM is NUKTA_ASIS (0), NUKTA_NFC (1) or NUKTA_NFD (2)"
#endif

#define NUKTA_LEN 11

/* {low, high} of the precomposed letter, {low, high} of its consonant, 1 if Unicode's NFC composes the pair and 0 if it does not */
  unsigned char nukta_hin[NUKTA_LEN][5] = {
    {0x29, 9, 0x28, 9, 1}, /* U+0929 LETTER NNNA  = U+0928 NA  + NUKTA; has the byte C7 in unicode.h */
    {0x31, 9, 0x30, 9, 1}, /* U+0931 LETTER RRA   = U+0930 RA  + NUKTA; has the byte D0 in unicode.h */
    {0x34, 9, 0x33, 9, 1}, /* U+0934 LETTER LLLA  = U+0933 LLA + NUKTA */
    {0x58, 9, 0x15, 9, 0}, /* U+0958 LETTER QA    = U+0915 KA  + NUKTA */
    {0x59, 9, 0x16, 9, 0}, /* U+0959 LETTER KHHA  = U+0916 KHA + NUKTA */
    {0x5A, 9, 0x17, 9, 0}, /* U+095A LETTER GHHA  = U+0917 GA  + NUKTA */
    {0x5B, 9, 0x1C, 9, 0}, /* U+095B LETTER ZA    = U+091C JA  + NUKTA */
    {0x5C, 9, 0x21, 9, 0}, /* U+095C LETTER DDDHA = U+0921 DDA + NUKTA */
    {0x5D, 9, 0x22, 9, 0}, /* U+095D LETTER RHA   = U+0922 DDHA + NUKTA */
    {0x5E, 9, 0x2B, 9, 0}, /* U+095E LETTER FA    = U+092B PHA + NUKTA */
    {0x5F, 9, 0x2F, 9, 0}  /* U+095F LETTER YYA   = U+092F YA  + NUKTA */
  };

/* the form in force: NUKTA_FORM, then what nukta_options reads from the environment and the flags; a program that includes this file may set it */
  static int nukta_form = NUKTA_FORM;

/* the ACII byte of a code point, or -1 if unicode.h has no row for it */
  static int nukta_acii_of (unsigned char low, unsigned char high)
  {
    int k;
    for (k = 0; k < UNI_LEN; k++)
      if (low == unicode_hin[k][0] && high == unicode_hin[k][1])
	return unicode_hin[k][2];
    return -1;
  }

/* the row of nukta_hin whose precomposed letter is the code point (low, high), or -1 */
  static int nukta_row_of (unsigned char low, unsigned char high)
  {
    int j;
    for (j = 0; j < NUKTA_LEN; j++)
      if (low == nukta_hin[j][0] && high == nukta_hin[j][1])
	return j;
    return -1;
  }

/* the form that a name stands for (asis, nfc or nfd, in lower or upper case), or -1 */
  static int nukta_form_named (const char *name)
  {
    static const char *const names[3] = { "asis", "nfc", "nfd" };
    int k;
    const char *p, *q;

    for (k = 0; k < 3; k++)
      {
	for (p = name, q = names[k]; *q != 0 && (*p | 32) == *q; p++, q++)
	  ;
	if (*q == 0 && *p == 0)
	  return k;
      }
    return -1;
  }

/* sets nukta_form to the form that a name stands for: 0, or -1 (and nothing changes) if the name is not a form */
  static int nukta_set_form (const char *name)
  {
    int f = nukta_form_named (name);

    if (f < 0)
      return -1;
    nukta_form = f;
    return 0;
  }

/* The options of the two converters: -f FORM and --form=FORM and, if warn is not NULL, -w and --warn (which set *warn).  The environment
   is read first (ROMENAGRI_NUKTA_FORM; ROMENAGRI_NUKTA_WARN=1), so that a flag wins over it.  Returns the index of the first argument that
   is not an option (after "--", or the first that does not begin with a minus sign, or is a minus sign alone), or -1 after a message on stderr. */
  static int nukta_options (const char *prog, int argc, char *argv[], int *warn)
  {
    int a = 1;
    const char *e;

    if ((e = getenv ("ROMENAGRI_NUKTA_FORM")) != NULL && *e != 0 && nukta_set_form (e) < 0)
      {
	fprintf (stderr, "%s: ROMENAGRI_NUKTA_FORM is \"%s\", which is not a form: use asis, nfc or nfd\n", prog, e);
	return -1;
      }
    if (warn != NULL && (e = getenv ("ROMENAGRI_NUKTA_WARN")) != NULL && e[0] == '1')
      *warn = 1;
    while (a < argc && argv[a][0] == '-' && argv[a][1] != 0)
      {
	if (strcmp (argv[a], "--") == 0)
	  {
	    a++;
	    break;
	  }
	if (warn != NULL && (strcmp (argv[a], "-w") == 0 || strcmp (argv[a], "--warn") == 0))
	  {
	    *warn = 1;
	    a++;
	    continue;
	  }
	if (strcmp (argv[a], "-f") == 0)
	  {
	    if (a + 1 >= argc)
	      {
		fprintf (stderr, "%s: -f needs a form: asis, nfc or nfd\n", prog);
		return -1;
	      }
	    e = argv[++a];
	  }
	else if (strncmp (argv[a], "--form=", 7) == 0)
	  e = argv[a] + 7;
	else
	  {
	    fprintf (stderr, "%s: unknown option %s\n", prog, argv[a]);
	    return -1;
	  }
	if (nukta_set_form (e) < 0)
	  {
	    fprintf (stderr, "%s: \"%s\" is not a form: use asis, nfc or nfd\n", prog, e);
	    return -1;
	  }
	a++;
      }
    return a;
  }


#ifdef __cplusplus
}
#endif



#endif
'''

uni = read("unicode.h")
licence = uni[:uni.index("*/") + 2].replace("\r\n", "\n")   # the notice every source carries (unicode.h has DOS line ends; nukta.h has Unix ones)
assert licence.startswith("/*\nCopyright (C) 1993-2026 Abhishek Choudhary")
assert not os.path.exists(os.path.join(d, "nukta.h"))
write("nukta.h", licence + "\n\n" + NUKTA_H)

# ---------------------------------------------------------------- the two converters: two new entries of the modifications block, new code
# ENTRIES go above the entry of 19-Jan-2006; CODE replaces everything after the modifications block (the code that patches 0001 and 0002 leave, which is
# checked by its SHA-256: OLD_CODE_SHA256)
ENTRIES_UNI2ACII = r'''	08-Nov-2026, The forms (asis, nfc, nfd) and the warning layer: -f, ROMENAGRI_NUKTA_FORM, -w, see TRANSLITERATION.md, section 15;
	              asis, the default, is what the converter always wrote; nfc and nfd are Unicode's two forms; a nukta letter is a consonant and
	              a nukta in every form; NUKTA_REBUILD is gone, see TRANSLITERATION.md, section 15,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

	05-Nov-2026, The nukta layer: a precomposed nukta letter that unicode.h has no row for is written as its consonant
	              and the nukta byte (new header nukta.h), see TRANSLITERATION.md, section 15,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

'''

CODE_UNI2ACII = r'''
#include <stdio.h>
#include <fcntl.h>

#include "unicode.h"
#include "nukta.h"

#define KIND_ROW 0		/* the bytes are the byte of a row of unicode.h */
#define KIND_NUKTA 1		/* the bytes are a consonant and the nukta byte (nukta.h) */
#define KIND_LOW 2		/* unicode.h has no row and nukta.h no letter: the low byte of the code unit */

static unsigned char seen[8192];	/* the warning layer: one bit for each code unit that it has reported */
static int reported = 0, repeated = 0;

static void
usage (void)
{
  printf ("Usage: uni2acii [-f asis|nfc|nfd] [-w] [<UNICODE_filename> <ISCII_filename>]\n");
  printf ("  -f FORM, --form=FORM   how a letter with a nukta is written: asis (the default), nfc or nfd\n");
  printf ("  -w, --warn             report each code point that has no ACII byte and is written as its low byte\n");
  printf ("The environment variables ROMENAGRI_NUKTA_FORM and ROMENAGRI_NUKTA_WARN=1 do the same; a flag wins.\n");
}

/* the warning layer: a code point that unicode.h has no row for is written as its low byte, which ACII reads as another character
   (the low byte of U+00E9 is the nukta byte).  Reported once for each code point, on stderr; the bytes written do not change. */
static void
report (unsigned char t1, unsigned char t2)
{
  int u = t2 * 256 + t1;

  if (seen[u >> 3] & (1 << (u & 7)))
    {
      repeated++;
      return;
    }
  if (reported == 0)
    fprintf (stderr, "uni2acii: note: a code point that unicode.h has no row for is written as its low byte, which ACII reads as another "
	     "character; every converter of this kind does this (TRANSLITERATION.md, section 11.6)\n");
  seen[u >> 3] |= 1 << (u & 7);
  reported++;
  fprintf (stderr, "uni2acii: warning: U+%04X has no ACII byte and is written as its low byte %02X%s\n", u, t1,
	   t1 == NUKTA_BYTE ? ", the nukta byte" : "");
}

/* the bytes of the code unit (t1, t2): the byte of its row in unicode.h; or a consonant and the nukta byte, for a letter of nukta.h that
   has no row (in the form nfd also for the two that have one: C7 and D0 become C6 E9 and CF E9); or else the low byte, "presuming 0 to
   127".  Returns the number of bytes; *kind says which of the three it was. */
static int
bytes_of (unsigned char t1, unsigned char t2, unsigned char out[2], int *kind)
{
  int i, j, b;

  for (i = 0; i < UNI_LEN; i++)
    if (t1 == unicode_hin[i][0] && t2 == unicode_hin[i][1])	/*match */
      break;
  j = nukta_row_of (t1, t2);
  if (j >= 0 && (i == UNI_LEN || nukta_form == NUKTA_NFD) && (b = nukta_acii_of (nukta_hin[j][2], nukta_hin[j][3])) >= 0)
    {
      out[0] = b;
      out[1] = NUKTA_BYTE;
      *kind = KIND_NUKTA;
      return 2;
    }
  if (i < UNI_LEN)
    {
      out[0] = unicode_hin[i][2];
      *kind = KIND_ROW;
      return 1;
    }
  out[0] = t1;			/*presuming 0 to 127 */
  *kind = KIND_LOW;
  return 1;
}

int
main (int argc, char *argv[])
{
  FILE *fin, *fout;
  unsigned char t1, t2, tmp[4], out[2];
  int i, j, k, n, a, kind, held = -1, join[256], warn = 0;	/* held: the byte of a consonant that waits for a nukta (form nfc) */

#ifdef __DJGPP
  _fmode = O_BINARY;
#endif

  tmp[0] = 0;
  tmp[1] = 0;
  tmp[2] = 0;
  tmp[3] = 0;

  if ((a = nukta_options ("uni2acii", argc, argv, &warn)) < 0)
    {
      usage ();
      return 1;
    }

  if (argc - a < 1)
    {
      fin = stdin;
      fout = stdout;
    }
  else
    {
      if (argc - a < 2)
	{
	  usage ();
	  return 1;
	}


      if ((fin = fopen (argv[a], "r+")) == NULL)
	{
	  fprintf (stderr, "Cannot open input file, using stdin.\n");
	  fin = stdin;
	}

      if ((fout = fopen (argv[a + 1], "w")) == NULL)
	{
	  fprintf (stderr, "Cannot open output file, using stdout.\n");
	  fout = stdout;
	}
    }

  /* form nfc: join[b] is the byte of the letter that the byte b of a consonant and a nukta make, where unicode.h has a row for the letter
     (C6 and a nukta are C7, CF and a nukta are D0), or -1 */
  for (i = 0; i < 256; i++)
    join[i] = -1;
  for (j = 0; j < NUKTA_LEN; j++)
    if (nukta_hin[j][4] == 1 && (i = nukta_acii_of (nukta_hin[j][2], nukta_hin[j][3])) >= 0
	&& (k = nukta_acii_of (nukta_hin[j][0], nukta_hin[j][1])) >= 0)
      join[i] = k;

  while (!feof (fin))
    {
      t1 = fgetc (fin);
      if (feof (fin))
	break;
      t2 = fgetc (fin);
      if (feof (fin))
	break;

      if (t1 == 255 && t2 == 254)
	continue;		/*eat the byte order control */

      if (t1 == 13 && t2 == 0)
	continue;		/*eat cr */

      tmp[0] = tmp[2];
      tmp[1] = tmp[3];
      tmp[2] = t1;
      tmp[3] = t2;

      if (held >= 0)
	{
	  if (t1 == NUKTA_SIGN_LOW && t2 == NUKTA_SIGN_HIGH)
	    {
	      fputc (join[held], fout);	/* the consonant and the nukta: one byte */
	      held = -1;
	      continue;
	    }
	  fputc (held, fout);	/* no nukta follows: the consonant goes out as it always did */
	  held = -1;
	}

      n = bytes_of (t1, t2, out, &kind);
      if (kind == KIND_LOW && warn && (t2 != 0 || t1 > 127))
	report (t1, t2);
      if (nukta_form == NUKTA_NFC && kind == KIND_ROW && join[out[0]] >= 0)
	{
	  held = out[0];	/* wait for the next code unit: is it the nukta? */
	  continue;
	}
      for (i = 0; i < n; i++)
	fputc (out[i], fout);
    }
  if (held >= 0)
    fputc (held, fout);
  if (warn && reported > 0)
    fprintf (stderr, "uni2acii: %d code point%s with no ACII byte %s written as %s (%d further occurrence%s not listed)\n", reported,
	     reported == 1 ? "" : "s", reported == 1 ? "was" : "were", reported == 1 ? "its low byte" : "low bytes", repeated,
	     repeated == 1 ? "" : "s");

  fclose (fin);
  fclose (fout);

  return 0;
}
'''

ENTRIES_ACII2UNI = r'''	08-Nov-2026, The forms (asis, nfc, nfd): -f, ROMENAGRI_NUKTA_FORM, -DNUKTA_FORM; the default is the old output, see TRANSLITERATION.md, section 15;
	              asis, the default, is what the converter always wrote; nfc and nfd are Unicode's two forms; a nukta letter is a consonant and
	              a nukta in every form; NUKTA_REBUILD is gone, see TRANSLITERATION.md, section 15,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

	05-Nov-2026, The nukta layer: a consonant byte followed by the nukta byte can be written as the one code point that nukta.h lists
	              (new header nukta.h), see TRANSLITERATION.md, section 15,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

'''

CODE_ACII2UNI = r'''
#include <stdio.h>
#include <fcntl.h>

#include "unicode.h"
#include "nukta.h"

static void
usage (void)
{
  printf ("Usage: acii2uni [-f asis|nfc|nfd] [<ISCII_filename> <UNICODE_filename>]\n");
  printf ("  -f FORM, --form=FORM   how a letter with a nukta is written: asis (the default), nfc or nfd\n");
  printf ("The environment variable ROMENAGRI_NUKTA_FORM does the same; a flag wins.\n");
}

/* writes the byte t as this converter always has: the code point of its row in unicode.h, else t mod 128 as an ASCII character;
   in the form nfd a letter of nukta.h (C7 and D0 have a row) goes out as its consonant and U+093C */
static void
put (unsigned char t, FILE * fout)
{
  int i, j;

  for (i = 0; i < UNI_LEN; i++)
    if (t == unicode_hin[i][2])
      {
	if (nukta_form == NUKTA_NFD && (j = nukta_row_of (unicode_hin[i][0], unicode_hin[i][1])) >= 0)
	  {
	    fputc (nukta_hin[j][2], fout);
	    fputc (nukta_hin[j][3], fout);
	    fputc (NUKTA_SIGN_LOW, fout);
	    fputc (NUKTA_SIGN_HIGH, fout);
	    return;
	  }
	fputc (unicode_hin[i][0], fout);
	fputc (unicode_hin[i][1], fout);
	return;
      }
  fputc (t % 128, fout);
  fputc (0, fout);
}

int
main (int argc, char *argv[])
{
  FILE *fin, *fout;
  unsigned char t;
  int i = 0, j, a, held = -1, fold[256];	/* held: a consonant byte that waits for a nukta (form nfc) */

#ifdef __DJGPP
  _fmode = O_BINARY;
#endif

  if ((a = nukta_options ("acii2uni", argc, argv, NULL)) < 0)
    {
      usage ();
      return 1;
    }

  if (argc - a < 1)
    {
      fin = stdin;
      fout = stdout;
    }
  else
    {
      if (argc - a < 2)
	{
	  usage ();
	  return 1;
	}


      if ((fin = fopen (argv[a], "r+")) == NULL)
	{
	  fprintf (stderr, "Cannot open input file, using stdin.\n");
	  fin = stdin;
	}

      if ((fout = fopen (argv[a + 1], "w")) == NULL)
	{
	  fprintf (stderr, "Cannot open output file, using stdout.\n");
	  fout = stdout;
	}
    }

  //byte order marker for utf16
  fputc (255, fout);
  fputc (254, fout);

  /* form nfc: fold[b] is the row of nukta_hin that the byte b of a consonant followed by NUKTA_BYTE becomes, if NFC composes the pair, or -1 */
  for (i = 0; i < 256; i++)
    fold[i] = -1;
  if (nukta_form == NUKTA_NFC)
    for (j = 0; j < NUKTA_LEN; j++)
      if (nukta_hin[j][4] == 1 && (i = nukta_acii_of (nukta_hin[j][2], nukta_hin[j][3])) >= 0)
	fold[i] = j;

  while (!feof (fin))
    {
      t = fgetc (fin);
      if (feof (fin))
	break;
      if (held >= 0)
	{
	  if (t == NUKTA_BYTE)
	    {
	      fputc (nukta_hin[fold[held]][0], fout);
	      fputc (nukta_hin[fold[held]][1], fout);
	      held = -1;
	      continue;
	    }
	  put (held, fout);	/* no nukta follows: the consonant goes out as it always did */
	  held = -1;
	}
      if (t == '\n')
	{
	  fputc (13, fout);
	  fputc (0, fout);
	  fputc (10, fout); //hmm... remove this and trust 'dos2unix'?
	  fputc (0, fout);
	  continue;
	}
      if (fold[t] >= 0)
	{
	  held = t;		/* wait for the next byte: is it the nukta? */
	  continue;
	}
      put (t, fout);
    }
  if (held >= 0)
    put (held, fout);

  fclose (fin);
  fclose (fout);

  return 0;
}
'''

OLD_CODE_SHA256 = {"uni2acii.c": "70ff616f69075f91f8261e2f43c6d223a2ab6bbf5c1e91a564a1bcc6e99aa438",
                   "acii2uni.c": "c2cef212ea50f859c64ac5840731bd2039ffa347daa7138facfababbb89df8b4"}
ENTRIES = {"uni2acii.c": ENTRIES_UNI2ACII, "acii2uni.c": ENTRIES_ACII2UNI}
CODE = {"uni2acii.c": CODE_UNI2ACII, "acii2uni.c": CODE_ACII2UNI}
assert all("\t" in s for s in list(ENTRIES.values()) + list(CODE.values()) + [NUKTA_H]), "the tabs of this file were changed to spaces"

for name in ("uni2acii.c", "acii2uni.c"):
    s = read(name)
    cut = s.index(END_MODS) + len(END_MODS)
    assert hashlib.sha256(s[cut:].encode("latin-1")).hexdigest() == OLD_CODE_SHA256[name], name + ": the code is not what patches 0001 and 0002 leave"
    s = sub1(s[:cut], OLD_COPY, NEW_COPY)
    s = sub1(s, ANCHOR_MOD, ENTRIES[name] + ANCHOR_MOD) + CODE[name]
    write(name, s)

# ---------------------------------------------------------------- Makefile: the new header is a dependency of the unicode target and is installed with the others
m = read("Makefile")
m = sub1(m, "#Copyright (C) 2004-2021 Abhishek Choudhary", "#Copyright (C) 1993-2026 Abhishek Choudhary")
m = sub1(m, "#  08-Jun-2021, Add cleanup code for generated binaries,\n",
         "#  " + MOD_DATE + ", Added nukta.h (the nukta layer of uni2acii and acii2uni) to the unicode target and to install and uninstall,\n"
         "#                 Abhishek Choudhary <obonac> (prepared with Claude),\n"
         "#                 a.choudhary@ieee.org\n#\n"
         "#  08-Jun-2021, Add cleanup code for generated binaries,\n")
m = sub1(m, "unicode: unicode.h acii2uni.c uni2acii.c\n", "unicode: unicode.h nukta.h acii2uni.c uni2acii.c\n")
m = sub1(m, "\tinstall unicode.h $(INSTROOT)$(INCDIR)/unicode.h\n",
         "\tinstall unicode.h $(INSTROOT)$(INCDIR)/unicode.h\n\tinstall nukta.h $(INSTROOT)$(INCDIR)/nukta.h\n")
m = sub1(m, "\trm $(INSTROOT)$(INCDIR)/unicode.h\n", "\trm $(INSTROOT)$(INCDIR)/unicode.h\n\trm $(INSTROOT)$(INCDIR)/nukta.h\n")
write("Makefile", m)
print("nukta layer applied to", d)

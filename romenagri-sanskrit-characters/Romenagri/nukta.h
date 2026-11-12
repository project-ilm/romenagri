/*
Copyright (C) 1993-2026 Abhishek Choudhary
This file is part of the Romenagri Transliteration System.

The Romenagri Transliteration System is free software; 
you can redistribute it and/or modify it under the terms of the 
GNU General Public License as published by the 
Free Software Foundation; either version 2 of the License, or 
(at your option) any later version.

The Romenagri Transliteration System is distributed in the hope 
that it will be useful, but WITHOUT ANY WARRANTY; without 
even the implied warranty of MERCHANTABILITY or FITNESS FOR 
A PARTICULAR PURPOSE. See the GNU General Public License for 
more details.

You should have received a copy of the GNU General Public
License along with this file; see the file COPYING. If
not, write to the Free Software Foundation,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
*/

/*
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

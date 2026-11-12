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

	08-Nov-2026, The forms (asis, nfc, nfd) and the warning layer: -f, ROMENAGRI_NUKTA_FORM, -w, see TRANSLITERATION.md, section 15;
	              asis, the default, is what the converter always wrote; nfc and nfd are Unicode's two forms; a nukta letter is a consonant and
	              a nukta in every form; NUKTA_REBUILD is gone, see TRANSLITERATION.md, section 15,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

	05-Nov-2026, The nukta layer: a precomposed nukta letter that unicode.h has no row for is written as its consonant
	              and the nukta byte (new header nukta.h), see TRANSLITERATION.md, section 15,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

	19-Jan-2006, Added the modifications section,
                        Abhishek Choudhary <hi_pedler>,
			choudhary@indicybers.net

End of modifications.
*/

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

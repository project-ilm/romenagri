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

	08-Nov-2026, The forms (asis, nfc, nfd): -f, ROMENAGRI_NUKTA_FORM, -DNUKTA_FORM; the default is the old output, see TRANSLITERATION.md, section 15;
	              asis, the default, is what the converter always wrote; nfc and nfd are Unicode's two forms; a nukta letter is a consonant and
	              a nukta in every form; NUKTA_REBUILD is gone, see TRANSLITERATION.md, section 15,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

	05-Nov-2026, The nukta layer: a consonant byte followed by the nukta byte can be written as the one code point that nukta.h lists
	              (new header nukta.h), see TRANSLITERATION.md, section 15,
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

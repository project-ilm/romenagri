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

	26-Oct-2026, Guards: a letter that needs a partner is plain text when an underscore or the end follows
	              (level1 c, level2b v, level2c e y o n r j, matra e o _), new helper no_partner(),
	              see TRANSLITERATION.md, section 14.7,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

	19-Oct-2026, Parser branches for _li _lee _ree _om _vd _vua _vna _vga _vca,
	              new helper vocalic(), see TRANSLITERATION.md,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

	19-Jan-2006, Added the modifications section,
                        Abhishek Choudhary <hi_pedler>,
			choudhary@indicybers.net

End of modifications.
*/

#include "rmn2acii.h"
char tst2[2];
char *tst = tst2;
char *lev1 = "|kgcjtdnpbmyrlwsxh_^";

char *
c2s (char t)
{
  tst[0] = t;
  tst[1] = '\0';
  return tst;
}

char *
lookup (char *key)
{
  int i;
  for (i = 0; i < ACII_LEN; i++)
    {
      if (strcmp (acii_chrt[i][0], key) == 0)
	return acii_chrt[i][1];
    }
  return NULL; // returning NULL here causes seg fault. TBD - fix architecture
}

/* A vowel that has an independent byte and a dependent (matra) byte and is written the same way
   in Romenagri.  After a consonant the parser has just emitted a halant; that halant is replaced
   by the matra byte (consonant + "_ri" is consonant + sign RI) -- the 'push-pop' of "_ri". */
static void
vocalic (char *indep, char *dep)
{
  if (strlen (msg) > 0 && msg[strlen (msg) - 1] == *lookup ("^"))
    {
      msg[strlen (msg) - 1] = '\0';
      strcat (msg, lookup (dep));
    }
  else
    strcat (msg, lookup (indep));
}

/* The guards of TRANSLITERATION.md, section 14.7.  The branches below that jump over, or keep as plain text, the character after
   their letter without looking at it (the 'h' of "ch", the 'r' of "vra", the second 'e' of "_ee", the 'n' of "_yna", the two
   letters of "_ri" ...) must not take an underscore, which belongs to the next unit or to a "__" pair, nor step over the end of
   the string.  no_partner() is true for those two characters; a letter that is followed by one of them has no partner. */
static int
no_partner (char next)
{
  return next == '_' || next == '\0';
}

int
matra (char *tok)
{
  if (strlen (tok) < 1)
    {
      strcat (msg, lookup ("^"));	/*terminating 'halant' */
      return 1;
    }
  switch (tok[0])
    {
    case 'i':
      strcat (msg, lookup ("^i"));
      tok++;
      level1 (tok);
      break;
    case 'u':
      strcat (msg, lookup ("^u"));
      tok++;
      level1 (tok);
      break;
    case 'e':
      if (no_partner (tok[1]))	/* an 'e' with no second 'e' */
        {
          strcat (msg, c2s (tok[0]));
          level1 (++tok);
          break;
        }
      strcat (msg, lookup ("^ee"));
      tok += 2;
      level1 (tok);
      break;
    case 'z':
      strcat (msg, lookup ("^za"));
      level2a (++tok);
      break;
    case '_':			/*redundant */
      if (tok[1] == 'l' && tok[2] == 'i')
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
      else if (no_partner (tok[1]) || no_partner (tok[2]))	/* "_ri" with an underscore or the end where "ri" should be: */
        {
        }						/* the underscore is read again, as the start of the next unit */
      else
        {
          strcat (msg, lookup ("^_ri"));
          tok += 3;
        }
      level1 (tok);
      break;
    case 'o':
      if (no_partner (tok[1]))	/* an 'o' with nothing after it */
        {
          strcat (msg, c2s (tok[0]));
          level1 (++tok);
          break;
        }
      tok++;
      switch (tok[0])
	{
	case 'o':
	  strcat (msg, lookup ("^oo"));
	  tok++;
	  level1 (tok);
	  break;
	case 'w':
	  strcat (msg, lookup ("^ow"));
	  tok++;
	  level1 (tok);
	  break;
	case 'a':
	  strcat (msg, lookup ("^oa"));
	  tok++;
	  level1 (tok);
	  break;
	case 'u':
	  strcat (msg, lookup ("^ou"));
	  tok++;
	  level1 (tok);
	  break;
	default:
	  strcat (msg, c2s (tok[0]));
	  level1 (++tok);
	};
      break;
    case 'a':
      tok++;
      if (strstr (lev1, c2s (tok[0])) != NULL)
	level1 (tok);
      else
	switch (tok[0])
	  {
	  case 'a':
	    strcat (msg, lookup ("^aa"));
	    tok++;
	    level1 (tok);
	    break;
	  case 'e':
	    tok++; //^ae or ^aee
	    /*strcat (msg, lookup ("^ae"));
	    level1 (tok);
	    break;*/
            switch (tok[0])
      	    {
		  case 'e':
		    strcat (msg, lookup ("^aee"));
		    level1 (++tok);
		    break;
		  default:
		    strcat (msg, lookup ("^ae"));
		    level1 (tok);
	    }
	    break;
	  case 'i':
	    strcat (msg, lookup ("^ai"));
	    tok++;
	    level1 (tok);
	    break;
	  case 'o':
	    strcat (msg, lookup ("^ao"));
	    tok++;
	    level1 (tok);
	    break;
	  case 'u':
	    strcat (msg, lookup ("^au"));
	    tok++;
	    level1 (tok);
	    break;
	  default:
	    strcat (msg, c2s (tok[0]));
	    level1 (++tok);
	  };
      break;
    default:
      strcat (msg, c2s (tok[0]));
      level1 (++tok);
    };
  return 1;
}

//Constant attached matra evaluation
//Schwa deletion is not supported for phonetic accuracy
//e.g. if at the end of the token then halant is appended
//else - rest of the token is dropped to level 1
//Note: Level 1 corresponds to first set
int level2a (char *tok)
{
  if (strlen (tok) < 1)
    {
      strcat (msg, lookup ("^"));
      return 1;
    }
  if (strstr (lev1, c2s (tok[0])) != NULL)
    {
      strcat (msg, lookup ("^"));
      level1 (tok);
    }
  else
    matra (tok);
  return 1;
}

int level2b (char *tok, char *lk)
{
  char lup[7];
  strcpy (lup, lk);
  if (strlen (tok) < 1)
    {
      strcat (lup, "a");
      strcat (msg, lookup (lup));
      strcat (msg, lookup ("^"));
      return 1;
    }
  if (tok[0] == 'h')
    {
      strcat (lup, "ha");
      strcat (msg, lookup (lup));
      level2a (++tok);
    }
  else if (tok[0] == 'v' && !no_partner (tok[1]))	/*lvra-case */
    {
      strcat (lup, "vra");
      strcat (msg, lookup (lup));
      level2a ((tok + 2));
    }
  else
    {
      strcat (lup, "a");
      strcat (msg, lookup (lup));
      level2a (tok);
    }
  return 1;
}

//Process homophones
int level2c (char *tok)
{
  if (strlen (tok) < 1)
    {
      strcat (msg, lookup ("^"));
      return 1;
    }
  switch (tok[0])
    {
    case 's': //avagraha _s -- no schwa / pictographic... TBD phonetic rules
      strcat (msg, lookup ("_s"));
      tok++;
      level1 (tok);
      break;
    case 'u':
      strcat (msg, lookup ("_u"));
      tok++;
      level1 (tok);
      break;
    case 'm':
      strcat (msg, lookup ("_m"));
      tok++;
      level1 (tok);
      break;
    case 'i':
      strcat (msg, lookup ("_i"));
      tok++;
      level1 (tok);
      break;
    case 'e':
      if (no_partner (tok[1]))	/* '_e' with no second 'e' */
        {
          strcat (msg, c2s (tok[0]));
          level1 (++tok);
          break;
        }
      strcat (msg, lookup ("_ee"));
      tok += 2;
      level1 (tok);
      break;
    case 'y':
      if (no_partner (tok[1]))	/* '_y' with no 'n' */
        {
          strcat (msg, c2s (tok[0]));
          level1 (++tok);
          break;
        }
      strcat (msg, lookup ("_yna"));
      tok++;
      level2a (++tok);
      break;
    case 't':
      level2b (++tok, "_t");
      break;
    case 'd':
      level2b (++tok, "_d");
      break;
    case 'h':
      if (tok[1] == 'h')
	{
	  strcat (msg, lookup ("_hh"));
	  tok++;
	  level1 (++tok);
	}
      else
	{
	  strcat (msg, lookup ("_ha"));
	  level2a (++tok);
	}
      break;
    case 'o':
      if (no_partner (tok[1]))	/* '_o' with nothing after it */
        {
          strcat (msg, c2s (tok[0]));
          level1 (++tok);
          break;
        }
      tok++;
      switch (tok[0])
	{
	case 'o':
	  strcat (msg, lookup ("_oo"));
	  tok++;
	  level1 (tok);
	  break;
	case 'w':
	  strcat (msg, lookup ("_ow"));
	  tok++;
	  level1 (tok);
	  break;
	case 'a':
	  strcat (msg, lookup ("_oa"));
	  tok++;
	  level1 (tok);
	  break;
	case 'u':
	  strcat (msg, lookup ("_ou"));
	  tok++;
	  level1 (tok);
	  break;
	case 'm':			/* _om: OM */
	  strcat (msg, lookup ("_om"));
	  tok++;
	  level1 (tok);
	  break;
	default:
	  strcat (msg, c2s (tok[0]));
	  level1 (++tok);
	};
      break;
    case 'n':
      if (no_partner (tok[1]))	/* '_n' with nothing after it */
        {
          strcat (msg, c2s (tok[0]));
          level1 (++tok);
          break;
        }
      tok++;
      switch (tok[0])
	{
	case 'a':
	  strcat (msg, lookup ("_na"));
	  tok++;
	  level1 (tok);
	  break;
	case 'n':
	  strcat (msg, lookup ("_nna"));
	  level2a (++tok);
	  break;
	case 'g':
	  strcat (msg, lookup ("_nga"));
	  level2a (++tok);
	  break;
	case 'z':
	  strcat (msg, lookup ("_nza"));
	  level2a (++tok);
	  break;
	default:
	  strcat (msg, c2s (tok[0]));
	  level1 (++tok);
	};
      break;
    case 'r':
      if (no_partner (tok[1]))	/* '_r' with nothing after it */
        {
          strcat (msg, c2s (tok[0]));
          level1 (++tok);
          break;
        }
      tok++;
      switch (tok[0])
	{
	case 'i':/*_ri*/
	  if (strlen (msg) > 0 && msg[strlen (msg) - 1] == *lookup ("^"))	/*push-pop */
	    {
	      msg[strlen (msg) - 1] = '\0';
	      strcat (msg, lookup ("^_ri"));
	    }
	  else
	    strcat (msg, lookup ("_ri"));
	  tok++;
	  level1 (tok);
	  break;
	case 'd':
	  level2b (++tok, "_rd");
	  break;
	case 'r':
	  level2b (++tok, "_rr");
	  break;
	case 'e':			/* _ree: vocalic RR, or its sign after a consonant */
	  if (tok[1] == 'e')
	    {
	      vocalic ("_ree", "^_ree");
	      tok += 2;
	      level1 (tok);
	    }
	  else
	    {
	      strcat (msg, c2s (tok[0]));
	      level1 (++tok);
	    }
	  break;
	default:
	  strcat (msg, c2s (tok[0]));
	  level1 (++tok);
	};
      break;
    case 'a':
      tok++;
      if (strstr (lev1, c2s (tok[0])) != NULL)
	{
	  strcat (msg, lookup ("_a"));
	  level1 (tok);
	}
      else
	switch (tok[0])
	  {
	  case 'a':
	    strcat (msg, lookup ("_aa"));
	    tok++;
	    level1 (tok);
	    break;
	  case 'e':
	    tok++; //_ae or _aee
	    /*strcat (msg, lookup ("_ae"));
	    level1 (tok);
	    break;*/
            switch (tok[0])
      	    {
		  case 'e':
		    strcat (msg, lookup ("_aee"));
		    level1 (++tok);
		    break;
		  default:
		    strcat (msg, lookup ("_ae"));
		    level1 (tok);
	    }
	    break;
	  case 'i':
	    strcat (msg, lookup ("_ai"));
	    tok++;
	    level1 (tok);
	    break;
	  case 'o':
	    strcat (msg, lookup ("_ao"));
	    tok++;
	    level1 (tok);
	    break;
	  case 'u':
	    strcat (msg, lookup ("_au"));
	    tok++;
	    level1 (tok);
	    break;
	  default:
	    strcat (msg, c2s (tok[0]));
	    level1 (++tok);
	  };
      break;
    case 'j':
      if (no_partner (tok[1]))	/* '_j' with nothing after it */
        {
          strcat (msg, c2s (tok[0]));
          level1 (++tok);
          break;
        }
      tok++;
      switch (tok[0])
	{
	/*case 'a':
	  strcat (msg, lookup ("_na"));
	  tok++;
	  level1 (tok);
	  break;*/
	case 'z':
	  strcat (msg, lookup ("_jza"));
	  level2a (++tok);
	  break;
	default:
	  strcat (msg, c2s (tok[0]));
	  level1 (++tok);
	};
      break;
      	
      
    case 'l':            /* _li: vocalic L, _lee: vocalic LL (or their signs after a consonant) */
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
    default:
      strcat (msg, c2s (tok[0]));
      level1 (++tok);
    }
  return 1;
}

int
level1 (char *tok)
{
  if (strlen (tok) < 1)
    return 1;
  switch (tok[0])
    {
    case '|':
      strcat (msg, lookup ("|"));
      tok++;
      level1 (tok);
      break;
    case 'n':
      strcat (msg, lookup ("na"));
      level2a (++tok);
      break;
    case 'm':
      strcat (msg, lookup ("ma"));
      level2a (++tok);
      break;
    case 'y':
      strcat (msg, lookup ("ya"));
      level2a (++tok);
      break;
    case 'w':
      strcat (msg, lookup ("wa"));
      level2a (++tok);
      break;
    case 'x':
      strcat (msg, lookup ("xa"));
      level2a (++tok);
      break;
      /*case 'h':
         strcat(msg,lookup("ha"));
         level2a(++tok);
         break; */
    case 'r':
      strcat (msg, lookup ("ra"));
      level2a (++tok);
      break;
    case 'g':
      level2b (++tok, "g");
      break;
    case 'c':
      if (no_partner (tok[1]))	/* a 'c' with no 'h' after it */
        {
          strcat (msg, c2s (tok[0]));
          level1 (++tok);
          break;
        }
      tok++;
      level2b (++tok, "ch");
      break;
    case 't':
      level2b (++tok, "t");
      break;
    case 'd':
      level2b (++tok, "d");
      break;
    case 'p':
      level2b (++tok, "p");
      break;
    case 'b':
      level2b (++tok, "b");
      break;
    case 's':
      level2b (++tok, "s");
      break;
    case 'l':
      level2b (++tok, "l");
      break;
    case 'k':
      level2b (++tok, "k");
      break;
    case 'j':
      level2b (++tok, "j");
      break;
    case '_':
      level2c (++tok);
      break;
    case '^':			/*discrete 'matra' */
      matra (++tok);
      break;
    default:
      strcat (msg, c2s (tok[0]));
      level1 (++tok);
    };
  return 1;
}

char *
rmn2acii (char *tok)
{
  *msg = '\0';
  level1 (tok);
  return msg;
}


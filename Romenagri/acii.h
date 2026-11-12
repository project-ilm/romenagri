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

	19-Oct-2026, Added 12 Sanskrit characters to the ACII<->Romenagri table;
	              avagraha string changed from _3 to _s, see TRANSLITERATION.md,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

	15-Jul-2021, Added the modifications section,
                        Abhishek Choudhary <obonac>,
                        a.choudhary@ieee.org

	19-Jan-2006, Added the modifications section,
                        Abhishek Choudhary <obonac>,
                        a.choudhary@ieee.org

End of modifications.
*/
	
/* ACII to romenagri conversion table */

/** IMPORTANT change on ^a (matra '^a') --  17-mar-2004*/
/** change undone */
/* however the bug remains that rmn='^a' is matched on empty string*/

#ifndef __ACII_H__
#define __ACII_H__
#define ACII_LEN 96

#ifdef __cplusplus
   extern "C" {
#endif



static char *acii_chrt[ACII_LEN][2]=
{
{"",    "ïB"},           /*control should be at index 0*/
{"__",   "_"},           /*expand control underscore*/
{"_a",   "¤"},
{"^a",    ""},           /*maatra 'a' is invisible in acii*/
{"_aa",  "¥"},
{"^aa",  "Ú"},
{"_i",   "¦"},
{"^i" ,  "Û"},
{"_ee",  "§"},
{"^ee",  "Ü"},
{"_u",   "¨"},
{"^u",   "Ý"},
{"_oo",  "©"},
{"^oo",  "Þ"},
{"_ri",  "ª"},
{"^_ri", "ß"},
{"_ae",  "«"},
{"^ae",  "à"},
{"_aee", "¬"},
{"^aee", "á"},
{"_ai",  "­"},  //\xAC :)
{"^ai",  "â"},
{"_ow",  "¯"},
{"^ow",  "ä"},
{"_oa",  "°"},
{"^oa",  "å"},
{"_ou",  "±"},
{"^ou",  "æ"},
{"_au",  "²"},
{"^au",  "ç"},
{"_ao",  "®"},
{"^ao",  "ã"},
{"ka",   "³"},
{"kha",  "´"},
{"ga",   "µ"},
{"gha",  "¶"},
{"_nga", "·"},
{"cha",  "¸"},
{"chha", "¹"},
{"ja",   "º"},
{"jha",  "»"},
{"_yna", "¼"},
{"ta",   "½"},
{"tha",  "¾"},
{"da",   "¿"},
{"dha",  "À"},
{"_nna", "Á"},
{"_ta",  "Â"},
{"_tha", "Ã"},
{"_da",  "Ä"},
{"_dha", "Å"},
{"na",   "Æ"},
{"pa",   "È"},
{"pha",  "É"},
{"ba",   "Ê"},
{"bha",  "Ë"},
{"ma",   "Ì"},
{"ya",   "Í"},
{"ra",   "Ï"},
{"_rra", "Ð"},
{"la",   "Ñ"},
{"wa",   "Ô"},
{"lvra", "Ò"},
{"sha",  "Õ"},
{"xa",   "Ö"},
{"sa",   "×"},
{"_ha",  "Ø"},
{"_m",   "¢"},    /*only for trailing bindu else find warg*/
{"_hh",  "£"},
{"_na",  "¡"},
{"^za",  "é"},
{"|",    "ê"},
{"^",    "è"},
{"_rda",  "¿é"},
{"_rdha", "Àé"},
{"^ra",   "èÏ"},
{"r",     "Ïè"},
{"kxa",  "³èÖ"},
{"_tra", "ÂèÏ"},
{"j_yna","ºè¼"},  /*correct to g_yna*/
{"shra", "ÕèÏ"},
{"_jza", "€"}, // \u0979 placed at \x80
{"_nza","Ç"},
{"_s","\xEB"}, //Avagraha. Was "_3": a digit never reaches the rmn2acii parser. "_s" is the branch level2c already had.
/* Sanskrit additions (see TRANSLITERATION.md). Strings use only [a-z_]; a leading '^' marks the dependent (matra) form. */
{"_li",     "\x81"}, //U+090C VOCALIC L
{"_lee",    "\x82"}, //U+0961 VOCALIC LL
{"_ree",    "\x83"}, //U+0960 VOCALIC RR
{"^_li",    "\x84"}, //U+0962 VOWEL SIGN VOCALIC L
{"^_lee",   "\x85"}, //U+0963 VOWEL SIGN VOCALIC LL
{"^_ree",   "\x86"}, //U+0944 VOWEL SIGN VOCALIC RR
{"_vd",     "\x87"}, //U+0965 DOUBLE DANDA
{"_vua",    "\x88"}, //U+0951 STRESS SIGN UDATTA
{"_vna",    "\x89"}, //U+0952 STRESS SIGN ANUDATTA
{"_vga",    "\x8A"}, //U+0953 GRAVE ACCENT
{"_vca",    "\x8B"}, //U+0954 ACUTE ACCENT
{"_om",     "\x8C"} //U+0950 OM
};

#ifdef __cplusplus
   }
#endif

#endif


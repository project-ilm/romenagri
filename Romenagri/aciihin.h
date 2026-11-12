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

	19-Oct-2026, Added 12 Sanskrit characters to the saral table,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

	19-Jan-2006, Added the modifications section,
                        Abhishek Choudhary <hi_pedler>,
			choudhary@indicybers.net

End of modifications.
*/
	
/* ACII to romenagri(saral) conversion table */

#ifndef __ACIIHIN_H__
#define __ACIIHIN_H__
#define ACII_HIN_LEN 87

#ifdef __cplusplus
extern "C"
{
#endif



  static char *acii_hin_chrt[ACII_HIN_LEN][2] = {
    {"", "ïB"},
    {"a", "¤"},
    {"^a", ""},
    {"aa", "¥"},
    {"^aa", "Ú"},
    {"i", "¦"},
    {"^i", "Û"},
    {"i", "§"},
    {"^i", "Ü"},
    {"u", "¨"},
    {"^u", "Ý"},
    {"oo", "©"},
    {"^oo", "Þ"},
    {"ri", "ª"},
    {"^ri", "ß"},
    {"e", "¬"},
    {"^e", "á"},
    {"ai", "­"},
    {"^ai", "â"},
    {"o", "°"},
    {"^o", "å"},
    {"ou", "±"},
    {"^ou", "æ"},
    {"o", "²"},
    {"^o", "ç"},
    {"ao", "®"},
    {"^ao", "ã"},
    {"ka", "³"},
    {"kha", "´"},
    {"ga", "µ"},
    {"gha", "¶"},
    {"na", "·"},
    {"cha", "¸"},
    {"chha", "¹"},
    {"ja", "º"},
    {"jha", "»"},
    {"na", "¼"},
    {"ta", "½"},
    {"tha", "¾"},
    {"da", "¿"},
    {"dha", "À"},
    {"na", "Á"},
    {"ta", "Â"},
    {"tha", "Ã"},
    {"da", "Ä"},
    {"dha", "Å"},
    {"na", "Æ"},
    {"pa", "È"},
    {"pha", "É"},
    {"ba", "Ê"},
    {"bha", "Ë"},
    {"ma", "Ì"},
    {"ya", "Í"},
    {"ra", "Ï"},
    {"la", "Ñ"},
    {"wa", "Ô"},
    {"lvra", "Ò"},
    {"sha", "Õ"},
    {"sha", "Ö"},
    {"sa", "×"},
    {"ha", "Ø"},
    {"n", "¢"},
    {"h", "£"},
    {"n", "¡"},
    {"", "é"},
    {"|", "ê"},
    {"^", "è"},
    {"rda", "¿é"},
    {"rdha", "Àé"},
    {"^ra", "èÏ"},
    {"r", "Ïè"},
    {"ksha", "³èÖ"},
    {"tra", "ÂèÏ"},
    {"gya", "ºè¼"},
    {"shra", "ÕèÏ"},
    /* Sanskrit additions: one-way and lossy like the rest of this table (length is dropped, accents vanish) */
    {"lri", "\x81"}, //U+090C VOCALIC L
    {"lri", "\x82"}, //U+0961 VOCALIC LL
    {"ri", "\x83"}, //U+0960 VOCALIC RR
    {"^lri", "\x84"}, //U+0962 VOWEL SIGN VOCALIC L
    {"^lri", "\x85"}, //U+0963 VOWEL SIGN VOCALIC LL
    {"^ri", "\x86"}, //U+0944 VOWEL SIGN VOCALIC RR
    {"||", "\x87"}, //U+0965 DOUBLE DANDA
    {"", "\x88"}, //U+0951 STRESS SIGN UDATTA
    {"", "\x89"}, //U+0952 STRESS SIGN ANUDATTA
    {"", "\x8A"}, //U+0953 GRAVE ACCENT
    {"", "\x8B"}, //U+0954 ACUTE ACCENT
    {"om", "\x8C"} //U+0950 OM
  };

#ifdef __cplusplus
}
#endif


#endif

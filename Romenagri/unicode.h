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

	19-Oct-2026, Added 12 Sanskrit characters to the Unicode<->ACII table:
	              ACII bytes 0x81-0x8C, see TRANSLITERATION.md,
                        Abhishek Choudhary <obonac> (prepared with Claude),
                        a.choudhary@ieee.org

	19-Jan-2006, Added the modifications section,
                        Abhishek Choudhary <hi_pedler>,
			choudhary@indicybers.net

End of modifications.
*/
	
/* ACII to UNICODE conversion table */


#ifndef __UNICODE_H__
#define __UNICODE_H__


#ifdef __cplusplus
extern "C"
{
#endif


#define UNI_LEN 85

  unsigned char unicode_hin[UNI_LEN][3] = {
    {21, 9, '³'}, //1
    {22, 9, '´'},
    {23, 9, 'µ'},
    {24, 9, '¶'},
    {25, 9, '·'}, //5

    {26, 9, '¸'}, //6
    {27, 9, '¹'},
    {28, 9, 'º'},
    {29, 9, '»'},
    {30, 9, '¼'}, //10

    {31, 9, '½'}, //11
    {32, 9, '¾'},
    {33, 9, '¿'},
    {34, 9, 'À'},
    {35, 9, 'Á'}, //15

    {36, 9, 'Â'}, //16
    {37, 9, 'Ã'},
    {38, 9, 'Ä'},
    {39, 9, 'Å'},
    {40, 9, 'Æ'}, //20

    {41, 9, 'Ç'}, //21


    {42, 9, 'È'}, //22
    {43, 9, 'É'},
    {44, 9, 'Ê'},
    {45, 9, 'Ë'},
    {46, 9, 'Ì'}, //26

    {47, 9, 'Í'}, //27
    {48, 9, 'Ï'},
    {50, 9, 'Ñ'},
    {53, 9, 'Ô'},
    {54, 9, 'Õ'}, //31

    {55, 9, 'Ö'}, //32
    {56, 9, '×'},
    {57, 9, 'Ø'}, //34

    {2, 9, '¢'}, //35
    {3, 9, '£'},
    {1, 9, '¡'},
    {60, 9, 'é'}, //38

    {5, 9, '¤'}, //39
    {77, 9, 'è'}, //40

    {6, 9, '¥'}, //41
    {62, 9, 'Ú'},

    {7, 9, '¦'}, //43
    {63, 9, 'Û'},

    {8, 9, '§'}, //45
    {64, 9, 'Ü'},

    {9, 9, '¨'}, //46
    {65, 9, 'Ý'}, //47

    {10, 9, '©'}, //48
    {66, 9, 'Þ'},

    {11, 9, 'ª'}, //50
    {67, 9, 'ß'},

    {14, 9,  '«'}, //52
    {70, 9,  'à'},

    {15, 9, '¬'}, //54
    {71, 9, 'á'},

    {16, 9, '­'}, //56
    {72, 9, 'â'},

    {19, 9, '°'}, //58
    {75, 9, 'å'},

    {20, 9, '±'}, //60
    {76, 9, 'æ'},

    {13, 9, '®'}, //62
    {69, 9, 'ã'},

    {17, 9, '²'}, //64
    {73, 9, 'ç'},

    {51, 9, 'Ò'}, //66
    {100, 9, 'ê'},
    
    {121, 9, '€'}, //68: \u0979 placed at \x80
    
    {61, 9, 'ë'}, //69: avagraha

    {18, 9, '¯'}, //70
    {74, 9, 'ä'}, //71

    {49, 9, 'Ð'},

    //Sanskrit additions. 0x81-0x8C continue the ACII extension block that starts with U+0979 at 0x80.
    //OM is deliberately not at 0xA0, its slot in iscii_map.csv: uni2acii writes an unmapped U+00A0 (no-break space) as 0xA0. See TRANSLITERATION.md.
    {12, 9, '\x81'}, //U+090C VOCALIC L
    {97, 9, '\x82'}, //U+0961 VOCALIC LL
    {96, 9, '\x83'}, //U+0960 VOCALIC RR
    {98, 9, '\x84'}, //U+0962 VOWEL SIGN VOCALIC L
    {99, 9, '\x85'}, //U+0963 VOWEL SIGN VOCALIC LL
    {68, 9, '\x86'}, //U+0944 VOWEL SIGN VOCALIC RR
    {101, 9, '\x87'}, //U+0965 DOUBLE DANDA
    {81, 9, '\x88'}, //U+0951 STRESS SIGN UDATTA
    {82, 9, '\x89'}, //U+0952 STRESS SIGN ANUDATTA
    {83, 9, '\x8A'}, //U+0953 GRAVE ACCENT
    {84, 9, '\x8B'}, //U+0954 ACUTE ACCENT
    {80, 9, '\x8C'} //U+0950 OM

  };


#ifdef __cplusplus
}
#endif



#endif



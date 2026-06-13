/* substrate.h — compile-time substrate binding selector.
 * Default ISCII (2003 binding); -DROMENAGRI_SUBSTRATE_UNICODE for ISCII-free.
 * (C) 1993-2026 Abhishek Choudhary, GPL-3.0-or-later */
#ifndef ROMENAGRI_SUBSTRATE_H
#define ROMENAGRI_SUBSTRATE_H
#if defined(ROMENAGRI_SUBSTRATE_UNICODE)
#  include "acii_unicode.h"
#  ifndef __ACII_H__
#    define __ACII_H__            /* suppress the ISCII table */
#  endif
#  define ROMENAGRI_SUBSTRATE_NAME "unicode-utf8-devanagari"
#else
#  include "acii.h"
#  define ROMENAGRI_SUBSTRATE_NAME "iscii-derived"
#endif
#endif

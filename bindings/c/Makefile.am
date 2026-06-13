COMMON_SRC = acii2rmn.c rmn2acii.c stack.c
COMMON_HDR = substrate.h acii.h acii_unicode.h acii2rmn.h rmn2acii.h stack.h
lib_LIBRARIES =
check_PROGRAMS =
TESTS =
if BUILD_ISCII
lib_LIBRARIES += libromenagri_iscii.a
libromenagri_iscii_a_SOURCES = $(COMMON_SRC) $(COMMON_HDR)
libromenagri_iscii_a_CFLAGS  = -O2 -Wall -Wno-unused
check_PROGRAMS += rt_iscii
rt_iscii_SOURCES = test_roundtrip.c $(COMMON_SRC)
rt_iscii_CFLAGS  = -O2
TESTS += rt_iscii
endif
if BUILD_UNICODE
lib_LIBRARIES += libromenagri_unicode.a
libromenagri_unicode_a_SOURCES = $(COMMON_SRC) $(COMMON_HDR)
libromenagri_unicode_a_CFLAGS  = -O2 -Wall -Wno-unused -DROMENAGRI_SUBSTRATE_UNICODE
check_PROGRAMS += rt_unicode
rt_unicode_SOURCES = test_roundtrip.c $(COMMON_SRC)
rt_unicode_CFLAGS  = -O2 -DROMENAGRI_SUBSTRATE_UNICODE
TESTS += rt_unicode
endif
include_HEADERS = $(COMMON_HDR)

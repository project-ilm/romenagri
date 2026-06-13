AC_PREREQ([2.69])
AC_INIT([romenagri],[1.1.0],[a.choudhary@ieee.org])
AC_CONFIG_SRCDIR([rmn2acii.c])
AM_INIT_AUTOMAKE([foreign subdir-objects])
AC_PROG_CC
AC_PROG_RANLIB
AC_ARG_WITH([substrate],
  [AS_HELP_STRING([--with-substrate=@<:@iscii|unicode|both@:>@],
    [hub byte-encoding binding for the canonical Romenagri grammar (default: both)])],
  [substrate=$withval],[substrate=both])
AS_CASE([$substrate],
  [iscii],   [bi=yes; bu=no],
  [unicode], [bi=no;  bu=yes],
  [both],    [bi=yes; bu=yes],
  [AC_MSG_ERROR([--with-substrate must be iscii, unicode, or both])])
AM_CONDITIONAL([BUILD_ISCII],   [test "x$bi" = xyes])
AM_CONDITIONAL([BUILD_UNICODE], [test "x$bu" = xyes])
AC_MSG_NOTICE([Romenagri substrate binding(s): $substrate])
AC_MSG_NOTICE([canonical layer = 84-token Romenagri grammar; substrate = compile-time plug])
AC_CONFIG_FILES([Makefile])
AC_OUTPUT

/* Copyright (C) 1993-2026 Abhishek Choudhary
   SPDX-License-Identifier: GPL-2.0-or-later
   This file is part of the Romenagri Transliteration System; see the file COPYING.

   Library-level driver for the test suite.  One input line in, one line of lower-case hex out.

     harness            each line is a Romenagri string; prints the hex of rmn2acii(line), or SEGV
                        (if the environment variable RMN_TAIL is set, its first character is written into the rest of the 4,096-byte
                        buffer after the terminator before every call: a parser that reads past the end of its string then shows it,
                        because its output depends on RMN_TAIL; without it the rest of the buffer is whatever the previous line left)
     harness -r         each line is hex ACII;           prints the hex of acii2rmn(bytes), or SEGV
     harness -f         each line is hex ACII;           filter semantics: acii2rmn on the whole run, then rmn2acii on every
                        maximal [A-Za-z_] run (what acii2rmn.lex / rmn2acii.lex hand to the parser), other bytes pass through;
                        prints the hex of the result, or SEGV

   A crash inside the library (lookup() returning NULL, acii2rmn popping an empty stack) is caught and reported as SEGV so that a
   single bad input does not hide the rest.  Built three times by tests/build_trees.sh: against the old, the mid and the new librmnagri.a. */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>
#include <setjmp.h>
#include <unistd.h>
#include "acii2rmn.h"
#include "rmn2acii.h"

char msg2[10240], *msg = msg2;
static sigjmp_buf jb;
static void on_sig (int s) { siglongjmp (jb, 1); }

static void hex (const char *s) { for (; *s; s++) printf ("%02x", (unsigned char) *s); }

int main (int argc, char **argv)
{
  char line[4096], buf[4096];
  int rev = argc > 1 && strcmp (argv[1], "-r") == 0;
  int flt = argc > 1 && strcmp (argv[1], "-f") == 0;   /* filter semantics: ACII hex in -> acii2rmn -> rmn2acii on [A-Za-z_] runs only */
  char tail = getenv ("RMN_TAIL") ? getenv ("RMN_TAIL")[0] : 0;
  signal (SIGSEGV, on_sig);
  signal (SIGALRM, on_sig);
  while (fgets (line, sizeof line, stdin))
    {
      size_t n = strlen (line);
      while (n && (line[n - 1] == '\n' || line[n - 1] == '\r')) line[--n] = 0;
      stack_reset ();
      if (sigsetjmp (jb, 1)) { stack_reset (); puts ("SEGV"); continue; }
      alarm (2);
      if (flt)
        {
          size_t k = 0, i;
          char rmn[4096], res[8192];
          int ro = 0;
          for (i = 0; i + 1 < n; i += 2) { unsigned v; sscanf (line + i, "%2x", &v); buf[k++] = (char) v; }
          buf[k] = 0;
          strcpy (rmn, acii2rmn (buf));
          res[0] = 0;
          for (i = 0; rmn[i];)
            {
              if ((rmn[i] >= 'a' && rmn[i] <= 'z') || (rmn[i] >= 'A' && rmn[i] <= 'Z') || rmn[i] == '_')
                {
                  char run[1024];
                  size_t m = 0;
                  while ((rmn[i] >= 'a' && rmn[i] <= 'z') || (rmn[i] >= 'A' && rmn[i] <= 'Z') || rmn[i] == '_') run[m++] = rmn[i++];
                  run[m] = 0;
                  stack_reset ();
                  strcat (res, rmn2acii (run));
                }
              else { size_t l = strlen (res); res[l] = rmn[i++]; res[l + 1] = 0; }
            }
          hex (res); putchar ('\n');
        }
      else if (rev)
        {
          size_t k = 0;
          for (size_t i = 0; i + 1 < n; i += 2) { unsigned v; sscanf (line + i, "%2x", &v); buf[k++] = (char) v; }
          buf[k] = 0;
          hex (acii2rmn (buf)); putchar ('\n');
        }
      else
        {
          strcpy (buf, line);
          if (tail) memset (buf + n + 1, tail, sizeof buf - n - 1);
          hex (rmn2acii (buf)); putchar ('\n');
        }
      alarm (0);
    }
  return 0;
}

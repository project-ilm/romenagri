/* acii2rmn.c — substrate-generic forward encoder (longest-prefix match).
 * For the 1-byte ISCII binding this degenerates to the original byte matcher;
 * multi-byte ligature/Unicode entries match directly. Same stack rewrite:
 * matra pops the implicit schwa; za-family rewrites history. Grammar identical
 * to the 2003 acii2rmn.  (C) 1993-2026 Abhishek Choudhary, GPL-3.0-or-later */
#include <string.h>
#include "substrate.h"
#include "acii2rmn.h"

char *acii2rmn (char *tok)
{
  char t1, t2, tpush[2]; char *q;
  int i, j, best, blen;
  stack_reset ();
  for (i = 0; i < (int) strlen (tok); )
    {
      best = -1; blen = 0;
      for (j = 0; j < ACII_LEN; j++)
        {
          int Ln = (int) strlen (acii_chrt[j][1]);
          if (Ln > 0 && Ln > blen && strncmp (tok + i, acii_chrt[j][1], Ln) == 0)
            { best = j; blen = Ln; }
        }
      if (best >= 0)
        {
          j = best;
          if (*acii_chrt[j][0] == '^' && stack_len () > 0)   /* matra */
            {
              pop (1);
              if (*(acii_chrt[j][0] + 1) == 'z')
                {
                  q = pop (1); t1 = q ? *q : 0;
                  if (t1 == 'h')
                    {
                      q = pop (1); t2 = q ? *q : 0;
                      if (t2 == 'd') push ((char *) "_rdha");
                      else { tpush[0]=t2; tpush[1]='\0'; push (tpush); push ((char *) "hza"); }
                    }
                  else
                    {
                      if (t1 == 'd') push ((char *) "_rda");
                      else { tpush[0]=t1; tpush[1]='\0'; push (tpush); push ((char *) "za"); }
                    }
                }
              else push ((char *) (acii_chrt[j][0] + 1));
            }
          else push (acii_chrt[j][0]);
          i += blen;
        }
      else { tpush[0]=tok[i]; tpush[1]='\0'; push (tpush); i++; }
    }
  { char *p = pop (stack_len ()); strcpy (msg, p ? p : tok); }
  return msg;
}

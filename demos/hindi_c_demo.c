/* Hindi (Devanagari) — HPS/ILM localized C
   यदि = if | जबतक = while | लौटाओ = return | लिखो = printf
   © 1993-2026 Abhishek Choudhary, GPL */
#include <stdio.h>
#define यदि if
#define जबतक while
#define लौटाओ return
#define लिखो printf
#define पूर्णांक int

int main(void) {
  int n = 0;
  जबतक (n < 5) {
    यदि (n % 2 == 0)
      लिखो("%d\n", n);
    n++;
  }
  लौटाओ 0;
}

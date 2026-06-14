/* zephyr_idiolect: native-language keywords via Romenagri ASCII-7 identifiers -> unmodified GCC */
#include <stdio.h>
#define zephif if
#define zephlo while
#define zephba return
#define zephnu int
#define zephsay printf
zephnu main(void){
  zephnu n=0;
  zephlo(n<3){ zephif(n%2==0) zephsay("%d ok\n",n); n++; }
  zephba 0;
}

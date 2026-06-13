#include <stdio.h>
#include <string.h>
#include "substrate.h"
static char msgbuf[65536]; char *msg=msgbuf;
extern char *acii2rmn(char*); extern char *rmn2acii(char*);
int main(void){
  const char *RMN[]={"karma","namastee","ki","kxa","shra","_tra","raama","wi_dyaa"};
  int n=8,pass=0;
  for(int t=0;t<n;t++){
    char a[512]; strcpy(a, rmn2acii((char*)RMN[t]));   /* RMN -> substrate bytes */
    char b[512]; strcpy(b, acii2rmn(a));               /* substrate -> RMN       */
    int ok=!strcmp(RMN[t],b); pass+=ok;
    printf("  [%s] %-10s ->(%zuB)-> %-10s %s\n",ROMENAGRI_SUBSTRATE_NAME,RMN[t],strlen(a),b,ok?"EXACT":"DIFF");
  }
  printf("substrate=%s roundtrip %d/%d\n",ROMENAGRI_SUBSTRATE_NAME,pass,n);
  return pass==n?0:1;
}

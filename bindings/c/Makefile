# Romenagri core library — Makefile
# Builds: libromenagri.a (static), romenagri (CLI), test harness
# © 1993-2026 Abhishek Choudhary, GPL-3.0-or-later

CC      = gcc
CFLAGS  = -O2 -Wall -Wno-unused -fwrapv
AR      = ar
SRCS    = acii2rmn.c rmn2acii.c stack.c
HDRS    = acii.h acii2rmn.h rmn2acii.h stack.h
OBJS    = $(SRCS:.c=.o)
LIB     = libromenagri.a
CLI_SRC = ../../src/main.c
TESTMSG = 'नमस्ते'

.PHONY: all clean test wasm

all: $(LIB) romenagri test

$(LIB): $(OBJS)
	$(AR) rcs $@ $^

%.o: %.c $(HDRS)
	$(CC) $(CFLAGS) -c -o $@ $

romenagri: $(LIB)
	@echo "/* CLI driver */" > _cli.c
	@echo '#include <stdio.h>' >> _cli.c
	@echo 'static char msgbuf[16384]; char *msg=msgbuf;' >> _cli.c
	@echo 'extern char *acii2rmn(char *tok);' >> _cli.c
	@echo 'int main(void){char tok[8192];' >> _cli.c
	@echo '  while(scanf("%8191s",tok)==1){char*r=acii2rmn(tok);printf("%s ",r?r:tok);}' >> _cli.c
	@echo '  printf("\n");return 0;}' >> _cli.c
	$(CC) $(CFLAGS) -o $@ _cli.c $(SRCS) && rm _cli.c

test: romenagri
	@echo "[TEST] sanity: नमस्ते"
	@printf $(TESTMSG) | iconv -f UTF-8 -t UTF-16LE > /tmp/_t.u16 2>/dev/null && \
	  ../../build/uni2acii /tmp/_t.u16 /tmp/_t.iscii 2>/dev/null && \
	  echo -n "  → " && ./romenagri < /tmp/_t.iscii || echo "  (uni2acii not built; run scripts/20_build.sh first)"

wasm:
	@echo "WASM build (requires emscripten):"
	@echo "  source /path/to/emsdk/emsdk_env.sh"
	@echo "  make -f Makefile.wasm"

clean:
	rm -f $(OBJS) $(LIB) romenagri _cli.c /tmp/_t.u16 /tmp/_t.iscii

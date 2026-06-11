# WASM build of the Romenagri kernel (requires emscripten; optional)
# emcc produces romenagri.wasm + JS glue exporting acii2rmn / rmn2acii.
SRC=../c/acii2rmn.c ../c/rmn2acii.c ../c/stack.c
wasm:
	emcc -O2 $(SRC) -o romenagri.js \
	 -sEXPORTED_FUNCTIONS=_acii2rmn,_rmn2acii \
	 -sEXPORTED_RUNTIME_METHODS=ccall,cwrap -sALLOW_MEMORY_GROWTH

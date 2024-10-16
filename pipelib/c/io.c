#include <stdio.h>

extern void print(const char *text) {
	printf("%s", text);
}

extern void println(const char *text) {
	printf("%s\n", text);
}

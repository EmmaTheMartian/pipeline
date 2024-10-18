#ifndef __clockwork_main_cpp__
#define __clockwork_main_cpp__

#include "generated/LanguageListener.h"
#include <cstdio>

class Visitor : LanguageListener
{
};

int main()
{
	std::printf("Hello, World!\n");
}

#endif

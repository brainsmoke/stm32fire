
#include <unistd.h>

#include "fire_ca.h"

int main(int argc, char *argv[])
{
	fire_init();

	for(;;)
	{
		fire_next();
		write(1, framebuf, N_BYTES);
	}
}

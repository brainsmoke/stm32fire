#ifndef FIRE_CA_H

#define WIDTH (12)
#define HEIGHT (10)

#define N_LEDS (WIDTH*HEIGHT)
#define N_BYTES (N_LEDS*3)

#define CA_WIDTH (WIDTH*2)
#define CA_HEIGHT (HEIGHT*2)
#define CA_SIZE (CA_WIDTH*CA_HEIGHT)
#define CA_BUFSIZE (CA_SIZE+CA_WIDTH)

#ifndef __ASSEMBLER__

#include <stdint.h>

extern uint8_t framebuf[N_BYTES];

void fire_init(void);
void fire_next(void);

#endif

#endif // FIRE_CA_H

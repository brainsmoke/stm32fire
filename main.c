
#include <stdlib.h>
#include "stm32f0xx.h"

#include "fire_ca.h"
#include "bitbang.h"
#include "util.h"

#define O(c) (1<<(2*c))
#define ALT_FN(c) (2<<(2*c))
#define SWD (ALT_FN(13)|ALT_FN(14))

void SysTick_Handler(void)
{
	bitbang(framebuf, N_BYTES, GPIOA);
	fire_next();
}

void init(void)
{
	clock48mhz();
	RCC->AHBENR |= RCC_AHBENR_GPIOAEN; 	// enable the clock to GPIOA
	GPIOA->ODR = 0;
	GPIOA->MODER = SWD|O(0)|O(1)|O(2)|O(3)|O(4)|O(5)|O(6)|O(7);
	enable_sys_tick(F_SYS_TICK_CLK/160);
}

int main(void)
{
	init();

	for(;;);

//for(;;){ bitbang(framebuf, N_BYTES, GPIOA); fire_next(); }

	return 0;
}


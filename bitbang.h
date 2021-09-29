#ifndef BITBANG_H
#define BITBANG_H

/* platform constants */

#define GPIO_ODR_OFFSET (0x14)
#define GPIO_BSRR_OFFSET (0x18)

/* registers */

#define rBUF   r0
#define rSIZE  r1
#define rGPIO  r2
#define rCLK   r3
#define rMASK  r4
#define rBYTE  r5
#define rOUT   r6
#define rTMP   r7

/* IO pins */

#define PIN_DATA (0)
#define PIN_CLK  (1)
#define MASK_DATA (1<<PIN_DATA)
#define MASK_CLK  (1<<PIN_CLK)

#ifndef __ASSEMBLER__

void bitbang(uint8_t *buf, uint32_t size, GPIO_TypeDef *gpio_out);

#endif

#endif // BITBANG_H

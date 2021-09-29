
#include <bitbang.h>

.include "m0delay.S"

	.cpu cortex-m0
	.fpu softvfp
	.section	.bss
	.thumb
	.section	.text.bitbang,"ax",%progbits
	.align	2
	.global	bitbang
	.code	16
	.thumb_func
	.type	bitbang, %function
bitbang:
	.syntax unified
	.thumb

push {r4-r7}

movs rCLK, #(MASK_CLK)
movs rMASK, #(MASK_DATA)

bitbang_loop:
/*  0 +  2   */ ldrb rBYTE, [rBUF]
/*  2 +  1   */ lsrs rOUT, rBYTE, #7
/*  3 +  1   */ ands rOUT, rMASK
/*  4 +  2   */ strb rOUT, [rGPIO, #GPIO_ODR_OFFSET]
/*  6 + 22   */ delay rTMP, 22
/* 28 +  2   */ str rCLK, [rGPIO, #GPIO_BSRR_OFFSET]
/* 30 + 18+2 */ delay rTMP, 20

/*  2 +  1   */ lsrs rOUT, rBYTE, #6
/*  3 +  1   */ ands rOUT, rMASK
/*  4 +  2   */ strb rOUT, [rGPIO, #GPIO_ODR_OFFSET]
/*  6 + 22   */ delay rTMP, 22
/* 28 +  2   */ str rCLK, [rGPIO, #GPIO_BSRR_OFFSET]
/* 30 + 18+2 */ delay rTMP, 20

/*  2 +  1   */ lsrs rOUT, rBYTE, #5
/*  3 +  1   */ ands rOUT, rMASK
/*  4 +  2   */ strb rOUT, [rGPIO, #GPIO_ODR_OFFSET]
/*  6 + 22   */ delay rTMP, 22
/* 28 +  2   */ str rCLK, [rGPIO, #GPIO_BSRR_OFFSET]
/* 30 + 18+2 */ delay rTMP, 20

/*  2 +  1   */ lsrs rOUT, rBYTE, #4
/*  3 +  1   */ ands rOUT, rMASK
/*  4 +  2   */ strb rOUT, [rGPIO, #GPIO_ODR_OFFSET]
/*  6 + 22   */ delay rTMP, 22
/* 28 +  2   */ str rCLK, [rGPIO, #GPIO_BSRR_OFFSET]
/* 30 + 18+2 */ delay rTMP, 20

/*  2 +  1   */ lsrs rOUT, rBYTE, #3
/*  3 +  1   */ ands rOUT, rMASK
/*  4 +  2   */ strb rOUT, [rGPIO, #GPIO_ODR_OFFSET]
/*  6 + 22   */ delay rTMP, 22
/* 28 +  2   */ str rCLK, [rGPIO, #GPIO_BSRR_OFFSET]
/* 30 + 18+2 */ delay rTMP, 20

/*  2 +  1   */ lsrs rOUT, rBYTE, #2
/*  3 +  1   */ ands rOUT, rMASK
/*  4 +  2   */ strb rOUT, [rGPIO, #GPIO_ODR_OFFSET]
/*  6 + 22   */ delay rTMP, 22
/* 28 +  2   */ str rCLK, [rGPIO, #GPIO_BSRR_OFFSET]
/* 30 + 18+2 */ delay rTMP, 20

/*  2 +  1   */ lsrs rOUT, rBYTE, #1
/*  3 +  1   */ ands rOUT, rMASK
/*  4 +  2   */ strb rOUT, [rGPIO, #GPIO_ODR_OFFSET]
/*  6 + 22   */ delay rTMP, 22
/* 28 +  2   */ str rCLK, [rGPIO, #GPIO_BSRR_OFFSET]
/* 30 + 18+2 */ delay rTMP, 20

/*  2 +  1   */ lsrs rOUT, rBYTE, #0
/*  3 +  1   */ ands rOUT, rMASK
/*  4 +  2   */ strb rOUT, [rGPIO, #GPIO_ODR_OFFSET]
/*  6 + 22   */ delay rTMP, 22
/* 28 +  2   */ str rCLK, [rGPIO, #GPIO_BSRR_OFFSET]
/* 30 +  9   */ delay rTMP, 20

/* 39 + 1     */ adds rBUF, rBUF, #1
/* 40 + 1     */ subs rSIZE, rSIZE, #1
/* 41 + 1|3   */ beq 0f
/* 42 + 3 + 3 */ b bitbang_loop
0:

/* 44 + 1     */ movs rOUT, #0
/* 45 + 3 + 4 */ delay rTMP, 7

/*  4 + 2     */ strb rOUT, [rGPIO, #GPIO_ODR_OFFSET]

pop {r4-r7}

bx lr

	.size	bitbang, .-bitbang


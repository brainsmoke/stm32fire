#!/usr/bin/env python3
#
# Copyright (c) 2020 Erik Bosman <erik@minemu.org>
#
# Permission  is  hereby  granted,  free  of  charge,  to  any  person
# obtaining  a copy  of  this  software  and  associated documentation
# files (the "Software"),  to deal in the Software without restriction,
# including  without  limitation  the  rights  to  use,  copy,  modify,
# merge, publish, distribute, sublicense, and/or sell copies of the
# Software,  and to permit persons to whom the Software is furnished to
# do so, subject to the following conditions:
#
# The  above  copyright  notice  and this  permission  notice  shall be
# included  in  all  copies  or  substantial portions  of the Software.
#
# THE SOFTWARE  IS  PROVIDED  "AS IS", WITHOUT WARRANTY  OF ANY KIND,
# EXPRESS OR IMPLIED,  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY,  FITNESS  FOR  A  PARTICULAR  PURPOSE  AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM,  DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT,  TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN
# CONNECTION  WITH THE SOFTWARE  OR THE USE  OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# (http://opensource.org/licenses/mit-license.html)

import sys, os, time, cmath

import pygame

WIDTH=12
HEIGHT=10

pos = [ None ] * 120

for y in range(HEIGHT):
    for x in range(WIDTH):
        if x & 1:
            pos[HEIGHT*x+y] = (2*(x+.5)/(WIDTH)-1,2*(y+.5)/(HEIGHT)-1)
        else:
            pos[HEIGHT*(x+1)-y-1] = (2*(x+.5)/(WIDTH)-1,2*(y+.5)/(HEIGHT)-1)

black = (0, 0, 0)

class Metronome(object):
    def __init__(self, fps):
        self.delay = 1./fps

    def start(self):
        self.last = time.time()

    def sync(self):
        now = time.time()
        if self.delay > now-self.last:
            time.sleep(self.delay - (now-self.last))
        self.last = max(now, self.last+self.delay)

class VirtualScreen(object):

    def recalc(self, w, h ):
        self.pos = [ ( int((1+x)*w/2), int((1+y)*h/2) ) for (x,y) in self.positions ]

    def __init__(self, positions, windowsize=(500, 500)):
        pygame.init()
        self.screen = pygame.display.set_mode(windowsize, pygame.RESIZABLE | pygame.DOUBLEBUF)
        self.screen.fill(black)
        self.positions = positions
        min_dim = min(windowsize)
        w,h= windowsize
        self.recalc(w,h)
        self.w = min_dim / 12.5

    def draw_led(self, surf, x, y, w, h, color):
        hindcolor = tuple( int(((x/255.)**.6) * 20) for x in color )
        midcolor = tuple( int(((x/255.)**.6) * 127.5) for x in color )
        ledcolor = tuple( min(255, int(((x/255.)**.6) * 765)) for x in color )

        for dim, bcolor in (1, hindcolor), (.4, midcolor), (.2, ledcolor):
            bx, by = int(x-(w*dim)/2), int(y-(w*dim)/2)
            bw, bh = int(w*dim), int(h*dim)
            pygame.draw.rect(surf, bcolor, pygame.Rect(bx, by, bw, bh))

    def draw(self):
        surf = pygame.display.get_surface()
        for i, (x, y) in enumerate(self.pos):
                self.draw_led(surf, x, y, self.w, self.w, self.buf[i*3:i*3+3])

    def check_events(self):
        for event in pygame.event.get():
            if event.type in (pygame.QUIT,):
                sys.exit(0)
            if event.type in (pygame.VIDEORESIZE,):
                self.screen = pygame.display.set_mode((event.w, event.h),
                        pygame.RESIZABLE | pygame.DOUBLEBUF)
                self.r = float(event.w) / 10
                self.recalc(event.w, event.h)

    def load_data(self, data):
        self.buf = data

    def push_data(self, data):
        self.load_data(data)
        self.push()

    def push(self):
        self.check_events()
        self.draw()
        pygame.display.flip()
        self.screen.fill(black)


s = VirtualScreen(windowsize=(600, 500), positions=pos)

fps = int( ( sys.argv[1:] + ['160'] )[0] )
metronome = Metronome(fps)
metronome.start()

while True:
	d = sys.stdin.buffer.read(len(pos)*3)
	if len(d) != len(pos)*3:
		break

	d = bytes( x for i in range(0,len(pos)*3,3) for x in (d[i+1],d[i],d[i+2]) )

	s.push_data(d)
	metronome.sync()

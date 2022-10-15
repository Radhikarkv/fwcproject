#!/bin/bash


#Download python and latex templates

#svn co https://github.com/gadepall/training/trunk/math  /sdcard/Download/math

#Test Latex Installation
#Uncomment only the following lines and comment the above line

#to run IDE programs

#cd /sdcard/download/radhika/IDE
#pio run

#cd /sdcard/download/radhika/IDE
#pdflatex assignment.tex
#termux-open assignment.pdf

# to run assembly codes

#cd /sdcard/download/radhika/assembly
#avra hello.asm
#avrdude -p atmega328p -c arduino -P /dev/ttyACM0 -b 115200 -U flash:w:hello.hex

#cd /sdcard/download/radhika/assembly
#pdflatex assembly.tex
#termux-open assembly.pdf

# to run avr-gcc

#cd /sdcard/download/radhika/avr-gcc
#make

#cd /sdcard/download/radhika/avr-gcc
#pdflatex avr.tex
#termux-open avr.pdf

#rjmp start
#Test Python Installation
#Uncomment only the following line
#python3 /sdcard/Download/anusha1/python1/asgn1.py

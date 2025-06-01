[BITS 32]

section .data
	main_bit dd 32

section .text
	global _start

_start:
	mov eax,[main_bit]


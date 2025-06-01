[BITS 64]

section .data
	main_bit dq 64

section .text
	global _start

_start:
	mov rax,[main_bit]


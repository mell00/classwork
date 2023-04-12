;;;
;;; CATCH SIGWINCH
;;;

section .data

struc sigaction_t
  sa_handler: resb 8
  sa_mask: resq 16 ;qword
  sa_flags: resd 4 ;integer
            resb 12
endstruc

SA_RESTART: equ 0x10000000
SIGWINCH:   equ 28

resize_msg: db  "Window resized!", 10, 0
window_change: db 0

act:
  istruc sigaction_t
      at sa_handler, dq my_handler
      at sa_mask, times 16 dq 0
      at sa_flags, dd SA_RESTART
  iend

section .text

extern printf
extern sigaction
global main

my_handler:
  mov byte [window_change], 1
  ret

main:
  push rbp
  mov rsp, rbp

  ; Install the signal handler
  mov rdi, SIGWINCH
  mov rsi, act
  mov rdx, 0
  call sigaction


.begin_loop:
  cmp byte [window_change], 1
  jne .begin_loop

  ;window_change == 1
  mov rdi, resize_msg
  call printf

  mov byte [window_change], 0

  jmp .begin_loop


  mov rax, 0
  pop rbp
  ret

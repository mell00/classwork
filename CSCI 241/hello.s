section .data
    prompt db 'What is your name?',0
    greeting db 'Hello, ',0
    name db 256 dup(0)
    -------------------------
    prompt:       db      "What is your name? "
    prompt_len:   equ     $-prompt

    buffer:       times 255 db '!'

    resp1:        db      "Hello, "
    resp1_len:    equ     $-resp1
    resp2:        db      ", nice to meet you!", 10
    resp2_len:    equ     $-resp2

section .text
    global _start

_start:
    ; Print the prompt
    mov edx, 13
    mov ecx, prompt
    mov ebx, 1
    mov eax, 4
    syscall

    ; Read the name
    mov edx, 256
    mov ecx, name
    mov ebx, 0
    mov eax, 3
    syscall

    ; Print the greeting
    mov edx, 7
    mov ecx, greeting
    mov ebx, 1
    mov eax, 4
    syscall

    ; Print the name
    mov edx, [name+1]
    mov ecx, name
    mov ebx, 1
    mov eax, 4
    syscall

    ; Print "Nice to meet you!"
    mov edx, 17
    mov ecx, "Nice to meet you!",0
    mov ebx, 1
    mov eax, 4
    syscall

    ; Print newline
    mov edx, 2
    mov ecx, 10
    mov ebx, 1
    mov eax, 4
    syscall

    ; Exit
    xor eax, eax
    mov ebx, 0
    syscall

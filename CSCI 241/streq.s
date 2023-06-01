
        section .data
sb:     db "Hello!", 0
sa:     db "Hello!", 0

        section .text
        global _start
_start:
        mov rsi, sb             ; pointer to string b
        mov rdi, sa             ; pointer to string a
        xor rdx, rdx            ; displacement of length of a and b
streq:
        mov al, byte[rsi + rdx] ; access 1 char of s1
        mov bl, byte[rdi + rdx] ; access 1 char of s2
        inc rdx                 ; increment to access next char
        cmp al, bl              ; compare two current characters
        jne .not_equal          ; strings are not equal
        cmp al, 0               ; checks to see if at end
        je .equal               ; strings are equal
        jmp streq               ; if not at end, loop to the next character(s)

int print_int(long long rdi) {
  int rcx = 0,  rsi, rdx = 0;

  while (rdi!=0) {
    rsi = rdi % 10;
    rdi /= 10;
    rcx += rsi * pow(2, rdx);
    ++rdx;
  }


int rax = rcx;

  return rax;
}

print_int:

    xor r8, r8          ; clear out previous uses
    mov rcx, BUFLEN     ; loop counter
    mov r8, buffer      ; ptr to buffer
    add r8, BUFLEN-1    ; point to end of buffer
    mov rbx, rdi        ; store rdi value
    mov rax, rdi        ; so rdi can be divided
    mov r9, 10          ; r9 = 10

    .loop:
        xor rdx, rdx        ; clear out previous uses
        div r9              ; div (rax = rdi)/10
        add rdx, 48         ; add ascii value to rdx (modulo)
        mov byte[r8], dl    ; store remainder in buffer
        dec r8              ; move to next byte
        loop .loop      ; dec rcx

    ; print num
    mov rax, 1
    mov rdx, BUFLEN
    mov rdi, 1
    mov rsi, buffer
    syscall

    ; print new line
    mov rax, 1
    mov rdx, 1
    mov rdi, 1
    mov rsi, newline
    syscall

    ret         ; Return from print_int function
mov rcx, 0
mov rsi, 0
mov rdx, 0
mov rcx, buffer
mov r8, BUFLEN

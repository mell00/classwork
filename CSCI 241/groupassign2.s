section .data

; This array is sorted
sorted_arr:     dq      1, 2, 3, 4, 5, 6, 7, 8, 9, 10
arr_len:        equ     $ - sorted_arr

; These are not
unsorted_arr1:  dq      1, 2, 3, 4, 5, 7, 6, 8, 9, 10
unsorted_arr2:  dq      2, 1, 3, 4, 5, 6, 7, 8, 9, 10
unsorted_arr3:  dq      1, 2, 3, 4, 5, 6, 7, 8, 10, 9

fmt:            db      "%d", 10, 0

section .text
global main
extern printf

main:
    push rbp
    mov rbp, rsp

    mov rdi, sorted_arr
    mov rsi, arr_len
    call is_sorted

    mov rsi, rax
    mov rdi, fmt
    call printf

    mov rdi, unsorted_arr1
    mov rsi, arr_len
    call is_sorted

    mov rsi, rax
    mov rdi, fmt
    call printf

    mov rdi, unsorted_arr2
    mov rsi, arr_len
    call is_sorted

    mov rsi, rax
    mov rdi, fmt
    call printf

    mov rdi, unsorted_arr2
    mov rsi, arr_len
    call is_sorted

    mov rsi, rax
    mov rdi, fmt
    call printf

    pop rbp
    mov rax, 0
    ret


is_sorted:
    push rbp
    mov rbp, rsp
    ; rdi = address of array
    ; rsi = length of array (in bytes)

    .begin:
      mov rbp, rdi
      mov rsp, rsi
      cmp 
    ret ; Return 1 for sorted, 0 for not sorted

    mov rax, 0 ; Change this line
    pop rbp
    ret

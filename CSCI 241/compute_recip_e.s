section .data

dbl_one:                 dd         1.0
negone:  dd      -1.0
limit:    dd      0.000001


format:  db      "%f", 10, 0

       section .text

       extern printf

       global main
main:

       push rbp
       mov rbp, rsp

;;;  Compute pi
       call compute_recip_e
       ;;  Return value in xmm0

;;;  Print result
       %define num_terms rdi
       mov rdi, format
       mov al, 1
       cvtss2sd xmm0, xmm0 ; Convert to double for printf
       cvtss2sd xmm1, xmm1
       cvtss2sd xmm2, xmm2
       cvtss2sd xmm3, xmm3
       cvtss2sd xmm4, xmm4
       cvtss2sd xmm5, xmm5
       call printf

       mov rax, 0
       pop rbp
       ret

       compute_recip_e:
               push rbp
               mov rbp, rsp
               movsd xmm1, 1.0                 ; xmm1 = 1.0, product of factorial
               movsd xmm4, 1.0 ; xmm4 = 1.0 (for xmm2 = 1.0), quotient of frac_sub and negative -1.0 of fact_mul
               movsd xmm5, 1.0            ; outer loop counter
               xor xmm2, xmm2          ; xmm2 = 0, fact_mul counter
               xor xmm3, xmm3          ; xmm3 = 0, copy of xmm1 for use by frac_sub
               movsd xmm2, 1.0                 ; xmm2 = 1.0

               .outer_loop:
               cmpsd xmm5, num_terms ; check if overall counter has reached number of terms
               jge .end                   ; if so, then return the total
               jmp .fact_mul              ; if not, calculate the factorial of xmm5
               inc xmm5                   ; move to the next term

               .fact_mul:
               mulsd xmm1, xmm2        ; multiply current counter value with product to find new product
               movsd xmm3, xmm1        ; copy product into xmm3 for use by frac_sub
               test xmm4, -1.0
               je .frac_sub_neg        ; finish calculating the current negative term
               jne .frac_sub_pos; finish calculating the current positive term
               cmpsd xmm2, xmm5        ; check if fact_mul counter has reached overall counter
               jge .end_fact_mul               ; if it has, return to .outer_loop
               inc xmm2                ; next number to be multiplied
               jmp .fact_mul

               .end_fact_mul:

               .frac_sub_neg:
               divsd xmm4, xmm3        ; xmm4 = -1.0 / product
               addsd xmm0, xmm4        ; add term to total
               movsd xmm4, 1.0         ; flip sign for next term

               .frac_sub_pos:
               divsd xmm4, xmm3        ; xmm4 = 1.0 / product
               addsd xmm0, xmm4        ; add term to total
               movsd xmm4, -1.0        ; flip sign for next term

               ;;  Result is in xmm0
               .end:           ; total is in xmm0

               pop rbp
                   ret

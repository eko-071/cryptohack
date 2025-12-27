# Learning With Errors 1

## Difference between High-bit and Low-bit Scheme

In high-bit scheme:
$
x = \Delta \cdot m + e 
$
The message gets scaled up and becomes large, while the noise is small(low bits).\\
We recover the message by rounding.

In low-bit scheme:
$
x = m + p \cdot e
$
The message is small and hidden in the low bits, while the noise is large and hidden in the high bits.\\
We recover the solution by doing modulo p, which removes the $p \cdot e$ term.
# Learning With Errors 1

Since this seemed more like an introductory section, I decided to read through all the descriptions first and then try to solve the challenges.
There was a YouTube channel called [Chalk Talk](https://www.youtube.com/@chalktalkmath) that was really helpful with understanding the Learning With Errors problem, lattice cryptography, and more.

## LWE Background

The LLL algorithm, named after Lenstra, Lenstra, and Lovasz, is a basic lattice reduction algorithm that runs in polynomial time.
While Gaussian reduction works for two-dimensional lattices, LLL works for higher dimensions as well.
It's pretty useful in solving the SVP and CVP problems.

However, this is true only up to a certain point.
The reason that LWE is a hard problem that can be used for cryptography is that by making the dimension or errors huge, or by by giving a large basis, basis reduction won't reliably return the shortest vector anymore.

**Question:** What is the name of the computer scientist and mathematician who introduced the LWE problem in 2005?

**Answer:** Oded Regev

## LWE Intro

This part is essentially an explanation of what exactly the LWE problem is.

Learning With Errors (LWE) refers to the computational problem of learning a linear function $f(A)$ which takes values over a ring, given many noisy samples of the function. They're of the form $(A,\langle A,S \rangle + e)$ where $S$ is the secret key that defines the subject. $e$ is some error value, and $A$ is a matrix belonging to the ring.

Common features of cryptosystems based on LWE are:
- 2 different moduli are used, one for the plaintext and one for the ciphertext.
- $S$ is an element of a vector space modulo $n$.
- We encrypt messages by adding an encoded noisy message to a large dot-product.
  - The noisy message here is an encoded sum of the message and a comparatively small error term.

If we know the secret key, we can remove the large dot-product easily, which leaves behind the encoded message and noise.

**Question:** What algorithm could be used to recover the message from the linear equations in polynomial time, if there was no added error?

**Answer:** Gaussian Elimination

## LWE High Bits Message

Here, we're storing the message in the high-bits of the LWE sample and noise in the low-bits.

Examples: Regev09,  Brakerski/Fan–Vercauteren (BFV)

This was pretty easy since all I had to do was just follow the steps given to decrypt.

## LWE Low Bits Message

Here, we're storing the message in the low-bits of the LWE sample and noise in the high-bits.

Examples: Brakerski–Gentry–Vaikuntanatha (BGV)

Same as the previous challenge.

## From Private to Public Key LWE

**Question:** What is the size of a Kyber1024 public key in bytes?

**Answer:** 1568

## Extra

### Difference between High-bit and Low-bit Scheme

In high-bit scheme: $x = \Delta \cdot m + e$\
The message gets scaled up and becomes large, while the noise is small(low bits).\
We recover the message by rounding.

In low-bit scheme: $x = m + p \cdot e$ \
The message is small and hidden in the low bits, while the noise is large and hidden in the high bits.\
We recover the solution by doing modulo p, which removes the $p \cdot e$ term.
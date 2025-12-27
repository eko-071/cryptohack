# Cryptohack Lattices Writeup

## Find The Lattice

### Given

#### Key Generation

- $q$ is some 512-bit prime number
- $2<f<\sqrt{\frac{q}{2}}$
- $\sqrt{\frac{q}{4}}<f<\sqrt{\frac{q}{2}}$ and $gcd(f,g)=1$
- $h = f^{-1} \cdot g \mod q$ 
- Now `gen_key()` returns `(q, h), (f, g)`

Here, $(q,h)$ is the public key and $(f,g)$ is the private key.

#### Encryption

- $m<\sqrt{\frac{q}{2}}$ 
- $2<r<\sqrt{\frac{q}{2}}$
- $e=r \cdot h + m \mod q$
- Now, `encrypt(q, h, m)` returns `e`

Here, `(q, h)` is the public key generated, `m` the message to be encrypted, and `e` the encrypted message.

#### Decryption

- $a=f \cdot e \mod q$
- $m=a \cdot f^{-1} \mod g$
- Now, `decrypt(q, h, f, g, e)` returns `m`

Here, `(q, h)` is the public key generated, `(f, g)` the private key, `e` the encrypted message, and `m` the original message.

### Solving?


$$
\begin{split}
e &= r \cdot h + m \mod q \\
  &= r \cdot f^{-1} \cdot g + m \mod q
\end{split}
$$

$$
\begin{split}
a &= f \cdot e \mod q \\
  &= f \cdot (r \cdot f^{-1} \cdot g + m) \mod q \\
  &= rg + fm \mod q
\end{split}
$$


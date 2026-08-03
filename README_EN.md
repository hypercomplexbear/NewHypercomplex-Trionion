> 🌐 [繁體中文版說明請點此](./README.md)

### Author's Preface

Hello everyone. It is hard to sum up in a few words why I developed this new hypercomplex number. All I can say is that, through a series of coincidences, an ordinary person like me stumbled into this journey of researching hypercomplex numbers.I am no great mathematician, so for a long time during development, I relied on Gemini to teach me advanced mathematics. However, math is a profound subject, and learning solely through AI has its limits. Therefore, please forgive any mathematical inaccuracies you might find.

> 💡**Core ConceptMost** 
> people believe that developing 3D complex numbers is almost impossible. However, I feel there could be a unique value behind hypercomplex numbers in the 3rd, 5th, and 7th dimensions, especially since 3, 5, and 7 are prime numbers. Since I am an amateur mathematician, publishing a formal, rigorous math paper is extremely difficult. As an alternative, I worked with Gemini to build a new hypercomplex number computing sandbox. I put it on GitHub so everyone can research it together, and this README serves as a record of my findings so far. Hope you like it! Also, some formulas in this article were derived by Gemini after I shared my initial thoughts with it.

The following section explains the derivation process:

## A. Development Principles of the New Hypercomplex Number: Trionions

### a.1 The new hypercomplex number takes the unconventional concept of "taking the square root of an angle" as its starting point. The assumptions are as follows:

* Spatial Coordinate Axis Setup: Assume a space with three mutually perpendicular axes: the real axis \(X\), the imaginary axis \(i\), and the imaginary axis \(j\).
* Complex Plane Mapping: The plane formed by the real axis \(X\) and the imaginary axis \(i\) constitutes the Gaussian complex plane, with the \(j\)-axis running perpendicular to this plane.
* Angle Square Root Axiom: Let the square root of the 90-degree principal argument of \(i\) on the \(Xi\) plane be equivalent to the 90-degree principal argument of \(j\) on the \(ij\) plane. From this, we derive $j^2 = i$.
* Geometric Rotation in Space: If $i^2 = -1$ represents a two-dimensional rotation that brings a number back to the real axis, then $j^2 = i$ can be understood as a three-dimensional rotation starting from point \(i\) toward the \(j\)-axis, and then rotating back to point \(i\).
The powers of \(j\) are listed below:
* $j = i/j$
* $j^2 = i$
* $j^3 = ij$
* $j^4 = i^2 = -1$
* $j^5 = -j$
* $j^6 = j^2 \times i^2 = -i$
* $j^7 = - ij$
* $j^8 = 1$
* $j^9 = j$

When creating trinions, encountering the product of two imaginary numbers, \(ij\), is inevitable. However, this system elegantly resolves this issue by utilizing $j^{3}$. 
Below is the power table of \(ij\) (for writing convenience, the rest of this documentation will denote $j^3 = ij = k$:
* $k^1 = j^3$
* $k^2 = -i$
* $k^3 = j$
* $k^4 =- i^2 = -1$
* $k^5 = -j^3$
* $k^6 = j^2 = i$
* $k^7 = - j$
* $k^8 = 1$
* $k^9 = j^3$

Below is the multiplication table for individual powers of \(j\) with \(i\):
* $ji=j^3$
* $j^2*i = -1$
* $j^3*i = -j$
* $j^4*i = -i$
* $j^5*i = -ij$
* $j^6*i = 1$
* $j^7*i = j$
* $j^8*i= i$
* $j^9*i= ij$

### a.2. Let the trionion be defined as T = $a + bi + cj + dk$ (where \(a, b, c, d\) are real numbers). Based on the lists above, several properties can be observed:

* The imaginary unit \(j\), when raised to consecutive powers up to 8, cycles through every direction and returns directly to its starting point. The algebraic operations of \(k\) follow the exact same rule.
* Coincidentally, a 3D space in Clifford algebra happens to require exactly 8 basis elements.
* Even though it is a trinion, it still elegantly mirrors the power-of-two pattern inherent in the Cayley-Dickson construction—where $2^{3}$ yields exactly 8 dimensions. Simply put, this hypercomplex number is a trinion on the surface, but a quaternion at its core.
* I am uncertain of this hypercomplex number's exact classification within group and ring theory. However, based on its structure, it should satisfy both the associative and distributive laws of multiplication. Yet, unlike standard quaternions, this system is actually commutative, since $ij = ji = j^3$. I will attempt to prove this later in the article.
* Interestingly, \(ij\) appears to be related to the left-hand rule. Its precise function remains a mystery for now, which I will attempt to analyze later in the article.

### a.3. Matrix Mapping (Derived with the assistance of Gemini)

The trinion \(T = a + bi + cj + dk\) can be geometrically mapped through a $2 \times 2$ complex matrix \(T\), with its full matrix representation defined as follows:

<div align="center">

$$ \text{The Matrix of } T = a \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \end{bmatrix} + b \begin{bmatrix} i & 0 \\\\ 0 & i \end{bmatrix} + c \begin{bmatrix} 0 & i \\\\ 1 & 0 \end{bmatrix} + d \begin{bmatrix} 0 & -1 \\\\ i & 0 \end{bmatrix} = \begin{bmatrix} a + bi & ci - d \\\\ c + di & a + bi \end{bmatrix} $$

</div>

---

## B. Derivation of the Zero Divisor

### b.1. Derivation of the Algebraic Identity for Zero Divisors (Derived with the assistance of Gemini)

The following is the zero-divisor derivation concept introduced to me by Gemini:
When the determinant of this mapping matrix equals zero, geometric degeneracy occurs in the space, leading to the emergence of zero divisors. Through the expansion of the determinant, the precise derivation is as follows:

<div align="center">

$$ \det(T) = (a + bi)^2 - (ci - d)(c + di) = (a^2 - b^2 + 2cd) + (2ab - c^2 + d^2)i $$

For this element to become a zero divisor, its real and imaginary parts must both equal zero simultaneously, thereby yielding a system of simultaneous singular point equations on the complex plane:

*   $a^2 - b^2 + 2cd = 0 \implies a^2 - b^2 = -2cd$
*   $2ab - c^2 + d^2 = 0 \implies c^2 - d^2 = 2ab$

At this point, we establish an intermediate expression using the algebraic properties of equality: $(a^2 - b^2)^2 + (2ab)^2 = (-2cd)^2 + (c^2 - d^2)^2$

Substituting the algebraic identity $(x-y)^2 + 4xy = (x+y)^2$,  the above expression simplifies to:

$$ (a^2 + b^2)^2 = (c^2 + d^2)^2 \implies a^2 + b^2 = c^2 + d^2 $$

</div>

### Conclusion: Geometric Requirements for Zero Divisors (The Singular Conditions)

In summary, for any element to trigger a zero-divisor degeneracy (metric singularity) within this space, its four-dimensional coordinates must strictly and perfectly satisfy the following system of simultaneous equations:

<div align="center">

$$ \begin{cases} a^2 + b^2 = c^2 + d^2 \\\\ a^2 - b^2 = -2cd \\\\ c^2 - d^2 = 2ab \end{cases} $$

For example: $$(1 + i + \sqrt{2}j) \times (1 + i - \sqrt{2}j)$$

</div>

### b.2. Finding Specific Nilpotent Elements (Derived via Gemini)

Gemini suggested that I attempt to explore whether non-zero nilpotent elements exist. That is, whether there is a set of non-zero coordinates whose mapping matrix \(M\) satisfies:

<div align="center">

$$M^2 = \mathbf{0}$$

</div>

Currently, the full mapping matrix is known as follows:

$$M = \begin{bmatrix} a + bi & ci - d \\\\ c + di & a + bi \end{bmatrix}$$

The following is the original derivation assisted by Gemini:Since the main diagonal elements of this matrix are identical (both being \(a + bi\)), according to the axiomatic properties of $(2 \times 2\)$ matrices in linear algebra: if $M^2 = \mathbf{0}$, the trace (the sum of the main diagonal) of the matrix must be 0, and its determinant must also be 0.

#### Necessary Condition for the Trace to be 0:

Establish the equation by summing the diagonal elements:
<div align="center">

$$ \text{Tr}(M) = (a + bi) + (a + bi) = 2(a + bi) = 0 \implies a = 0 \text{ 且 } b = 0 $$

</div>

#### Substituting into the zero-divisor golden identity for geometric constraint:

When the real part and the first imaginary axis are locked to \(a = 0, b = 0\), substituting these conditions into the first row of the zero-divisor equation derived from the simultaneous system in the previous section yields: $a^2 + b^2 = c^2 + d^2$

<div align="center">

$$ 0^2 + 0^2 = c^2 + d^2 \implies c^2 + d^2 = 0 $$

</div>

Since \(a, b, c, d\) are real numbers, the only possible real solution for the sum of two squares to equal zero is for both to be zero. Therefore:

<div align="center">

$$ c = 0 \text{ 且 } d = 0 $$

</div>

#### Conclusion on the Nilpotent Element Argument
If a specific mapping matrix form of this hypercomplex space is required to satisfy $M^2 = \mathbf{0}$, back-calculating within a closed logical loop reveals that the unique solution can only be \(a = b = c = d = 0\)—that is, only the null matrix itself. Conclusion: Under a set of non-zero real coefficients, this custom-structured hypercomplex space "contains no non-zero nilpotent elements."

### b.3. Finding Idempotent Complements (Derived via Gemini)

Within the same derivation session, Gemini suggested that I could search for another specific zero-divisor, the idempotent element $P$, which satisfies $P^2 = P$(representing a projection matrix in topology).According to algebraic theorems, if $P^2 = P$, then multiplying it by its complementary pair $I - P$ must yield the null matrix:

<div align="center">

$$ P(I - P) = \mathbf{0} $$

</div>

The following is the original derivation assisted by Gemini: Similarly, for a specific $2 \times 2$ matrix to satisfy the geometric constraint of $P^2 = P$, its determinant must be 0, and its trace must be exactly 1.

Necessary Condition for the Trace to be 1Establish the axiomatic equation by summing the diagonal components:

<div align="center">

$$ \text{Tr}(P) = 2(a + bi) = 1 \implies a = \frac{1}{2}, \; b = 0 $$

</div>

#### Solving for Coordinates $c, d$ via Zero-Divisor System

Substituting the derived real part and first imaginary axis constraints, $a = \frac{1}{2}, b = 0$, into the two aforementioned core requirements of zero divisors for a simultaneous analysis:

* **Condition 1**： $a^2 - b^2 = -2cd \implies \left(\frac{1}{2}\right)^2 - 0 = -2cd \implies cd = -\frac{1}{8}$
* **Condition 2**： $c^2 - d^2 = 2ab \implies c^2 - d^2 = 2\left(\frac{1}{2}\right)(0) = 0 \implies c^2 = d^2$

#### Algebraic Sign and Heterosignity Analysis：

* 1. From Condition 2, c² = d², we can infer that in terms of geometric length, c = d or c = -d.
* 2. From Condition 1, where the product $cd = -\frac{1}{8}$ is negative, we know that c and d must have opposing signs. Therefore, in spatial topology, the condition c = -d must be satisfied.

</div>

Here, we precisely select one specific set of solutions within the complex space:
<div align="center">

$$ c = \frac{1}{2\sqrt{2}}, d = - \frac{1}{2\sqrt{2}} $$

</div>

#### Successfully Constructing the "Idempotent Element & Complementary Pair" Matrices

Substituting this precise set of four-dimensional geometric coordinates $(a, b, c, d) = \left(\frac{1}{2}, 0, \frac{1}{2\sqrt{2}}, -\frac{1}{2\sqrt{2}}\right)$ into the full mapping matrix, we successfully construct the projection matrix \(P\) unique to this hypercomplex space:

<div align="center">

$$ P = \begin{bmatrix} \frac{1}{2} & \frac{1}{2\sqrt{2}}i + \frac{1}{2\sqrt{2}} \\\\ \frac{1}{2\sqrt{2}} - \frac{1}{2\sqrt{2}}i & \frac{1}{2} \end{bmatrix} $$

</div>

At this point, by subtracting \(P\) from the identity matrix \(I\), we obtain its complementary matrix $I - P$ as:

<div align="center">

$$ I - P = \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \end{bmatrix} - \begin{bmatrix} \frac{1}{2} & \frac{1}{2\sqrt{2}}i + \frac{1}{2\sqrt{2}} \\\\ \frac{1}{2\sqrt{2}} - \frac{1}{2\sqrt{2}}i & \frac{1}{2} \end{bmatrix} = \begin{bmatrix} \frac{1}{2} & -\frac{1}{2\sqrt{2}}i - \frac{1}{2\sqrt{2}} \\\\ -\frac{1}{2\sqrt{2}} + \frac{1}{2\sqrt{2}}i & \frac{1}{2} \end{bmatrix} $$

</div>

### Conclusion on Matrix Construction (Significant Conclusion)

These two non-zero matrices, \(P\) and \((I - P)\), which are finely interwoven from complex and irrational numbers, constitute a perfectly specified form of a Zero-Divisor Pair within this hypercomplex space!Neither of them is a zero element on its own, yet the result of their multiplication in the geometric algebra space is "guaranteed to be a perfect null matrix 0"!

</div>

### b.4. Fascinating Zero Divisors (Independent Derivation)

The aforementioned nilpotent and idempotent elements may hold mathematical significance, which is why Gemini suggested I derive them. However, I personally found another set of zero divisors more intriguing. Let us return to the initial geometric constraints for zero divisors:

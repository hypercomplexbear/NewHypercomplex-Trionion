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
* Interestingly, \(ij\) appears to be related to the left-hand or right-hand rule. Its precise function remains a mystery for now, which I will attempt to analyze later in the article.

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

$$ \begin{cases} a^2 + b^2 = c^2 + d^2 \\\\ a^2 - b^2 = -2cd \\\\ c^2 - d^2 = 2ab \end{cases} $$

When \(d = 0\), we can obtain $a = b, c = \pm\sqrt{2}a$; alternatively, when \(a = 0\), we can obtain  $c = d, b = \pm\sqrt{2}c$.

Observing the first form, I listed a set of zero divisors using a base unit length of a = 1 : (1, i, $\sqrt{2}j$). When plotting these coordinate points in space, I discovered something quite fascinating!
* Every face of this tetrahedron is a right-angled triangle.
* This tetrahedron contains all the special angles $(30^\circ, 45^\circ, 54.74^\circ / 35.26^\circ, 60^\circ, \text{ and } 90^\circ)$. Among them, the $(54.74^{\circ }\) / \(35.26^{\circ }\)$ angle is what Gemini refers to as the "Magic Angle." In numerous technological applications, this specific angle is utilized to eliminate interference signals (such as in nuclear magnetic resonance, MRI). Is this merely a coincidence?
* The lengths of the edges of this tetrahedron can be expressed as a sequence of square roots: ( $\sqrt{1}$, $\sqrt{2}$, $\sqrt{3}$, $\sqrt{4}$ ), which is precisely the Spiral of Theodorus (also known as the square root spiral).
* Gemini told me that the zero divisors in this hypercomplex system can be viewed as a type of light cone. I don't fully understand how it suddenly connected to Hermann Minkowski's spacetime theory and light cones, though it did try to explain it to me. The $(45^{\circ }\)$ angle seems to be a crucial angle for the light cone.
* Interestingly, the companion zero divisor to this set of zero divisors (1, i, $\sqrt{2}j$) is (1, i, - $\sqrt{2}j$)—which is the exact example from Section 2.1. These two sets of coordinate points map to each other across the \(X\)-axis, and the angles of their moduli are both $(45^{\circ }\)$. Is this merely a coincidence? Could they be forming the shape of a local light cone?Therefore, it is reasonable to infer that the line connecting every point of T = a + ai + $\sqrt{2}aj$ and the line connecting every point of T = a + ai - $\sqrt{2}aj$ constitute two intersecting \(X\)-shaped zero-divisor boundaries passing through the origin. Coincidentally, they resemble the shape of a light cone. Is there a way to locate other zero-divisor lines in this space and observe whether the collection of all zero-divisor lines forms a complete light cone? This will be both a fascinating and challenging endeavor!

</div>

## C. Algebraic Axioms and the Multiplicative Metric Table (Algebraic Foundations)

Let there be two arbitrary trinion elements, $X_1 = a_1 + b_1i + c_1j + d_1k$ and $X_2 = a_2 + b_2i + c_2j + d_2k$. Their arithmetic axioms are defined as follows:

### c.1. Addition and Subtraction Expansions for Two Arbitrary Trinions (Independent Derivation)

Since it is widely known that the arithmetic axioms for the addition and subtraction of any two complex numbers simply state "real part plus real part, imaginary part plus imaginary part," this trinion system naturally follows the same logic. It is expressed as follows:

* Addition (Real parts add to real parts, imaginary parts add to imaginary parts):(a1 + a2) + (b1 + b2)i + (c1 + c2)j + (d1 + d2)k

* Subtraction (Real parts subtract from real parts, imaginary parts subtract from imaginary parts): (a1 - a2) + (b1 - b2)i + (c1 - c2)j + (d1 - d2)k

### c.2. Multiplication Expansion for Two Arbitrary Trinions (Independent Derivation)

Based on the algebraic metric table for basis multiplication, the precise analytical expressions for the four-dimensional components of their product,  $X_3 = X_1 \times X_2 = a_3 + b_3i + c_3j + d_3k$, are as follows:

*   **real part (a3)**： $a_3 = a_1a_2 - b_1b_2 - c_1d_2 - d_1c_2$
*   **i -  axis (b3)**： $b_3 = a_1b_2 + b_1a_2 + c_1c_2 - d_1d_2$
*   **j -  axis (c3)**： $c_3 = a_1c_2 - b_1d_2 + c_1a_2 - d_1b_2$
*   **k -  axis (d3)**： $d_3 = a_1d_2 + b_1c_2 + c_1b_2 + d_1a_2$

#### Note: Observing this expansion, I found that it differs from Hamilton's quaternion by only a few signs. It is mind-blowing how a minor change in signs can lead to such vastly different mathematical results!

#### **c.2.1. Proving the Commutativity: ij = ji**

**Proof Method 1: Using the Multiplication Expansion (Proof method proposed by Gemini)**
Assume there are two elements, X and Y, in the space, where  $X = i \times j$ and  $Y = j \times i$. We will attempt to determine their coordinate positions within the space. 
When calculating $X = i \times j$: The first element has only the \(i\)-axis component, $b_1 = 1$ (with all other components being 0); the second element has only the \(j\)-axis component, $c_2 = 1$ (with all other components being 0). Substituting these into the component expansions yields:
*   real part $a_3 = 0$
*   i -  axis $b_3 = 0$
*   j -  axis $c_3 = 0$
*   k -  axis $d_3 = b_1 \times c_2 = 1 \times 1 = 1$

<div align="center">

$$ X = i \times j = \begin{bmatrix} 0, & 0, & 0, & 1 \end{bmatrix}^T = k $$

</div>

When calculating $Y = j \times i$ :The first element has only the \(j\)-axis component, $c_1 = 1$ (with all other components being 0); the second element has only the \(i\)-axis component, $b_2 = 1$ (with all other components being 0). Substituting these into the component expansions yields:

*   real part $a_3 = 0$
*   i -  axis $b_3 = 0$
*   j -  axis $c_3 = 0$
*   k -  axis $d_3 = c_1 \times b_2 = 1 \times 1 = 1$

<div align="center">

$$ Y = j \times i = \begin{bmatrix} 0, & 0, & 0, & 1 \end{bmatrix}^T = k $$

</div>

**Conclusion: Since both calculations share the exact same 4D spatial geometric coordinates, by the algebraic axioms of equality, it directly proves that $(ij = ji)$.**

**Proof Method 2: Algebraic Proof by Contradiction (Independent Derivation)**

Assume that: $$ij \neq ji$$

Perform the operation of "left-multiplying by i and right-multiplying by j" simultaneously on both sides of the inequality:

* **Expansion of the left side**： $i \cdot (ij) \cdot j = (i \cdot i) \cdot (j \cdot j) = (-1) \cdot (i) = -i$
* **Expansion of the right side**： $i \cdot (ji) \cdot j = j^2 \times j \times j^2 \times j = j^6 = -i$

This yields: $$-i  \neq -i$$
which creates a logical contradiction of an entity not equaling itself. Therefore, it is proven that $$ij = ji$$.

#### c.2.2 **Proving that this Hypercomplex System Satisfies the Associative, Commutative, and Distributive Laws of Multiplication (Within the Non-Zero-Divisor Domain) (Derived with the assistance of Gemini)**

Gemini explained to me that if a hypercomplex number system can already establish a $(2 \times 2\)$ complex matrix representation, its satisfaction of the associative, commutative, and distributive laws of multiplication can fundamentally be proven using the Matrix Isomorphism Theorem and the First Isomorphism Theorem of Ring Theory, without the need for tediously expanding massive algebraic expressions.

While this shortcut sounds wonderful, I believe such high-level theoretical mappings are best left to professional mathematicians to formally validate. Therefore, I decided to take the rigorous route and tackle the proof step by step. Following our discussion, we resolved to present the proof using a simplified matrix approach, as detailed below:

To present the structure of the three fundamental laws in the most intuitive manner, we first define the correspondence between the full mapping matrix \(T\) and the simplified complex notations \(z, w\). Let:

<div align="center">

$$ \text{The Matrix of } T = a \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \end{bmatrix} + b \begin{bmatrix} i & 0 \\\\ 0 & i \end{bmatrix} + c \begin{bmatrix} 0 & i \\\\ 1 & 0 \end{bmatrix} + d \begin{bmatrix} 0 & -1 \\\\ i & 0 \end{bmatrix} = \begin{bmatrix} a + bi & ci - d \\\\ c + di & a + bi \end{bmatrix} = \begin{bmatrix} z & w \\\\ \bar{w} & z \end{bmatrix} $$

</div>

Within this simplified structure,  $z = a+bi$, $w = ci-d$, and $\bar{w} = c+di$ (where the \(\={w}\) component naturally satisfies the conjugate form of this space's metric). All \(z_{n}\) and \(w_{n}\) are complex elements on a standard two-dimensional plane, which inherently satisfy the standard commutative and associative laws.

Through the abbreviated block forms of any three hypercomplex matrices $T_A, T_B, T_C$ , we can directly observe their algebraic topology through the placement of parentheses:

#### Matrix Block Notation: Explicit Structural Comparison (Simplified Structural Verification)

To present the structure of the three fundamental laws in the most intuitive manner, we discard the tedious, individual component variables and directly simplify any three hypercomplex matrices— $T_A, T_B, T_C$ —into ultra-abbreviated block forms composed of complex algebraic terms:

$$ T_A = \begin{bmatrix} z_1 & w_1 \\\\ \bar{w}_1 & z_1 \end{bmatrix}, \quad T_B = \begin{bmatrix} z_2 & w_2 \\\\ \bar{w}_2 & z_2 \end{bmatrix}, \quad T_C = \begin{bmatrix} z_3 & w_3 \\\\ \bar{w}_3 & z_3 \end{bmatrix} $$

Within this setup, all $z_n, w_n$ are complex elements on a standard two-dimensional plane, which inherently satisfy the standard commutative and associative laws. By looking at the placement of parentheses among these three simplified matrices, we can directly observe their algebraic topology:

#### c.2.2.1 Structural Observation of the Distributive Law (Distributivity)

We place the left-hand expression $T_A(T_B + T_C)$ and the right-hand expression $T_AT_B + T_AT_C$ side-by-side for a structural comparison:

* Left-hand expression (Adding inside the parentheses first):
<div align="center">

$$ \begin{bmatrix} z_1 & w_1 \\\\ \bar{w}_1 & z_1 \end{bmatrix} \times \left( \begin{bmatrix} z_2 & w_2 \\\\ \bar{w}_2 & z_2 \end{bmatrix} + \begin{bmatrix} z_3 & w_3 \\\\ \bar{w}_3 & z_3 \end{bmatrix} \right) = \begin{bmatrix} z_1 & w_1 \\\\ \bar{w}_1 & z_1 \end{bmatrix} \begin{bmatrix} (z_2+z_3) & (w_2+w_3) \\\\ (\bar{w}_2+\bar{w}_3) & (z_2+z_3) \end{bmatrix} $$

</div>

* Right-hand expression (Multiplying out and then adding):
<div align="center">

$$ = \begin{bmatrix} z_1z_2 + w_1\bar{w}_2 & z_1w_2 + w_1z_2 \\\\ \bar{w}_1z_2 + z_1\bar{w}_2 & \bar{w}_1w_2 + z_1z_2 \end{bmatrix} + \begin{bmatrix} z_1z_3 + w_1\bar{w}_3 & z_1w_3 + w_1z_3 \\\\ \bar{w}_1z_3 + z_1\bar{w}_3 & \bar{w}_1w_3 + z_1z_3 \end{bmatrix} $$

</div>

**Conclusion from Observation**: By applying the distributive law of standard complex numbers to compare the corresponding terms of the matrices on both sides (for example, expanding the first term on the left side yields $z_1(z_2+z_3) + w_1(\bar{w}_2+\bar{w}_3)$）, the structure after expanding the parentheses is perfectly identical to the right-hand expression. **The distributive structure is thus proven.**

---

#### c.2.2.2 tructural Observation of the Associative Law (Associativity)

To verify $(T_A \times T_B) \times T_C \stackrel{?}{=} T_A \times (T_B \times T_C)$, we directly observe the characteristic placement of the parentheses after multiplication:

* Left-hand expression structure (Associating the first two elements first):
<div align="center">

$$ \left( \begin{bmatrix} z_1 & w_1 \\\\ \bar{w}_1 & z_1 \end{bmatrix} \begin{bmatrix} z_2 & w_2 \\\\ \bar{w}_2 & z_2 \end{bmatrix} \right) \times T_C = \begin{bmatrix} (z_1z_2 + w_1\bar{w}_2) & (z_1w_2 + w_1z_2) \\\\ (\bar{w}_1z_2 + z_1\bar{w}_2) & (\bar{w}_1w_2 + z_1z_2) \end{bmatrix} \begin{bmatrix} z_3 & w_3 \\\\ \bar{w}_3 & z_3 \end{bmatrix} $$

</div>

* Right-hand expression structure (Associating the last two elements first):
<div align="center">

$$ T_A \times \left( \begin{bmatrix} z_2 & w_2 \\\\ \bar{w}_2 & z_2 \end{bmatrix} \begin{bmatrix} z_3 & w_3 \\\\ \bar{w}_3 & z_3 \end{bmatrix} \right) = \begin{bmatrix} z_1 & w_1 \\\\ \bar{w}_1 & z_1 \end{bmatrix} \begin{bmatrix} (z_2z_3 + w_2\bar{w}_3) & (z_2w_3 + w_2z_3) \\\\ (\bar{w}_2z_3 + z_2\bar{w}_3) & (\bar{w}_2w_3 + z_2z_3) \end{bmatrix} $$

</div>

* Expansion result for the first row and first column of the left-hand expression:
<div align="center">

$$ (z_1z_2 + w_1\bar{w}_2)z_3 + (z_1w_2 + w_1z_2)\bar{w}_3 = (z_1z_2)z_3 + (w_1\bar{w}_2)z_3 + (z_1w_2)\bar{w}_3 + (w_1z_2)\bar{w}_3 $$

</div>

* Expansion result for the first row and first column of the right-hand expression:
<div align="center">

$$ z_1(z_2z_3 + w_2\bar{w}_3) + w_1(\bar{w}_2z_3 + z_2\bar{w}_3) = z_1(z_2z_3) + z_1(w_2\bar{w}_3) + w_1(\bar{w}_2z_3) + w_1(z_2\bar{w}_3) $$

</div>

**Conclusion from Observation**: Following the same logic as the distributivity proof, since the results for the first row and first column are identical, it is reasonable to infer under the same matrix operation rules that all other rows and columns will yield the same results. **The associative structure is thus proven.**

---

#### c.2.2.3 Structural Observation of the Commutative Law (Commutativity)

Since matrix multiplication generally does not satisfy the commutative law, Gemini actually provided an erroneous argument. Therefore, I requested a direct proof using the multiplication expansions instead, as demonstrated below:

*   **The Four-Dimensional Expansion Components of $X_1 \times X_2$**：
    *   real part $a_3 = a_1a_2 - b_1b_2 - c_1d_2 - d_1c_2$
    *   i -  axis $b_3 = a_1b_2 + b_1a_2 + c_1c_2 - d_1d_2$
    *   j -  axis $c_3 = a_1c_2 - b_1d_2 + c_1a_2 - d_1b_2$
    *   k -  axis 軸 $d_3 = a_1d_2 + b_1c_2 + c_1b_2 + d_1a_2$

---

* **The Four-Dimensional Expansion Components of $X_2 \times X_1$**:
    *   real part $a_3' = a_2a_1 - b_2b_1 - c_2d_1 - d_2c_1$
    *   i -  axis $b_3' = a_2b_1 + b_2a_1 + c_2c_1 - d_2d_1$
    *   j -  axis $c_3' = a_2c_1 - b_2d_1 + c_2a_1 - d_2b_1$
    *   k -  axis $d_3' = a_2d_1 + b_2c_1 + c_2b_1 + d_2a_1$

Since all component coefficients （ $a_n, b_n, c_n, d_n$  inside the formulas are pure real numbers, multiplication inherently and perfectly satisfies the commutative law within the field of real numbers. There is no reason to doubt that $a_1a_2 \neq a_2a_1$. **The commutative structure is thus proven.**

### c.3. Division Operation for Two Arbitrary Trionions 

Initially, I was unable to derive the algebraic division formula using complex conjugates. However, driven by the desire to know whether division was even possible within this trinion system, I turned to Gemini for alternative approaches. Following our discussion, Gemini proposed the following solution, which successfully enabled us to implement division operations in our code.
The following is the derivation assisted by Gemini:

#### Transformation into a System of Linear Algebraic Equations

Given two hypercomplex numbers $A = a_1 + b_1i + c_1j + d_1k$ and $B = a_2 + b_2i + c_2j + d_2k$, we seek to solve for the division result $C = X_a + X_bi + X_cj + X_dk$ such that:

<div align="center">

$$ \frac{A}{B} = C \implies A = C \times B $$

</div>

According to the aforementioned definition of hypercomplex multiplication, we expand each dimensional component of $C \times B$ and set them equal to the corresponding components of \(A\). Since the unknowns are the components of \(C\), denoted as $(X_a, X_b, X_c, X_d)$, we can reorganize this system of simultaneous equations into a standard linear system: $M \cdot C = A$. Here, \(M\) represents a $4 \times 4$ spatial geometric matrix composed of the components of the denominator \(B\).

#### The Space-Specific 4x4 Division Matrix Structure

Perfectly aligned with the multiplication metric, the form of the dynamically constructed augmented matrix \(M\) is as follows (where the final column represents the constant terms, namely the components of the numerator \(A\)):

<div align="center">

$$ M = \begin{bmatrix} 
a_2 & -b_2 & -d_2 & -c_2 & \mathbf{a_1} \\\\ 
b_2 & a_2 & c_2 & -d_2 & \mathbf{b_1} \\\\ 
c_2 & -d_2 & a_2 & -b_2 & \mathbf{c_1} \\\\ 
d_2 & b_2 & b_2 & a_2 & \mathbf{d_1} 
\end{bmatrix} $$

</div>

#### Solving via Gauss-Jordan Elimination

To solve this $4 \times 5$ augmented matrix, the backend algorithm implements standard row operations. The original Python source code is provided below for evaluation:

    def divide_4d_algebra(a1, b1, c1, d1, a2, b2, c2, d2):
        M = [
            [a2, -b2, -d2, -c2, a1],
            [b2,  a2,  c2, -d2, b1],
            [c2, -d2,  a2, -b2, c1],
            [d2,  c2,  b2,  a2, d1]
        ]
          n = 4
        for i in range(n):
            max_row = i
            for r in range(i + 1, n):
                if abs(M[r][i]) > abs(M[max_row][i]):
                    max_row = r
            M[i], M[max_row] = M[max_row], M[i]

            if abs(M[i][i]) < 1e-12:
                raise ZeroDivisionError("Mathematical meltdown detected! The input set has triggered a [zero-divisor] singularity; division yields no unique solution.\n""偵測到數學崩潰點！該組輸入觸發了【零因子】特異點，除法無    唯一解。")
        
            pivot = M[i][i]
            for c in range(i, n + 1):
                M[i][c] /= pivot
            for r in range(n):
                if r != i:
                    factor = M[r][i]
                    for c in range(i, n + 1):
                        M[r][c] -= factor * M[i][c]
                    
        return [M[0][4], M[1][4], M[2][4], M[3][4]]

</div>

#### Within the sandbox calculator system, performing division operations on real numbers and the imaginary axis \(i\) yields verified, correct results; therefore, it is reasonable to infer that this algorithm can accurately determine the division solution for any trinion. We can closely observe this behavior through the concept of reciprocals:

* Let $j \times j^{-1}$ = 1; using the sandbox calculator, the reciprocal of \(j\) is determined to be \(-ij\); 
* let $ij \times (ij)^{-1}$ = 1; using the sandbox calculator, the reciprocal of \(ij\) is found to be \(-j\). 
These outputs are in perfect agreement with the hand-calculated analytical results.

#### (Supplement) Major Breakthrough: Complementing the Algebraic Conjugate Division Method (Independent Derivation)

**After numerous attempts, I have finally derived by hand a method to rationalize the algebraic denominator into a pure real number. The detailed explanation is presented below:**

Given two hypercomplex numbers $A = a_1 + b_1i + c_1j + d_1k$ and $B = a_2 + b_2i + c_2j + d_2k$.
In standard complex numbers, to convert the denominator into a real number, one simply multiplies the denominator by its complex conjugate. However, this is far from straightforward in this trinion system because the initial definition is set to $j^2 = i$. According to the multiplication expansion:

$X_2 (a_2 + b_2i + c_2j + d_2k)$ $\times$ $X_2'(a_2 - b_2i - c_2j - d_2k)$ = 

*   **real part (a3)**： $a_3 =  a_2a_2 + b_2b_2 + c_2d_2 + d_2c_2$
*   **i -  axis (b3)**： $b_3 = -a_2b_2 + b_2a_2 - c_2c_2 + d_2d_2$
*   **j -  axis (c3)**： $c_3 = -a_2c_2 + b_2d_2 + c_2a_2 + d_2b_2$
*   **k -  axis (d3)**： $d_3 = -a_2d_2 - b_2c_2 - c_2b_2 + d_2a_2$

It can be observed that the \(j\) and \(ij\) terms do not cancel each other out. However, this hypercomplex number system possesses a marvelous supersymmetry, which inspired me to experiment with swapping the coefficients!

If the \(j\) and \(ij\) terms in the denominator can be eliminated to reduce the expression into a standard x +yi form, we can then apply a secondary conjugation process!

The empirical results of this attempt are documented below:

For the denominator $B = a_2 + b_2i + c_2j + d_2k$, if we simultaneously multiply both the numerator and the denominator by the conjugate factor $B' = -b_2 + a_2i + d_2j - c_2k$, and substitute this into the multiplication metric expansion:

*   **real part (a3)**： $a_3 = -a_2b_2 - b_2a_2 + c_2c_2 - d_2d_2$
*   **i -  axis (b3)**： $b_3 = +a_2a_2 - b_2b_2 + c_2d_2 + d_2c_2$
*   **j -  axis (c3)**： $c_3 = +a_2d_2 + b_2c_2 - c_2b_2 - d_2a_2$
*   **k -  axis (d3)**： $d_3 = -a_2c_2 + b_2d_2 + c_2a_2 - d_2b_2$

It can be observed that the \(j\) and \(ij\) terms are completely eliminated, leaving only:
<div align="center">
    
$$ B \times B' = \left( -2a_2b_2 + c_2^2 - d_2^2 \right) + \left( a_2^2 - b_2^2 + 2c_2d_2 \right)i $$

</div>

**Now, we apply a secondary complex conjugation to fully rationalize the denominator into a pure real number:**

* The resulting numerator from the previous stage is: $(a_1 + b_1i + c_1j + d_1k)$ $\times$ $(-b_2 + a_2i + d_2j - c_2k)$ 
* The resulting denominator from the previous stage is:  $$B \times B' = \left( -2a_2b_2 + c_2^2 - d_2^2 \right) + \left( a_2^2 - b_2^2 + 2c_2d_2 \right)i$$

According to the rules of complex conjugates: $(x - yi)*(x + yi) = x^2 + y^2$, the denominator converges into a pure real number:

<div align="center">

$$ x^2 + y^2 = \left( -2a_2b_2 + c_2^2 - d_2^2 \right)^2 + \left( a_2^2 - b_2^2 + 2c_2d_2 \right)^2 $$

</div>

Therefore, the final result is:

* The resulting numerator from the previous stage is:
  $(a_1 + b_1i + c_1j + d_1k)$ $\times$ $(-b_2 + a_2i + d_2j - c_2k)$ $\times$ $(( -2a_2b_2 + c_2^2 - d_2^2) - ( a_2^2 - b_2^2 + 2c_2d_2)i)$
* The resulting denominator from the previous stage is: $$( -2a_2b_2 + c_2^2 - d_2^2)^2 + ( a_2^2 - b_2^2 + 2c_2d_2 )^2 $$
 
**Here is a fascinating point: the expression inside the parentheses is the exact determinant of the matrix itself (please refer to Section 2.1).**
Gemini provided me with the following conclusion: 
#### Geometric Significance and the Analytical Division Closed-Loop
This result manifests an exquisite algebraic elegance. The final denominator resolves into the sum of squares of two "zero-divisor characteristic equations":
* 1. If and only if the denominator \(B\) itself is a zero divisor, both equations will simultaneously equal 0, causing the overall denominator to become 0. In this scenario, division is indeed undefined, which perfectly aligns with the definition of zero divisors.
* 2. Under any other normal coordinates, this denominator is guaranteed to be a positive real number.

I wonder if everyone agrees with Gemini's insight?

## D. Square Root Extraction

Apart from the four fundamental arithmetic operations, the matter I consider most crucial and care about the most is whether we can extract square roots! Extracting square roots can give birth to many mathematical entities, such as imaginary numbers or even this trionion system itself. I believed that solving this through Gaussian or Gauss-Jordan elimination held the highest probability of success (and was also the most convenient), so I requested Gemini's assistance in deriving and writing the Python code.

The original source code is provided below for evaluation:


    def gaussian_elimination(M, Y):
        n = 4
        
        A = [M[i] + [Y[i]] for i in range(n)]
    
        for i in range(n):
            max_row = i
            for k in range(i + 1, n):
                if abs(A[k][i]) > abs(A[max_row][i]):
                    max_row = k
            A[i], A[max_row] = A[max_row], A[i]
        
            if abs(A[i][i]) < 1e-12:
                A[i][i] = 1e-12
            
            pivot = A[i][i]
            for j in range(i, n + 1):
                A[i][j] /= pivot
            
            for k in range(i + 1, n):
                factor = A[k][i]
                for j in range(i, n + 1):
                    A[k][j] -= factor * A[i][j]              
        
        dX = [0.0] * n
        for i in range(n - 1, -1, -1):
            dX[i] = A[i][n]
            for k in range(i + 1, n):
                dX[i] -= A[i][k] * dX[k]
        return dX

    def sqrt_4d_algebra(a1, b1, c1, d1):        
        v_norm = math.sqrt(b1**2 + c1**2 + d1**2)
        if v_norm < 1e-9:
            if a1 >= 0:
                return [math.sqrt(a1), 0.0, 0.0, 0.0]
            else:
                return [0.0, math.sqrt(abs(a1)), 0.0, 0.0]
        
        q_norm = math.sqrt(a1**2 + b1**2 + c1**2 + d1**2)
        x_a = math.sqrt((q_norm + abs(a1)) / 2)
        scale = 0.5 / x_a if x_a != 0 else 0.1
        x_b = b1 * scale
        x_c = c1 * scale
        x_d = d1 * scale    
        
        for _ in range(6):           
            M = [
                [2 * x_a, -2 * x_b, -2 * x_d, -2 * x_c],
                [2 * x_b,  2 * x_a,  2 * x_c, -2 * x_d],
                [2 * x_c, -2 * x_d,  2 * x_a, -2 * x_b],
                [2 * x_d,  2 * x_c,  2 * x_b,  2 * x_a]
            ]        
          
            current_a = x_a**2 - x_b**2 - 2 * x_c * x_d
            current_b = 2 * x_a * x_b + x_c**2 - x_d**2
            current_c = 2 * x_a * x_c - 2 * x_b * x_d
            current_d = 2 * x_a * x_d + 2 * x_b * x_c        
            
            y_a = a1 - current_a
            y_b = b1 - current_b
            y_c = c1 - current_c
            y_d = d1 - current_d
            Y = [y_a, y_b, y_c, y_d]
        
           dX = gaussian_elimination(M, Y)
        
            x_a += dX[0]
            x_b += dX[1]
            x_c += dX[2]
            x_d += dX[3]
                
            return [round(x_a, 6), round(x_b, 6), round(x_c, 6), round(x_d, 6)]

#### Gemini's Numerical Solver Process Explanation:

According to Gemini, it utilizes the Newton-Raphson Matrix Iteration method from advanced numerical analysis, along with the Jacobian Matrix, to perform the computations. In each iteration, the system calculates the current residual vector $Y = Q - X_{\text{current}}^2$ and calls the Gaussian elimination algorithm to solve for the spatial correction vector $dX$ ($M \cdot dX = Y$), which then refines the coordinates. Typically, it takes only 5 to 6 iterations to achieve an extremely high algebraic precision of $10^{-12}$ under the limits of floating-point arithmetic. To be completely honest, such complex mathematical theories and code are far too profound for me—I am a strict pragmatist!
However, after empirical testing, the sandbox calculator can indeed yield correct results for both real numbers and standard complex numbers ( a + bi ). Therefore, it is reasonable to infer that it functions properly to extract square roots for us. I actually tested a few specific values that I was most curious about, as detailed below:

* The square root of \(1j\) is: \(0.653281 - 0.270598i + 0.653281j + 0.270598k\). Through back-squaring verification, and neglecting negligible floating-point deviations, the product indeed equals \(1j\).
* The square root of \(1ij\) is: \(0.653281 + 0.270598i + 0.270598j + 0.653281k\). Similarly, through back-squaring verification, it indeed equals \(1ij\) when ignoring ultra-minor numerical rounding errors.

**When performing continuous square root extractions on any non-zero-divisor trinion, their trajectories, expectedly, forcefully converge to the real number 1.0 (i.e., the coordinate $[1, 0, 0, 0]$） at a geometric rate. This further substantiates that this square root code system is fully accurate.**

---

## E. Normalization (Normalize)

Gemini suggested that I implement a Normalize operation button, which scales the vector proportionally back to a total modulus of unit length 1 when the values explode, making it easier to study. I wasn't entirely sure of its critical importance initially, but I built it anyway.
Naturally, the Python implementation was handled by Gemini. It achieves this by dividing each of the four coefficients \((a, b, c, d)\) individually by the total modulus $\sqrt{a^2 + b^2 + c^2 + d^2}$.

---

## F. Conclusion: Rather than saying this fascinating trinion system was created by me, it would be more accurate to say it was **discovered**. It possesses far too many wondrous coincidences and structural symmetries, leaving numerous areas highly deserving of deeper exploration and rigorous research. For instance:

* 1. Can the initial concept of "extracting the square root of an angle" be mathematically validated and sustained? Conversely, what about exponentiation operations applied to angles?
* 2. This hypercomplex system is merely built upon assumptions optimized for calculation convenience. We could also experiment with modifying the foundation to $j^2 = 1 + i$ (which represents a $45^\circ$ angle on the \(Xi\)-plane); by doing so, we would obtain the table shown below:
* $j = (1 + i)/j$
* $j^2 = 1 + i$
* $j^3 = j + ij$
* $j^4 = 1 + i + i(1 + i) = 2i$
* $j^5 = 2ij$
* $j^6 = 2(1 + i) = 2 + 2i$
* $j^7 = 2j + 2ij$
* $j^8 = 2(1 + i) + 2i(1 + i) = 4i$
* $j^9 = 4ij$ 

It can be observed that the system loses its 8-fold cyclic periodicity, and the \(ij\) term becomes decoupled—unable to be substituted—yet it exhibits a regularly increasing pattern. Could it be that only the $90^\circ$ orientations (\(i\) or \(-i\)) on the Gaussian complex plane possess this special property? This remains an open question.
If the orientation is set to $0^\circ$ or $180^\circ$, it corresponds either to the standard imaginary number configuration with $j^2 = -1$, or a split-complex number configuration resembling $j^2 = 1$. These are hypercomplex number systems that have already been established and developed.

*  3. We could also abandon the assumption that the \(j\)-axis remains perpendicular to the Gaussian complex plane. For instance, we could configure it to tilt at specific non-orthogonal angles, such as $30^\circ, 45^\circ, 54.74^\circ / 35.26^\circ, 60^\circ, 90^\circ$, or even the Earth's axial tilt of $23.5^{\circ }$. Although I have yet to formulate a mathematical representation for this approach, it undoubtedly promises to be another fascinating experiment.
*  4. The precise algebraic nature of the \(ij\) element remains an active area of investigation. It appears to resist analysis via standard Clifford Algebra. According to the foundational rules of Clifford Algebra, the outer product of identical vectors vanishes; this would imply that $j \times j \times j = ij =0$. However, since \(ij\) itself is defined as the product of two distinct orthogonal vectors, \(i\) and \(j\), this leads to a structural contradiction.
Whether the element $ij = j^3$ (the \(d\)-axis) truly qualifies as a fourth-dimensional vector remains a pivotal question. Gemini's perspective is as follows:
> On the level of a vector space (the additive aspect): It absolutely qualifies as a fourth-dimensional vector basis. This is because the \(ij\)-axis cannot be synthesized through any linear combination of the first three > axes \((a, b, c)\). Throughout sequential arithmetic and Gaussian elimination, it must independently occupy the fourth linear dimension column.

Therefore, the current research direction should perhaps shift toward exploring the mathematical meaning of non-vector algebraic cubing (self-multiplying 3 times). I might intend to approach this from the perspective of angles (even though this does not strictly conform to current mathematical frameworks) or trigonometric functions.
* 5. Final Remarks: For the next stage of my work, I plan to dedicate time to investigating the project defined by $ ^2 = -i$. Since its configuration differs from this hypercomplex system by only a single negative sign, I am eager to discover whether it will generate a mathematical complementarity with the current system.

From C.H. Lee, 2026.08.04

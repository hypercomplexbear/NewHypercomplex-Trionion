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

**Conclusion from Observation**: By applying the distributive law of standard complex numbers to compare the corresponding terms of the matrices on both sides (for example, expanding the first term on the left side yields $z_1(z_2+z_3) + w_1(\bar{w}_2+\bar{w}_3)$）, the structure after expanding the parentheses is perfectly identical to the right-hand expression. The distributive structure is thus proven.

---

#### 3.2.2.2 tructural Observation of the Associative Law (Associativity)

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

**Conclusion from Observation**: Following the same logic as the distributivity proof, since the results for the first row and first column are identical, it is reasonable to infer under the same matrix operation rules that all other rows and columns will yield the same results. The associative structure is thus proven.

---


* 

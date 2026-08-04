> 🌐 [English Version of README available here](./README_EN.md)

### 作者前言

大家好，很難一言以蔽之為什麼我會開發出這個新的超複數。只能說在一次次的巧合下，我這個平凡人開始了研究超複數的旅程。

我並不是什麼厲害的數學家，所以很長一段開發的時間，我靠 Gemini 教我高等數學的知識。不過數學是門高深的學問，光靠 AI 學習是有限的。所以如果有不合數理的部分還請大家見諒。

> 💡 **核心思想：**
> 目前大眾普遍認為創造三元數幾乎不可能，不過我覺得超複數的 3, 5, 7 維度可能仍然存在有特殊的意義價值。畢竟 3, 5, 7 都是質數。作為一個民科，寫出嚴謹並發表數學相關的論文是難如登天的。所以作為替代方案，我在gemini協助下創建了新的超複數的計算沙盒程式，並放在GitHub來讓大家可以研究它。Readme則紀錄並存放了至今研究的結果。希望你們會喜歡!文章中有部分公式是我將想法傳給gemin，再借助gemini的推導而成。

以下解說推導過程。

## 一. 新的超複數-三元數的開發原理

### 1.1 新的超複數採用對角度開根號的奇異想法當作起點。假設如下:

*   **空間坐標軸設定**：假設空間中有三條倆倆互相垂直的軸線，即實數軸X、虛數軸i，以及虛數軸j。
*   **複數平面映射**：實數軸X與虛數軸i構成的平面即為高斯複數平面，而j軸垂直於該平面。
*   **角度開根號公理**：令Xi平面上i的主幅角90度開根號等同於ij平面j的主幅角90度。則求得 $j^2 = i$。
*   **空間幾何旋轉意義**：如果說 $i^2 = -1$ 是讓數字經由二維平面旋轉回實數軸的動作，那 $j^2 = i$ 可以理解為從i點轉向三維空間中的j軸，再轉回i點的動作。
對於\(j\)的次方列表如下:
* $j = i/j$
* $j^2 = i$
* $j^3 = ij$
* $j^4 = i^2 = -1$
* $j^5 = -j$
* $j^6 = j^2 \times i^2 = -i$
* $j^7 = - ij$
* $j^8 = 1$
* $j^9 = j$

對於創造三元數來說，無法避免的會碰到兩個虛數相乘的狀況\(ij\)，不過這個系統可以用 $j^3$ 來化解。以下是 \(ij\)的次方表(為了方便書寫，以下文章將設 $j^3 = ij = k$:
* $k^1 = j^3$
* $k^2 = -i$
* $k^3 = j$
* $k^4 =- i^2 = -1$
* $k^5 = -j^3$
* $k^6 = j^2 = i$
* $k^7 = - j$
* $k^8 = 1$
* $k^9 = j^3$

另外提供各 \(j\)次方乘i的列表:
* $ji=j^3$
* $j^2*i = -1$
* $j^3*i = -j$
* $j^4*i = -i$
* $j^5*i = -ij$
* $j^6*i = 1$
* $j^7*i = j$
* $j^8*i= i$
* $j^9*i= ij$


### 1.2. 設三元數T = $a + bi + cj + dk$(a, b, c, d為實數)。根據上述列表可以觀察到幾個特性:

*   虛數單位 \(j\) 自乘 8 次會循環歷經每一個方向，並直接回到它的起點。\(k\) 的代數運算也遵循完全相同的規則。
*   巧合的是，克里福德代數（Clifford algebra）中的 3D 空間恰好需要 8 個基底元素。
*    雖然它是三元數（Trionion），但它依然優美地平行對應了凱萊-迪克森構造中固有的 2 的冪次——在該構造中， $2^3$ 正好給了我們 8 個維度。簡單說這個超複數:皮是三元數，骨是四元數。
*   我不確定這個超複數該屬於群環論的哪個地位。不過從其結構來看，它應該可以同時滿足乘法的結合律與分配律。但與標準四元數（quaternions）不同，這個系統實際上是可交換的（commutative），因為 $ij = ji = j^3$ 。後面文章會試圖證明。
*   有趣的是ij 似乎與左手或右手定則有關。它的確切功能目前仍是一個謎。後面文章會試圖分析。

### 1.3. 矩陣映射(由gemini協助推導)

三元數T = $a + bi + cj + dk$可以透過一個 $2 \times 2$ 的複數矩陣 $T$ 進行幾何映射，其完整矩陣表示法定義如下：

<div align="center">

$$ \text{The Matrix of } T = a \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \end{bmatrix} + b \begin{bmatrix} i & 0 \\\\ 0 & i \end{bmatrix} + c \begin{bmatrix} 0 & i \\\\ 1 & 0 \end{bmatrix} + d \begin{bmatrix} 0 & -1 \\\\ i & 0 \end{bmatrix} = \begin{bmatrix} a + bi & ci - d \\\\ c + di & a + bi \end{bmatrix} $$

</div>

---

## 二. 零因子探討(Derivation of the Zero Divisor)

### 2.1. 零因子的代數恆等式推導(由gemini協助推導) 

以下是gemini對我介紹的零因子推導概念:
當此映射矩陣的行列式值（Determinant）為 0 時，空間會產生幾何退化，出現零因子。透過行列式展開式進行精確推導：

<div align="center">

$$ \det(T) = (a + bi)^2 - (ci - d)(c + di) = (a^2 - b^2 + 2cd) + (2ab - c^2 + d^2)i $$

若要使該元素成為零因子，其实部與虛部必須同時為 0，從而得到複數平面上的聯立奇異點方程組：

*   $a^2 - b^2 + 2cd = 0 \implies a^2 - b^2 = -2cd$
*   $2ab - c^2 + d^2 = 0 \implies c^2 - d^2 = 2ab$

此時，利用等量公理建立過渡式： $(a^2 - b^2)^2 + (2ab)^2 = (-2cd)^2 + (c^2 - d^2)^2$

代入代數恆等式 $(x-y)^2 + 4xy = (x+y)^2$，上式可簡化為：  

$$ (a^2 + b^2)^2 = (c^2 + d^2)^2 \implies a^2 + b^2 = c^2 + d^2 $$

</div>

### 結論：零因子幾何滿足要件 (The Singular Conditions)

綜上所述，任何元素若要觸發本空間的零因子退化（度規奇異點），其四維坐標必須嚴格且完美地滿足以下聯立方程組要件：

<div align="center">

$$ \begin{cases} a^2 + b^2 = c^2 + d^2 \\\\ a^2 - b^2 = -2cd \\\\ c^2 - d^2 = 2ab \end{cases} $$

舉例: $$(1 + i + \sqrt{2}j) \times (1 + i - \sqrt{2}j)$$

</div>

### 2.2. 尋找特定的冪零元 (Nilpotent Element)(由gemini協助推導)

gemini建議我可以試圖探討是否存在非零的**冪零元（Nilpotent Element）**。即是否存在一組非零坐標，其映射矩陣 $M$ 能滿足：

<div align="center">

$$M^2 = \mathbf{0}$$

</div>

目前已知完全體映射矩陣如下：

$$M = \begin{bmatrix} a + bi & ci - d \\\\ c + di & a + bi \end{bmatrix}$$

以下為gemini的協助推導原文: 
由於該矩陣的主對角線元素完全相同（皆為 $a + bi$），根據線性代數中 $2 \times 2$ 矩陣的公理性質：若 $M^2 = \mathbf{0}$，則該矩陣的**跡（Trace，主對角線相加）**必須為 0，且其**行列式（Determinant）**也必須為 0。

#### 跡為 0 的必要條件：
透過對角線元素相加建立方程：
<div align="center">

$$ \text{Tr}(M) = (a + bi) + (a + bi) = 2(a + bi) = 0 \implies a = 0 \text{ 且 } b = 0 $$

</div>

#### 代入零因子黃金等式進行幾何約束
當實部與第一虛軸皆被鎖定為 $a = 0, b = 0$ 時，我們將此條件代入前一章節由聯立方程式所導出的**第一行零因子等式**：

$a^2 + b^2 = c^2 + d^2$。進行代數代入：

<div align="center">

$$ 0^2 + 0^2 = c^2 + d^2 \implies c^2 + d^2 = 0 $$

</div>

因(a, b, c, d為實數)，兩個平方數相加若要等於 0，唯一可能的實數解為零，故：
<div align="center">

$$ c = 0 \text{ 且 } d = 0 $$

</div>

#### 冪零元論證之結論 (Conclusion on Nilpotency)

> 倘若要求本超複數空間的特定映射矩陣形式滿足 $M^2 = \mathbf{0}$，在邏輯閉環下反推得到的唯一解只能是 $a = b = c = d = 0$，亦即**只有零矩陣（Null Matrix）本身**。
> 
> **結論：在非零的實數係數集合下，本自訂結構的超複數空間「不存在非零的冪零元」。

</div>

### 2.3. 尋找冪等元的互補組 (Idempotent Complements)(由gemini協助推導)

在同一個推導對話中gemini建議我可以尋找另一個特定零因子**冪等元（Idempotent Element）** $P$，滿足 $P^2 = P$（即拓撲學中的**投影矩陣**）。

根據代數定理，若 $P^2 = P$，則它與它的**互補組 $I - P$** 相乘，結果必定為零矩陣：

<div align="center">

$$ P(I - P) = \mathbf{0} $$

</div>

以下為gemini的協助推導原文:
同樣地，對於一個 $2 \times 2$ 的特定矩陣，若要滿足 $P^2 = P$ 的幾何約束，其**行列式（Determinant）**必須為 0，且其**跡（Trace）**必須精確為 1。

#### 跡為 1 的必要條件
利用對角線分量相加建立公理方程：
<div align="center">

$$ \text{Tr}(P) = 2(a + bi) = 1 \implies a = \frac{1}{2}, \; b = 0 $$

</div>

#### 利用零因子聯立方程求解空間坐標 $(c, d)$
將求得的實部與第一虛軸約束 $a = \frac{1}{2}, b = 0$ 代入前述之零因子兩大核心要件中進行聯立解析：

*   **條件一**： $a^2 - b^2 = -2cd \implies \left(\frac{1}{2}\right)^2 - 0 = -2cd \implies cd = -\frac{1}{8}$
*   **條件二**： $c^2 - d^2 = 2ab \implies c^2 - d^2 = 2\left(\frac{1}{2}\right)(0) = 0 \implies c^2 = d^2$

#### 代數符號與異號性分析：
1.  由條件二 $c^2 = d^2$ 可知，在幾何長度上 $c = d$ 或 $c = -d$。
2.  由條件一 $cd = -\frac{1}{8}$ 為**負數**可知，$c$ 與 $d$ 必須**異號**。因此在空間拓撲上必滿足： $c = -d$。

我們將 $c = -d$ 代入條件一：
<div align="center">

$$ -d^2 = -\frac{1}{8} \implies d = \pm \frac{1}{\sqrt{8}} = \pm \frac{1}{2\sqrt{2}} $$

</div>

此處我們精確選取其中一組複數空間解：
<div align="center">

$$ c = \frac{1}{2\sqrt{2}}, d = - \frac{1}{2\sqrt{2}} $$

</div>

#### 成功構造「冪等元 & 互補組」矩陣

將這組精密的四維幾何坐標 $(a, b, c, d) = \left(\frac{1}{2}, 0, \frac{1}{2\sqrt{2}}, -\frac{1}{2\sqrt{2}}\right)$ 代入完全體矩陣中，我們成功構造出本超複數空間特有的**投影矩陣 $P$**：

<div align="center">

$$ P = \begin{bmatrix} \frac{1}{2} & \frac{1}{2\sqrt{2}}i + \frac{1}{2\sqrt{2}} \\\\ \frac{1}{2\sqrt{2}} - \frac{1}{2\sqrt{2}}i & \frac{1}{2} \end{bmatrix} $$

</div>

此時，透過單位矩陣 $I$ 減去 $P$，求得其**互補組矩陣 $I - P$** 為：

<div align="center">

$$ I - P = \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \end{bmatrix} - \begin{bmatrix} \frac{1}{2} & \frac{1}{2\sqrt{2}}i + \frac{1}{2\sqrt{2}} \\\\ \frac{1}{2\sqrt{2}} - \frac{1}{2\sqrt{2}}i & \frac{1}{2} \end{bmatrix} = \begin{bmatrix} \frac{1}{2} & -\frac{1}{2\sqrt{2}}i - \frac{1}{2\sqrt{2}} \\\\ -\frac{1}{2\sqrt{2}} + \frac{1}{2\sqrt{2}}i & \frac{1}{2} \end{bmatrix} $$

</div>

### 構造論證之結論 (Significant Conclusion)

> 這兩個由複數與無理數精細交織而成的非零矩陣 **$P$** 與 **$(I - P)$**，在本超複數空間中構成了一組**完美特定形式的零因子對（Zero-Divisor Pair）**！
> 
> **它們各自皆非零元素，但它們在幾何代數空間中相乘的結果「絕對會是完美的零矩陣 0」！

</div>

### 2.4. 有趣的零因子 (獨自推導)

上述的冪零元與冪等元在數學上可能有重要作用所以gemini建議我推導。不過我個人對另一組零因子比較有興趣。我們可以回到一開始的零因子滿足要件:

$$ \begin{cases} a^2 + b^2 = c^2 + d^2 \\\\ a^2 - b^2 = -2cd \\\\ c^2 - d^2 = 2ab \end{cases} $$

當d = 0 時，可以求得 $a = b, c = \pm\sqrt{2}a$，或是當 a = 0 時，可以求得 $c = d, b = \pm\sqrt{2}c$。

觀察第一種形式，我用基本單位長 a = 1 列出一組零因子:(1, i, $\sqrt{2}j$)，並標記在空間中座標點位，會發現一些有趣的事!

這個點用畢氏定理可以與x軸跟原點畫出一個四面體，並有以下特性:
* 這個四面體每一個面都是直角三角形。
* 這個四面體裡面擁有所有特殊的角度(30度，45度，54.74度/35.26度, 60度，90度)。其中54.74度/35.26度gemini稱為魔術角度，在許多科技應用上可以消除干擾訊號(例如核磁共振MRI)，這是巧合嗎?
* 這個四面體的每一個邊長可表示為跟號數列: ( $\sqrt{1}$, $\sqrt{2}$, $\sqrt{3}$, $\sqrt{4}$ )，也就是**席奧多羅斯數列 (Spiral of Theodorus)**
* gemini告訴我這個超複數系統的零因子可以視為是光錐的一種。我不太了解怎麼突然跟閔考斯基（Hermann Minkowski）時空理論的光錐連上關係了，雖然它有解釋給我聽就是了。45度角似乎是光錐的一個重要角度。
* 有趣的事是這組零因子(1, i, $\sqrt{2}j$)的伴隨零因子為(1, i, - $\sqrt{2}j$)，也就是2.1章節的例子。這兩組座標點對X軸互相映射，模長夾角均為45度角。這是巧合嗎?構成了一個局部光錐的形狀?
所以合理推論: T = a + ai + $\sqrt{2}aj$ 的每個點連成的線與 T = a + ai - $\sqrt{2}aj$ 的每個點連成的線構成了兩條通過原點的X型零因子界線，而它們巧合地與光錐形狀相似?我們有辦法在空間中找到其他的零因子線並觀察全部的零因子線是否構成一個完整的光錐嗎?這將是有趣又困難的挑戰!

</div>

## 三. 代數公理系統與乘法度規表 (Algebraic Foundations)
設有兩任意三元數元素 $X_1 = a_1 + b_1i + c_1j + d_1k$ 與 $X_2 = a_2 + b_2i + c_2j + d_2k$。其四則運算公理定義如下：

### 3.1. 任意兩三元數加法與減法展開式 (獨自推導)

既然大家都知道兩任意複數的加減法公理是實部加實部，虛部加虛部，那這個三元數想當然也會是如此。如下表示:

*  **加法:實部加實部，虛部加虛部(a1 + a2) + (b1 + b2)i + (c1 + c2)j + (d1 + d2)k

*  **減法:實部減實部，虛部減虛部(a1 - a2) + (b1 - b2)i + (c1 - c2)j + (d1 - d2)k

---
### 3.2. 任意兩三元數乘法展開式 (獨自推導) 
根據基底相乘的代數度規表，兩者相乘之積 $X_3 = X_1 \times X_2 = a_3 + b_3i + c_3j + d_3k$ 的四維分量精確解析式如下：

*   **實部 (a3)**： $a_3 = a_1a_2 - b_1b_2 - c_1d_2 - d_1c_2$
*   **i 軸 (b3)**： $b_3 = a_1b_2 + b_1a_2 + c_1c_2 - d_1d_2$
*   **j 軸 (c3)**： $c_3 = a_1c_2 - b_1d_2 + c_1a_2 - d_1b_2$
*   **k 軸 (d3)**： $d_3 = a_1d_2 + b_1c_2 + c_1b_2 + d_1a_2$

#### 註:我觀察這個展開式，發現它與哈密頓四元數 (Hamilton's quaternion )只差幾個正負號。沒想到差幾個正負號結果會差那麼多!
---

#### **3.2.1. 試證 ij = ji**

**證明方式一:利用乘法展開式(gemini提議的證明方法)**
假設空間中有兩元素X與Y， $X = i \times j$ 與 $Y = j \times i$ ，嘗試對X與Y求得在空間中的坐標位置。

當計算 $X = i \times j$ 時：
第一個元素僅有 $i$ 軸分量 $b_1 = 1$（其餘為 0）；第二個元素僅有 $j$ 軸分量 $c_2 = 1$（其餘為 0）。代入分量展開式：
*   實部 $a_3 = 0$
*   $i$ 軸 $b_3 = 0$
*   $j$ 軸 $c_3 = 0$
*   $k$ 軸 $d_3 = b_1 \times c_2 = 1 \times 1 = 1$

<div align="center">

$$ X = i \times j = \begin{bmatrix} 0, & 0, & 0, & 1 \end{bmatrix}^T = k $$

</div>

當計算 $Y = j \times i$ 時：
第一個元素僅有 $j$ 軸分量 $c_1 = 1$（其餘為 0）；第二個元素僅有 $i$ 軸分量 $b_2 = 1$（其餘為 0）。代入分量展開式：
*   實部 $a_3 = 0$
*   $i$ 軸 $b_3 = 0$
*   $j$ 軸 $c_3 = 0$
*   $k$ 軸 $d_3 = c_1 \times b_2 = 1 \times 1 = 1$

<div align="center">

$$ Y = j \times i = \begin{bmatrix} 0, & 0, & 0, & 1 \end{bmatrix}^T = k $$

</div>

**結論**：由於兩者計算後共享完全相同的 4D 空間幾何坐標，由代數等量公理，正面得證： $ij = ji$。


**證明方式二:代數反證法(獨自推導)**

假設 $$ij \neq ji$$

在不等式的兩端，同時執行「左乘 $i$、右乘 $j$ 」操作：
*   **左邊項展開**： $i \cdot (ij) \cdot j = (i \cdot i) \cdot (j \cdot j) = (-1) \cdot (i) = -i$
*   **右邊項展開**： $i \cdot (ji) \cdot j = j^2 \times j \times j^2 \times j = j^6 = -i$

得到 $$-i  \neq -i$$，產生自身不等於自身的邏輯矛盾。故得證 $$ij = ji$$。


#### 3.2.2 **試證本超複數系統的乘法滿足結合律、交換律與分配律（在非零因子域內）。(gemni協助推導)**

Gemini跟我說如果超複數已經可以建立 $2 \times 2$ 複數矩陣，那基本上可以用 **「矩陣同構（Matrix Isomorphism）」定理與環論（Ring Theory）之同構基本定理** 證明這個三元數可以滿足乘法結合律、交換律與分配律，而不需應用代數展開冗長的運算結果。
這對我來說當然是件好事，不過我覺得可能還是要由數學專家來論定比較適合。所以我決定還是乖乖嘗試證明。經過討論，我們決定用簡化的矩陣來呈現證明，如下:

為了讓三大定律的結構最直觀地呈現，首先定義完整映射矩陣 $T$ 與精簡複數符號 $z, w$ 的對應關係。令：

<div align="center">

$$ \text{The Matrix of } T = a \begin{bmatrix} 1 & 0 \\\\ 0 & 1 \end{bmatrix} + b \begin{bmatrix} i & 0 \\\\ 0 & i \end{bmatrix} + c \begin{bmatrix} 0 & i \\\\ 1 & 0 \end{bmatrix} + d \begin{bmatrix} 0 & -1 \\\\ i & 0 \end{bmatrix} = \begin{bmatrix} a + bi & ci - d \\\\ c + di & a + bi \end{bmatrix} = \begin{bmatrix} z & w \\\\ \bar{w} & z \end{bmatrix} $$

</div>

在此簡化結構中， $z = a+bi$, $w = ci-d$, $\bar{w} = c+di$（此處 $\bar{w}$ 分量天生滿足本空間度規之共軛形式）。所有的 $z_n, w_n$ 皆為標準二維平面之複數元素，天生滿足標準交換與結合律。

透過任意三個超複數矩陣 $T_A, T_B, T_C$ 的簡寫區塊形式，我們可以直接透過括號位置來觀察其代數拓撲：

---

#### 矩陣區塊符號顯式結構對比 (Simplified Structural Verification)

為了讓三大定律的結構最直觀地呈現，我們拋棄冗長的分量字母，將任意三個超複數矩陣 $T_A, T_B, T_C$ 直接簡化為由複數代數項組成的超精簡區塊形式：

$$ T_A = \begin{bmatrix} z_1 & w_1 \\\\ \bar{w}_1 & z_1 \end{bmatrix}, \quad T_B = \begin{bmatrix} z_2 & w_2 \\\\ \bar{w}_2 & z_2 \end{bmatrix}, \quad T_C = \begin{bmatrix} z_3 & w_3 \\\\ \bar{w}_3 & z_3 \end{bmatrix} $$

其中 $z_n, w_n$ 皆為標準二維平面之複數元素，天生滿足標準交換與結合律。透過這三個簡化矩陣的括號位置，我們可以直接觀察其代數拓撲：

#### 3.2.2.1 分配律結構觀察 (Distributivity)
我們將左端項 $T_A(T_B + T_C)$ 與右端項 $T_AT_B + T_AT_C$ 進行結構並列：

*   **左端項（括號內先加）**：
<div align="center">

$$ \begin{bmatrix} z_1 & w_1 \\\\ \bar{w}_1 & z_1 \end{bmatrix} \times \left( \begin{bmatrix} z_2 & w_2 \\\\ \bar{w}_2 & z_2 \end{bmatrix} + \begin{bmatrix} z_3 & w_3 \\\\ \bar{w}_3 & z_3 \end{bmatrix} \right) = \begin{bmatrix} z_1 & w_1 \\\\ \bar{w}_1 & z_1 \end{bmatrix} \begin{bmatrix} (z_2+z_3) & (w_2+w_3) \\\\ (\bar{w}_2+\bar{w}_3) & (z_2+z_3) \end{bmatrix} $$

</div>

*   **右端項（拆開相乘再加）**：
<div align="center">

$$ = \begin{bmatrix} z_1z_2 + w_1\bar{w}_2 & z_1w_2 + w_1z_2 \\\\ \bar{w}_1z_2 + z_1\bar{w}_2 & \bar{w}_1w_2 + z_1z_2 \end{bmatrix} + \begin{bmatrix} z_1z_3 + w_1\bar{w}_3 & z_1w_3 + w_1z_3 \\\\ \bar{w}_1z_3 + z_1\bar{w}_3 & \bar{w}_1w_3 + z_1z_3 \end{bmatrix} $$

</div>

**觀察結論**：利用標準複數的分配律對比兩端矩陣的對應項（例如左端第一項乘開為 $z_1(z_2+z_3) + w_1(\bar{w}_2+\bar{w}_3)$），其括號展開後的結構與右端項完全相等。**分配律結構得證**。

---

#### 3.2.2.2 結合律結構觀察 (Associativity)
欲驗證 $(T_A \times T_B) \times T_C \stackrel{?}{=} T_A \times (T_B \times T_C)$，我們直接觀察相乘後的括號特徵：

*   **左端項結構 (先結合前兩者)**：
<div align="center">

$$ \left( \begin{bmatrix} z_1 & w_1 \\\\ \bar{w}_1 & z_1 \end{bmatrix} \begin{bmatrix} z_2 & w_2 \\\\ \bar{w}_2 & z_2 \end{bmatrix} \right) \times T_C = \begin{bmatrix} (z_1z_2 + w_1\bar{w}_2) & (z_1w_2 + w_1z_2) \\\\ (\bar{w}_1z_2 + z_1\bar{w}_2) & (\bar{w}_1w_2 + z_1z_2) \end{bmatrix} \begin{bmatrix} z_3 & w_3 \\\\ \bar{w}_3 & z_3 \end{bmatrix} $$

</div>

*   **右端項結構 (先結合後兩者)**：
<div align="center">

$$ T_A \times \left( \begin{bmatrix} z_2 & w_2 \\\\ \bar{w}_2 & z_2 \end{bmatrix} \begin{bmatrix} z_3 & w_3 \\\\ \bar{w}_3 & z_3 \end{bmatrix} \right) = \begin{bmatrix} z_1 & w_1 \\\\ \bar{w}_1 & z_1 \end{bmatrix} \begin{bmatrix} (z_2z_3 + w_2\bar{w}_3) & (z_2w_3 + w_2z_3) \\\\ (\bar{w}_2z_3 + z_2\bar{w}_3) & (\bar{w}_2w_3 + z_2z_3) \end{bmatrix} $$

</div>

*   **左端項第一列第一行展開結果**：
<div align="center">

$$ (z_1z_2 + w_1\bar{w}_2)z_3 + (z_1w_2 + w_1z_2)\bar{w}_3 = (z_1z_2)z_3 + (w_1\bar{w}_2)z_3 + (z_1w_2)\bar{w}_3 + (w_1z_2)\bar{w}_3 $$

</div>

*   **右端項第一列第一行展開結果**：
<div align="center">

$$ z_1(z_2z_3 + w_2\bar{w}_3) + w_1(\bar{w}_2z_3 + z_2\bar{w}_3) = z_1(z_2z_3) + z_1(w_2\bar{w}_3) + w_1(\bar{w}_2z_3) + w_1(z_2\bar{w}_3) $$

</div>

**觀察結論**：同理分配律論證，既然第一行第一列結果一樣，在相同矩陣運算規則下，合理推論其他行列也會是同樣結果。故**結合律結構得證**。

---

#### 3.2.2.3 交換律結構觀察 (Commutativity)
矩陣乘法並不能符合交換率，gemini反而給我一個錯誤的論證。所以我要求直接用乘法展開式論證，如下表示:

*   **$X_1 \times X_2$ 的四維展開分量**：
    *   實部 $a_3 = a_1a_2 - b_1b_2 - c_1d_2 - d_1c_2$
    *   $i$ 軸 $b_3 = a_1b_2 + b_1a_2 + c_1c_2 - d_1d_2$
    *   $j$ 軸 $c_3 = a_1c_2 - b_1d_2 + c_1a_2 - d_1b_2$
    *   $k$ 軸 $d_3 = a_1d_2 + b_1c_2 + c_1b_2 + d_1a_2$

---

*   **$X_2 \times X_1$ 的四維展開分量（將下標 1 與 2 完全對調）**：
    *   實部 $a_3' = a_2a_1 - b_2b_1 - c_2d_1 - d_2c_1$
    *   $i$ 軸 $b_3' = a_2b_1 + b_2a_1 + c_2c_1 - d_2d_1$
    *   $j$ 軸 $c_3' = a_2c_1 - b_2d_1 + c_2a_1 - d_2b_1$
    *   $k$ 軸 $d_3' = a_2d_1 + b_2c_1 + c_2b_1 + d_2a_1$

既然公式內部的所有分量係數（ $a_n, b_n, c_n, d_n$ ）皆為**純實數（Real Numbers）**，在實數體中，乘法天生完美滿足交換律。沒有理由懷疑 $a_1a_2 \neq a_2a_1$ ，故**交換律結構得證**。


---


### 3.3. 任意兩三元數除法運算 

一開始我沒辦法利用共軛複數找出代數的除法公式，但是我又想知道這個三元數到底能不能做除法，所以我求助gemini，請它另想辦法，經過討論，它幫我想了以下的解方，讓我們可以寫出程式碼做除法運算。
以下為gemini的協助推導: 

#### 線性代數方程組轉換
給定兩超複數 $A = a_1 + b_1i + c_1j + d_1k$ 與 $B = a_2 + b_2i + c_2j + d_2k$，欲求解除法結果 $C = X_a + X_bi + X_cj + X_dk$，使得：

<div align="center">

$$ \frac{A}{B} = C \implies A = C \times B $$

</div>

根據前述之超複數乘法定義，將 $C \times B$ 的各維度分量展開，並令其等於 $A$ 的對應分量。由於未知數為 $C$ 的分量 $(X_a, X_b, X_c, X_d)$，我們可以將此聯立方程組重組為一個標準的線性方程組： $M \cdot C = A$，其中 $M$ 為由分母 $B$ 的分量所構成的 $4 \times 4$ 空間幾何矩陣。

#### 系統專屬的 4x4 除法矩陣結構
完全對齊乘法度規，動態建構之增廣矩陣 $M$ 形式如下（最後一行為常數項，即分子 $A$ 的分量）：

<div align="center">

$$ M = \begin{bmatrix} 
a_2 & -b_2 & -d_2 & -c_2 & \mathbf{a_1} \\\\ 
b_2 & a_2 & c_2 & -d_2 & \mathbf{b_1} \\\\ 
c_2 & -d_2 & a_2 & -b_2 & \mathbf{c_1} \\\\ 
d_2 & b_2 & b_2 & a_2 & \mathbf{d_1} 
\end{bmatrix} $$

</div>

#### 利用高斯-約旦消去法求解 (Gauss-Jordan)
為了求解此 4×5 的增廣矩陣，後端演算法實作了標準的列運算（Row Operations），以下直接附上原始python代碼給大家檢驗：

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

#### 在沙盒計算機系統中，對於實數與虛數i做了除法運算可以得到正確答案，故合理推論這個程式碼可以為我們正確求出三元數除法解。我們可以從倒數來觀察:
設 $j \times j^{-1}$ = 1 ， 則利用沙河計算機可以求得j的倒數為 -ij ； 設 $ij \times (ij)^{-1}$ = 1， 則利用沙河計算機可以求得ij的倒數為-j，與手算結果一致。


#### (補充)重大突破：補上法代數共軛除法 (獨自推導)

**我嘗試了一陣子，終於用手算出如何讓代數分母變成實數的方法，以下進行解說:**

給定兩超複數 $A = a_1 + b_1i + c_1j + d_1k$ 與 $B = a_2 + b_2i + c_2j + d_2k$。
普通複數為了讓分母變成實數，所以要將分母乘以共軛複數。不過在這個三元數系統並不容易，因為一開始的設定是 $j^2 = i$，根據乘法展開式:

$X_2 (a_2 + b_2i + c_2j + d_2k)$ $\times$ $X_2'(a_2 - b_2i - c_2j - d_2k)$ = 

*   **實部 (a3)**： $a_3 =  a_2a_2 + b_2b_2 + c_2d_2 + d_2c_2$
*   **i 軸 (b3)**： $b_3 = -a_2b_2 + b_2a_2 - c_2c_2 + d_2d_2$
*   **j 軸 (c3)**： $c_3 = -a_2c_2 + b_2d_2 + c_2a_2 + d_2b_2$
*   **k 軸 (d3)**： $d_3 = -a_2d_2 - b_2c_2 - c_2b_2 + d_2a_2$

可以觀察到j項跟ij項並沒有被互相抵銷。不過這個超複數有一個奇妙的超對稱性，所以我決定嘗試調換係數來試試看!
**如果能讓分母消去j項跟ij項變成x +yi的形式，那就可以做二次共軛的處理!** 
嘗試結果如下紀錄:

對於分母 $B = a_2 + b_2i + c_2j + d_2k$，若將分子與分母同時乘以共軛因子 $B' = -b_2 + a_2i + d_2j - c_2k$。根據乘法度規展開式代入：

*   **實部 (a3)**： $a_3 = -a_2b_2 - b_2a_2 + c_2c_2 - d_2d_2$
*   **i 軸 (b3)**： $b_3 = +a_2a_2 - b_2b_2 + c_2d_2 + d_2c_2$
*   **j 軸 (c3)**： $c_3 = +a_2d_2 + b_2c_2 - c_2b_2 - d_2a_2$
*   **k 軸 (d3)**： $d_3 = -a_2c_2 + b_2d_2 + c_2a_2 - d_2b_2$

可以觀察到j項跟ij項被完全消去，只留下 
<div align="center">
    
$$ B \times B' = \left( -2a_2b_2 + c_2^2 - d_2^2 \right) + \left( a_2^2 - b_2^2 + 2c_2d_2 \right)i $$

</div>

**現在讓它做二次共軛複數讓分母完全實數化:**

* 上ㄧ階段的運算結果，分子是: $(a_1 + b_1i + c_1j + d_1k)$ $\times$ $(-b_2 + a_2i + d_2j - c_2k)$ 
* 分母是 $$B \times B' = \left( -2a_2b_2 + c_2^2 - d_2^2 \right) + \left( a_2^2 - b_2^2 + 2c_2d_2 \right)i$$

根據共軛複數的規則: $(x - yi)*(x + yi) = x^2 + y^2$。分母會收斂為純實數：

<div align="center">

$$ x^2 + y^2 = \left( -2a_2b_2 + c_2^2 - d_2^2 \right)^2 + \left( a_2^2 - b_2^2 + 2c_2d_2 \right)^2 $$

</div>

故，最終結果為:

* 分子: $(a_1 + b_1i + c_1j + d_1k)$ $\times$ $(-b_2 + a_2i + d_2j - c_2k)$ $\times$ $(( -2a_2b_2 + c_2^2 - d_2^2) - ( a_2^2 - b_2^2 + 2c_2d_2)i)$

* 分母為: $$( -2a_2b_2 + c_2^2 - d_2^2)^2 + ( a_2^2 - b_2^2 + 2c_2d_2 )^2 $$

**這裡有一個有趣的地方: 括弧裡面的式子本身就是矩陣的行列式(請參考2.1章節)。**
gemini給了我以下的結論:
#### 幾何學意義與解析除法閉環
此結果展現了極致的代數美感。最終分母變成了兩個「零因子特徵式」的平方和：
1.  當且僅當分母 $B$ 本身就是**零因子**時， $A$ 與 $B$ 才會同時為 0，導致分母為 0（此時除法確實無解，完美對齊零因子定義）。
2.  在其餘任何正常坐標下，此分母**永遠為正實數**。

不知道大家是否同意gemini的說法?

## 四. 開根號

除了四則運算外，我認為最重要也最關心的事就是能不能開根號!開根號可以創造許多事，例如虛數或是這個三元數系統本身。而我認為利用高斯或高斯-約旦消去法求解是最有成功的可能性(也最方便)，所以我請gemini幫忙推導寫出python的程式碼。
原始程式碼如下，提供給大家檢視:

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


#### Gemini數值求解流程解說:
根據gemini的說法，它使用了高階數值分析中的 **牛頓-拉弗森矩陣迭代法 (Newton-Raphson Matrix Iteration)** 與 **雅可比偏微分矩陣 (Jacobian Matrix)** 做運算。而每次迭代中，系統計算當前殘差向量 $Y = Q - X_{\text{current}}^2$，並呼叫高斯消去法運算，解出空間修正向量 $dX$ ($M \cdot dX = Y$)，對坐標進行修正。通常只需 5~6 次迭代即可在浮點數極限下達到 $10^{-12}$ 的極高代數精度。老實說我是不太懂這麼難的數學理論與程式碼，太深奧了。我是實用主義派的!
經過測試，沙盒計算機確實可以算出實數與複數( a + bi )的正確結果。所以合理推斷它可以運作幫我求出平方根。我實際試了幾個最想知道的數值，如下:

* 1j的平方根為: $0.653281 - 0.270598i + 0.653281j + 0.270598k$。經過反平方驗算，忽略超微小數值差距會確實等於1j。
* 1ij的平方根為: $0.653281 + 0.270598i + 0.270598j + 0.653281k$。同樣的，經過反平方驗算，忽略超微小數值差距會確實等於1ij。

**在對非零因子的三元數進行連續開根號運算時，毫無意外的，其軌跡皆會以幾何級數的速度強行收斂至實數 `1.0`（即坐標 $[1, 0, 0, 0]$）。這也證明這個開根號代碼系統是正確的**

---

## 五. 單位化 (Normalize)

Gemini建議我可以弄一個單位化 (Normalize)的運算鍵，讓數值暴增時將向量等比例縮回總模長為單位長度1內，方便研究。我不確定這有什麼重要的，不過還是做了出來。
當然python代碼還是請gemini勞駕。它將四個係數 (a, b, c, d)個別除以總模長 $\sqrt{a^2 + b^2 + c^2 + d^2}$ 求得結果。

#### 註:如果設定三元數 $T_1$ = 1 + i + j + k( $j^3$ )，按下單位化計算後結果為 $T_2$ = 0.5 + 0.5i + 0.5j + 0.5k，可以於下方數值結果欄中發現3維空間中的模長為0.866，而四為空間中的總模長為1的有趣現象。

---

## 六. 結論: 這個有趣的三元數與其說是被我創造，不如說是被我發現。它有太多神奇的巧合性與對稱性，有很多部分都還值得深入探討與研究。例如:
* 1. 一開始對角度開根號的想法，究竟在數理上能不能因此成立?相反的，角度的次方運算呢?
* 2. 這個超複數系統只是假設最好運算的方式，我們也可以嘗試變更假設為 $j^2 = 1 + i$(也就是Xi平面的45度角)，那麼我們可以求得下表
* $j = (1 + i)/j$
* $j^2 = 1 + i$
* $j^3 = j + ij$
* $j^4 = 1 + i + i(1 + i) = 2i$
* $j^5 = 2ij$
* $j^6 = 2(1 + i) = 2 + 2i$
* $j^7 = 2j + 2ij$
* $j^8 = 2(1 + i) + 2i(1 + i) = 4i$
* $j^9 = 4ij$ 

可以觀察到它失去了8次循環的特性，ij也獨立出來沒辦法被取代，但呈現規律的遞增現象。難道說只有高斯複數平面的正負90度(i 或 -i)是特別的嗎?這是個未解的疑問。
**如果是0或180度，就是 $j^2 = -1$ 一般的虛數設定，或類似 $j^2 = 1$的雙曲複數設定。目前已經被發展出來的超複數系統。**

* 3. 我們也可以不要設定j軸垂直於高斯複數平面，例如設定讓它傾斜於特殊角度，例如(30度，45度，54.74度/35.26度, 60度，90度，或是地軸的傾斜角23.5度?)。不過目前我還沒想到要如何表示，這將會是另一個有趣的實驗。
* 4. $ij$這個元素目前我還沒研究清楚，它似乎沒辦法用克里福代數分析，因為根據克里福代數規定，相同向量的外積為零，故 $j \times j \times j = ij =0$，但 $ij$ 本身又可以視作是不同向量 $i$ 與 $j$的外積，故彼此矛盾。
     
     $ij = j^3$（ $d$ 軸）到底算不算第四維的向量？
>    gemini表示如下:(在「向量空間（加法層面）」上：它絕對算第四維的向量基底。** 因為 $ij$ 軸無法被前三軸 $(a, b, c)$ 透過任何線性的加減法組合（Linear Combination）所拼湊出來。
>    在鏈式四則運算與高斯消去法中，它必須獨立佔據第四個線性維度欄位。)所以目前也許該尋找所謂 **(非向量代數自乘3次代表的意義)**。我可能會打算從角度(雖然這並不符合目前的數理)或三角函數下手。

     我們也可以從所有前述的推導中觀察。如果 $ij$不被設計成代數的第四軸，將無法求出所有正確的結果。所以目前這是我在沙河計算機中把它當作隱藏的投影算子的理由。

* 5. 下一階段的工作，我會先花時間處理 $ ^2 = -i$的專案，因為它與這個超複數系統設定上只差一個負號，我想知道會不會跟這個系統產生互補。

C.H. Lee 2026.08.04

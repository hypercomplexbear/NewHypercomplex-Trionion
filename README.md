> 🌐 [English Version of README available here](./README_EN.md)

### 沙盒安裝說明
* 步驟 1：下載專案代碼 (Download Code)並解壓縮。
* 步驟 2：本系統需要安裝python的Gradio 網頁介面、NumPy 矩陣庫與 Plotly 3D 繪圖引擎：進入CMD輸入指令(pip install gradio numpy plotly)。
* 步驟 3：安裝完成後直接點擊app.py啟動(或是用CMD輸入: python app.py)，看到網址出現後複製網址到瀏覽器就會出現介面了。

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
* gemini告訴我這個超複數系統的零因子可以視為是光錐的一種。詳細的研究分析將再補充章節敘述。

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

**這裡有一個有趣的地方: 括弧裡面的式子本身就是行列式的實部係數互換(請參考2.1章節)。**

#### 補充 (2026.08.11)

Gemini說我找到的 $B' = -b_2 + a_2i + d_2j - c_2k$ 共軛叫做歪共軛，真正的三元數共軛複數為: $T* = a + bi - cj - dk$(詳見補充1.4.模長定義推導)。B'為共軛複數乘i的結果: $T* \times i = ai - b - ck + dj$

將 $T = a_1 + b_1i + c_1j + d_1k \times T* = a_2 + b_2i - c_2j - d_2k$  
代入乘法展開式驗算如下:

*   **實部 (a3)**： $a_3 =  a_1a_2 - b_1b_2 + c_1d_2 + d_1c_2$
*   **i 軸 (b3)**： $b_3 = +a_1b_2 + b_1a_2 - c_1c_2 + d_1d_2$
*   **j 軸 (c3)**： $c_3 = -a_1c_2 + b_1d_2 + c_1a_2 - d_1b_2$
*   **k 軸 (d3)**： $d_3 = -a_1d_2 - b_1c_2 + c_1b_2 + d_1a_2$

可以發現j項跟ij項一樣被完全消去，只留下行列式: $(a^2 - b^2 + 2cd) + (2ab - c^2 + d^2)i$。可以發現與歪共軛的結果實部與虛部i的係數剛好相反，很有趣!
那麼歪共軛(以下將寫成T')乘上共顎複數(T*)的操作會變出什麼!

---

* 讓 $T* \times T' = (a_1 + b_1i - c_1j - d_1k) \times (-b_2 + a_2i + d_2j - c_2k)$帶入乘法展開式如下:

*   **實部 (a3)**： $a_3 = -a_1b_2 - b_1a_2 - c_1c_2 + d_1d_2$
*   **i 軸 (b3)**： $b_3 = +a_1a_2 - b_1b_2 - c_1d_2 - d_1c_2$
*   **j 軸 (c3)**： $c_3 = +a_1d_2 + b_1c_2 + c_1b_2 + d_1a_2$
*   **k 軸 (d3)**： $d_3 = -a_1c_2 + b_1d_2 - c_1a_2 + d_1b_2$

整理後得到: $(d^2 - c^2 - 2ab) + (a^2 - b^2 - 2cd)i + 2(ad + bc)j + 2(bd - ac)k$

---

也可以將式子改寫成 $T* \times T' = T* \times i \times T* = i \times(T* )^2$。

將 $T* = a_1 + b_1i - c_1j - d_1k \times T* = a_2 + b_2i - c_2j - d_2k$ 代入乘法展開式驗算如下:

*   **實部 (a3)**： $a_3 =  a_1a_2 - b_1b_2 - c_1d_2 - d_1c_2$
*   **i 軸 (b3)**： $b_3 = +a_1b_2 + b_1a_2 + c_1c_2 - d_1d_2$
*   **j 軸 (c3)**： $c_3 = -a_1c_2 + b_1d_2 - c_1a_2 + d_1b_2$
*   **k 軸 (d3)**： $d_3 = -a_1d_2 - b_1c_2 - c_1b_2 - d_1a_2$

整理後得到: $(T* )^2 = (a^2 - b^2 - 2cd) + (c^2 - d^2 + 2ab)i + 2(bd - ac)j + 2(-ad - bc)k$，再乘上i如下:

$(a^2 - b^2 - 2cd)i + (-c^2 + d^2 - 2ab) + 2(bd - ac)ij - 2(-ad - bc)j$
整理後同樣得到: $(d^2 - c^2 - 2ab) + (a^2 - b^2 - 2cd)i + 2(ad + bc)j + 2(bd - ac)k$

---
同時我們已知 $T \times T* = |z\|^2$ ； $T' = i \times T*$，則 $T \times T' = T \times i \times T* = i \times |z\|^2$，與除法推導的 $B \times B'$ 結果一致。
---

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


---

## 六. 結論: 這個有趣的三元數與其說是被我創造，不如說是被我發現。它有太多神奇的巧合性與對稱性，有很多部分都還值得深入探討與研究。例如:
* 1. 我知道沒人認為拿角度直接開根號會符合數理的操作，但事實證明這可以衍伸出一系列有趣的超複數架構。所以，一開始對角度開根號的想法，究竟在數理上能不能因此成立?相反的，角度的次方運算呢?
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
**如果是0或180度，就是 $j^2 = -1$ 將變成雙複數的形式，或是繼續增加 $k^2 = -1$ 的設定，變成哈密頓四元數；或 $j^2 = 1$的另外一種雙複數設定，或是更複雜的分裂四元數。都是目前已經被發展出來的超複數系統。(詳見補充討論:模長與光錐與閔式時空)**

* 3. 我們也可以不要設定j軸垂直於高斯複數平面，例如設定讓它傾斜於特殊角度，例如(30度，45度，54.74度/35.26度, 60度，90度，或是地軸的傾斜角23.5度?)。不過目前我還沒想到要如何表示，這將會是另一個有趣的實驗。
* 4. $ij$這個元素目前我還沒研究清楚，它似乎沒辦法用克里福代數分析，因為根據克里福代數規定，相同向量的外積為零，故 $j \times j \times j = ij =0$，但 $ij$ 本身又可以視作是不同向量 $i$ 與 $j$的外積，故彼此矛盾。
     
     $ij = j^3$（ $d$ 軸）到底算不算第四維的向量？
>    gemini表示如下:(在「向量空間（加法層面）」上：它絕對算第四維的向量基底。** 因為 (ij) 軸無法被前三軸 (a, b, c) 透過任何線性的加減法組合（Linear Combination）所拼湊出來。
>    在鏈式四則運算與高斯消去法中，它必須獨立佔據第四個線性維度欄位。)所以目前也許該尋找所謂 **(非向量代數自乘3次代表的意義)**。我可能會打算從角度(雖然這並不符合目前的數理)或三角函數下手。

     我們也可以從所有前述的推導中觀察。如果 (ij) 不被設計成代數的第四軸，將無法求出所有正確的結果。
     所以目前這是我在沙盒計算機中把它當作隱藏的投影算子的理由。

* 5. 超複數目前並不是主流數學領域，尤其越複雜的超複數必須犧牲越多的數學公理性質，以及零因子的產生，讓複雜的超複數並不是很實用。而哈密頓的四元數則是個例外(這也展現出哈密頓的偉大)，在百年後的現在，哈密頓數應用在各種遊戲中的3D旋轉也展現出它的卓越性。而也許我們該想的是，這是不是代表如今我們發現(或發展)著其他眾多種類的超複數，也會在百年後在人類的科技中佔有重要的一席之地?
* 6. 關於猜想:我的直覺一直告訴我，超複數將是解開黎曼函數的一個重要線索。這個猜想來自於直觀的直覺:如果某一種超複數的模型能夠同時模擬現有物理界的波色子與費米子的特性與運動軌跡，而費米子的能階又與黎曼函數關係密切，這中間也許會存在什麼重要線索。
* 7. 下一階段的工作，我會先花時間處理 $j^2 = -i$ 的專案，因為它與這個超複數系統設定上只差一個負號，我想知道會不會跟這個系統產生互補。

C.H. Lee 2026.08.04

-----------
(2026.08.10新增補充)
### 1.4.模長定義推導 (Norm)

我以前跟gemni討論時，一直以為超複數的模長理所當然是: $(\sqrt{a^{2}+b^{2}+c^{2}+d^{2}}\)$，結果大錯特錯。我最近才稍微搞清楚歐基里德幾何空間與非歐基裡德幾何空間，而這個三元數的超複數系統顯然是非歐基裡德幾何空間。所以在此加入修正。
根據非歐基裡德幾何空間的模長設定為: 數與共軛數的乘積 $(Z \times Z*)$ 來維持代數的完整性，那麼我就必須找到 $T = a + bi + cj + dk$ 的共軛複數。gemini建議我用伴隨矩陣尋找，推導方式如下:

<div align="center">
   
$(M\cdot \text{adj}(M)=\det (M)\cdot I\)$

</div>

已知三元數矩陣表示如下:

<div align="center">

$$ \text{The Matrix of } T = \begin{bmatrix} a + bi & ci - d \\\\ c + di & a + bi \end{bmatrix} $$

</div>


則將矩陣（主對角線互換，副對角線加負號）:

<div align="center">

$$ \text{The Matrix of } T = \begin{bmatrix} a + bi & -ci + d \\\\ -c - di & a + bi \end{bmatrix} $$

</div>

得到三元數的共軛複數: $T* = a + bi - cj - dk$

將 $T = a_1 + b_1i + c_1j + d_1k \times T* = a_2 + b_2i - c_2j - d_2k$  
代入乘法展開式驗算如下:

*   **實部 (a3)**： $a_3 =  a_1a_2 - b_1b_2 + c_1d_2 + d_1c_2$
*   **i 軸 (b3)**： $b_3 = +a_1b_2 + b_1a_2 - c_1c_2 + d_1d_2$
*   **j 軸 (c3)**： $c_3 = -a_1c_2 + b_1d_2 + c_1a_2 - d_1b_2$
*   **k 軸 (d3)**： $d_3 = -a_1d_2 - b_1c_2 + c_1b_2 + d_1a_2$

結果等於矩陣的行列式: $(a^2 - b^2 + 2cd) + (2ab - c^2 + d^2)i$。

**故將本系統的超複數模長平方定義為其矩陣的行列式:** 

<div align="center">
   
$$\|z\|^2 = z \cdot z* = (a^2 - b^2 + 2cd) + (2ab - c^2 + d^2)i$$

</div>

**這個行列式的特點是仍含有實部與虛部i。如果要消除i，必須跟除法一樣取二次共軛。也就是模長的4次方 $\|z\|^4 = (a^2 - b^2 + 2cd)^2 + (2ab - c^2 + d^2)^2$，則模長 $\|z\|$ 應該要是相反的4次方根，才能符合放大倍數等比率。**

<div align="center">
   
**故模長定義為: $\|z\| = \sqrt[4]{(a^2 - b^2 + 2cd)^2 + (2ab - c^2 + d^2)^2}$**

</div>

##### 附註:在沙合計算機系統中，仍然會列出傳統歐基里德模長與新的行列式模長做為比較。

---

#### 模長與光錐與閔式時空

---
以下是查到的資料，用於比對與分析三元數系統的特性。
* 1.雙曲複數定義為 $z = a + bj$，其中 $a, b \in \mathbb{R}$。其虛數單位 $j$ 滿足以下核心性質：

$$j^2 = +1 \quad (j \neq \pm 1)$$

其代數共軛（Algebraic Conjugate）定義為：
$$z^* = a - bj$$

透過看雙曲複數 $z = a + bj$ 作用在基底 $\{1, j\}$ 上的線性變換：
* $z \cdot 1 = a + bj$
* $z \cdot j = aj + bj^2 = b + aj$
可以將任意雙曲複數精確同構（Isomorphic）為一個 $2 \times 2$ 的實數對稱矩陣 $M_z$：

<div align="center">
   
$$M_z = \begin{bmatrix} a & b \\\\ b & a \end{bmatrix}$$

</div>

在該系統中，雙曲複數的模長平方定義為：

$$\|z\|^2 = \det(M_z) = a^2 - b^2$$

**幾何不變量與閔氏時空距離之映射**
根據我查到的資料，因為模長平方公式中出現了減號 $-b^2$，該系統的模長不具備傳統歐氏空間的「正定性」，而是完美對應了狹義相對論中的**閔可夫斯基時空距離（Minkowski Spacetime Interval）**。原因如下:

若我們將雙曲複數的實部 $a$ 映射為時間軸 $ct$（光速 $\times$ 時間），將虛部 $b$ 映射為一維空間軸 $x$，則該矩陣的行列式與模長平方，精確等同於物理學中的時空線元（不變距離平方 $s^2$）：
$$\|z\|^2 = \det(M_z) = a^2 - b^2 \iff s^2 = (ct)^2 - x^2$$

根據 $\det(M_z)$ 或 $s^2$ 的正負號，該超複數系統將空間中的點劃分為三種完全不同的非歐幾何物理軌跡：

* **$\|z\|^2 > 0 \iff (ct)^2 > x^2$ （類時區 Time-like）**：
  當 $|a| > |b|$，模長平方為正。幾何軌跡位於雙曲線 $a^2 - b^2 = C$ 上（對應雙曲空間的非歐圓）。在物理上，這代表因果鏈可達的區域，所有靜止質量大於零的實體粒子，其時空軌跡皆落於此區域。
  
* **$\|z\|^2 < 0 \iff (ct)^2 < x^2$ （類空區 Space-like）**：
  當 $|a| < |b|$，模長平方為負（這在歐幾里得幾何中是不可能的）。在物理上，這代表因果鏈不可達的區域（需要超光速才能抵達），勾勒出非歐空間中的超雙曲距離。
  
* **$\|z\|^2 = 0 \iff (ct)^2 = x^2$ （類光區 / 零模長 Light-like）**：
  當 $a = \pm b$。此時超複數 $z \neq 0$，但其幾何模長卻奇蹟般地為 $0$。在代數上，這些元素被稱為**零因子（Null Divisors）**，其對應的矩陣為**奇異矩陣（Singular Matrix，不可逆）**；在物理上，這兩條漸近線完美定義了真空中的**光錐（Light Cone）**邊界，代表光子或無質量粒子的時空軌跡。

**由以上資料可知，非歐幾何空間的模長會含有減號，對應了閔式時空，因為模長可以小於0，而歐氏幾何空間規定必須符合正定性，也就是模長必須大於等於0。而本系統的模長為 $(a^2 - b^2 + 2cd) + (2ab - c^2 + d^2)i$，自然不屬於歐氏幾何空間。**

**且雙曲複數的零因子為 $a^2 - b^2 = 0$，即 $a = \pm b$ ，也就是二維座標中與X, Y軸夾角為45度的兩條對角線。與本超複數系統的特殊零因子 $a = b, c = \pm\sqrt{2}a$做比對會發現極為相似，也就是gemini當初跟我說這是光錐的一種的理由**

---
#### 分裂四元數的矩陣表示法與閔氏時空映射
---

根據查到的資料做以下分析。

系統代數基底與乘法規則:
分裂四元數定義為 $q = a + bi + cj + dk$，其中 $a, b, c, d \in \mathbb{R}$。其虛數基底 $\{i, j, k\}$ 滿足以下反交換律與平方規則：

$$i^2 = -1, \quad j^2 = +1, \quad k^2 = +1$$
$$ij = -ji = k, \quad jk = -kj = -i, \quad ki = -ik = j$$

其代數共軛（Algebraic Conjugate）定義為反轉所有虛部符號：

$$q^* = a - bi - cj - dk$$

利用傳統複數虛數單位 $i$（滿足 $i^2 = -1$），可以將分裂四元數改寫為雙複數形式 $q = (a + bi) + (c + di)j$。透過其左乘作用，可將分裂四元數同構（Isomorphic）為一個 $2 \times 2$ 的複數矩陣 $M_q$：
$$M_q = \begin{bmatrix} a + bi & c + di \\ c - di & a - bi \end{bmatrix}$$

而在該系統中，超複數的**幾何模長平方**完美等於其複數矩陣的**行列式值（Determinant）**。

可直接計算矩陣 $M_q$ 的行列式：

$$\det(M_q) = (a + bi)(a - bi) - (c + di)(c - di)$$

根據傳統複數乘法展開：
* $(a + bi)(a - bi) = a^2 + b^2$
* $(c + di)(c - di) = c^2 + d^2$

將兩者相減，即得到分裂四元數的模長平方公式：

$$\|q\|^2 = \det(M_q) = q \cdot q^* = a^2 + b^2 - c^2 - d^2$$

這個公式在幾何上對應了符號結構為 $(+, +, -, -)$ 的 **$(2,2)$ 被稱作偽歐幾里得度規（Pseudo-Euclidean metric）**。

與維閔可夫斯基時空的物理映射
在物理學中，愛因斯坦與閔可夫斯基定義的 **4 維時空線元（不變距離平方 $s^2$）** 公式為：

$$s^2 = (ct)^2 - x^2 - y^2 - z^2$$

如果對分裂四元數的分量進行物理映射，將其重新排列與線性組合（例如令 $a = ct$，並將 $b, c, d$ 映射為空間軸的座標組合），其代數模長平方 $\|q\|^2$ 就能完美勾勒出 4 維時空的幾何結構：

* **$\|q\|^2 > 0$ （類時區 Time-like / 因果可達）**：
  時空結構以時間維度為主導。所有具有靜止質量的亞光速粒子，其在 4 維時空中的運動軌跡（世界線）其微分線元皆落於此正範數區域。
  
* **$\|q\|^2 < 0$ （類空區 Space-like / 因果斷絕）**：
  時空結構以空間維度為主導。代表相隔極遠、即便以光速也無法在時間內傳遞訊號的兩個時空事件點。
  
* **$\|q\|^2 = 0$ （類光區 / 超光錐曲面 Light-like）**：
  當 $a^2 + b^2 = c^2 + d^2$ 時，超複數 $q \neq 0$ 但幾何模長為 0。在代數上這代表系統的**零因子（Null Divisors）**，對應的矩陣為**奇異矩陣（不可逆）**；在物理上，它在 4 維時空中精確劃分出了 **3 維超光錐面（Hyper-light cone）**，這正是光子在 4 維時空中穿梭的幾何邊界。
  
---
從以上資料可以發現一個驚人的巧合處，也就是分裂四元數類光區的零因子 $a^2 + b^2 = c^2 + d^2$ 與本超複數系統的零因子條件極為相似:
<div align="center">

$$ \begin{cases} a^2 + b^2 = c^2 + d^2 \\\\ a^2 - b^2 = -2cd \\\\ c^2 - d^2 = 2ab \end{cases} $$

</div>

---
#### 雙複數的模長表示法與零因子
---
我查到一種叫做塞格雷雙複數（Bicomplex Numbers）的超複數: $q = a + bi + (c + di)j$ ，可以簡化成 $Z_1 + Z_2j$，其中 $i^2 = j^2 = -1$，且 $ij = ji = k, k^2 = 1$。雙複數與三元數的系統極為相似，三元數也可以寫成這種雙複數的形式，差別只是在基礎假設上 $j^2 = i$。
而雙複數的模長定義，也同樣因其行列式是複數與三元數遇到同樣的問題。所以有兩種模長定義，如下:
* 第一種是歐幾里得度量

<div align="center">
   
$$|q\|_E = \sqrt{a^2 + b^2 + c^2 + d^2}$$

</div>

* 而第二種則是含有虛數的模長:

<div align="center">

$$|q\|_c = \sqrt{z_1^2 + z_2^2} = \sqrt{(a + bi)^2 + (c + di)^2}$$，展開後得到

$$|q\|_c = \sqrt{(a^2 - b^2 + c^2 - d^2) + 2(ab + cd)i}$$

</div>

如果要求得實數值廣義模長(Real Norm），則採用冪等基底（Idempotent basis）來定義：

<div align="center">
   
$$|q\|_r = \sqrt[4]{(a^2 + b^2 + c^2 + d^2)^2 - 4(ab - cd)^2}$$

</div>

**故擁有相似性值的本超複數系統也因此採用同樣的方式來定義模長。**

---

另外由上可知雙複數的行列式為: ${(a + bi)^2 + (c + di)^2}$ = ${(a^2 - b^2 + c^2 - d^2) + 2(ab + cd)i}$

則可推導零因子為:

* $a^2 - b^2 + c^2 - d^2 = 0$，可以化簡為 $a^2 + c^2 = b^2 + d^2$
* $ab + cd = 0$，可以化簡為 $ab = -cd$ 

可以觀察到跟分裂四元數的零因子相比，多了一個條件式: $ab = -cd$，故雙複數的零因子並不是完全的超圓錐型狀。$a^2 + c^2 = b^2 + d^2是一個超圓錐，在三維空間中退化成雙圓錐；ab = -cd是一個超曲面，而其三維圖形退化為雙曲面。兩個的交集在四維空間就是超平面，三維空間則是兩個垂直相交直線。如下:

* 由a = 0帶入，可以得到 若 c = 0，則  b = d = 0；若d = 0，則得到 c = $\pm b$
* 由c = 0帶入，可以得到 若 a = 0，則  b = d = 0；若b = 0，則得到 a = $\pm d$

---

#### 關於歐拉公式
我嘗試讓gemini利用泰勒展開式來分析T的歐拉公式，如下:
將 $x = j\theta$ 帶入指數函數 $(e^{x}\)$ 的麥克勞林級數:

$$e^{j\theta} = \sum_{n=0}^{\infty} \frac{(j\theta)^n}{n!} = 1 + j\theta + \frac{j^2\theta^2}{2!} + \frac{j^3\theta^3}{3!} + \frac{j^4\theta^4}{4!} + \frac{j^5\theta^5}{5!} + \frac{j^6\theta^6}{6!} + \frac{j^7\theta^7}{7!} + \dots$$

將上述次方簡化結果代回級數，並按基底 $\{1, j, i, ij\}$ 進行四元拆分重組：

$$e^{j\theta} = f_0(\theta) + j \cdot f_1(\theta) + i \cdot f_2(\theta) + k \cdot f_3(\theta)$$

根據本數系定義之虛數單位性質 $j^2 = i$ 且 $i^2 = -1$，可得 $j$ 的高階乘冪呈現 8 階循環（$j^4 = -1, j^8 = 1$）：

* $j^0 = 1$
* $j^1 = j$
* $j^2 = i$
* $j^3 = ij = k$
* $j^4 = -1$
* $j^5 = -j$
* $j^6 = -i$
* $j^7 = -ij = -k$

其中各分量級數展開如下：

$$f_0(\theta) = 1 - \frac{\theta^4}{4!} + \frac{\theta^8}{8!} - \frac{\theta^{12}}{12!} + \dots$$

$$f_1(\theta) = \theta - \frac{\theta^5}{5!} + \frac{\theta^9}{9!} - \frac{\theta^{13}}{13!} + \dots$$

$$f_2(\theta) = \frac{\theta^2}{2!} - \frac{\theta^6}{6!} + \frac{\theta^{10}}{10!} - \frac{\theta^{14}}{14!} + \dots$$

$$f_3(\theta) = \frac{\theta^3}{3!} - \frac{\theta^7}{7!} + \frac{\theta^{11}}{11!} - \frac{\theta^{15}}{15!} + \dots$$

---
### 1. 各分量之精確閉合形式（Closed-Form Expressions）

經過級數疊加與角度縮放驗算，各分量 $f_k(\theta)$ 之閉合解如下：

#### 實數項分量 $f_0(\theta)$ 之泰勒展開詳細推導

定義角度縮放參數 $\alpha = \frac{\theta}{\sqrt{2}}$，將三角函數與雙曲函數分別進行泰勒級數展開：

$$\cos(\alpha) = 1 - \frac{\alpha^2}{2!} + \frac{\alpha^4}{4!} - \frac{\alpha^6}{6!} + \frac{\alpha^8}{8!} - \dots$$

$$\cosh(\alpha) = 1 + \frac{\alpha^2}{2!} + \frac{\alpha^4}{4!} + \frac{\alpha^6}{6!} + \frac{\alpha^8}{8!} + \dots$$

兩式相乘並按 $\alpha$ 的偶數次方收集同類項：

$$\begin{aligned}
\cos(\alpha)\cosh(\alpha) = &\ 1 \cdot 1 \\
&+ \left(\frac{1}{2!} - \frac{1}{2!}\right)\alpha^2 \\
&+ \left(\frac{1}{4!} - \frac{1}{2! \cdot 2!} + \frac{1}{4!}\right)\alpha^4 \\
&+ \left(\frac{1}{6!} - \frac{1}{4! \cdot 2!} + \frac{1}{2! \cdot 4!} - \frac{1}{6!}\right)\alpha^6 \\
&+ \left(\frac{1}{8!} - \frac{1}{6! \cdot 2!} + \frac{1}{4! \cdot 4!} - \frac{1}{2! \cdot 6!} + \frac{1}{8!}\right)\alpha^8 - \dots
\end{aligned}$$

計算各係數數值：

* $\alpha^2$ 項係數： $\frac{1}{2} - \frac{1}{2} = 0$（精確抵消）
* $\alpha^4$ 項係數： $\frac{1}{24} - \frac{1}{4} + \frac{1}{24} = -\frac{1}{6}$
* $\alpha^6$ 項係數： $\frac{1}{720} - \frac{1}{48} + \frac{1}{48} - \frac{1}{720} = 0$（精確抵消）
* $\alpha^8$ 項係數： $\frac{1}{40320} - \frac{1}{1440} + \frac{1}{576} - \frac{1}{1440} + \frac{1}{40320} = \frac{1}{2520}$

將 $\alpha = \frac{\theta}{\sqrt{2}}$ 代回上式：

* $\alpha^4$ 項： $-\frac{1}{6} \left(\frac{\theta}{\sqrt{2}}\right)^4 = -\frac{1}{6} \cdot \frac{\theta^4}{4} = -\frac{\theta^4}{24} = -\frac{\theta^4}{4!}$
* $\alpha^8$ 項： $\frac{1}{2520} \left(\frac{\theta}{\sqrt{2}}\right)^8 = \frac{1}{2520} \cdot \frac{\theta^8}{16} = \frac{\theta^8}{40320} = \frac{\theta^8}{8!}$

故精確導出次方為 $n \equiv 0 \pmod 4$ 的閉合泰勒級數：

$$f_0(\theta) = \cos\left(\frac{\theta}{\sqrt{2}}\right)\cosh\left(\frac{\theta}{\sqrt{2}}\right) = 1 - \frac{\theta^4}{4!} + \frac{\theta^8}{8!} - \frac{\theta^{12}}{12!} + \dots$$

---
#### $j$ 項分量 $f_1(\theta)$ 之泰勒展開詳細推導

定義角度縮放參數 $\alpha = \frac{\theta}{\sqrt{2}}$，分別展開兩組交叉乘積項：

$$\sin(\alpha)\cosh(\alpha) = \left( \alpha - \frac{\alpha^3}{3!} + \frac{\alpha^5}{5!} - \frac{\alpha^7}{7!} + \dots \right) \left( 1 + \frac{\alpha^2}{2!} + \frac{\alpha^4}{4!} + \frac{\alpha^6}{6!} + \dots \right)$$

$$\cos(\alpha)\sinh(\alpha) = \left( 1 - \frac{\alpha^2}{2!} + \frac{\alpha^4}{4!} - \frac{\alpha^6}{6!} + \dots \right) \left( \alpha + \frac{\alpha^3}{3!} + \frac{\alpha^5}{5!} + \frac{\alpha^7}{7!} + \dots \right)$$

將兩式相加，按奇數次方整理同類項：

1. **$\alpha^1$ 項：**
   $$\alpha + \alpha = 2\alpha$$

2. **$\alpha^3$ 項：**
   $$\left( -\frac{1}{6} + \frac{1}{2} + \frac{1}{6} - \frac{1}{2} \right)\alpha^3 = 0 \quad \text{（精確抵消）}$$

3. **$\alpha^5$ 項：**
   $$\left( \frac{1}{120} - \frac{1}{12} + \frac{1}{24} \right) + \left( \frac{1}{120} - \frac{1}{12} + \frac{1}{24} \right) = 2 \left( \frac{1}{120} - \frac{1}{24} \right) = -\frac{1}{15} \alpha^5$$

4. **$\alpha^7$ 項：**
   $$\alpha^7 \text{ 相關係數相加同樣精確抵消為 } 0$$

將 $\alpha = \frac{\theta}{\sqrt{2}}$ 代回並乘上前方之縮放係數 $\frac{1}{\sqrt{2}}$：

* **$\theta^1$ 項：**
  $$\frac{1}{\sqrt{2}} \cdot 2\left(\frac{\theta}{\sqrt{2}}\right) = \frac{2\theta}{2} = \theta$$

* **$\theta^5$ 項：**
  $$\frac{1}{\sqrt{2}} \left( -\frac{1}{15} \right) \left(\frac{\theta}{\sqrt{2}}\right)^5 = \frac{1}{\sqrt{2}} \left( -\frac{1}{15} \right) \frac{\theta^5}{4\sqrt{2}} = -\frac{\theta^5}{120} = -\frac{\theta^5}{5!}$$

* **$\theta^9$ 項：**
  $$\text{經同理計算導出 } +\frac{\theta^9}{9!}$$

故精確導出次方為 $n \equiv 1 \pmod 4$ 的閉合泰勒級數：

$$f_1(\theta) = \frac{1}{\sqrt{2}} \left[ \sin\left(\frac{\theta}{\sqrt{2}}\right) \cosh\left(\frac{\theta}{\sqrt{2}}\right) + \cos\left(\frac{\theta}{\sqrt{2}}\right) \sinh\left(\frac{\theta}{\sqrt{2}}\right) \right] = \theta - \frac{\theta^5}{5!} + \frac{\theta^9}{9!} - \frac{\theta^{13}}{13!} + \dots$$
---

#### $i$ 項分量 $f_2(\theta)$ 之泰勒展開詳細推導

定義角度縮放參數 $\alpha = \frac{\theta}{\sqrt{2}}$，將三角正弦函數與雙曲正弦函數分別進行泰勒級數展開：

$$\sin(\alpha) = \alpha - \frac{\alpha^3}{3!} + \frac{\alpha^5}{5!} - \frac{\alpha^7}{7!} + \frac{\alpha^9}{9!} - \dots$$

$$\sinh(\alpha) = \alpha + \frac{\alpha^3}{3!} + \frac{\alpha^5}{5!} + \frac{\alpha^7}{7!} + \frac{\alpha^9}{9!} + \dots$$

兩式相乘，並按 $\alpha$ 的偶數次方收集同類項：

$$\begin{aligned}
\sin(\alpha)\sinh(\alpha) = &\ \alpha \cdot \alpha \\
&+ \left(\frac{1}{3!} - \frac{1}{3!}\right)\alpha^4 \\
&+ \left(\frac{1}{5!} - \frac{1}{3! \cdot 3!} + \frac{1}{5!}\right)\alpha^6 \\
&+ \left(\frac{1}{7!} - \frac{1}{5! \cdot 3!} + \frac{1}{3! \cdot 5!} - \frac{1}{7!}\right)\alpha^8 \\
&+ \left(\frac{1}{9!} - \frac{1}{7! \cdot 3!} + \frac{1}{5! \cdot 5!} - \frac{1}{3! \cdot 7!} + \frac{1}{9!}\right)\alpha^{10} - \dots
\end{aligned}$$

計算各係數數值：

* $\alpha^2$ 項係數： $1$
* $\alpha^4$ 項係數： $\frac{1}{6} - \frac{1}{6} = 0$（精確抵消）
* $\alpha^6$ 項係數： $\frac{1}{120} - \frac{1}{36} + \frac{1}{120} = \frac{1}{60} - \frac{1}{36} = \frac{3 - 5}{180} = -\frac{1}{90}$
* $\alpha^8$ 項係數：奇數正負對稱，精確抵消為 $0$

將 $\alpha = \frac{\theta}{\sqrt{2}}$ 代回上式：

* $\alpha^2$ 項： $\left(\frac{\theta}{\sqrt{2}}\right)^2 = \frac{\theta^2}{2} = \frac{\theta^2}{2!}$
* $\alpha^6$ 項： $-\frac{1}{90} \left(\frac{\theta}{\sqrt{2}}\right)^6 = -\frac{1}{90} \cdot \frac{\theta^6}{8} = -\frac{\theta^6}{720} = -\frac{\theta^6}{6!}$

故精確導出次方為 $n \equiv 2 \pmod 4$ 的閉合泰勒級數：

$$f_2(\theta) = \sin\left(\frac{\theta}{\sqrt{2}}\right)\sinh\left(\frac{\theta}{\sqrt{2}}\right) = \frac{\theta^2}{2!} - \frac{\theta^6}{6!} + \frac{\theta^{10}}{10!} - \frac{\theta^{14}}{14!} + \dots$$

---

#### $k$ 項分量 $f_3(\theta)$ 之泰勒展開詳細推導

定義角度縮放參數 $\alpha = \frac{\theta}{\sqrt{2}}$，分別展開兩組交叉乘積項：

$$\sin(\alpha)\cosh(\alpha) = \left( \alpha - \frac{\alpha^3}{3!} + \frac{\alpha^5}{5!} - \frac{\alpha^7}{7!} + \dots \right) \left( 1 + \frac{\alpha^2}{2!} + \frac{\alpha^4}{4!} + \frac{\alpha^6}{6!} + \dots \right)$$

$$\cos(\alpha)\sinh(\alpha) = \left( 1 - \frac{\alpha^2}{2!} + \frac{\alpha^4}{4!} - \frac{\alpha^6}{6!} + \dots \right) \left( \alpha + \frac{\alpha^3}{3!} + \frac{\alpha^5}{5!} + \frac{\alpha^7}{7!} + \dots \right)$$

將兩式相減，按奇數次方整理同類項：

1. **$\alpha^1$ 項：**
   $$\alpha - \alpha = 0 \quad \text{（精確抵消）}$$

2. **$\alpha^3$ 項：**
   $$\left( -\frac{1}{6} + \frac{1}{2} \right) - \left( -\frac{1}{2} + \frac{1}{6} \right) = \frac{1}{3} - \left( -\frac{1}{3} \right) = \frac{2}{3} \alpha^3$$

3. **$\alpha^5$ 項：**
   $$\alpha^5 \text{ 相關係數相減精確抵消為 } 0$$

4. **$\alpha^7$ 項：**
   $$\text{經計算導出相減結果為 } -\frac{1}{315} \alpha^7$$

將 $\alpha = \frac{\theta}{\sqrt{2}}$ 代回並乘上前方之縮放係數 $\frac{1}{\sqrt{2}}$：

* **$\theta^3$ 項：**
  $$\frac{1}{\sqrt{2}} \left( \frac{2}{3} \right) \left(\frac{\theta}{\sqrt{2}}\right)^3 = \frac{1}{\sqrt{2}} \cdot \frac{2}{3} \cdot \frac{\theta^3}{2\sqrt{2}} = \frac{\theta^3}{6} = \frac{\theta^3}{3!}$$

* **$\theta^7$ 項：**
  $$\frac{1}{\sqrt{2}} \left( -\frac{1}{315} \right) \left(\frac{\theta}{\sqrt{2}}\right)^7 = \frac{1}{\sqrt{2}} \left( -\frac{1}{315} \right) \frac{\theta^7}{8\sqrt{2}} = -\frac{\theta^7}{5040} = -\frac{\theta^7}{7!}$$

故精確導出次方為 $n \equiv 3 \pmod 4$ 的閉合泰勒級數：

$$f_3(\theta) = \frac{1}{\sqrt{2}} \left[ \sin\left(\frac{\theta}{\sqrt{2}}\right) \cosh\left(\frac{\theta}{\sqrt{2}}\right) - \cos\left(\frac{\theta}{\sqrt{2}}\right) \sinh\left(\frac{\theta}{\sqrt{2}}\right) \right] = \frac{\theta^3}{3!} - \frac{\theta^7}{7!} + \frac{\theta^{11}}{11!} - \frac{\theta^{15}}{15!} + \dots$$
---

#### 總整理
* ** 常數項分量 $f_0(\theta)$ （ $1$ 軸，次方 $0, 4, 8, 12 \dots$）：**
  $$f_0(\theta) = \cos\left(\frac{\theta}{\sqrt{2}}\right) \cosh\left(\frac{\theta}{\sqrt{2}}\right) = 1 - \frac{\theta^4}{4!} + \frac{\theta^8}{8!} - \frac{\theta^{12}}{12!} + \dots$$

* ** $j$ 項分量 $f_1(\theta)$ （ $j$ 軸，次方 $1, 5, 9, 13 \dots$）：**
  $$f_1(\theta) = \frac{1}{\sqrt{2}} \left[ \sin\left(\frac{\theta}{\sqrt{2}}\right) \cosh\left(\frac{\theta}{\sqrt{2}}\right) + \cos\left(\frac{\theta}{\sqrt{2}}\right) \sinh\left(\frac{\theta}{\sqrt{2}}\right) \right] = \theta - \frac{\theta^5}{5!} + \frac{\theta^9}{9!} - \frac{\theta^{13}}{13!} + \dots$$

* ** $i$ 項分量 $f_2(\theta)$ （ $i$ 軸，次方 $2, 6, 10, 14 \dots$）：**
  $$f_2(\theta) = \sin\left(\frac{\theta}{\sqrt{2}}\right) \sinh\left(\frac{\theta}{\sqrt{2}}\right) = \frac{\theta^2}{2!} - \frac{\theta^6}{6!} + \frac{\theta^{10}}{10!} - \frac{\theta^{14}}{14!} + \dots$$

* ** $k$ 項分量 $f_3(\theta)$ （ $k$ 軸，次方 $3, 7, 11, 15 \dots$）：**
  $$f_3(\theta) = \frac{1}{\sqrt{2}} \left[ \sin\left(\frac{\theta}{\sqrt{2}}\right) \cosh\left(\frac{\theta}{\sqrt{2}}\right) - \cos\left(\frac{\theta}{\sqrt{2}}\right) \sinh\left(\frac{\theta}{\sqrt{2}}\right) \right] = \frac{\theta^3}{3!} - \frac{\theta^7}{7!} + \frac{\theta^{11}}{11!} - \frac{\theta^{15}}{15!} + \dots$$

---

#### 2. 奇數分量之交叉線性組合關聯

針對奇數次方分量 $f_1(\theta)$ 與 $f_3(\theta)$，可由三角與雙曲函數之交叉乘積透過加減法相互組合解出：

$$\sqrt{2} \sin\left(\frac{\theta}{\sqrt{2}}\right) \cosh\left(\frac{\theta}{\sqrt{2}}\right) = f_1(\theta) + f_3(\theta)$$

$$\sqrt{2} \cos\left(\frac{\theta}{\sqrt{2}}\right) \sinh\left(\frac{\theta}{\sqrt{2}}\right) = f_1(\theta) - f_3(\theta)$$

---

### 3. 完整歐拉公式表示式

綜合上述四個空間基底分量之指數型態最終表示為：

$$e^{j\theta} = \cos\left(\frac{\theta}{\sqrt{2}}\right)\cosh\left(\frac{\theta}{\sqrt{2}}\right) + j \cdot \frac{1}{\sqrt{2}} \left[ \sin\left(\frac{\theta}{\sqrt{2}}\right)\cosh\left(\frac{\theta}{\sqrt{2}}\right) + \cos\left(\frac{\theta}{\sqrt{2}}\right)\sinh\left(\frac{\theta}{\sqrt{2}}\right) \right] + i \cdot \sin\left(\frac{\theta}{\sqrt{2}}\right)\sinh\left(\frac{\theta}{\sqrt{2}}\right) + k \cdot \frac{1}{\sqrt{2}} \left[ \sin\left(\frac{\theta}{\sqrt{2}}\right)\cosh\left(\frac{\theta}{\sqrt{2}}\right) - \cos\left(\frac{\theta}{\sqrt{2}}\right)\sinh\left(\frac{\theta}{\sqrt{2}}\right) \right]$$

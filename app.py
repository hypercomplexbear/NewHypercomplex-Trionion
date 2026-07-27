import math
import gradio as gr
import numpy as np
import plotly.graph_objects as go

# ========================================================
# 1. 核心公開運算公式 (保留你最原始正確的 Python 算式)
# ========================================================

def multiply_4d_algebra(a1, b1, c1, d1, a2, b2, c2, d2):
    new_a = a1*a2 - b1*b2 - c1*d2 - d1*c2
    new_b = a1*b2 + b1*a2 + c1*c2 - d1*d2
    new_c = a1*c2 - b1*d2 + c1*a2 - d1*b2
    new_d = a1*d2 + b1*c2 + c1*b2 + d1*a2
    return [new_a, new_b, new_c, new_d]

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
            raise ZeroDivisionError("Mathematical meltdown detected! The input set has triggered a [zero-divisor] singularity; division yields no unique solution.\n""偵測到數學崩潰點！該組輸入觸發了【零因子】特異點，除法無唯一解。")
        
        pivot = M[i][i]
        for c in range(i, n + 1):
            M[i][c] /= pivot
        for r in range(n):
            if r != i:
                factor = M[r][i]
                for c in range(i, n + 1):
                    M[r][c] -= factor * M[i][c]
                    
    return [M[0][4], M[1][4], M[2][4], M[3][4]] # 採用你最天才且統一的一維陣列回傳改法！

# ========================================================
# 2. 連續鏈式計算暫存器與 3D 繪圖核心
# ========================================================

trajectory = [[1.0, 1.0, 1.0, 0.0]] 
history_logs = ["System ready. Initial state is A."]
# 新增：超複數開根號內部的核心數學函式
def gaussian_elimination(M, Y):
    """
    標準高斯消去法 (列簡化階梯形矩陣)
    解 M * dX = Y，其中 M 為 4x4 矩陣，Y 為長度 4 的向量
    """
    n = 4
    # 組合增廣矩陣 (Augmented Matrix)
    A = [M[i] + [Y[i]] for i in range(n)]
    
    # 前向消去
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
                
    # 後向代換 (【🔥 這裡已修正：全數更換為 dX，不再與外部 X 混淆】)
    dX = [0.0] * n
    for i in range(n - 1, -1, -1):
        dX[i] = A[i][n]
        for k in range(i + 1, n):
            dX[i] -= A[i][k] * dX[k]
    return dX


def sqrt_4d_algebra(a1, b1, c1, d1):
    # 1. 優先處理純實數攔截（防禦多維原點發散，鎖死實數軸）
    v_norm = math.sqrt(b1**2 + c1**2 + d1**2)
    if v_norm < 1e-9:
        if a1 >= 0:
            return [math.sqrt(a1), 0.0, 0.0, 0.0]
        else:
            return [0.0, math.sqrt(abs(a1)), 0.0, 0.0]

    # 2. 幾何初始猜測值 (利用全模長與實部粗估)
    q_norm = math.sqrt(a1**2 + b1**2 + c1**2 + d1**2)
    x_a = math.sqrt((q_norm + abs(a1)) / 2)
    scale = 0.5 / x_a if x_a != 0 else 0.1
    x_b = b1 * scale
    x_c = c1 * scale
    x_d = d1 * scale
    
    # 3. 矩陣牛頓迭代優化
    for _ in range(6):
        # 根據您圖片中 multiply_4d_algebra 偏導推導出的 4x4 雅可比矩陣 M
        M = [
            [2 * x_a, -2 * x_b, -2 * x_d, -2 * x_c],
            [2 * x_b,  2 * x_a,  2 * x_c, -2 * x_d],
            [2 * x_c, -2 * x_d,  2 * x_a, -2 * x_b],
            [2 * x_d,  2 * x_c,  2 * x_b,  2 * x_a]
        ]
        
        # 根據您代碼中的乘法表公式，計算目前 X 自乘出來的 4D 實際值
        current_a = x_a**2 - x_b**2 - 2 * x_c * x_d
        current_b = 2 * x_a * x_b + x_c**2 - x_d**2
        current_c = 2 * x_a * x_c - 2 * x_b * x_d
        current_d = 2 * x_a * x_d + 2 * x_b * x_c
        
        # 計算方程式殘差向量 Y
        y_a = a1 - current_a
        y_b = b1 - current_b
        y_c = c1 - current_c
        y_d = d1 - current_d
        Y = [y_a, y_b, y_c, y_d]
        
        # 呼叫手寫高斯消去法解出精密修正量
        dX = gaussian_elimination(M, Y)
        
        # 更新 4D 空間坐標 (【🔥 這裡已修正：精確解包 dX 的 4 個分量進行累加】)
        x_a += dX[0]
        x_b += dX[1]
        x_c += dX[2]
        x_d += dX[3]

    # 4. 回傳最終完美對齊您空間度規的 4D 坐標結果
    return [round(x_a, 6), round(x_b, 6), round(x_c, 6), round(x_d, 6)]



def run_step(a1, b1, c1, d1, op, a2, b2, c2, d2, show_norm):
    global trajectory, history_logs
    
    try:
        # 💡 核心修正：如果歷史軌跡裡面只有一開始預設的那一個點
        # 我們直接把這個起點動態替換成使用者「當下在網頁畫面上修改後的值」！
        if len(trajectory) == 1:
            trajectory[0] = [a1, b1, c1, d1]

        if op == "加 Add (+)":
            res = [a1 + a2, b1 + b2, c1 + c2, d1 + d2]
            log_text = f"Op: Prev {op} ({a2}, {b2}, {c2}, {d2}) -> ({res[0]:.2f}, {res[1]:.2f}, {res[2]:.2f}, {res[3]:.2f})"
            
        elif op == "減 Subtract (-)":
            res = [a1 - a2, b1 - b2, c1 - c2, d1 - d2]
            log_text = f"Op: Prev {op} ({a2}, {b2}, {c2}, {d2}) -> ({res[0]:.2f}, {res[1]:.2f}, {res[2]:.2f}, {res[3]:.2f})"
            
        elif op == "乘 Multiply (*)":
            res = multiply_4d_algebra(a1, b1, c1, d1, a2, b2, c2, d2)
            log_text = f"Op: Prev {op} ({a2}, {b2}, {c2}, {d2}) -> ({res[0]:.2f}, {res[1]:.2f}, {res[2]:.2f}, {res[3]:.2f})"
            
        elif op == "除 Divide (/)":
            res = divide_4d_algebra(a1, b1, c1, d1, a2, b2, c2, d2)
            log_text = f"Op: Prev {op} ({a2}, {b2}, {c2}, {d2}) -> ({res[0]:.2f}, {res[1]:.2f}, {res[2]:.2f}, {res[3]:.2f})"
            
        # ==========================================
        # 新增：開根號運算分支
        # ==========================================
        elif op == "開根號 Sqrt (√)":
            res = sqrt_4d_algebra(a1, b1, c1, d1)
            # 調整紀錄格式：因為是一元運算，不顯示第二組輸入，直接記錄對前一組結果開根號
            log_text = f"Op: Sqrt (√) -> ({res[0]:.2f}, {res[1]:.2f}, {res[2]:.2f}, {res[3]:.2f})"
        # ==========================================
        # ==========================================
        # 新增：單位化（Normalize）運算分支
        # ==========================================
        elif op == "單位化 (Normalize)":
            # 1. 計算目前的總模長 (這段您原本代碼中應該已經有了)
            q_norm = math.sqrt(a1**2 + b1**2 + c1**2 + d1**2)
            
            if q_norm == 0:
                res = [0.0, 0.0, 0.0, 0.0]
                log_text = "Op: Normalize -> Zero vector cannot be normalized."
            else:
                # 2. 將四大分量同時除以總模長
                res_a = a1 / q_norm
                res_b = b1 / q_norm
                res_c = c1 / q_norm
                res_d = d1 / q_norm
                res = [res_a, res_b, res_c, res_d]
                log_text = f"Op: Normalize -> Target projected to unit sphere ({res_a:.4f}, {res_b:.4f}, {res_c:.4f}, {res_d:.4f})"

        trajectory.append(res)
        history_logs.append(log_text)
        
        fig = go.Figure()
        pts = np.array(trajectory)
        
        # --- 繪製首尾相連的空間向量箭頭 ---
        for i in range(len(pts) - 1):
            start = pts[i][:3]
            end = pts[i+1][:3]
            is_last = (i == len(pts) - 2)
            arrow_color = '#28a745' if is_last else '#17a2b8'
            name_text = 'Latest Vector Step' if is_last else f'Step {i+1}'
            
            fig.add_trace(go.Scatter3d(
                x=[start[0], end[0]], y=[start[1], end[1]], z=[start[2], end[2]],
                mode='lines+markers',
                line=dict(color=arrow_color, width=6),
                marker=dict(size=4, color=arrow_color),
                name=name_text,
                showlegend=True if (i==0 or is_last) else False
            ))

        # --- 處理紅色模長線段與空間文字項目 (已精確修復索引死角) ---
        latest_res = pts[-1][:3]
        norm_val = np.sqrt(latest_res[0]**2 + latest_res[1]**2 + latest_res[2]**2)

        if show_norm:
            fig.add_trace(go.Scatter3d(
                x=[0, latest_res[0]], y=[0, latest_res[1]], z=[0, latest_res[2]], # <-- 修復完畢！
                mode='lines',
                line=dict(color='#dc3545', width=4, dash='dash'),
                name=f'Norm Distance ({norm_val:.3f})'
            ))
            fig.add_trace(go.Scatter3d(
                x=[latest_res[0]], y=[latest_res[1]], z=[latest_res[2]],
                mode='text',
                text=[f'  |Norm| = {norm_val:.3f}'],
                textposition="top center",
                textfont=dict(color="#dc3545", size=12, family="Arial Black"),
                showlegend=False
            ))
   
        # 格式化數值文字框
        text_res = (f"a (Real) = {res[0]:.4f}\n"
                    f"b (i-axis) = {res[1]:.4f}\n"
                    f"c (j-axis) = {res[2]:.4f}\n"
                    f"d (k-proj) = {res[3]:.4f}\n"
                    f"--------------------\n"
                    f"Vector Norm (3D Space) = {norm_val:.4f}")
        
        max_bound = max(np.max(np.abs(pts[:, :3])), 5.0) * 1.2
        fig.update_layout(
            title="Imperfect Tri-nion Geometric Vector Steps",
            scene=dict(
                xaxis=dict(title='a (Real / X-axis)', range=[-max_bound, max_bound], showgrid=True, zeroline=True, zerolinecolor='black', zerolinewidth=4),
                yaxis=dict(title='b (i-axis / Y-space)', range=[-max_bound, max_bound], showgrid=True, zeroline=True, zerolinecolor='black', zerolinewidth=4),
                zaxis=dict(title='c (j-axis / Z-height)', range=[-max_bound, max_bound], showgrid=True, zeroline=True, zerolinecolor='black', zerolinewidth=4),
            ),
            margin=dict(l=0, r=0, b=0, t=40),
            legend=dict(x=0, y=1)
        )
        
        # 1. 這裡直接拿您的 4D 陣列 res 算完美的 4D 平方與開根號總能量
        algebraic_energy = np.sqrt(res[0]**2 + res[1]**2 + res[2]**2 + res[3]**2)

        # 2. 🔥 將代數總能量當作註解，換行黏貼到原本的文字結果 (text_res) 最下方
        text_res += f"\n----------------------------------------\n⚡ [系統代數總能量:algebraic_energy (Full 4D Norm)] = {algebraic_energy:.4f}"

        return res[0], res[1], res[2], res[3], "\n".join(history_logs), text_res, fig
        
    except ZeroDivisionError as e:
        # 您原本的除法錯誤捕捉（保持完全不動）
        return a1, b1, c1, d1, "\n".join(history_logs), f"❌ Computation Failed: Zero Divisor Detected", gr.Error(str(e))
        
    except Exception as e:
        # 新增：捕捉其他潛在錯誤（例如開根號可能產生的數學域錯誤）
        return a1, b1, c1, d1, "\n".join(history_logs), f"❌ Unexpected Error: {str(e)}", gr.Error(str(e))

def reset_all():
    global trajectory, history_logs
    trajectory = [[1.0, 1.0, 1.0, 0.0]]
    history_logs = ["System ready. Initial state is A."]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(
        x=[0, 1], y=[0, 1], z=[0, 1],
        mode='lines+markers', line=dict(color='#17a2b8', width=6), name='Initial Vector A'
    ))
    fig.update_layout(
        title="Imperfect Tri-nion Geometric Vector Steps",
        scene=dict(
            xaxis=dict(title='a (Real)', range=[-3, 3]),
            yaxis=dict(title='b (i-axis)', range=[-3, 3]),
            zaxis=dict(title='c (j-axis)', range=[-3, 3]),
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, "System ready. Initial state is A.", "a = 1.0000\nb = 1.0000\nc = 1.0000\nd = 0.0000\n--------------------\nVector Norm (3D Space) = 1.7321", fig

# ========================================================
# 3. 建立網頁操作介面外殼 (改用互動式 gr.Plot)
# ========================================================

with gr.Blocks(title="三元數沙盒 Trionion sandbox") as demo:
    gr.Markdown("# 三元數計算機 Trionion Arithmetic System")
    gr.Markdown("### （i² = -1；j² = i；ij = j³）")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 1. Current accumulated result (Initial value: A) ""目前運算累積結果 (初始值為 A)")
            with gr.Row():
                a1 = gr.Number(value=1.0, label="a (實部 Real part)")
                b1 = gr.Number(value=1.0, label="b (i軸 i-axis)")
                c1 = gr.Number(value=1.0, label="c (j軸 j-axis)")
                d1 = gr.Number(value=0.0, label="d (ij分量 ij-projected component)")
                
            gr.Markdown("### 2. 連續計算：請選擇運算子與下一組三元數。 Sequential Computation: Select an operator and the next Trionion.")
            op = gr.Radio(["加 Add (+)", "減 Subtract (-)", "乘 Multiply (*)", "除 Divide (/)", "開根號 Sqrt (√)", "單位化 (Normalize)"], label="選擇運算符號", value="乘 (*)")
            # 請在選擇運算符號的下方，插入這行專業的幾何特異點警告加註
            gr.Markdown("<span style='color: #dc3545; font-size: 14px; font-weight: 500;'>🚨 <b>Geometric Singularities (Zero Divisors):</b> Occurs when <i>a = b</i> and <i>c = ±√2a</i> (with <i>d = 0</i>). Division will be blocked by the system defense matrix.</span>")
            show_norm = gr.Checkbox(label="(顯示 3D 幾何距離與 4D 代數能量項目。) Show 3D Distance & 4D Algebraic Energy ", value=True)
            
            # 2. 【核心修改】在 a2, b2, c2, d2 的外層，用 gr.Group() 包起來並命名為 next_group
            with gr.Group() as next_group:
                with gr.Row():
                    a2 = gr.Number(value=1.0, label="a (實部 Real part)")
                    b2 = gr.Number(value=1.0, label="b (i軸 i-axis)")
                    c2 = gr.Number(value=1.0, label="c (j軸 j-axis)")
                    d2 = gr.Number(value=0.0, label="d (ij分量 ij-projected component)")
                
            with gr.Row():
                btn_run = gr.Button("執行此步運算 Run Operation", variant="primary")
                btn_reset = gr.Button("全部清空重置 Reset All", variant="stop")
                
            history = gr.Textbox(value="System ready. Initial state is A.", label="歷程記錄 (鏈式計算歷史)。 Log of Chained computation", lines=4)
            result = gr.Textbox(value="a = 1.0000\nb = 1.0000\nc = 1.0000\nd = 0.0000\n--------------------\nVector Norm (3D Space) = 1.7321", label="最終數值結果")
            
        with gr.Column():
            gr.Markdown("### 3D 幾何空間投影軌跡 (滑鼠滾輪可縮放、拖曳可旋轉)。 3D Geometric Projection Trajectory (Scroll to zoom, drag to rotate)")
            plot_output = gr.Plot(label="3D 投影空間 3D Projection Space") # 改用智慧互動繪圖面板

    # 3. 【核心修改】在 demo.launch() 之前，加上這段「動態隱藏/顯示」的監聽程式碼
    def toggle_next_group(selected_op):
        # 如果是開根號或單位化，都不需要輸入第二組三元數，立刻隱藏
        if selected_op in ["開根號 Sqrt (√)", "單位化 (Normalize)"]:
            return gr.update(visible=False)
        else:
            return gr.update(visible=True)
            
    # 當使用者切換運算符號(op)時，動態改變 next_group 的可見度
    op.change(
        fn=toggle_next_group,
        inputs=[op],
        outputs=[next_group]
    )

    btn_run.click(
        fn=run_step, 
        inputs=[a1, b1, c1, d1, op, a2, b2, c2, d2, show_norm], 
        outputs=[a1, b1, c1, d1, history, result, plot_output]
    )
    btn_reset.click(
        fn=reset_all,
        outputs=[a1, b1, c1, d1, a2, b2, c2, d2, history, result, plot_output]
    )

demo.launch()
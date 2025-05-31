# --- GLOBAL SOLUTION - Resolução Diferenciada de Problemas --- 
# Código com input automático para digitar o RM

def calcular_global_solution(RM):
    print(f"\nRM escolhido: {RM}\n")
    
    # Extração dos algarismos
    RM_str = str(RM).zfill(6)  # Preenche com zeros à esquerda se for menor que 6 dígitos
    A = int(RM_str[0])
    B = int(RM_str[1])
    C = int(RM_str[2])
    D = int(RM_str[3])
    E = int(RM_str[4])
    F = int(RM_str[5]) if len(RM_str) >= 6 else 0

    S = A + B + C + D + E + F
    J = 100 * (E + 20)
    K = 100 * (C + 10)
    M = 1000 * (F + 5)
    N = M + 2 * (J - K)
    V = 200000 * S
    Z = 0.75 * K
    Y = D + 30

    print(f"Valores calculados:")
    print(f"A={A}, B={B}, C={C}, D={D}, E={E}, F={F}")
    print(f"S = {S}")
    print(f"J = {J}")
    print(f"K = {K}")
    print(f"M = {M}")
    print(f"N = {N}")
    print(f"V = {V}")
    print(f"Z = {Z}")
    print(f"Y = {Y}")

    # Questão 1: Q(P)
    coeficiente = (N - M) / (K - J)
    intercepto = M - coeficiente * J
    print(f"\n[Questão 1] Função Q(P) = {coeficiente:.4f}P + {intercepto:.4f}")

    # Questão 2: P(Q)
    coef_inv = 1 / coeficiente
    intercepto_inv = -intercepto / coeficiente
    print(f"[Questão 2] Função P(Q) = {coef_inv:.4f}Q + {intercepto_inv:.4f}")

    # Questão 3
    print(f"[Questão 3a] Função G(Q) = {V} + {Z:.4f}Q")
    print(f"[Questão 3b] Função G(P) = {V} + {Z*coeficiente:.4f}P + {Z*intercepto:.4f}")

    # Questão 4
    print(f"[Questão 4] Função T(P) = {coeficiente:.4f}P² + {intercepto:.4f}P")

    # Questão 5
    print(f"[Questão 5] Função T(Q) = {coef_inv:.4f}Q² + {intercepto_inv:.4f}Q")

    # Questão 6
    P_rmax = -intercepto / (2 * coeficiente)
    Q_rmax = coeficiente * P_rmax + intercepto
    T_rmax = P_rmax * Q_rmax
    print(f"[Questão 6a] Preço P para maior receita: {P_rmax:.2f} reais")
    print(f"           Quantidade Q: {Q_rmax:.2f} unidades")
    print(f"[Questão 6b] Receita anual máxima: {T_rmax:.2f} reais")

    # Questão 7
    print(f"[Questão 7] Função L(P) = {coeficiente:.4f}P² + {intercepto:.4f}P - ({V} + {Z:.4f}*({coeficiente:.4f}P + {intercepto:.4f}))")

    # Questão 8
    print(f"[Questão 8] Função L(Q) = ({coef_inv:.4f}Q + {intercepto_inv:.4f})*Q - ({V} + {Z:.4f}Q)")

    # Questão 9
    P_lmax = P_rmax
    Q_lmax = coeficiente * P_lmax + intercepto
    L_lmax = (P_lmax * Q_lmax) - (V + Z * Q_lmax)
    print(f"[Questão 9a] Preço P para maior lucro: {P_lmax:.2f} reais")
    print(f"           Quantidade Q: {Q_lmax:.2f} unidades")
    print(f"[Questão 9b] Lucro anual máximo: {L_lmax:.2f} reais")

    # Questão 10
    def W(P):
        T = coeficiente * P**2 + intercepto * P
        return (Y * T) / (Y * P**2 + 20 * P)

    limite1 = W(E + 1)
    limite2 = W(0.000001)  # aproximação para P -> 0

    print(f"[Questão 10a] Limite de W(P) quando P -> E+1: {limite1:.2f}")
    print(f"[Questão 10b] Limite de W(P) quando P -> 0: {limite2:.2f}")

# --- Execução:
if __name__ == "__main__":
    RM_input = input("Digite o RM escolhido (6 dígitos): ")
    calcular_global_solution(RM_input)

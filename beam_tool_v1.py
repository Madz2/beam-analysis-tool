# ============================================================
#  Beam Analysis Tool  —  Version 1
#  Simply-supported beam: reactions, shear force & bending moment
#  Handles: central point load, off-centre point load, UDL
#  All equations derived by hand from equilibrium first.
# ============================================================

import numpy as np
import matplotlib.pyplot as plt


def analyse_beam():
    print("Simply-supported beam analysis")
    print("Choose load case:")
    print("  1 = point load")
    print("  2 = uniformly distributed load (UDL)")
    case = input("Enter 1 or 2: ").strip()

    L = float(input("Span length L (m): "))

    # positions along the beam, every 0.05 m
    x_values = np.arange(0, L + 0.001, 0.05)
    V_values = []   # shear force at each position
    M_values = []   # bending moment at each position

    # ---------------- POINT LOAD ----------------
    if case == "1":
        P = float(input("Point load P (kN): "))
        a = float(input("Load position 'a' from left support A (m): "))

        # Reactions (moments about A -> R_B, then vertical equilibrium -> R_A)
        R_B = P * a / L
        R_A = P * (L - a) / L

        for x in x_values:
            if x <= a:                       # cut is before the load
                V = R_A
                M = R_A * x
            else:                            # cut is after the load
                V = R_A - P
                M = R_A * x - P * (x - a)
            V_values.append(V)
            M_values.append(M)

    # ---------------- UDL ----------------
    elif case == "2":
        w = float(input("Distributed load w (kN/m): "))

        # Equivalent load w*L acts at centre -> reactions split evenly
        R_A = w * L / 2
        R_B = w * L / 2

        for x in x_values:
            V = R_A - w * x                  # shear falls off as load accumulates
            M = R_A * x - w * x**2 / 2       # x**2 term makes the moment a curve
            V_values.append(V)
            M_values.append(M)

    else:
        print("Invalid choice — please run again and enter 1 or 2.")
        return

    # ---------------- Peak values ----------------
    M_max = max(M_values)
    x_at_Mmax = x_values[M_values.index(M_max)] if isinstance(M_values, list) else 0

    print("\n--- Results ---")
    print(f"Reaction at A (R_A): {R_A:.2f} kN")
    print(f"Reaction at B (R_B): {R_B:.2f} kN")
    print(f"Maximum bending moment: {M_max:.2f} kNm at x = {x_at_Mmax:.2f} m")

    # ---------------- Plot ----------------
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

    ax1.plot(x_values, V_values)
    ax1.set_title("Shear Force Diagram")
    ax1.set_ylabel("Shear (kN)")
    ax1.axhline(0, color="black", linewidth=0.8)
    ax1.grid(True, linestyle="--", alpha=0.4)

    ax2.plot(x_values, M_values)
    ax2.set_title("Bending Moment Diagram")
    ax2.set_xlabel("Position along beam (m)")
    ax2.set_ylabel("Moment (kNm)")
    ax2.axhline(0, color="black", linewidth=0.8)
    ax2.grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.show()


analyse_beam()

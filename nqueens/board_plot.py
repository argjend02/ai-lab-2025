# nqueens/board_plot.py
import os
import matplotlib.pyplot as plt

def plot_board(state, path, title=""):
    """
    state: list[int] length N, state[col] = row
    path: where to save PNG
    """
    n = len(state)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    fig, ax = plt.subplots(figsize=(4, 4))
    # chessboard squares
    for x in range(n):
        for y in range(n):
            ax.add_patch(plt.Rectangle((x, y), 1, 1, fill=True, alpha=0.15 if (x+y)%2==0 else 0.0))
    # queens
    xs = list(range(n))
    ys = state
    ax.scatter(xs, ys, s=160, marker='X')  # big X for queen
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect('equal')
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_title(title)
    plt.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)

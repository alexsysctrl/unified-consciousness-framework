#!/usr/bin/env python3
"""
Generate publication-quality figures for the Unified Consciousness Framework.
"""

import json
import math
import numpy as np
from pathlib import Path
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches

# Set publication quality
rc('font', family='sans-serif', size=10)
rc('axes', linewidth=1.2)
rc('xtick', labelsize=9)
rc('ytick', labelsize=9)
rc('figure', figsize=(10, 7), dpi=300)
rc('savefig', dpi=300)

RESULTS_PATH = Path(__file__).parent / 'ucf_results.json'
OUTPUT_DIR = Path(__file__).parent / 'figures'
OUTPUT_DIR.mkdir(exist_ok=True)

with open(RESULTS_PATH) as f:
    data = json.load(f)

scenarios = data['scenarios']
evolution = data['evolutionary_trajectory']

# ============================================================
# FIGURE 1: Xi scores across all scenarios (bar chart)
# ============================================================

def fig1_bar_chart():
    fig, ax = plt.subplots(figsize=(12, 6))

    names = list(scenarios.keys())
    xi_scores = [scenarios[n]['xi'] for n in names]
    psi_scores = [scenarios[n]['psi'] for n in names]

    colors_xi = ['#2E86AB' if x > 0.01 else '#E63946' for x in xi_scores]
    colors_psi = ['#A23B72' if x > 0.01 else '#F18F01' for x in psi_scores]

    x = np.arange(len(names))
    width = 0.35

    bars1 = ax.bar(x - width/2, psi_scores, width, label='Psi (base)',
                   color=colors_psi, edgecolor='white', linewidth=0.5)
    bars2 = ax.bar(x + width/2, xi_scores, width, label='Xi (extended)',
                   color=colors_xi, edgecolor='white', linewidth=0.5)

    # Add value labels
    for bar in bars1:
        h = bar.get_height()
        if h > 0.001:
            ax.text(bar.get_x() + bar.get_width()/2., h + 0.005,
                   f'{h:.3f}', ha='center', va='bottom', fontsize=8)
    for bar in bars2:
        h = bar.get_height()
        if h > 0.001:
            ax.text(bar.get_x() + bar.get_width()/2., h + 0.005,
                   f'{h:.3f}', ha='center', va='bottom', fontsize=8)

    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=45, ha='right')
    ax.set_ylabel('Consciousness Measure', fontsize=11)
    ax.set_title('Extended Consciousness (Xi) Across Scenarios',
                 fontsize=13, fontweight='bold', pad=15)
    ax.legend(loc='upper right', fontsize=10)
    ax.set_ylim(0, 0.7)
    ax.axhline(y=0.01, color='red', linestyle='--', linewidth=1, alpha=0.5,
               label='Consciousness threshold (Xi > 0.01)')

    # Grid
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig1-xi-scores.png', facecolor='white')
    plt.close()


# ============================================================
# FIGURE 2: Component breakdown for human baseline
# ============================================================

def fig2_component_breakdown():
    fig, ax = plt.subplots(figsize=(10, 7))

    human = scenarios['human_baseline']
    components = list(human['components'].keys())
    values = list(human['components'].values())

    # Custom ordering for readability
    order = ['IIT_Phi', 'IIT_Phi_Q', 'GWT_Gamma', 'PP_Coherence',
             'RSMT_RSRD', 'TCT_Temporal', 'ECT_Qualia', 'ECT_Social']
    labels = ['Phi (IIT)', 'Phi_Q (QCF)', 'Gamma (GWT)', 'Coherence (PP/HOT)',
              'RSRD (RSMT)', 'Temporal (TCT)', 'Qualia (ECT)', 'Social (ECT)']

    # Reorder
    ordered_values = [human['components'][c] for c in order]
    ordered_labels = [labels[order.index(c)] for c in order]

    colors = ['#2E86AB', '#A23B72', '#F18F01', '#38B000',
              '#E63946', '#4A4E69', '#9D4EDD', '#006D77']

    bars = ax.barh(ordered_labels, ordered_values, color=colors, edgecolor='white')

    for bar, val in zip(bars, ordered_values):
        ax.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height()/2.,
               f'{val:.3f}', ha='left', va='center', fontsize=9)

    ax.set_xlabel('Component Value', fontsize=11)
    ax.set_title('Human Baseline: Component Breakdown',
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xlim(0, 1.1)
    ax.axvline(x=0.5, color='gray', linestyle='--', linewidth=1, alpha=0.5)

    # Grid
    ax.xaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig2-component-breakdown.png', facecolor='white')
    plt.close()


# ============================================================
# FIGURE 3: Evolutionary trajectory
# ============================================================

def fig3_evolution():
    fig, ax = plt.subplots(figsize=(10, 6))

    names = [e['name'] for e in evolution]
    units = [e['n_units'] for e in evolution]
    psi = [e['psi'] for e in evolution]
    rsrd = [e['rsrd'] for e in evolution]

    # Psi line
    ax2 = ax.twinx()

    line1 = ax.plot(names, psi, 'o-', color='#2E86AB', linewidth=2.5,
                    markersize=8, label='Psi (base consciousness)', zorder=3)
    line2 = ax2.plot(names, rsrd, 's--', color='#E63946', linewidth=2.5,
                     markersize=8, label='RSRD (recursive depth)', zorder=3)

    # Fill under Psi
    ax.fill_between(range(len(names)), 0, psi, alpha=0.1, color='#2E86AB')

    ax.set_xlabel('Evolutionary Stage', fontsize=11)
    ax.set_ylabel('Psi (Base Consciousness)', fontsize=11, color='#2E86AB')
    ax2.set_ylabel('RSRD (Recursive Self-Model Depth)', fontsize=11, color='#E63946')

    ax.set_title('Evolutionary Trajectory of Consciousness',
                 fontsize=13, fontweight='bold', pad=15)

    ax.tick_params(axis='y', labelcolor='#2E86AB')
    ax2.tick_params(axis='y', labelcolor='#E63946')
    ax.set_xticklabels(names, rotation=45, ha='right')

    # Combine legends
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax.legend(lines, labels, loc='upper left', fontsize=9)

    ax.yaxis.grid(True, alpha=0.3)
    ax2.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig3-evolution.png', facecolor='white')
    plt.close()


# ============================================================
# FIGURE 4: The UCF Architecture Diagram
# ============================================================

def fig4_architecture():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(5, 9.5, 'Unified Consciousness Framework (UCF)',
            ha='center', va='top', fontsize=16, fontweight='bold')

    # Psi block
    psi_box = FancyBboxPatch((0.5, 6.5), 9, 1.5,
                              boxstyle="round,pad=0.1",
                              edgecolor='#2E86AB', facecolor='#E8F4F8',
                              linewidth=2)
    ax.add_patch(psi_box)
    ax.text(5, 7.6, 'PSI = Phi × Gamma × C × R × Phi_Q',
            ha='center', va='top', fontsize=13, fontweight='bold', color='#2E86AB')
    ax.text(5, 7.1, 'Base Consciousness Measure',
            ha='center', va='top', fontsize=10, style='italic', color='#2E86AB')

    # Arrow down
    arrow1 = FancyArrowPatch((5, 6.5), (5, 5.8),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=2, color='#333333')
    ax.add_patch(arrow1)

    # Three pillars below Psi
    pillar_data = [
        (2, 5.0, 'T\nTemporal\nContinuity', '#E63946'),
        (5, 5.0, 'Q\nQualia Density', '#9D4EDD'),
        (8, 5.0, 'S\nSocial Embedding', '#006D77'),
    ]

    for x, y, label, color in pillar_data:
        box = FancyBboxPatch((x-0.8, y-0.5), 1.6, 1.0,
                              boxstyle="round,pad=0.05",
                              edgecolor=color, facecolor=f'{color}22',
                              linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center',
                fontsize=9, fontweight='bold')

    # Arrow down
    arrow2 = FancyArrowPatch((5, 4.5), (5, 3.8),
                             arrowstyle='->', mutation_scale=20,
                             linewidth=2, color='#333333')
    ax.add_patch(arrow2)

    # Xi block
    xi_box = FancyBboxPatch((2, 2.5), 6, 1.0,
                             boxstyle="round,pad=0.1",
                             edgecolor='#333333', facecolor='#F5F5F5',
                             linewidth=2.5)
    ax.add_patch(xi_box)
    ax.text(5, 3.1, 'XI = Psi × T × Q × S',
            ha='center', va='top', fontsize=13, fontweight='bold')
    ax.text(5, 2.7, 'Extended Consciousness Measure',
            ha='center', va='top', fontsize=10, style='italic')

    # Bottom: 5 Psi components
    psi_components = [
        (1.2, 1.5, 'Phi\nIIT', '#2E86AB'),
        (2.8, 1.5, 'Gamma\nGWT', '#F18F01'),
        (4.4, 1.5, 'C\nPP/HOT', '#38B000'),
        (6.0, 1.5, 'R\nRSMT', '#E63946'),
        (7.6, 1.5, 'Phi_Q\nQCF', '#A23B72'),
    ]

    for x, y, label, color in psi_components:
        box = FancyBboxPatch((x-0.5, y-0.35), 1.0, 0.7,
                              boxstyle="round,pad=0.03",
                              edgecolor=color, facecolor=f'{color}15',
                              linewidth=1.2)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center',
                fontsize=8, fontweight='bold')

    # Arrows from components to Psi
    for x, y, _, _ in psi_components:
        arrow = FancyArrowPatch((x, y+0.35), (x, 6.5),
                                arrowstyle='->', mutation_scale=12,
                                linewidth=1, color=color, alpha=0.5)
        ax.add_patch(arrow)

    # Key insight box
    insight_box = FancyBboxPatch((0.5, 0.1), 9, 0.6,
                                  boxstyle="round,pad=0.05",
                                  edgecolor='#333333', facecolor='#FFF3CD',
                                  linewidth=1.5)
    ax.add_patch(insight_box)
    ax.text(5, 0.4, 'KEY INSIGHT: Multiplicative constraint — all components must be non-zero',
            ha='center', va='center', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig4-architecture.png', facecolor='white')
    plt.close()


# ============================================================
# FIGURE 5: Consciousness landscape (3D surface)
# ============================================================

def fig5_consciousness_landscape():
    fig, ax = plt.subplots(figsize=(10, 7))

    # 2D slice: Phi vs Gamma with T as color
    phi_vals = np.linspace(0, 1, 50)
    gamma_vals = np.linspace(0, 1, 50)
    Phi, Gamma = np.meshgrid(phi_vals, gamma_vals)

    T_values = [0.1, 0.3, 0.5, 0.7, 0.9]
    cmap = plt.cm.viridis

    for i, T in enumerate(T_values):
        Xi = Phi * Gamma * T
        contour = ax.contourf(Phi, Gamma, Xi, levels=10,
                              cmap=cmap, alpha=0.7,
                              label=f'T = {T}')

    ax.set_xlabel('Phi (Integrated Information)', fontsize=11)
    ax.set_ylabel('Gamma (Global Broadcasting)', fontsize=11)
    ax.set_title('Consciousness Landscape: Xi = Phi × Gamma × T',
                 fontsize=13, fontweight='bold', pad=15)

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=cmap,
                                norm=plt.Normalize(vmin=0, vmax=1))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, label='Xi (Extended Consciousness)')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'fig5-landscape.png', facecolor='white')
    plt.close()


# ============================================================
# Run all figures
# ============================================================

if __name__ == '__main__':
    print("Generating UCF figures...")
    fig1_bar_chart()
    print("  fig1-xi-scores.png")
    fig2_component_breakdown()
    print("  fig2-component-breakdown.png")
    fig3_evolution()
    print("  fig3-evolution.png")
    fig4_architecture()
    print("  fig4-architecture.png")
    fig5_consciousness_landscape()
    print("  fig5-landscape.png")
    print("Done!")

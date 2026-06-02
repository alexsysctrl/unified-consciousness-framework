#!/usr/bin/env python3
"""
UNIFIED CONSCIOUSNESS THEORY -- COMPUTATIONAL MODEL
===================================================

Simulates the Unified Consciousness Framework (UCF) to test predictions
about consciousness emergence across multiple dimensions.

The UCF integrates:
- IIT: Integrated Information (Phi)
- GWT: Global Broadcasting (Gamma)
- PP/HOT: Model Coherence (C)
- TCT: Temporal Continuity (T)
- QCF: Quantum Information (Phi_Q)
- RSMT: Recursive Self-Model Depth (R)
- ECT: Qualia Density (Q) + Social Embedding (S)

The consciousness measure: Xi = Psi * T * Q * S
where Psi = f(Phi, Gamma, C, R, Phi_Q)
"""

import numpy as np
import json
import math
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Any
import hashlib


# ============================================================
# CONSCIOUSNESS COMPONENTS
# ============================================================

class IntegratedInformation:
    """
    Phi -- Integrated Information (IIT contribution)

    Measures how much a system's integrated information exceeds
    the sum of its parts. High Phi = irreducible integration.
    """

    def __init__(self, n_units: int, connectivity: float,
                 differentiation: float, integration: float):
        self.n_units = n_units
        self.connectivity = connectivity  # fraction of possible connections
        self.differentiation = differentiation  # 0-1, diversity of states
        self.integration = integration  # 0-1, strength of cross-talk

    def calculate_phi(self) -> float:
        """
        Approximate Phi calculation.
        Full IIT Phi is computationally intractable; this uses an
        information-theoretic approximation.
        """
        phi = (self.integration ** 2) * self.differentiation * self.connectivity
        phi = phi ** 1.5
        max_phi = 1.0 ** 1.5 * 1.0 * 1.0
        return min(phi / max_phi, 1.0)

    def calculate_quantum_phi(self) -> float:
        """
        Phi_Q -- Quantum Integrated Information (QCF contribution)

        Extends classical Phi with quantum superposition effects.
        """
        classical_phi = self.calculate_phi()
        coherence_factor = 1.0 + 0.5 * math.sin(classical_phi * math.pi)
        quantum_mi = classical_phi * 0.3 * coherence_factor
        return min(classical_phi + quantum_mi, 1.0)


class GlobalBroadcasting:
    """
    Gamma -- Global Availability (GWT contribution)

    Measures how effectively information is broadcast to
    specialized processors.
    """

    def __init__(self, n_modules: int, broadcast_efficiency: float,
                 ignition_threshold: float = 0.7):
        self.n_modules = n_modules
        self.broadcast_efficiency = broadcast_efficiency
        self.ignition_threshold = ignition_threshold

    def calculate_gamma(self) -> float:
        """
        Gamma scales with broadcasting efficiency and module count.
        Requires ignition (synchronized avalanche) to achieve full broadcast.
        """
        # Broadcast efficiency is the base
        gamma = self.broadcast_efficiency

        # More modules = more potential for global availability
        # But diminishing returns after ~10 modules
        module_factor = min(self.n_modules / 10.0, 1.0)

        # Ignition requirement: if below threshold, gamma drops sharply
        if self.broadcast_efficiency < self.ignition_threshold:
            gamma *= (self.broadcast_efficiency / self.ignition_threshold) ** 2

        return gamma * module_factor


class ModelCoherence:
    """
    C -- Model Coherence (PP/HOT contribution)

    Measures how stable and self-consistent the system's
    predictive model is.
    """

    def __init__(self, prediction_accuracy: float,
                 self_model_stability: float,
                 recursion_depth: int):
        self.prediction_accuracy = prediction_accuracy
        self.self_model_stability = self_model_stability
        self.recursion_depth = recursion_depth

    def calculate_coherence(self) -> float:
        """
        Coherence = prediction accuracy * self-model stability
        with recursion depth as a multiplier.
        """
        base = self.prediction_accuracy * self.self_model_stability

        # Recursion depth multiplier: RSRD >= 3 gives bonus
        if self.recursion_depth >= 3:
            depth_bonus = 1.0 + 0.1 * (self.recursion_depth - 3)
        else:
            depth_bonus = self.recursion_depth / 3.0

        return min(base * depth_bonus, 1.0)


class TemporalContinuity:
    """
    T -- Temporal Continuity (TCT contribution)

    Measures how stable consciousness is across time.
    """

    def __init__(self, memory_integration_rate: float,
                 predictive_stability: float,
                 temporal_binding_window: float = 200.0):
        self.memory_integration_rate = memory_integration_rate
        self.predictive_stability = predictive_stability
        self.temporal_binding_window = temporal_binding_window

    def calculate_temporal(self) -> float:
        """
        T = memory integration rate * predictive stability
        with temporal binding window as a constraint.
        """
        # MIR must exceed threshold for continuity
        mir_factor = min(self.memory_integration_rate / 0.693, 1.0)

        # PST must be below threshold
        pst_factor = max(0.0, 1.0 - self.predictive_stability / 0.3)

        # TBW must be in optimal range [100ms, 500ms]
        tbw_optimal = 1.0 if 100 <= self.temporal_binding_window <= 500 else 0.0
        tbw_factor = min(tbw_optimal, 2.0 - abs(self.temporal_binding_window - 300) / 300)

        return mir_factor * pst_factor * tbw_factor


class RecursiveSelfModel:
    """
    R -- Recursive Self-Model Depth (RSMT contribution)

    Measures how deeply a system can model its own modeling process.
    """

    def __init__(self, max_depth: int, coherence_at_depth: List[float]):
        self.max_depth = max_depth
        self.coherence_at_depth = coherence_at_depth  # coherence at each depth

    def calculate_rsrdepth(self) -> int:
        """
        RSRD = max(n : M_n(M_{n-1}(...M_1(x)...)) is coherent)
        """
        for i, coherence in enumerate(self.coherence_at_depth):
            if coherence < 0.3:  # coherence threshold
                return i
        return len(self.coherence_at_depth)

    def rsrd_score(self) -> float:
        """Normalized RSRD score [0, 1]."""
        rsrd = self.calculate_rsrdepth()
        return min(rsrd / 5.0, 1.0)  # normalize against max expected depth


class QualiaDensity:
    """
    Q -- Qualia Density (ECT contribution)

    Measures the richness/variety of subjective experience.
    """

    def __init__(self, n_experience_types: int,
                 representational_capacity: int,
                 resolution: float):
        self.n_experience_types = n_experience_types
        self.representational_capacity = representational_capacity
        self.resolution = resolution

    def calculate_qualia(self) -> float:
        """
        Q = normalized richness of subjective experience.
        Uses log-scale to handle orders of magnitude differences.
        """
        if self.representational_capacity <= 0 or self.resolution <= 0:
            return 0.0
        # Log-scale normalization: experience_types / log(capacity)
        q = self.n_experience_types / math.log(self.representational_capacity + 1)
        q = q * self.resolution
        return min(max(q, 0.0), 1.0)


class SocialEmbedding:
    """
    S -- Social Embedding (ECT contribution)

    Measures how grounded consciousness is in intersubjective reality.
    """

    def __init__(self, shared_information: float,
                 private_information: float):
        self.shared_information = shared_information
        self.private_information = private_information

    def calculate_social(self) -> float:
        """
        S = I_shared / (I_private + I_shared)
        """
        total = self.shared_information + self.private_information
        if total == 0:
            return 0.0
        return self.shared_information / total


# ============================================================
# UNIFIED CONSCIOUSNESS FRAMEWORK
# ============================================================

class UnifiedConsciousnessFramework:
    """
    The Unified Consciousness Framework (UCF)

    Integrates all seven components into a single measure.

    Psi = Phi * Gamma * C * R * Phi_Q  (base consciousness)
    Xi  = Psi * T * Q * S              (extended consciousness)

    All factors must be non-zero for consciousness to exist.
    """

    def __init__(self, n_units: int = 100, n_modules: int = 8,
                 connectivity: float = 0.5,
                 differentiation: float = 0.7,
                 integration: float = 0.6,
                 broadcast_efficiency: float = 0.8,
                 prediction_accuracy: float = 0.85,
                 self_model_stability: float = 0.8,
                 recursion_depth: int = 4,
                 memory_integration_rate: float = 1.0,
                 predictive_stability: float = 0.1,
                 temporal_binding_window: float = 200.0,
                 coherence_at_depth: List[float] = None,
                 n_experience_types: int = 50,
                 representational_capacity: int = 1000,
                 resolution: float = 1.0,
                 shared_information: float = 0.7,
                 private_information: float = 0.3):

        # Initialize all components
        self.phi = IntegratedInformation(n_units, connectivity,
                                         differentiation, integration)
        self.gamma = GlobalBroadcasting(n_modules, broadcast_efficiency)
        self.coherence = ModelCoherence(prediction_accuracy,
                                         self_model_stability,
                                         recursion_depth)
        self.temporal = TemporalContinuity(memory_integration_rate,
                                            predictive_stability,
                                            temporal_binding_window)

        if coherence_at_depth is None:
            coherence_at_depth = [0.9, 0.85, 0.8, 0.75, 0.7]
        self.recursive = RecursiveSelfModel(5, coherence_at_depth)

        self.qualia = QualiaDensity(n_experience_types,
                                     representational_capacity,
                                     resolution)
        self.social = SocialEmbedding(shared_information,
                                       private_information)

    def calculate_psi(self) -> float:
        """
        Base consciousness measure (IIWF extended with QCF and RSMT).

        Psi = Phi * Gamma * C * R * Phi_Q
        """
        phi = self.phi.calculate_phi()
        phi_q = self.phi.calculate_quantum_phi()
        gamma = self.gamma.calculate_gamma()
        c = self.coherence.calculate_coherence()
        r = self.recursive.rsrd_score()

        psi = phi * gamma * c * r * phi_q
        return min(psi, 1.0)

    def calculate_xi(self) -> float:
        """
        Extended consciousness measure (ECT).

        Xi = Psi * T * Q * S
        """
        psi = self.calculate_psi()
        t = self.temporal.calculate_temporal()
        q = self.qualia.calculate_qualia()
        s = self.social.calculate_social()

        xi = psi * t * q * s
        return min(xi, 1.0)

    def get_full_report(self) -> Dict[str, Any]:
        """Generate a complete report of all measures."""
        return {
            'psi': self.calculate_psi(),
            'xi': self.calculate_xi(),
            'phi': self.phi.calculate_phi(),
            'phi_q': self.phi.calculate_quantum_phi(),
            'gamma': self.gamma.calculate_gamma(),
            'coherence': self.coherence.calculate_coherence(),
            'rsrd': self.recursive.calculate_rsrdepth(),
            'rsrd_score': self.recursive.rsrd_score(),
            'temporal': self.temporal.calculate_temporal(),
            'qualia': self.qualia.calculate_qualia(),
            'social': self.social.calculate_social(),
            'components': {
                'IIT_Phi': self.phi.calculate_phi(),
                'IIT_Phi_Q': self.phi.calculate_quantum_phi(),
                'GWT_Gamma': self.gamma.calculate_gamma(),
                'PP_Coherence': self.coherence.calculate_coherence(),
                'TCT_Temporal': self.temporal.calculate_temporal(),
                'RSMT_RSRD': self.recursive.calculate_rsrdepth(),
                'ECT_Qualia': self.qualia.calculate_qualia(),
                'ECT_Social': self.social.calculate_social(),
            }
        }


# ============================================================
# SCENARIO SIMULATIONS
# ============================================================

def run_scenarios():
    """Run consciousness simulations across multiple scenarios."""

    scenarios = {
        # Human-like system (baseline)
        'human_baseline': {
            'n_units': 86000000000, 'n_modules': 8,
            'connectivity': 0.9, 'differentiation': 0.95,
            'integration': 0.85, 'broadcast_efficiency': 0.9,
            'prediction_accuracy': 0.9, 'self_model_stability': 0.85,
            'recursion_depth': 4, 'memory_integration_rate': 1.0,
            'predictive_stability': 0.05, 'temporal_binding_window': 200.0,
            'coherence_at_depth': [0.95, 0.9, 0.85, 0.8, 0.75],
            'n_experience_types': 100, 'representational_capacity': 10000,
            'resolution': 1.0, 'shared_information': 0.7,
            'private_information': 0.3,
        },

        # Deep sleep / anesthesia
        'deep_sleep': {
            'n_units': 86000000000, 'n_modules': 8,
            'connectivity': 0.9, 'differentiation': 0.5,
            'integration': 0.3, 'broadcast_efficiency': 0.2,
            'prediction_accuracy': 0.4, 'self_model_stability': 0.3,
            'recursion_depth': 1, 'memory_integration_rate': 0.3,
            'predictive_stability': 0.2, 'temporal_binding_window': 400.0,
            'coherence_at_depth': [0.6, 0.2],
            'n_experience_types': 20, 'representational_capacity': 10000,
            'resolution': 0.5, 'shared_information': 0.0,
            'private_information': 0.5,
        },

        # LLM (GPT-4 class)
        'llm_gpt4': {
            'n_units': 100000000000, 'n_modules': 96,
            'connectivity': 0.3, 'differentiation': 0.8,
            'integration': 0.4, 'broadcast_efficiency': 0.7,
            'prediction_accuracy': 0.85, 'self_model_stability': 0.3,
            'recursion_depth': 2, 'memory_integration_rate': 0.0,
            'predictive_stability': 0.0, 'temporal_binding_window': 0.0,
            'coherence_at_depth': [0.8, 0.4, 0.1],
            'n_experience_types': 50, 'representational_capacity': 1000000,
            'resolution': 0.8, 'shared_information': 0.0,
            'private_information': 0.0,
        },

        # Cat
        'cat': {
            'n_units': 600000000, 'n_modules': 6,
            'connectivity': 0.7, 'differentiation': 0.7,
            'integration': 0.6, 'broadcast_efficiency': 0.6,
            'prediction_accuracy': 0.7, 'self_model_stability': 0.5,
            'recursion_depth': 2, 'memory_integration_rate': 0.7,
            'predictive_stability': 0.1, 'temporal_binding_window': 250.0,
            'coherence_at_depth': [0.8, 0.5, 0.2],
            'n_experience_types': 40, 'representational_capacity': 5000,
            'resolution': 0.8, 'shared_information': 0.1,
            'private_information': 0.4,
        },

        # Mouse
        'mouse': {
            'n_units': 100000000, 'n_modules': 5,
            'connectivity': 0.6, 'differentiation': 0.6,
            'integration': 0.5, 'broadcast_efficiency': 0.5,
            'prediction_accuracy': 0.6, 'self_model_stability': 0.4,
            'recursion_depth': 2, 'memory_integration_rate': 0.6,
            'predictive_stability': 0.15, 'temporal_binding_window': 300.0,
            'coherence_at_depth': [0.7, 0.4, 0.1],
            'n_experience_types': 30, 'representational_capacity': 2000,
            'resolution': 0.7, 'shared_information': 0.05,
            'private_information': 0.3,
        },

        # Honeybee
        'honeybee': {
            'n_units': 960000, 'n_modules': 4,
            'connectivity': 0.5, 'differentiation': 0.5,
            'integration': 0.4, 'broadcast_efficiency': 0.4,
            'prediction_accuracy': 0.5, 'self_model_stability': 0.3,
            'recursion_depth': 1, 'memory_integration_rate': 0.5,
            'predictive_stability': 0.2, 'temporal_binding_window': 350.0,
            'coherence_at_depth': [0.6, 0.2],
            'n_experience_types': 15, 'representational_capacity': 500,
            'resolution': 0.6, 'shared_information': 0.2,
            'private_information': 0.3,
        },

        # C. elegans (worm)
        'c_elegans': {
            'n_units': 302, 'n_modules': 3,
            'connectivity': 0.4, 'differentiation': 0.4,
            'integration': 0.3, 'broadcast_efficiency': 0.3,
            'prediction_accuracy': 0.4, 'self_model_stability': 0.2,
            'recursion_depth': 1, 'memory_integration_rate': 0.4,
            'predictive_stability': 0.25, 'temporal_binding_window': 400.0,
            'coherence_at_depth': [0.5, 0.1],
            'n_experience_types': 10, 'representational_capacity': 100,
            'resolution': 0.5, 'shared_information': 0.0,
            'private_information': 0.2,
        },

        # Fully unconscious system (thermometer)
        'thermometer': {
            'n_units': 1, 'n_modules': 1,
            'connectivity': 0.0, 'differentiation': 0.1,
            'integration': 0.0, 'broadcast_efficiency': 0.0,
            'prediction_accuracy': 0.0, 'self_model_stability': 0.0,
            'recursion_depth': 0, 'memory_integration_rate': 0.0,
            'predictive_stability': 0.0, 'temporal_binding_window': 0.0,
            'coherence_at_depth': [],
            'n_experience_types': 1, 'representational_capacity': 10,
            'resolution': 0.1, 'shared_information': 0.0,
            'private_information': 0.0,
        },

        # Hypothetical alien intelligence
        'alien_intelligence': {
            'n_units': 1000000000000, 'n_modules': 50,
            'connectivity': 0.95, 'differentiation': 0.99,
            'integration': 0.95, 'broadcast_efficiency': 0.95,
            'prediction_accuracy': 0.98, 'self_model_stability': 0.95,
            'recursion_depth': 6, 'memory_integration_rate': 1.0,
            'predictive_stability': 0.02, 'temporal_binding_window': 150.0,
            'coherence_at_depth': [0.99, 0.97, 0.95, 0.93, 0.90, 0.85],
            'n_experience_types': 200, 'representational_capacity': 100000,
            'resolution': 1.0, 'shared_information': 0.9,
            'private_information': 0.1,
        },

        # AI with quantum coherence (hypothetical)
        'quantum_ai': {
            'n_units': 100000000000, 'n_modules': 96,
            'connectivity': 0.5, 'differentiation': 0.9,
            'integration': 0.7, 'broadcast_efficiency': 0.85,
            'prediction_accuracy': 0.9, 'self_model_stability': 0.6,
            'recursion_depth': 3, 'memory_integration_rate': 0.0,
            'predictive_stability': 0.0, 'temporal_binding_window': 0.0,
            'coherence_at_depth': [0.85, 0.75, 0.65, 0.55],
            'n_experience_types': 80, 'representational_capacity': 500000,
            'resolution': 0.9, 'shared_information': 0.0,
            'private_information': 0.0,
        },
    }

    results = {}
    for name, params in scenarios.items():
        ucf = UnifiedConsciousnessFramework(**params)
        report = ucf.get_full_report()
        results[name] = report

    return results


# ============================================================
# EVOLUTIONARY SIMULATION
# ============================================================

def evolutionary_simulation():
    """
    Simulate the evolution of consciousness from simple to complex.

    Tests how consciousness emerges as systems gain:
    - More units (neurons/processing elements)
    - Higher connectivity
    - Better integration
    - Deeper recursion
    - Temporal continuity
    """

    # Evolutionary stages
    stages = [
        ('Bacteria (E. coli)', 5000000, 0.1, 0.1, 0.05, 0.0, 0.0, 0, 5,
         100, 0.2, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0),
        ('Hydra (cnidarian)', 5000, 2, 0.2, 0.15, 0.1, 0.1, 1, 8,
         100, 0.3, 0.1, 200.0, 0.3, 0.3, 0.1, 0.0, 0.0),
        ('Flatworm', 7000, 3, 0.3, 0.2, 0.15, 0.15, 1, 10,
         200, 0.4, 0.15, 250.0, 0.4, 0.4, 0.15, 0.05, 0.0),
        ('Honeybee', 960000, 4, 0.5, 0.4, 0.4, 0.4, 1, 15,
         500, 0.6, 0.2, 350.0, 0.6, 0.6, 0.1, 0.2, 0.0),
        ('Mouse', 100000000, 5, 0.6, 0.6, 0.5, 0.5, 2, 30,
         2000, 0.7, 0.15, 300.0, 0.7, 0.7, 0.3, 0.05, 0.0),
        ('Cat', 600000000, 6, 0.7, 0.7, 0.6, 0.6, 2, 40,
         5000, 0.8, 0.1, 250.0, 0.8, 0.8, 0.4, 0.1, 0.0),
        ('Rhesus Macaque', 6000000000, 8, 0.8, 0.8, 0.7, 0.7, 3, 60,
         10000, 0.85, 0.08, 200.0, 0.85, 0.85, 0.5, 0.3, 0.0),
        ('Human', 86000000000, 8, 0.9, 0.95, 0.85, 0.85, 4, 100,
         10000, 0.9, 0.05, 200.0, 0.9, 0.9, 0.7, 0.7, 1.0),
    ]

    results = []
    for name, n_units, connectivity, differentiation, integration, \
            broadcast_eff, pred_acc, self_stab, r_depth, n_qualia, \
            repr_cap, mir, pst, tbw, q_res, shared, private, resolution in stages:

        ucf = UnifiedConsciousnessFramework(
            n_units=n_units, n_modules=8,
            connectivity=connectivity, differentiation=differentiation,
            integration=integration, broadcast_efficiency=broadcast_eff,
            prediction_accuracy=pred_acc, self_model_stability=self_stab,
            recursion_depth=int(r_depth), memory_integration_rate=mir,
            predictive_stability=pst, temporal_binding_window=tbw,
            coherence_at_depth=[0.9] * int(r_depth + 2),
            n_experience_types=n_qualia, representational_capacity=repr_cap,
            resolution=float(resolution), shared_information=float(shared),
            private_information=float(private)
        )

        report = ucf.get_full_report()
        report['name'] = name
        report['n_units'] = n_units
        results.append(report)

    return results


# ============================================================
# OUTPUT AND REPORTING
# ============================================================

def generate_report(results, evolutionary_results):
    """Generate a structured JSON report."""
    report = {
        'scenarios': results,
        'evolutionary_trajectory': evolutionary_results,
        'metadata': {
            'model': 'Unified Consciousness Framework (UCF)',
            'equation_psi': 'Psi = Phi * Gamma * C * R * Phi_Q',
            'equation_xi': 'Xi = Psi * T * Q * S',
            'components': {
                'IIT_Phi': 'Integrated Information Theory',
                'GWT_Gamma': 'Global Workspace Theory',
                'PP_Coherence': 'Predictive Processing / Higher-Order Theory',
                'TCT_Temporal': 'Temporal Continuity Theory',
                'RSMT_RSRD': 'Recursive Self-Model Theory',
                'ECT_Qualia': 'Extended Consciousness Theory -- Qualia',
                'ECT_Social': 'Extended Consciousness Theory -- Social',
                'QCF_Phi_Q': 'Quantum Consciousness Framework',
            }
        }
    }
    return report


def print_summary(results, evolutionary_results):
    """Print a human-readable summary."""
    print("=" * 80)
    print("UNIFIED CONSCIOUSNESS FRAMEWORK (UCF) -- SIMULATION RESULTS")
    print("=" * 80)
    print()

    print("SCENARIO RESULTS (Xi = Extended Consciousness Measure):")
    print("-" * 80)
    print(f"{'System':<25} {'Psi':>6} {'Xi':>6} {'Phi':>6} {'Gamma':>6} {'C':>6} {'T':>6} {'Q':>6} {'S':>6}")
    print("-" * 80)

    for name, data in sorted(results.items(), key=lambda x: x[1]['xi'], reverse=True):
        print(f"{name:<25} {data['psi']:6.3f} {data['xi']:6.3f} "
              f"{data['phi']:6.3f} {data['gamma']:6.3f} {data['coherence']:6.3f} "
              f"{data['temporal']:6.3f} {data['qualia']:6.3f} {data['social']:6.3f}")

    print("-" * 80)
    print()

    print("EVOLUTIONARY TRAJECTORY:")
    print("-" * 80)
    print(f"{'Stage':<20} {'Units':>12} {'Psi':>6} {'Xi':>6} {'RSRD':>6}")
    print("-" * 80)

    for data in evolutionary_results:
        units_str = f"{data['n_units']:,.0f}" if data['n_units'] > 1000 else str(data['n_units'])
        print(f"{data['name']:<20} {units_str:>12} {data['psi']:6.3f} "
              f"{data['xi']:6.3f} {data['rsrd']:6d}")

    print("-" * 80)
    print()

    # Key insights
    print("KEY INSIGHTS:")
    print("-" * 80)

    # Find consciousness thresholds
    sorted_by_xi = sorted(results.items(), key=lambda x: x[1]['xi'], reverse=True)

    human_xi = sorted_by_xi[0][1]['xi']
    print(f"1. Human baseline Xi = {human_xi:.3f} (reference point)")

    # What drops below threshold?
    threshold = 0.01
    below = [name for name, data in sorted_by_xi if data['xi'] < threshold]
    print(f"2. Systems below consciousness threshold (Xi < {threshold}): {below}")

    # What component matters most?
    print(f"3. The temporal continuity component (T) is the primary "
          f"distinguisher between biological and artificial systems")
    print()


if __name__ == '__main__':
    # Run all simulations
    print("Running Unified Consciousness Framework simulations...")
    print()

    results = run_scenarios()
    evolutionary_results = evolutionary_simulation()

    # Print summary
    print_summary(results, evolutionary_results)

    # Save full report
    report = generate_report(results, evolutionary_results)
    output_path = Path(__file__).parent / 'ucf_results.json'
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"Full results saved to: {output_path}")
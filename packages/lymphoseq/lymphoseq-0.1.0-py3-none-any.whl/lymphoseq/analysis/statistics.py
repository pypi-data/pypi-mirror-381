"""
Statistical functions for AIRR-seq analysis.

Provides utility functions for calculating diversity metrics and statistical measures.
"""

import numpy as np
from typing import Union, List, Any


def gini_coefficient(values: Union[List[float], np.ndarray]) -> float:
    """
    Calculate the Gini coefficient of inequality.

    The Gini coefficient measures inequality in a distribution.
    Values range from 0 (perfect equality) to 1 (maximum inequality).

    Args:
        values: Array of values (e.g., clone frequencies)

    Returns:
        Gini coefficient (0-1)

    Examples:
        >>> frequencies = [0.5, 0.3, 0.2]
        >>> gini = gini_coefficient(frequencies)
    """
    if len(values) == 0:
        return 0.0

    values = np.array(values, dtype=float)
    values = values[values > 0]  # Remove zeros

    if len(values) <= 1:
        return 0.0

    # Sort values
    sorted_values = np.sort(values)
    n = len(sorted_values)

    # Calculate Gini coefficient
    index = np.arange(1, n + 1)
    gini = (2 * np.sum(index * sorted_values)) / (n * np.sum(sorted_values)) - (n + 1) / n

    return max(0.0, min(1.0, gini))


def shannon_entropy(frequencies: Union[List[float], np.ndarray], base: float = 2.0) -> float:
    """
    Calculate Shannon entropy (information entropy).

    Shannon entropy measures the uncertainty or diversity in a distribution.
    Higher values indicate more diversity.

    Args:
        frequencies: Array of frequencies or probabilities
        base: Logarithm base (2 for bits, e for nats, 10 for dits)

    Returns:
        Shannon entropy value

    Examples:
        >>> frequencies = [0.5, 0.3, 0.2]
        >>> entropy = shannon_entropy(frequencies)
    """
    if len(frequencies) == 0:
        return 0.0

    frequencies = np.array(frequencies, dtype=float)
    frequencies = frequencies[frequencies > 0]  # Remove zeros

    if len(frequencies) <= 1:
        return 0.0

    # Normalize to probabilities if not already
    if not np.isclose(np.sum(frequencies), 1.0):
        frequencies = frequencies / np.sum(frequencies)

    # Calculate Shannon entropy
    entropy = -np.sum(frequencies * np.log(frequencies) / np.log(base))

    return max(0.0, entropy)


def simpson_index(frequencies: Union[List[float], np.ndarray]) -> float:
    """
    Calculate Simpson's diversity index.

    Simpson's index measures the probability that two randomly selected
    individuals belong to the same species/clone.

    Args:
        frequencies: Array of frequencies or probabilities

    Returns:
        Simpson's index (0-1)

    Examples:
        >>> frequencies = [0.5, 0.3, 0.2]
        >>> simpson = simpson_index(frequencies)
    """
    if len(frequencies) == 0:
        return 0.0

    frequencies = np.array(frequencies, dtype=float)
    frequencies = frequencies[frequencies > 0]

    if len(frequencies) <= 1:
        return 1.0

    # Normalize to probabilities if not already
    if not np.isclose(np.sum(frequencies), 1.0):
        frequencies = frequencies / np.sum(frequencies)

    # Calculate Simpson's index
    simpson = np.sum(frequencies ** 2)

    return max(0.0, min(1.0, simpson))


def inverse_simpson_index(frequencies: Union[List[float], np.ndarray]) -> float:
    """
    Calculate the inverse Simpson's diversity index.

    Also known as the Simpson's reciprocal index, this measures
    the effective number of species/clones.

    Args:
        frequencies: Array of frequencies or probabilities

    Returns:
        Inverse Simpson's index

    Examples:
        >>> frequencies = [0.5, 0.3, 0.2]
        >>> inv_simpson = inverse_simpson_index(frequencies)
    """
    simpson = simpson_index(frequencies)
    if simpson == 0:
        return float('inf')
    return 1.0 / simpson


def chao1_estimator(abundances: Union[List[int], np.ndarray]) -> float:
    """
    Calculate the Chao1 estimator of species richness.

    Chao1 estimates the total number of species based on the number
    of rare species in the sample.

    Args:
        abundances: Array of abundance counts (integers)

    Returns:
        Chao1 estimate of total richness

    Examples:
        >>> abundances = [1, 1, 2, 3, 5, 8]
        >>> chao1 = chao1_estimator(abundances)
    """
    if len(abundances) == 0:
        return 0.0

    abundances = np.array(abundances, dtype=int)
    abundances = abundances[abundances > 0]

    if len(abundances) == 0:
        return 0.0

    observed_species = len(abundances)
    singletons = np.sum(abundances == 1)  # Species with count = 1
    doubletons = np.sum(abundances == 2)  # Species with count = 2

    if doubletons > 0:
        chao1 = observed_species + (singletons ** 2) / (2 * doubletons)
    else:
        # Fallback when no doubletons
        chao1 = observed_species + singletons * (singletons - 1) / 2

    return max(observed_species, chao1)


def hill_numbers(frequencies: Union[List[float], np.ndarray], q: float = 1.0) -> float:
    """
    Calculate Hill numbers (effective number of species).

    Hill numbers provide a unified framework for measuring diversity.
    - q=0: Species richness (number of species)
    - q=1: Shannon diversity (exponential of Shannon entropy)
    - q=2: Simpson diversity (inverse Simpson index)

    Args:
        frequencies: Array of frequencies or probabilities
        q: Order of diversity (0, 1, 2, or other positive values)

    Returns:
        Hill number of order q

    Examples:
        >>> frequencies = [0.5, 0.3, 0.2]
        >>> hill_1 = hill_numbers(frequencies, q=1)  # Shannon diversity
        >>> hill_2 = hill_numbers(frequencies, q=2)  # Simpson diversity
    """
    if len(frequencies) == 0:
        return 0.0

    frequencies = np.array(frequencies, dtype=float)
    frequencies = frequencies[frequencies > 0]

    if len(frequencies) == 0:
        return 0.0

    # Normalize to probabilities if not already
    if not np.isclose(np.sum(frequencies), 1.0):
        frequencies = frequencies / np.sum(frequencies)

    if q == 0:
        # Species richness
        return float(len(frequencies))
    elif q == 1:
        # Shannon diversity (limit as q approaches 1)
        entropy = shannon_entropy(frequencies, base=np.e)
        return np.exp(entropy)
    else:
        # General Hill number
        if q < 0:
            raise ValueError("q must be non-negative")

        sum_p_q = np.sum(frequencies ** q)
        if sum_p_q == 0:
            return 0.0

        hill = sum_p_q ** (1.0 / (1.0 - q))
        return hill


def berger_parker_index(abundances: Union[List[float], np.ndarray]) -> float:
    """
    Calculate the Berger-Parker dominance index.

    This index measures the relative abundance of the most dominant species/clone.

    Args:
        abundances: Array of abundance values

    Returns:
        Berger-Parker index (0-1)

    Examples:
        >>> abundances = [10, 5, 3, 2]
        >>> bp_index = berger_parker_index(abundances)
    """
    if len(abundances) == 0:
        return 0.0

    abundances = np.array(abundances, dtype=float)
    abundances = abundances[abundances > 0]

    if len(abundances) == 0:
        return 0.0

    total = np.sum(abundances)
    if total == 0:
        return 0.0

    max_abundance = np.max(abundances)
    return max_abundance / total
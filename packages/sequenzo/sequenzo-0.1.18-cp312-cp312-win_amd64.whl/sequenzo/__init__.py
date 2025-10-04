"""
@Author  : Yuqi Liang 梁彧祺
@File    : __init__.py
@Time    : 11/02/2025 16:41
@Desc    : 
"""
# sequenzo/sequenzo/__init__.py (Inside the inner sequenzo package)
# This file is now needed for making the submodules accessible.

# You *don't* need to handle the Rust extension here.
# You can have package level docstring here.
# No need for __all__ here, use relative import in the top-level __init__.py

from .datasets import load_dataset, list_datasets

# Import the core functions that should be directly available from the sequenzo package

from .data_preprocessing import helpers
from .data_preprocessing.helpers import (assign_unique_ids,
                                         wide_to_long_format_data,
                                         long_to_wide_format_data,
                                         summarize_missing_values,
                                         replace_cluster_id_by_labels)

from sequenzo.define_sequence_data import *

from .visualization import (plot_sequence_index,
                            plot_most_frequent_sequences,
                            plot_single_medoid,
                            plot_state_distribution,
                            plot_modal_state,
                            plot_relative_frequency,
                            plot_mean_time,
                            plot_transition_matrix,
                            )

from .dissimilarity_measures.get_distance_matrix import get_distance_matrix
from .dissimilarity_measures.get_substitution_cost_matrix import get_substitution_cost_matrix
from .dissimilarity_measures.utils.get_LCP_length_for_2_seq import get_LCP_length_for_2_seq

from .clustering import Cluster, ClusterResults, ClusterQuality
from .clustering.KMedoids import KMedoids
from .big_data.clara.clara import clara
from .big_data.clara.visualization import plot_scores_from_dataframe

from .multidomain import (create_idcd_sequence_from_csvs,
                          compute_cat_distance_matrix,
                          compute_dat_distance_matrix,
                          get_interactive_combined_typology,
                          merge_sparse_combt_types,
                          get_association_between_domains,
                          linked_polyadic_sequence_analysis
                          )

from .prefix_tree import (
    build_prefix_tree,
    compute_prefix_count,
    IndividualDivergence,
    extract_sequences,
    get_state_space,
    compute_branching_factor,
    compute_js_divergence,
    convert_to_prefix_tree_data,
    plot_system_indicators,
    plot_system_indicators_multiple_comparison,
    plot_prefix_rarity_distribution,
    plot_individual_indicators_correlation
)

from .suffix_tree import (
    build_suffix_tree,
    compute_suffix_count,
    compute_merging_factor,
    compute_js_convergence,
    IndividualConvergence,
    convert_to_suffix_tree_data,
    plot_system_indicators,
    plot_system_indicators_multiple_comparison,
    plot_suffix_rarity_distribution,
)

from .sequence_characteristics import (
    get_subsequences_in_single_sequence,
    get_subsequences_all_sequences,
    get_number_of_transitions,

    get_turbulence,
    get_complexity_index,
    get_within_sequence_entropy,
    get_spell_duration_variance,
    get_state_freq_and_entropy_per_seq,

    get_cross_sectional_entropy,
    plot_cross_sectional_characteristics,
    plot_longitudinal_characteristics

)

# Event History Analysis (SAMM)
from .with_event_history_analysis import (
    SAMM,
    sequence_analysis_multi_state_model,
    plot_samm,
    seqsammseq,
    set_typology,
    seqsammeha,
    # Keep old names for backward compatibility
    seqsamm
)

# Define `__all__` to specify the public API when using `from sequenzo import *`
__all__ = [
    # Datasets
    "load_dataset",
    "list_datasets",

    # Data preprocessing
    "helpers",
    "assign_unique_ids",
    "wide_to_long_format_data",
    "long_to_wide_format_data",
    "summarize_missing_values",
    "replace_cluster_id_by_labels",

    "SequenceData",

    # Visualization
    "plot_sequence_index",
    "plot_most_frequent_sequences",
    "plot_single_medoid",
    "plot_state_distribution",
    "plot_modal_state",
    "plot_relative_frequency",
    "plot_mean_time",
    "plot_transition_matrix",

    # Dissimilarity measures
    "get_distance_matrix",
    "get_substitution_cost_matrix",
    "get_LCP_length_for_2_seq",

    # Hierarchical clustering
    "Cluster",
    "ClusterResults",
    "ClusterQuality",
    "KMedoids",

    # Big data
    "clara",
    "plot_scores_from_dataframe",

    # Multi-domain sequence analysis
    "create_idcd_sequence_from_csvs",
    "compute_cat_distance_matrix",
    "compute_dat_distance_matrix",
    "get_interactive_combined_typology",
    "merge_sparse_combt_types",
    "get_association_between_domains",
    "linked_polyadic_sequence_analysis",

    # Prefix Tree
    "build_prefix_tree",
    "compute_prefix_count",
    "IndividualDivergence",
    "extract_sequences",
    "get_state_space",
    "compute_branching_factor",
    "compute_js_divergence",
    "convert_to_prefix_tree_data",
    "plot_system_indicators",
    "plot_system_indicators_multiple_comparison",
    "plot_prefix_rarity_distribution",
    "plot_individual_indicators_correlation",

    # Suffix Tree
    "build_suffix_tree",
    "compute_suffix_count",
    "compute_merging_factor",
    "compute_js_convergence",
    "IndividualConvergence",
    "convert_to_suffix_tree_data",
    "plot_system_indicators",
    "plot_system_indicators_multiple_comparison",
    "plot_suffix_rarity_distribution",

    # Sequence characteristics
    "get_subsequences_in_single_sequence",
    "get_subsequences_all_sequences",
    "get_number_of_transitions",
    "get_turbulence",
    "get_complexity_index",
    "get_within_sequence_entropy",
    "get_spell_duration_variance",
    "get_state_freq_and_entropy_per_seq",
    "get_cross_sectional_entropy",
    "plot_longitudinal_characteristics",
    "plot_cross_sectional_characteristics",

    # Event History Analysis (SAMM)
    "SAMM",
    "sequence_analysis_multi_state_model",
    "plot_samm",
    "seqsammseq",
    "set_typology",
    "seqsammeha",
    # Keep old names for backward compatibility
    "seqsamm"
]

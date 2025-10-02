#!/usr/bin/env python3
"""
AutoClustal - Comprehensive Bioinformatics Pipeline
===================================================

A comprehensive bioinformatics pipeline for sequence analysis, including:
- Multiple sequence alignment (MUSCLE, ClustalW, MAFFT)
- Phylogenetic tree construction (Neighbor-Joining, UPGMA, Maximum Likelihood)
- Sequence clustering (hierarchical, k-means, DBSCAN)
- BLAST/BLAT database searches with batch processing
- PCA analysis and comprehensive visualizations
- Organism classification and annotation

Author: Stella Hartono
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Stella Hartono"
__email__ = "srhartono@users.noreply.github.com"

# Import main classes for easy access
try:
    from .modules.sequence_handler import SequenceHandler
    from .modules.alignment import AlignmentProcessor
    from .modules.phylogeny import PhylogenyBuilder
    from .modules.clustering import ClusteringProcessor
    from .modules.blast_search import BlastSearcher
    from .modules.analysis import AnalysisEngine
    from .modules.simple_analysis import SimpleAnalysisEngine
except ImportError:
    # Handle case where dependencies might not be installed yet
    pass

__all__ = [
    "SequenceHandler",
    "AlignmentProcessor", 
    "PhylogenyBuilder",
    "ClusteringProcessor",
    "BlastSearcher",
    "AnalysisEngine",
    "SimpleAnalysisEngine"
]
from .evaluation_strategies import (
    AbstractEvaluationStrategy,
    DistributedEvaluation,
    ParallelEvaluation,
    SequentialEvaluation,
)
from .factory import GeneticAlgorithmFactory
from .genetic_algorithm import GeneticAlgorithm, GeneticAlgorithmParameters

# Optional imports for distributed computing
try:
    from .distribution_manager import DistributionManager
    _HAS_DASK_SUPPORT = True
except ImportError:
    DistributionManager = None
    _HAS_DASK_SUPPORT = False

# Import protocols for type checking and runtime validation
from seapopym_optimization.algorithm.protocol import (
    OptimizationAlgorithmProtocol,
    OptimizationParametersProtocol,
)

__all__ = [
    # Core classes
    "GeneticAlgorithm",
    "GeneticAlgorithmParameters",
    "GeneticAlgorithmFactory",

    # Evaluation strategies
    "AbstractEvaluationStrategy",
    "SequentialEvaluation",
    "DistributedEvaluation",
    "ParallelEvaluation",

    # Distribution management (optional)
    "DistributionManager",

    # Protocols
    "OptimizationAlgorithmProtocol",
    "OptimizationParametersProtocol",
]

# Remove None values from __all__ if Dask is not available
if not _HAS_DASK_SUPPORT:
    __all__ = [item for item in __all__ if item != "DistributionManager"]

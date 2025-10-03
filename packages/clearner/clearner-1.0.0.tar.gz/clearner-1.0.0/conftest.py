"""
Pytest configuration and Python 3.12 compatibility patch
"""
# Apply Python 3.12 compatibility patch before any imports
import sys
import os

# Add the project root to the path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Apply the collections patch immediately
from learner.utilities import collections_patch

# Import LightGBM early to prevent segmentation faults on macOS
# Based on: https://github.com/shap/shap/issues/3092
try:
    import lightgbm
except ImportError:
    pass  # LightGBM not available, continue without it

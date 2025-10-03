#! /usr/bin/env python

# Copyright (C) Prizmi, LLC - All Rights Reserved
# Unauthorized copying or use of this file is strictly prohibited and subject to prosecution under applicable laws
# Proprietary and confidential

# Apply Python 3.12 compatibility patch
from learner.utilities import collections_patch

# Import LightGBM early to prevent segmentation faults on macOS
# Based on: https://github.com/shap/shap/issues/3092
try:
    import lightgbm
except ImportError:
    pass  # LightGBM not available, continue without it

from learner.setup.main import main

if __name__ == '__main__':
    main()

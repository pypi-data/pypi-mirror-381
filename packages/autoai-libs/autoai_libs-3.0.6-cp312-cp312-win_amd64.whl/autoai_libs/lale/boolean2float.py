################################################################################
# IBM Confidential
# OCO Source Materials
# 5737-H76, 5725-W78, 5900-A1R, 5737-L65
# (c) Copyright IBM Corp. 2024-2025. All Rights Reserved.
# The source code for this program is not published or otherwise divested of its trade secrets,
# irrespective of what has been deposited with the U.S. Copyright Office.
################################################################################

import autoai_libs.transformers.exportable
import numpy as np
import pandas as pd

import lale.datasets.data_schemas
import lale.docstrings
import lale.operators

from ._common_schemas import _hparam_activate_flag_unmodified


class _boolean2floatImpl:
    def __init__(self, **hyperparams):
        self._hyperparams = hyperparams

        self._wrapped_model = autoai_libs.transformers.exportable.boolean2float(**hyperparams)

    def fit(self, X, y=None):
        self._wrapped_model.fit(X, y)
        return self

    def transform(self, X):
        raw = self._wrapped_model.transform(X)
        if isinstance(raw, (np.ndarray, pd.DataFrame)):
            s_X = lale.datasets.data_schemas.to_schema(X)
            s_result = self.transform_schema(s_X)
            result = lale.datasets.data_schemas.add_schema(raw, s_result, recalc=True)
        else:
            result = raw
        return result

    def transform_schema(self, s_X):
        """Used internally by Lale for type-checking downstream operators."""
        if self._hyperparams["activate_flag"]:
            result = {
                "type": "array",
                "items": {"type": "array", "items": {"type": "number"}},
            }
        else:
            result = s_X
        return result


_hyperparams_schema = {
    "allOf": [
        {
            "description": "This first object lists all constructor arguments with their types, but omits constraints for conditional hyperparameters.",
            "type": "object",
            "additionalProperties": False,
            "required": ["activate_flag"],
            "relevantToOptimizer": [],
            "properties": {"activate_flag": _hparam_activate_flag_unmodified},
        }
    ]
}

_input_fit_schema = {
    "type": "object",
    "required": ["X"],
    "additionalProperties": False,
    "properties": {
        "X": {  # Handles 1-D arrays as well
            "anyOf": [
                {"type": "array", "items": {"laleType": "Any"}},
                {
                    "type": "array",
                    "items": {"type": "array", "items": {"laleType": "Any"}},
                },
            ]
        },
        "y": {"laleType": "Any"},
    },
}

_input_transform_schema = {
    "type": "object",
    "required": ["X"],
    "additionalProperties": False,
    "properties": {
        "X": {  # Handles 1-D arrays as well
            "anyOf": [
                {"type": "array", "items": {"laleType": "Any"}},
                {
                    "type": "array",
                    "items": {"type": "array", "items": {"laleType": "Any"}},
                },
            ]
        }
    },
}

_output_transform_schema = {
    "description": "Features; the outer array is over samples.",
    "type": "array",
    "items": {"type": "array", "items": {"laleType": "Any"}},
}

_combined_schemas = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": """Operator from `autoai_libs`_. Converts strings that represent booleans to floats and replaces missing values with np.nan.

.. _`autoai_libs`: https://pypi.org/project/autoai-libs""",
    "documentation_url": "https://lale.readthedocs.io/en/latest/modules/lale.lib.autoai_libs.boolean2float.html",
    "import_from": "autoai_libs.transformers.exportable",
    "type": "object",
    "tags": {"pre": [], "op": ["transformer"], "post": []},
    "properties": {
        "hyperparams": _hyperparams_schema,
        "input_fit": _input_fit_schema,
        "input_transform": _input_transform_schema,
        "output_transform": _output_transform_schema,
    },
}


boolean2float = lale.operators.make_operator(_boolean2floatImpl, _combined_schemas)

lale.docstrings.set_docstrings(boolean2float)

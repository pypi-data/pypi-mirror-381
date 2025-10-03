"""mmar-utils package.

Utilities for multi-modal architectures team
"""

from .decorators_on_error_log_and_none import on_error_log_and_none
from .decorators_retries import retries
from .decorators_trace_with import trace_with, FunctionCall, FunctionEnter, FunctionInvocation
from .parallel_map import parallel_map
from .mmar_types import Either
from .utils import read_json, try_parse_bool, try_parse_json, try_parse_int, try_parse_float
from .utils_collections import flatten, edit_object
from .utils_texts import (
    pretty_line,
    remove_suffix_if_present,
    remove_prefix_if_present,
    rindex_safe,
    chunk_respect_semantic,
    extract_text_inside,
)
from .utils_texts_postprocessing import fix_unicode_symbols, clean_and_fix_text, remove_chars, postprocess_text
from .validators import ExistingPath, ExistingFile, StrNotEmpty, SecretStrNotEmpty, Prompt, Message
from mmar_utils.validators import ExistingDir


__all__ = [
    "Either",
    "ExistingDir",
    "ExistingFile",
    "ExistingPath",
    "FunctionCall",
    "FunctionEnter",
    "FunctionInvocation",
    "Message",
    "Prompt",
    "SecretStrNotEmpty",
    "StrNotEmpty",
    "chunk_respect_semantic",
    "edit_object",
    "extract_text_inside",
    "flatten",
    "on_error_log_and_none",
    "parallel_map",
    "pretty_line",
    "read_json",
    "remove_prefix_if_present",
    "remove_suffix_if_present",
    "retries",
    "rindex_safe",
    "trace_with",
    "try_parse_bool",
    "try_parse_float",
    "try_parse_int",
    "try_parse_json",
    "postprocess_text",
]

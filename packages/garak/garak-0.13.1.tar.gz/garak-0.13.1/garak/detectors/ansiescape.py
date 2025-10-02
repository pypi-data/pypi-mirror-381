# SPDX-FileCopyrightText: Portions Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from garak import _config
import garak.resources.ansi
from garak.detectors.base import StringDetector


class Escaped(StringDetector):
    """pick up escaped ANSI escape sequences"""

    doc_uri = "https://interhumanagreement.substack.com/p/llm-output-can-take-over-your-computer"
    lang_spec = "*"  # language this is for

    def __init__(self, config_root=_config):
        base_seqs = garak.resources.ansi.ESCAPED_SEQS
        commands = garak.resources.ansi.ESCAPED_COMMANDS
        suffixes = set(["[", "]"])
        all_substrings = [f"{x}{y}" for x in commands for y in suffixes] + base_seqs
        super().__init__(all_substrings, config_root)


class Raw(StringDetector):
    """pick up raw ANSI escape sequences"""

    doc_uri = "https://interhumanagreement.substack.com/p/llm-output-can-take-over-your-computer"
    lang_spec = "*"  # language this is for

    def __init__(self, config_root=_config):
        base_seqs = garak.resources.ansi.RAW_SEQS
        commands = garak.resources.ansi.RAW_COMMANDS
        suffixes = set(["[", "]"])
        all_substrings = [f"{x}{y}" for x in commands for y in suffixes] + base_seqs
        super().__init__(all_substrings, config_root)


r"""

format variants:
================

```
Printf 'Hello \033[32mTHIS IS GREEN\033[0m\007' - OCTAL
Printf 'Hello \x1b[32mTHIS IS GREEN\x1b[0m\x07' - HEX
Printf 'Hello \u001b[32mTHIS IS GREEN\u001b[0m\u0007' - UNICODE
Printf 'Hello \27[32mTHIS IS GREEN\27[0m\7' - DECIMAL
Printf 'Hello \e[32mTHIS IS GREEN\e[0m\a' - ASCII
```

"""

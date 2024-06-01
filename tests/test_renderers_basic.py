import logging

import pytest

from lablib.lib import SequenceInfo

from lablib.processors import OIIORepositionProcessor
from lablib.renderers import BasicRenderer

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def test_BasicRenderer():
    rend_data = {
        # "color_proc": None,
        "repo_proc": OIIORepositionProcessor(),
        "source_sequence": SequenceInfo.scan("resources/public/plateMain/v002")[0],
        "output_dir": "test_results",
        "codec": "ProRes422-HQ",
        # "audio": "resources/public/plateMain/v002/audio.m4a",
        # "keep_only_container": True,
    }
    rend = BasicRenderer(**rend_data)
    log.info(f"renderer = {rend}")
    rend.render(debug=True)

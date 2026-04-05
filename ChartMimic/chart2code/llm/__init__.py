from .openai import OPENAI_GPT
import os
if "3e12762e" in os.getcwd():
    # from .gemini import GEMINI
    # from .deepseekvl import DeepSeekVL
    # from .qwenvl import QwenVL
    # from .qwenvl2 import QwenVL2
    # from .internvl import InternVL
    from .internvl2 import InternVL2
    # from .idefics2 import Idefics2
    # from .llava import Llava
    # from .cogvlm2 import Cogvlm2
    from .phi3 import Phi3
    # from .minicpm import Minicpm
    # from .claude import Claude
from common.registry import registry

__all__ = [
    "OPENAI_GPT",
    "QwenVL2",
    "GEMINI",
    "DeepSeekVL",
    "QwenVL",
    "InternVL",
    "InternVL2",
    "Idefics2",
    "Llava",
    "Cogvlm2",
    "Phi3",
    "Minicpm",
    "Claude",
]


def load_llm(name, config):
    llm = registry.get_llm_class(name).from_config(config)
    return llm

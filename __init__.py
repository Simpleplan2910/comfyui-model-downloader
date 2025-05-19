from .nodes.hf.hf_download import HFDownloader
from .nodes.auto.downloader import AutoModelDownloader
from .nodes.cai.cai_download import CivitAIDownloader
import os

class GetImageSize:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "execute"
    CATEGORY = "essentials"

    def execute(self, image):
        return (image.shape[2], image.shape[1],)

# Node mappings
NODE_CLASS_MAPPINGS = { 
    "HF Downloader": HFDownloader,
    "Auto Model Downloader": AutoModelDownloader,
    "CivitAI Downloader": CivitAIDownloader,
    "GetImageSize+": GetImageSize,
}

# Display names
NODE_DISPLAY_NAME_MAPPINGS = { 
    "HF Downloader": "HF Download",
    "Auto Model Downloader": "Auto Model Finder (Experimental)",
    "CivitAI Downloader": "CivitAI Download",
    "GetImageSize+": "Get Image Size",
}

# Web directory for JavaScript files
WEB_DIRECTORY = "./js"

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY"
]
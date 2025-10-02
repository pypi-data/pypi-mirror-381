import torch
import torch.nn as nn
import monai
from fmcib.preprocessing import SeedBasedPatchCropd

from .utils import get_transforms
from .base import BaseModel

from huggingface_hub import hf_hub_download
from loguru import logger

class CTFMExtractor(BaseModel):
    def __init__(self):
        super().__init__()
        self.model = monai.networks.nets.segresnet_ds.SegResEncoder(
            blocks_down=(1, 2, 2, 4, 4),
            head_module=lambda x: torch.nn.functional.adaptive_avg_pool3d(
                x[-1], 1
            ).flatten(
                start_dim=1
            ),  # Get only the last feature across block levels and average pool it.
        )
        self.transforms = get_transforms(
            orient="SPL",
            scale_range=(-1024, 2048),
            spatial_size=(48, 48, 48),
            spacing=(1, 1, 1),
        )

    def load(self, weights_path: str = None):
        # Download weights from huggingface if path not provided
        if weights_path is None:
            weights_path = hf_hub_download(
                repo_id="surajpaib/CT-FM-SegResNet",
                filename="pretrained_segresnet.torch",
            )

        weights = torch.load(weights_path)
        weights = {
            k.replace("encoder.", ""): v for k, v in weights.items()
        }
        msg = self.model.load_state_dict(
            weights, strict=False
        )  # Set strict to False as we load only the encoder
        logger.info(msg)
        self.model.eval()

    def preprocess(self, x):
        return self.transforms(x)

    def forward(self, x):
        with torch.no_grad():
            return self.model(x)

import os
import torch
import monai.transforms
import base64
import io
from PIL import Image
import numpy as np
from fmcib.preprocessing import SeedBasedPatchCropd
from .medimageinsightmodel import MedImageInsight

from .utils import get_transforms
from .base import BaseModel

class MedImageInsightExtractor(BaseModel):
    """MedImageInsight model for extracting image embeddings"""

    def __init__(self):
        super().__init__()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.transforms = get_transforms(
            orient="LPS",
            scale_range=(-1000, 1000),
            spatial_size=(48, 48, 48),
            spacing=(1, 1, 1),
        )

    def load(self, weights_path: str = None):
        """Load pretrained model"""
        model_dir = (
            os.path.dirname(weights_path)
            if weights_path
            else "/home/suraj/Repositories/MedImageInsights/2024.09.27"
        )
        vision_model = (
            os.path.basename(weights_path)
            if weights_path
            else "medimageinsigt-v1.0.0.pt"
        )

        self.model = MedImageInsight(
            model_dir=model_dir,
            vision_model_name=vision_model,
            language_model_name="language_model.pth",
        )
        self.model.load_model()

    def preprocess(self, x):
        """Apply transforms to input data"""
        return self.transforms(x)

    def _convert_to_base64(self, image):
        """Convert 3D tensor to list of base64 strings"""
        base64_images = []
        for slice_idx in range(image.shape[-1]):
            curr_slice = image[0, :, :, slice_idx].cpu().numpy()
            curr_slice = (curr_slice * 255).astype(np.uint8)
            curr_slice = np.squeeze(curr_slice)  # Remove singleton dimensions
            pil_image = Image.fromarray(curr_slice, mode="L")  # Specify grayscale mode

            buffer = io.BytesIO()
            pil_image.save(buffer, format="PNG")
            base64_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
            base64_images.append(base64_image)
        return base64_images

    def forward(self, image):
        """
        Forward pass to extract embeddings
        Args:
            image: Input image tensor
        Returns:
            Image embeddings
        """
        base64_images = self._convert_to_base64(image)
        results = self.model.encode(images=base64_images)
        return torch.tensor(results["image_embeddings"]).to("cuda:0")

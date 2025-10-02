import monai
import matplotlib.pyplot as plt
from fmcib.preprocessing import SeedBasedPatchCropd


def get_transforms(
    orient="RAS",
    scale_range=(-1024, 2048),
    spatial_size=(48, 48, 48),
    spacing=(1, 1, 1),
    clamp=(0, 1)
):
    T = monai.transforms.Compose(
        [
            monai.transforms.CopyItemsd(keys=["image_path"], names=["image"]),
            monai.transforms.LoadImaged(
                keys=["image"], ensure_channel_first=True, reader="ITKReader"
            ),
            monai.transforms.EnsureTyped(keys=["image"]),
            monai.transforms.Orientationd(keys=["image"], axcodes="LPS"),
            monai.transforms.Spacingd(
                keys=["image"],
                pixdim=spacing,
                padding_mode="zeros",
                mode="linear",
                align_corners=True,
                diagonal=True,
            ),
            SeedBasedPatchCropd(
                keys=["image"],
                roi_size=spatial_size,
                coord_orientation="LPS",
                global_coordinates=True,
            ),
            monai.transforms.Orientationd(keys=["image"], axcodes=orient),
            monai.transforms.ScaleIntensityRanged(
                keys="image",
                a_min=scale_range[0],
                a_max=scale_range[1],
                b_min=clamp[0],
                b_max=clamp[1],
                clip=True,
            ),
            monai.transforms.SpatialPadd(keys=["image"], spatial_size=spatial_size),
            monai.transforms.Lambda(func=lambda x: x["image"].as_tensor()),
        ]
    )
    return T


def plot_3d_image(ret):
    # Plot axial slice
    plt.figure(figsize=(10, 10))
    plt.subplot(3, 1, 1)
    plt.imshow(ret[:, ret.shape[1] // 2, :, :].permute(1, 2, 0), cmap="gray")
    plt.title("Axial")
    plt.axis("off")

    # Plot sagittal slice
    plt.subplot(3, 1, 2)
    plt.imshow(ret[:, :, ret.shape[2] // 2, :].permute(1, 2, 0), cmap="gray")
    plt.title("Coronal")
    plt.axis("off")

    # Plot coronal slice
    plt.subplot(3, 1, 3)
    plt.imshow(ret[:, :, :, ret.shape[3] // 2].permute(1, 2, 0), cmap="gray")
    plt.title("Sagittal")

    plt.axis("off")
    plt.show()
from io import BytesIO

import torch
import torch.nn.functional as F
from PIL import Image
from torchvision.models.resnet import resnet50, ResNet50_Weights
from torchvision.transforms import transforms

model = resnet50(weights=ResNet50_Weights.DEFAULT)

model.eval()

# Define the image transformations
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def is_cat(image):
    try:
        img = Image.open(BytesIO(image.read()))

        # Preprocess the image
        img_t = preprocess(img)
        batch_t = torch.unsqueeze(img_t, 0)

        # Make the prediction
        out = model(batch_t)

        # Apply softmax to get probabilities
        probabilities = F.softmax(out, dim=1)

        # Get the maximum predicted class and its probability
        max_prob, max_class = torch.max(probabilities, dim=1)
        max_prob = max_prob.item()
        max_class = max_class.item()

        # Check if the maximum predicted class is within the range 281-285
        if 281 <= max_class <= 285:
            return max_class, max_prob
        else:
            return max_class, None
    except Exception as e:
        print("Error while processing the image:", e)
        return None

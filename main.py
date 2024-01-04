from PIL import Image
import torch
import torch.nn.functional as F
from torchvision.models.resnet import resnet50, ResNet50_Weights
from torchvision.transforms import transforms

# Load the pre-trained model
model = resnet50(weights=ResNet50_Weights.DEFAULT)

model.eval()

# Define the image transformations
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def is_cat(image_path):
    # Open the image
    img = Image.open(image_path)

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


image_path = 'wolf.jpg'
max_class, max_prob = is_cat(image_path)
translator = {
    281: "tabby cat",
    282: "tiger cat",
    283: "persian cat",
    284: "siamese cat",
    285: "egyptian cat"
}
if max_prob is not None:
    print(f"The image is recognized as '{translator[max_class]}' with a probability of {round(max_prob * 100, 2)}%")
else:
    print(f"The image is not recognized as a class within the range 281-285 ({max_class})")

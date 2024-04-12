import cv2
import torch
import numpy as np
import matplotlib.pyplot as plt
import time

cam = cv2.VideoCapture(0)

fig = plt.figure()
#model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
#model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)

# midas = torch.hub.load("midas_v21_small_256.pt",)
midas = torch.hub.load("intel-isl/MiDaS",model_type)


device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
# device = torch.device("cpu")
midas.to(device)
midas.eval()

# midas_transforms = torch.hub.load("midas_v21_small_256.pt", "transforms", map_location=torch.device("cpu"))
midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")


if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    transform = midas_transforms.dpt_transform
else:
    transform = midas_transforms.small_transform

while True:
    ret, frame = cam.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    start = time.time()

    input_batch = transform(img).to(device)

    with torch.no_grad():
        prediction = midas(input_batch)

        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=img.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()

    output = prediction.cpu().numpy()
    depth = np.uint8(255*(output-output.min())/(output.max()-output.min()))

    end = time.time()

    cv2.imshow('Inference',depth)
    print(1/(end-start))

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

# Release resources
cam.release()
# cv2.destroyAllWindows()

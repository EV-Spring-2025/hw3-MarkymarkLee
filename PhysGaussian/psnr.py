import sys
import torch
import cv2
import os


def read_video_frames(path):
    cap = cv2.VideoCapture(path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = torch.from_numpy(frame).float() / 255.0  # Normalize to [0,1]
        frame = frame.permute(2, 0, 1).unsqueeze(0)  # Shape: (1,3,H,W)
        frames.append(frame)
    cap.release()
    return frames


def calculate_psnr(img1, img2):
    mse = torch.mean((img1 - img2) ** 2)
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 1.0
    return 20 * torch.log10(torch.tensor(PIXEL_MAX) / torch.sqrt(mse))


def main():
    if len(sys.argv) != 3:
        print('Usage: python psnr.py video1.mp4 video2.mp4')
        sys.exit(1)
    video1, video2 = sys.argv[1], sys.argv[2]
    video1 = f"output/{video1}/output.mp4"
    video2 = f"output/{video2}/output.mp4"

    frames1 = read_video_frames(video1)
    frames2 = read_video_frames(video2)

    if len(frames1) != len(frames2):
        print('Videos have different number of frames!')
        sys.exit(1)
    psnr_vals = []
    for f1, f2 in zip(frames1, frames2):
        psnr_val = calculate_psnr(f1.cuda(), f2.cuda()).item()
        psnr_vals.append(psnr_val)
    print(f'Average PSNR: {sum(psnr_vals)/len(psnr_vals):.4f} dB')


if __name__ == '__main__':
    main()

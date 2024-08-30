import torch

def check_cuda():
    print(f"PyTorch Version: {torch.__version__}")
    print(f"CUDA Version: {torch.version.cuda}")
    print(f"CUDA Available: {torch.cuda.is_available()}")

if __name__ == "__main__":
    check_cuda()

# youtube_transcription
Transcripts a youtube video

## Installation
```
pip install -r requirements.txt
```

### Other Requirements

ffmpeg

### Optional

CUDA (12.1 Tested and Verified as Functional) -> [Link](https://developer.nvidia.com/cuda-12-1-0-download-archive)

To get GPU support run the following series of commands after installing requirements

```bash
pip uninstall torch
pip cache purge
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
python -c "import torch; print(\"CUDA enabled:\", torch.cuda.is_available());"
```



sudo docker run -it --gpus=all \
 -v $(pwd):/app \
 dream:v0 \
 python download_weights.py
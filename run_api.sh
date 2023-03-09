sudo docker run -d --gpus=all --ipc=host \
 -v $(pwd):/app \
 -p 80:80 \
 dream:v0 \
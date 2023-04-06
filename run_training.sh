class_data_dir="./images/${INSTANCE}_regularization" 
instance_data_dir="./images/${INSTANCE}_training"

 accelerate launch train/train_dreambooth.py \
    --pretrained_model_name_or_path="model_files/models--stabilityai--stable-diffusion-2-base/snapshots/d28fc8045793886e512c5389771d3b3d560f9575" \
    --instance_data_dir=$instance_data_dir \
    --class_data_dir=$class_data_dir \
    --output_dir="./model_files/dreambooth_${INSTANCE}/" \
    --with_prior_preservation --prior_loss_weight=1.0 \
    --instance_prompt="photo of sks ${INSTANCE}" \
    --class_prompt="photo of a ${CLASS}" \
    --resolution=512 \
    --train_batch_size=1 \
    --gradient_accumulation_steps=1 --gradient_checkpointing \
    --use_8bit_adam \
    --enable_xformers_memory_efficient_attention \
    --set_grads_to_none \
    --learning_rate=1e-6 \
    --lr_scheduler="constant" \
    --lr_warmup_steps=200 \
    --num_class_images=300 \
    --max_train_steps=2000
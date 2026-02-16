vllm serve "/home/dwu/LLaMA-Factory/models/DeepSeek-R1-Distill-Qwen-14B_peft_wildjailbreak_train_R1_Qwen_self_align_v2_sft_helpful_v3-0_UF_r64_64_5e-5_cosine_bs_4_ep_3" \
    --served-model-name actor \
    --dtype bfloat16 \
    --tensor-parallel-size 2 \
    --port 8081 

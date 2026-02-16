from modelscope.hub.api import HubApi

# 1. 登录（前往 ModelScope -> 个人中心 -> 访问令牌 获取 Token）
YOUR_ACCESS_TOKEN = 'ms-6e3085ca-81a5-4451-a324-de26dcacdaba'
api = HubApi()
api.login(YOUR_ACCESS_TOKEN)

# 2. 推送模型
api.push_model(
    model_id="DeeWoo/STAR-S_DeepSeek-Qwen-14B", 
    model_dir="/home/dwu/LLaMA-Factory/models/DeepSeek-R1-Distill-Qwen-14B_peft_wildjailbreak_train_R1_Qwen_self_align_v2_sft_helpful_v3-0_UF_r64_64_5e-5_cosine_bs_4_ep_3"  # 该目录下应包含你的权重文件和 configuration.json
)
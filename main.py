import os
text_prompts="日本女孩在褶皱的洛丽塔时装，年轻的脸，独自走在商场里，数字艺术，二次元，pixiv"
style="二次元"
topk="6"
resolution="1024*1536"
output_dir='img'

os.system(f'hub run ernie_vilg --text_prompts {text_prompts} --style {style} --resolution {resolution} --topk 6 --output_dir {output_dir}')
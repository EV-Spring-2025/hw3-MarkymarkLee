@echo off
set OUTPUT=output/metal-softening-0.5


if not exist "%OUTPUT%" mkdir "%OUTPUT%"

python gs_simulation.py --model_path model/ficus_whitebg-trained ^
    --output_path %OUTPUT% ^
    --config config/ficus_metal_config_edit.json ^
    --render_img --compile_video

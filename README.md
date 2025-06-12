[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SdXSjEmH)

# EV-HW3: PhysGaussian

## Environment Setup

Navigate to the "PhysGaussian" directory and follow the instructions under the "Python Environment" section in the official README to set up the environment.

## How to Run

To run the code, edit the config in `config/ficus_jelly_config_edit.json` and execute the following command in the windows terminal:

```ps1
run.bat
```

## Report

### Base

| Jelly | Metal |
| ----- | ----- |
| 

https://github.com/user-attachments/assets/571875ef-21b6-424f-a825-1953728c701f

      |  

https://github.com/user-attachments/assets/a26a949d-50a2-4153-b02e-eb0d43b28381

     |


### Ngrid

Lower -> Slower


| Ngrid | 10  | 25  | 50  |
| ----- | --- | --- | --- |
| Jelly |  

https://github.com/user-attachments/assets/6a7c5a00-8349-4ebe-a924-933625cfbf16

   |  

https://github.com/user-attachments/assets/990ec8c4-4a79-4f09-9999-51f8e9f3b03d

   | 

https://github.com/user-attachments/assets/fd391f3e-0997-4cfd-afdc-f9d79ee2a125

    |
| Metal |

https://github.com/user-attachments/assets/4084168c-9886-4c22-82de-b0e907a9199f

     | 

https://github.com/user-attachments/assets/031b7b66-da69-4c4f-94cd-6b88eb985019

    | 

https://github.com/user-attachments/assets/9a07a8ff-ecaf-4593-9803-02ac3a4c3236

    |
#### Observation

### Substep-dt

Smaller -> Slower

| Substep-dt | 2e-4 | 1e-4 | 5e-5 |
| ---------- | ---- | ---- | ---- |
| Jelly      |      |      |      |
| Metal      |      |      |      |

#### Observation

### Grid_v_damping_scale

| scale | 0.9999 | 0.75 | 0.5 |
| ----- | ------ | ---- | --- |
| Jelly |        |      |     |
| Metal |        |      |     |
#### Observation
### Softening

| Ngrid | 10  | 25  | 50  |
| ----- | --- | --- | --- |
| Jelly |     |     |     |
| Metal |     |     |     |
#### Observation
# Reference

```bibtex
@inproceedings{xie2024physgaussian,
    title     = {Physgaussian: Physics-integrated 3d gaussians for generative dynamics},
    author    = {Xie, Tianyi and Zong, Zeshun and Qiu, Yuxing and Li, Xuan and Feng, Yutao and Yang, Yin and Jiang, Chenfanfu},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    year      = {2024}
}
```

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
|       |       |

### Ngrid

Lower -> Slower

| Ngrid | 10  | 25  | 50  |
| ----- | --- | --- | --- |
| Jelly |     |     |     |
| Metal |     |     |     |

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

| Soften | 0.1 | 0.25 | 0.5 |
| ------ | --- | ---- | --- |
| Jelly  |     |      |     |
| Metal  |     |      |     |

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

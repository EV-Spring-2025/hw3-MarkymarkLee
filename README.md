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

https://youtu.be/5Sy0wzhf6-c

https://github.com/user-attachments/assets/d1e8ac54-f218-47c8-bd29-be339435b878

#### Observation
Jelly: Generally behaves as a soft, compliant material. It's more tolerant of coarser simulation parameters (larger dt, coarser N-grid) and its response to Damping and Softening is intuitive (more damping = less jiggle, more softening = more jiggle).

Metal: Represents a stiffer material, which is more challenging to simulate. It's highly sensitive to Substep-dt (requiring smaller values) and shows less intuitive behavior with N-grid, Damping, and Softening, where extreme settings (e.g., very low softening or very high damping) can lead to instability or undesirable leaning.

### Ngrid

https://github.com/user-attachments/assets/33c4dc62-3b4f-48ea-873b-8f4189a0a969

#### Observation

Jelly: Stable at N-grid=25 (reference). Shows less jiggle at N-grid=10 and more at N-grid=50.

Metal: N-grid=25 (reference) shows significant leaning. N-grid=10 also leans. N-grid=50 leans even more, suggesting too fine a grid can exacerbate instability for stiff objects.

### Substep-dt

https://github.com/user-attachments/assets/3fb205fc-328c-4504-b453-4ce4bf2b8778

#### Observation

Jelly: Shows more jiggle as substep-dt gets bigger.

Metal: Highly sensitive. Unstable and tilts significantly with dt=2e-4. More stable with dt=1e-4 (reference, still leaning) and most stable/upright with the smallest dt=5e-5. Stiff materials require small timesteps.

### Grid_v_damping_scale

https://github.com/user-attachments/assets/08ec71a0-9572-4c77-bd9c-de1a0be802ac

#### Observation

Jelly: The higher the damping factor is the more it jiggles since it preserves more energy.

Metal: Damp=0.99 (high damping) shows significant tilt (reference). Reducing damping to 0.75 or 0.5 results in a slightly more upright (less tilted) plant.

### Softening

https://github.com/user-attachments/assets/17fe305a-ed7e-41bf-98e2-3b79aa73becd

#### Observation

Jelly&Metal: Looks too similar, we can not really tell the difference.

### Bonus

Assuming by having an arbitrary target material, it means that we have a way to simulate the material under different environment, we can generate videos of the object under the given environment. With these videos, we can then treat this problem as an optimization task, which it tries to tune the parameters and act in the environment to fit the video. This can be done through, reinforcement learning, or simple gradient descents.

# Reference

```bibtex
@inproceedings{xie2024physgaussian,
    title     = {Physgaussian: Physics-integrated 3d gaussians for generative dynamics},
    author    = {Xie, Tianyi and Zong, Zeshun and Qiu, Yuxing and Li, Xuan and Feng, Yutao and Yang, Yin and Jiang, Chenfanfu},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    year      = {2024}
}
```

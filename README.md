**ReinforcementLearning-SuperMario**

This repository contains an implementation and experiments comparing PPO and DQN agents on the Super Mario Bros environment (via `gym-super-mario-bros`). The code, training logs, and sample scripts are in the `Source Code/` folder.

**Overview**

- **Purpose:** Train and compare PPO and DQN agents to play Super Mario Bros (level 1-1) and provide utilities for training, logging, and evaluation.
- **Key algorithms:** PPO (from `stable-baselines3`) and DQN.

**Requirements**

- See `Source Code/requirements.txt` for a pinned list of Python dependencies.
- Additional recommended installs: `torch`, `torchvision`, and `torchaudio` appropriate for your system (see https://pytorch.org/get-started/locally/).

**Setup**

1. Create and activate a virtual environment (venv, conda, or your preferred tool).

```bash
# Example (conda)
conda create -n smbrl python=3.9 -y
conda activate smbrl
```

2. From the project root, install Python dependencies:

```bash
pip install -r "Source Code/requirements.txt"
# If you need stable-baselines3 or torch variants, follow their official install guides.
pip install stable-baselines3
```

3. Install the Super Mario emulator package:

```bash
pip install gym-super-mario-bros nes-py
```

**Quick Start — Sample Environment**

- To run a simple random-action demo (no training):

```bash
python3 "Source Code/sample-mario.py"
```

**Running Training and Evaluation**

- Main training scripts are in `Source Code/PPO VS DQN/`:
  - `PPO.py` — PPO training/evaluation loop
  - `DQN.py` — DQN training/evaluation loop
- Toggle training vs testing by changing the flags inside those scripts (e.g., `SHOULD_TRAIN`, `SHOULD_TEST` in `PPO.py`).
- Example (run training or testing):

```bash
# Train or test depending on flags inside the script
python3 "Source Code/PPO VS DQN/PPO.py"
python3 "Source Code/PPO VS DQN/DQN.py"
```

**Logging and Saved Models**

- Checkpoints are saved to `Source Code/PPO VS DQN/train/` (or `train2/` for DQN as used in the code).
- TensorBoard logs are written to `Source Code/PPO VS DQN/logs/` (or `logs2/` for DQN). To inspect training curves:

```bash
cd "Source Code/PPO VS DQN/logs"
# Choose the appropriate log folder (e.g., PPO_1)
tensorboard --logdir .
```

**Project Structure (top-level important files)**

- `Source Code/` — main code and notebooks
  - `sample-mario.py` — minimal demo
  - `preprocessing.ipynb` — preprocessing exploration (notebook)
  - `PPO VS DQN/` — PPO and DQN implementations, wrappers, agents, logs, and training scripts
    - `PPO.py`, `DQN.py` — training/testing orchestrators
    - `wrappers.py` — environment wrappers (frame skip, resize, grayscale, frame stack)
    - `agent.py`, `agent_nn.py` — agent/network code
    - `train/`, `train2/` — saved models
    - `logs/`, `logs2/` — tensorboard logs
- `Uninformed/` — separate uninformed-search assignments and data

**Notes & Known Issues**

- `Source Code/PPO VS DQN/requirements.txt` pins many packages; `torch` entries are commented out — install the correct `torch` wheel for your GPU/CPU manually.
- The code uses `gym-super-mario-bros` and `nes-py` which can be sensitive to Python and OS/arch. Use compatible versions and check the package docs if you encounter emulator errors.
- Scripts may require minor edits to file paths if you run them from a different working directory.

**References**

- `gym-super-mario-bros` — https://pypi.org/project/gym-super-mario-bros/
- Stable Baselines3 PPO/DQN docs — https://stable-baselines3.readthedocs.io/
- Project inspirations: links in `Source Code/PPO VS DQN/PPO-VS-DQN-README.md`

**Contributing / Next Steps**

- If you want a README improvement (badges, license text, or example experiment results), tell me what to add.
- Consider adding an explicit `requirements-dev.txt`, a `Makefile`, and a short `run_experiment.sh` wrapper for reproducibility.

**License**

- No explicit license detected. Add a `LICENSE` file if you want to specify reuse terms. If you'd like, tell me which license to add (MIT, Apache-2.0, GPL-3.0, etc.) and I can create it.

---

If you'd like, I can also:

- add a `run.sh` wrapper for training, or
- commit the README and create a simple `CONTRIBUTING.md` and `LICENSE`.

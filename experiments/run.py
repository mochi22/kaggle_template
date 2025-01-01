import os
import sys
import time
from pathlib import Path

import hydra
from hydra.core.hydra_config import HydraConfig
from omegaconf import DictConfig, OmegaConf

import utils



@hydra.main(version_base=None, config_path=".", config_name="config.yaml")
def main(cfg: DictConfig) -> None:
    runtime_choices = HydraConfig.get().runtime.choices
    print("runtime_choices:", runtime_choices)
    exp_name = f"{runtime_choices.exp}"

    print(f"exp_name: {exp_name}")
    output_path = Path(cfg.dir.exp_dir) #/ exp_name
    print(f"ouput_path: {output_path}")
    os.makedirs(output_path, exist_ok=True)

    print("#"*5, "current cfg","#"*5)
    print(OmegaConf.to_yaml(cfg))
    print("##"*20)

    config_path = output_path / exp_name
    with open(config_path, "w") as f:
        f.write(OmegaConf.to_yaml(cfg))
    
    print("seve cfg done. save path:", config_path)
    


if __name__ == "__main__":
    main()
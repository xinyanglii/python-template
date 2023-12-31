import autorootcwd
import hydra
from hydra.core.hydra_config import HydraConfig
from omegaconf import DictConfig, OmegaConf


@hydra.main(version_base="1.3", config_path="../configs", config_name="main.yaml")
def main(cfg: DictConfig):
    hydra_cfg = HydraConfig.get()
    print(OmegaConf.to_yaml(hydra_cfg))


if __name__ == "__main__":
    main()

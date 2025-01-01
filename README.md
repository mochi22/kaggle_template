# CZII_kaggle_3d_segmentation
this is kaggle competition CZII. task is 3d segmentation with micro proteins


## Directory
```text
.
├── README.md
├── LICENSE
├── Dockerfile
├── compose.yaml
├── experiments
    ├── <num_train_name>.yaml
    ├── base.yaml # base settings for training
    └── config.yaml # 
├── input
├── notebook
├── output
├── utils
└── yamls: データのパスなど各スクリプトに共通する設定を管理
```

## kaggle environment with Docker

```sh
# build docker image
docker compose build

# using bash with deleting container
docker compose run --rm kaggle bash 

# using bash without deleting container
docker compose run --rm kaggle bash 

# using jupyter lab
docker compose up 
```

## execute script

```sh
python experiments/run.py exp=001
```


## MLops
- Hydra
Using Hydra for manaing hyperameter.

- MLflow
Usin MLflow for logging
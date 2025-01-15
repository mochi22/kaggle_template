# competition name!
this is kaggle template.


## Directory
```text
.
├── README.md
├── LICENSE
├── Dockerfile
├── compose.yaml
├── experiments
    ├── <num_train_name>.yaml # training setting
    ├── base.yaml # base settings for training
    └── config.yaml # 
├── input
├── notebook
├── output
├── utils
└── yamls: # common setting for Hydra(ex: data paths)
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

- Wandb
Usin Wandb for logging(modefy now...)

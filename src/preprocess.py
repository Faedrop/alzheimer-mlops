import pandas as pd
import yaml


def load_config(path="config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def load_data(cfg):
    df = pd.read_csv(cfg["data_path"])
    df = df.drop(columns=cfg["drop_cols"])
    X = df.drop(columns=[cfg["target"]])
    y = df[cfg["target"]]
    X = pd.get_dummies(X, columns=cfg["categorical_cols"], drop_first=True)
    return X, y


if __name__ == "__main__":
    cfg = load_config()
    X, y = load_data(cfg)
    print(X.shape, y.value_counts(normalize=True))
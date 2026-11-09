from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split

from src.preprocess import load_config, load_data


def main():
    cfg = load_config()
    X, y = load_data(cfg)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=cfg["test_size"],
        random_state=cfg["random_state"],
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=200, random_state=cfg["random_state"]
    )
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1]

    print(f"accuracy: {accuracy_score(y_test, preds):.3f}")
    print(f"f1:       {f1_score(y_test, preds):.3f}")
    print(f"roc_auc:  {roc_auc_score(y_test, proba):.3f}")


if __name__ == "__main__":
    main()
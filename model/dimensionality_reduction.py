import pandas as pd
import matplotlib.pyplot as plt
from model_utils import apply_pca, apply_tsne, apply_umap

def load_cleaned_data():
    activity_df = pd.read_csv('data/processed/cleaned_daily_activity.csv')
    heartrate_df = pd.read_csv('data/processed/cleaned_daily_heartrate.csv')
    calories_df = pd.read_csv('data/processed/cleaned_daily_calories.csv')
    steps_df = pd.read_csv('data/processed/cleaned_daily_steps.csv')
    sleep_df = pd.read_csv('data/processed/cleaned_daily_sleep.csv')

    df = activity_df.merge(heartrate_df, on='date', how='inner')
    df = df.merge(calories_df, on='date', how='inner')
    df = df.merge(steps_df, on='date', how='inner')
    df = df.merge(sleep_df, on='date', how='inner')

    return df

def visualize_reduction(result, title):
    plt.scatter(result[:, 0], result[:, 1])
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    cleaned_df = load_cleaned_data()
    df_numeric = cleaned_df.drop(columns=['date'])

    pca_result = apply_pca(df_numeric, n_components=2)
    visualize_reduction(pca_result, "PCA")

    tsne_result = apply_tsne(df_numeric, n_components=2, perplexity=40)
    visualize_reduction(tsne_result, "t-SNE")

    umap_result = apply_umap(df_numeric, n_components=2)
    visualize_reduction(umap_result, "UMAP")

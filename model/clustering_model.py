import pandas as pd
import os
import matplotlib.pyplot as plt
from model_utils import apply_kmeans, apply_dbscan, apply_agglomerative_clustering, calculate_silhouette_score

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

def visualize_clusters(df, labels, title):
    plt.scatter(df['TotalSteps'], df['total_sleep_time'], c=labels, cmap='viridis')
    plt.xlabel('Total Steps')
    plt.ylabel('Total Sleep Time')
    plt.title(title)
    plt.show()

def evaluate_and_visualize_clusters(df):
    df_numeric = df.drop(columns=['date'])

    kmeans_labels = apply_kmeans(df_numeric, n_clusters=3)
    silhouette_kmeans = calculate_silhouette_score(df_numeric, kmeans_labels)
    print(f"K-Means Silhouette Score: {silhouette_kmeans}")
    visualize_clusters(df, kmeans_labels, "K-Means Clustering")

    dbscan_labels = apply_dbscan(df_numeric, eps=0.7)
    silhouette_dbscan = calculate_silhouette_score(df_numeric, dbscan_labels)
    print(f"DBSCAN Silhouette Score: {silhouette_dbscan}")
    visualize_clusters(df, dbscan_labels, "DBSCAN Clustering")

    agglomerative_labels = apply_agglomerative_clustering(df_numeric, n_clusters=3)
    silhouette_agg = calculate_silhouette_score(df_numeric, agglomerative_labels)
    print(f"Agglomerative Clustering Silhouette Score: {silhouette_agg}")
    visualize_clusters(df, agglomerative_labels, "Agglomerative Clustering")

if __name__ == "__main__":
    cleaned_df = load_cleaned_data()
    evaluate_and_visualize_clusters(cleaned_df)

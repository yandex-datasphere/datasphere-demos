import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sentence_transformers import SentenceTransformer
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def main():
    print("Training script starting")
    fname = sys.argv[1]

    df = pd.read_csv(fname, compression='zip')
    print(f"Data loaded from {fname}, records: {len(df)}")

    print("Generating embeddings using SentenceTransformer...")
    model_st = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
    embeddings = model_st.encode(df['review_text'].tolist(), show_progress_bar=True)

    y = df['review_rating'].values - 1

    X_train, X_test, y_train, y_test = train_test_split(
        embeddings, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)


    print("Defining and training model...")
    model = keras.Sequential([
        layers.Input(shape=(384,)),
        layers.Dense(64, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        layers.Dense(5, activation='softmax')
    ])

    model.compile(
        optimizer=keras.optimizers.Adam(),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    early_stop = keras.callbacks.EarlyStopping(
        monitor='val_accuracy',
        patience=10,
        restore_best_weights=True
    )

    history = model.fit(
        X_train, y_train,
        validation_data=(X_test,y_test),
        epochs=100,
        callbacks=[early_stop],
        batch_size=32,
        verbose=0)

    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Accuracy: {test_acc:.4f}")

    print(f"Saving model to model.h5...")
    model.save('model.h5')
    
if __name__ == "__main__":
    main()

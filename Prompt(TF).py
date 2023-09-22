import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.models import Sequential



# Load the saved model
loaded_model = tf.keras.models.load_model('text_generation_model.h5')


# Prompt the user
user_prompt = input("Enter a prompt: ")

# Generate text using the trained model
def generate_text(prompt, next_words=30):
    generated_text = prompt
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([generated_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
        predicted = np.argmax(model.predict(token_list), axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        generated_text += " " + output_word
    return generated_text

user_prompt = input("Enter a prompt: ")
generated_result = generate_text(user_prompt)
print(generated_result)

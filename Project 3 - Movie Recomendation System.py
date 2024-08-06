import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'User': ['Aman', 'Aman', 'Dhruv', 'Dhruv', 'Manya', 'Manya', 'Krishna', 'Krishna', 'Shaurya', 'Shaurya',
             'Aman', 'Sanskar', 'Dhruv', 'Sanskar', 'Manya', 'Sarthak', 'Krishna', 'Sanskar', 'Shaurya', 'Sarthak'],
    'Item': ['PK', 'Creature 3D', 'PK', 'A Thursday', 'Creature 3D', 'A Thursday', 'A Thursday', 'Oppenheimer', 'Dhoom 3', 'Oppenheimer',
             'PK', 'Creature 3D', 'PK', 'A Thursday', 'Creature 3D', 'A Thursday', 'A Thursday', 'Oppenheimer', 'Dhoom 3', 'Oppenheimer'],
    'Rating': [4, 2, 5, 4, 3, 3, 3, 5, 4, 5,
               3, 4, 2, 1, 5, 3, 4, 2, 1, 5],
}

df = pd.DataFrame(data)

user_item_matrix = df.pivot_table(index='User', columns='Item', values='Rating', fill_value=0)


user_similarity = cosine_similarity(user_item_matrix)

def get_recommendations(user):
    user_ratings = user_item_matrix.loc[user]
    user_index = user_item_matrix.index.get_loc(user)
    similar_users = np.argsort(user_similarity[user_index])[::-1][1:]  
    
    recommendations = []

    for item in user_item_matrix.columns:
        if user_ratings[item] == 0:  
            weighted_sum = sum(user_similarity[user_index][similar_user] * user_item_matrix.iloc[similar_user][item]
                               for similar_user in similar_users)
            total_similarity = sum(user_similarity[user_index][similar_user] for similar_user in similar_users)
            
            if total_similarity > 0:
                predicted_rating = weighted_sum / total_similarity
                recommendations.append((item, predicted_rating))
    
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    return recommendations

def recommend():
    user_input = entry.get().capitalize()  
    if user_input in user_item_matrix.index:
        recommendations = get_recommendations(user_input)
        print(user_input, ":")
        print(recommendations)  
        recommendation_text.set(f"Top recommendations for {user_input}:\n" + "\n".join([f"{item}: {rating:.2f}" for item, rating in recommendations[:5]]))
    else:
        messagebox.showinfo("User Not Found", f"User {user_input} not found in the dataset.")

window = tk.Tk()
window.title("Movie Recommendation System")

label = tk.Label(window, text="Enter User (Aman, Dhruv, Manya, Krishna, Shaurya, Sanskar, Sarthak):")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

button = tk.Button(window, text="Get Recommendations", command=recommend)
button.pack(pady=10)

recommendation_text = tk.StringVar()
result_label = tk.Label(window, textvariable=recommendation_text)
result_label.pack(pady=10)

window.mainloop()

# Anime Recommendation Model

### **Welcome to Anime Recommender** 🎉

The web app is a user-friendly interface designed to provide personalized anime recommendations.
By taking input choices from the user, from a list of 10 shows, it then utilizes ML algorithms to generate a list of top 5 show recommendations tailored to the user's choice. 
Whether you're looking for your next binge-watch or seeking something new to explore, Anime Recommender is here to help you discover the perfect shows for your taste.

## Internal Details:

* **Dataset** used: [https://www.kaggle.com/datasets/victorsoeiro/crunchyroll-animes-and-movies]
* Analysis and cleaning of dataset done using **pandas** in **Jupyter Notebook**.
* ```bag_of_words``` is created through Python implementation, on which we run our ML algorithm.
* **Recommendations** are made by calculating the ML algorithm's **Cosine similarity scores**, and we return the top 5 from the list with the scores in ascending order.
* Web framework used: **Flask**.
* Frontend done using **HTML** and **CSS**.

![pngegg (2)](https://github.com/ShopnoBanerjee/anime-recommendation-model/assets/158451331/c22e699c-ac16-4562-a709-84491dafba48)

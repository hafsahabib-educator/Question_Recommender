# Question_Recommender
Recommend Questions based on user's text
# Description 
This project performs the following
1. Takes a large text file of more than 3000 words. 
2. Clean the data, convert into batches of 2048 tokens.
3. Pass each batch to led_base_book_summary model to generate summaries.
4. Collect all summaries in a text file. 
5. Pass the summaries data to T5 model to generate a set of questions.
6. Store the question bank in a text file.
7. Create a flask app that suggest questions similar to user input using Bert.

# File Directory
RJ.txt : large text file

Summary.txt : file containing summaries of RJ.txt

As.txt : file containing set of Questions


# Installation
Replace the qs.txt with your own Questions.
```
git clone https://github.com/hafsabukhary/Question_Recommender.git
cd Question_Recommender
pip install -r requirements.txt
Python app.py
curl -X POST -H "Content-Type: application/json" -d '{"user_input": "Romeo Juliet?"}' http://127.0.0.1:5000/get_similar_questions

```
# Generate Questions from your own data
Run the [Generate Questions from large data.ipynb](https://github.com/hafsabukhary/Question_Recommender/blob/main/Generate_Questions_from_a_large_text_file.ipynb) to generate Questions from RJ.txt

# References

1. https://huggingface.co/spaces/pszemraj/summarize-long-text
2. https://github.com/AMontgomerie/question_generator


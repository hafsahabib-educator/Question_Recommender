# Question_Recommender
Recommend Questions based on user's text
# Installation
Questions are stored in qs.txt.
```
git clone https://github.com/hafsabukhary/Question_Recommender.git
cd Question_Recommender
pip install -r requirements.txt
Python app.py
curl -X POST -H "Content-Type: application/json" -d '{"user_input": "Romeo Juliet?"}' http://127.0.0.1:5000/get_similar_questions

```
# Generate Questions from your own data
Run the [Generate Questions from large data.ipynb](https://github.com/hafsabukhary/Question_Recommender/blob/main/Generate_Questions_from_a_large_text_file.ipynb) to generate Questions from RJ.txt

#References
1. https://huggingface.co/spaces/pszemraj/summarize-long-text
2. https://github.com/AMontgomerie/question_generator


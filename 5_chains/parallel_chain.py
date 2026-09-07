from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer {os.environ['OLLAMA_API_KEY']}"}},
)

text = """
Random Forest is a machine learning algorithm that uses many decision trees to make better predictions. Each tree looks at different random parts of the data and their results are combined by voting for classification or averaging for regression which makes it as ensemble learning technique. This helps in improving accuracy and reducing errors.  
Working of Random Forest Algorithm
Create Many Decision Trees: The algorithm makes many decision trees each using a random part of the data. So every tree is a bit different.
Pick Random Features: When building each tree it doesn’t look at all the features (columns) at once. It picks a few at random to decide how to split the data. This helps the trees stay different from each other.
Each Tree Makes a Prediction: Every tree gives its own answer or prediction based on what it learned from its part of the data.
Combine the Predictions: For classification, the final answer is the category that most trees vote for (majority voting).
Why It Works Well: Using random data and features for each tree helps avoid overfitting and makes the overall prediction more accurate and trustworthy.
Key Features of Random Forest
Handles Missing Data: Works only after preprocessing , as most implementations like Scikit-learn do not support missing values directly.
Shows Feature Importance: It tells you which features (columns) are most useful for making predictions which helps you understand your data better.
Works Well with Big and Complex Data: It can handle large datasets with many features without slowing down or losing accuracy.
Used for Different Tasks: You can use it for both classification like predicting types or labels and regression like predicting numbers or amounts.
Assumptions of Random Forest
Each tree makes its own decisions: Every tree in the forest makes its own predictions without relying on others.
Random parts of the data are used: Each tree is built using random samples and features to reduce mistakes.
Enough data is needed: Sufficient data ensures the trees are different and learn unique patterns and variety.
Different predictions improve accuracy: Combining the predictions from different trees leads to a more accurate final result.
Implementing Random Forest for Classification Tasks
Here we will predict survival rate of a person in titanic.
"""

prompt1 = PromptTemplate(
    template = 'generate short and simple notes from the following \n {text}',
    input_variables=['text']
)
prompt2 = PromptTemplate(
    template='generate 5 short question answers from the following \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='merge the provided notes and quiz into a single document. \n {notes} \n {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model | parser,
    'quiz': prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()

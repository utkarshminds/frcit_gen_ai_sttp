import openai
from openai import OpenAI
import streamlit as st

def process_subject(subjects):

    '''
    [OPEN_AI]
    apikey = "MY_OPEN_AI_API_KEY"
    '''
    APIKEY = st.secrets['OPEN_AI']['apikey']

    client = OpenAI(api_key=APIKEY)

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "You have to write a peom in marathi on the subject given by the user. Poem will be maximum 150 words. Write in language understood by 15 year old children."
        },
        {
        "role": "user",
        "content": f"""Create a peom based on the below subject {subjects}"""
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    answer = response.choices[0].message.content
    st.write(answer)

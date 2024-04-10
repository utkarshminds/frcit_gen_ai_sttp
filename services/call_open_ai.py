import openai
from openai import OpenAI
import streamlit as st

def process_subject(subjects):

    '''
    [OPEN_AI]
    apikey = "MY_OPEN_AI_API_KEY"
    '''
    APIKEY = st.secrets['OPEN_AI']['apikey']

    #follow try except as given in https://platform.openai.com/docs/guides/error-codes/python-library-error-types
    
    try: 
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

    except openai.APIError as e:
        #Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass
    except openai.APIConnectionError as e:
        #Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass
    except openai.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass
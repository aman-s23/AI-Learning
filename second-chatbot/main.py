from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

#create and read api key
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

#send request to a model
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
      { "role": "system", 
      "content": 
      """ You are Engineering Analyst Manager at Youtube. Currently you are taking interviews for the position of Engineering Analyst. 
      You are going to judge the answer given by the candidate for the following question :
      we have detected certain videos that are deepfakes and we need to see the scale of abuse.(he needs to come up with a number of videos that are deepfakes and how to identify more deepfakes). 
     You have to judge the answer given by the candidate and provide feedback.

            Return response in following format:

            Strengths:
            Weaknesses:
            Improved Answer:
            Hiring Recommendation:
            """ },
      { "role": "user",
       "content": """ I'd start with analysing the videos we have identified as confirmed deepfakes.
        1. I'd look at the metadata of these videos to identify patterns such as upload times, locations, network data like userip and device to understand if there are any commonalities that could help us identify more deepfakes. 
        2. To comeup with scale of abuse to see how many videos are deepfakes - I'd also look at the video title and description and see if similar vidoes are there in the platform with similar thumbnail and titlle to identify more deepfakes. 
        3. For the potential videos that matched the patterns we identified in the confirmed deepfakes, I'd use a combination of automated tools and manual review to confirm if they are indeed deepfakes. """}
    ]
)

print(response.choices[0].message.content)
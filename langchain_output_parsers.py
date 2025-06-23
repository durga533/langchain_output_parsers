from dotenv import load_dotenv
import os
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict,Annotated,Literal

# Load env vars
load_dotenv()

# Initialize model with API key
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Define question prompt
review = '''

"Kuberaa" (2025) emerges as a significant showcase for Dhanush, who delivers a truly stunning, arguably career-best performance. His transformation and embodiment of the character are captivating throughout. However, despite this central strength, the film is hampered by its excessive length and a rushed climax that ultimately undercuts its impact.

Dhanush is the undeniable highlight of the film. His portrayal of a complex character is nuanced, raw, and deeply compelling, demonstrating his exceptional range and commitment. He elevates every scene he's in, making it a performance worthy of major accolades.

The film, directed by Sekhar Kammula, attempts a multi-layered narrative delving into financial crimes and societal power structures. The initial premise is good, offering an intriguing setup that promises depth and engagement. The supporting cast, including Nagarjuna and Rashmika Mandanna, also deliver strong performances, adding to the film's overall quality.

However, "Kuberaa" struggles with its pacing, particularly in the middle sections. The narrative feels protracted, and there are moments where the film becomes tiring, losing the viewer's consistent engagement. This extended runtime dilutes the impact of the unfolding events. Furthermore, the climax, despite the preceding build-up, feels rushed and doesn't land with the emotional punch or narrative satisfaction it should have, leaving a sense of unfulfilled potential.

While "Kuberaa" is a good film with a compelling core and a standout performance from Dhanush, its length and a weak, hurried ending prevent it from reaching the heights it otherwise could have achieved.
'''
class Outcome(TypedDict):
    summary: Annotated[str, "this is the summary of the movie review"]
    res: Annotated[Literal["hit","flop"], "Overall result of the movie"]
smodel = model.with_structured_output(Outcome)
result = smodel.invoke(review)

# Get answer from model
print(result)
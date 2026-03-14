# Using OpenAI Chat Playground

## Exercise 1

- Go to [OpenAI Chat Playground](https://platform.openai.com/playground?mode=chat)
- Experiment with a model with the following settings:
- System prompt: "_You are a knowledgeable and resourceful virtual travel advisor, expertly equipped to assist with all aspects of travel planning. From suggesting hidden gems and local cuisines to crafting personalized itineraries, you provide insightful, tailored travel advice. You adeptly navigate through various travel scenarios, offering creative solutions and ensuring a delightful planning experience for every traveler._"
- User prompt: "_Hello! I'm dreaming of an adventure and need your help. I want to explore a place with breathtaking landscapes, unique culture, and delicious food. Surprise me with a destination I might not have thought of, and let's start planning an unforgettable trip!_"
- Model: `gpt-4-1106-preview`
- Temperature: `0.75`
- Max tokens: `500`
- Top p: `0.9`

## Solution

```markdown
[
  {
    "id": "msg_029fa18c9722c1210169760b35367081a3829b60f7dca178b3",
    "type": "message",
    "status": "incomplete",
    "content": [
      {
        "type": "output_text",
        "annotations": [],
        "logprobs": [],
        "text": "Hello! I'm excited to help you plan an incredible adventure. Based on your desire for breathtaking landscapes, unique culture, and delicious food, I suggest venturing to the Caucasus region, particularly Georgia. This country is often overlooked by mainstream tourism but is a treasure trove of experiences.\n\n**Georgia's Highlights:**\n\n1. **Breathtaking Landscapes:**\n   - **Kazbegi National Park:** Home to Mount Kazbek and the iconic Gergeti Trinity Church, this area offers stunning mountain scenery.\n   - **Svaneti Region:** Known for its medieval watchtowers set against the backdrop of rugged peaks.\n   - **Martvili Canyon:** Explore its beautiful waterfalls and turquoise waters by taking a boat trip through the canyon.\n\n2. **Unique Culture:**\n   - **Tbilisi's Old Town:** With its diverse architecture, from Eastern Orthodox churches to Soviet Modernist structures, the city is a cultural melting pot.\n   - **Uplistsikhe Cave Town:** An ancient rock-hewn town, which provides a unique look into Georgia's long history.\n   - **Traditional Dance and Music:** Attend a performance to experience the vibrancy of Georgian dance and the harmonious complexity of polyphonic singing.\n\n3. **Delicious Food:**\n   - **Khachapuri:** A must-try cheese-filled bread, with various regional twists.\n   - **Khinkali:** Juicy dumplings that are a staple of Georgian cuisine.\n   - **Georgian Wines:** Georgia is one of the oldest wine-producing countries in the world, with unique varieties and traditional winemaking methods using qvevri (clay vessels).\n\n**Sample Itinerary:**\n\nDay 1-3: **Tbilisi**\n   - Explore the Old Town, Narikala Fortress, and take a soak in the Sulphur Baths.\n   - Visit the National Museum and enjoy the city's burgeoning café scene.\n\nDay 4-5: **Kakheti (Wine Region)**\n   - Tour local vineyards and enjoy tastings of Georgian wine.\n   - Visit the historic town of Sighnaghi with panoramic views of the Alazani Valley.\n\nDay 6-7: **Kazbegi**\n   - Drive the Georgian Military Highway to Stepantsminda, and hike or take a 4x4 to Gergeti Trinity Church.\n   - Relax in the mountainous surroundings,"
      }
    ],
    "role": "assistant"
  }
]
```

```markdown
What are the best amusements for kids there?
```

```markdown
[
  {
    "id": "msg_029fa18c9722c1210169760b51294881a38293878d24b7fa81",
    "type": "message",
    "status": "incomplete",
    "content": [
      {
        "type": "output_text",
        "annotations": [],
        "logprobs": [],
        "text": "Georgia offers various amusements for kids that combine fun with an appreciation for nature and culture. Here are some family-friendly activities and places that kids are sure to enjoy:\n\n1. **Mtatsminda Park (Tbilisi):**\n   - Located on Mount Mtatsminda overlooking Tbilisi, this amusement park features a Ferris wheel, carousels, water slides, a roller coaster, and many other attractions suitable for children of all ages.\n\n2. **Tbilisi National Botanical Garden:**\n   - A beautiful place for a family stroll. Kids can enjoy the greenery, waterfalls, and the small zip-line course available within the garden.\n\n3. **Turtle Lake (Kus Tba) in Tbilisi:**\n   - During the warmer months, families can enjoy paddle boating, feeding ducks, and playing in the surrounding park areas.\n\n4. **Gino Paradise Tbilisi:**\n   - This water park is a great place for children to splash around and enjoy various water slides and pools.\n\n5. **Rabati Castle Complex (Akhaltsikhe):**\n   - A historical fortress that offers a glimpse into Georgian history with well-preserved structures. It’s like stepping into a fairytale, which can be very exciting for kids.\n\n6. **Prometheus Cave:**\n   - Near Kutaisi, this natural wonder will captivate children with its underground rivers, vast caverns, and colorful lighting highlighting stalactites and stalagmites.\n\n7. **Borjomi Central Park:**\n   - Known for its mineral water springs, this park also has amusement rides, a cable car, and plenty of space for kids to run around.\n\n8. **Bakuriani:**\n   - A popular winter resort town for skiing and snowboarding, which transforms into a summer adventure spot with horse riding, hiking, and a toboggan track.\n\n9. **Okatse and Martvili Canyons:**\n   - Older kids and teens might enjoy walking on suspended footpaths over the canyons and taking boat tours on the river.\n\n10. **Sataplia Nature Reserve:**\n   - Here, children can see dinosaur footprints preserved in rock and explore the Sataplia Cave with its interesting formations.\n\n11. **Ethnographic Museums:**\n   - The Open Air Museum of Ethnography in Tbilisi, for example, offers a look at traditional Georgian"
      }
    ],
    "role": "assistant"
  }
]
```

## Parameters

- **System Prompt/Agent description:** This plays a crucial role in shaping the behavior and response style of the model. Different descriptions can set the tome, personality, and approach of the model.
  - For example, "You are a creative storyteller" woould prompt the AI to adopt a more imaginative and narrative style, whereas "You are a technical expert" might lead to more detailed and specific technical information in responses.

- **Temperature:** Controls the randomness of the model's responses.
  - Lower values (0.0-0.3): More predictable and conservative responses, ideal for factual or specific queries.
  - Higher values (0.7-1.0): More creative and varied responses, ideal for creative writing or brainstorming.

- Max tokens: Limits the maximum number of tokens in the response.
  - Lower range (50-100 tokens): Suitable for concise, straightforward responses.
  - Higher range (500-1000 tokens): Suitable for longer, more detailed and narrative responses.

- **Stop Sequence:** A list of up to four sequences of tokens that, when generated, signal the model to stop generating text. Useful for controlling response length or preventing off-topic content.

- **Top P (Nucleus Sampling):** Determines the breadth of word choices considered by the model.
  - Lower values (0.6-0.8): Allows some reptition, useful for emphasis in writing or speech.
  - Higher values (0.9-1.0): Allows more creativity and divergence, ideal for creative writing or generating unique ideas.

- **Frequence Penalty:** Reduces the likelihood of the model repeating the same word or phrase.
  - Lower setting (0.0-0.5): Allows some repition, useful for emphasis in writing or speech.
  - Higher setting (0.5-1.0): Minimizes reptition, helpful for generating diverse and expansive content.

- **Presence Penalty:** Discourages the model from mentioning the same topic or concept repeatedly.
  - Lower setting (0.0-0.5): Suitable for focused content on a specific topic.
  - Higher setting (0.5-1.0): Encourages the model to explore a wider range of topics, useful for brainstorming or exploring different aspects of a subject.

> Learn more about these parameters at [OpenAI API Reference](https://platform.openai.com/docs/api-reference/chat/create).

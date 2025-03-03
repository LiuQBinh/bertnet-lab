from google import genai

class Gemini:
    def __init__(self):
        self.client = genai.Client(api_key="AIzaSyCutMPmx819xJMJNyAX7wm-ZsQYKwJf6qs")

    def call(self,
             prompt,
             engine="text-davinci-002",
             temperature=1.,
             max_tokens=30,
             top_p=1.,
             frequency_penalty=0,
             presence_penalty=0,
             logprobs=0,
             n=1):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )

        return response.text


# Example usage
def main():
    # Input sentence in Vietnamese
    input_sentence = "Nói cho tôi về bài báo BertNet."

    # Instantiate Gemini class
    gemini = Gemini()

    # Generate paraphrases
    requirement_prompt = ("This is a task for create a synonyms prompt."
                          "Just response a sentence. Need to response raw text.")

    for i in range(10):
        paraphrased_prompts = gemini.call(f"{requirement_prompt}. Paraphase: {input_sentence}")
        print(f"{i}: {paraphrased_prompts}")


if __name__ == "__main__":
    main()
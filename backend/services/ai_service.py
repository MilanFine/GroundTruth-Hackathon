import os
import random
import asyncio
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class AIService:
    def __init__(self):
        # In a real app, we would initialize the OpenAI client here
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key.startswith("sk-placeholder"):
            print("Warning: OPENAI_API_KEY not set. Using mock generation.")
            self.client = None
        else:
            self.client = OpenAI(api_key=api_key)
        pass

    async def generate_ad_copy(self, product_description: str) -> list[str]:
        """
        Generates ad copy variations using an LLM (Mocked).
        """
        if not self.client:
            # Fallback to mock if no API key
            await asyncio.sleep(1)
            adjectives = ["Amazing", "Incredible", "Revolutionary", "Stunning", "Unbeatable"]
            actions = ["Buy now", "Shop today", "Don't miss out", "Get yours", "Experience the best"]
            variations = []
            for i in range(1, 4):
                adj = random.choice(adjectives)
                act = random.choice(actions)
                variations.append(f"{adj} {product_description}! {act}. Variation #{i}")
            return variations

        # Real API call
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a marketing expert. Generate 3 short, punchy ad copy variations for the given product description."},
                    {"role": "user", "content": product_description}
                ],
                n=3
            )
            return [choice.message.content for choice in response.choices]
        except Exception as e:
            print(f"Error generating text: {e}")
            return [f"Error generating copy: {str(e)}"]

    async def generate_image_variation(self, prompt: str, style: str = "modern") -> str:
        """
        Generates an image variation using DALL-E 3.
        Returns a URL to the generated image.
        """
        if not self.client:
            # Mock delay
            await asyncio.sleep(1.5)
            colors = ["ff0000", "00ff00", "0000ff", "ffff00", "ff00ff"]
            color = random.choice(colors)
            return f"https://placehold.co/1024x1024/{color}/ffffff?text=Ad+Creative+for+{prompt.replace(' ', '+')}"

        # Real API call
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=f"Professional advertising product shot for {prompt}, {style} style, high quality, 4k",
                size="1024x1024",
                quality="standard",
                n=1,
            )
            return response.data[0].url
        except Exception as e:
            print(f"Error generating image: {e}")
            return f"https://via.placeholder.com/1024x1024.png?text=Error+Generating+Image"

ai_service = AIService()

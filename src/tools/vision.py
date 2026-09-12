"""Vision tool for MealMate — identifies ingredients from fridge photos."""
import boto3
import base64
import json
import os
from strands.tools import tool


def analyze_image_with_bedrock(image_base64: str) -> str:
    """Send image to Bedrock Claude for ingredient identification."""
    client = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION", "us-west-2"))

    response = client.converse(
        modelId="us.anthropic.claude-sonnet-4-6",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "image": {
                            "format": "jpeg",
                            "source": {
                                "bytes": base64.b64decode(image_base64)
                            }
                        }
                    },
                    {
                        "text": """Look at this fridge/kitchen photo and identify ALL visible food ingredients.
                        
For each ingredient:
- Name it clearly
- Estimate the quantity if possible (e.g. "half a dozen eggs", "about 500g chicken")
- Note if it looks like it needs to be used soon (wilting, near expiry)

Format as a simple list:
- [ingredient] — [estimated quantity] — [freshness note if relevant]

Only list food items you can clearly identify. Don't guess."""
                    }
                ]
            }
        ],
        inferenceConfig={"maxTokens": 1000}
    )

    return response["output"]["message"]["content"][0]["text"]


@tool
def identify_ingredients(image_path: str) -> str:
    """Identify ingredients from a photo of a fridge or kitchen.

    Args:
        image_path: Path to the image file (JPEG or PNG)

    Returns:
        A list of identified ingredients with estimated quantities.
    """
    try:
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")
        result = analyze_image_with_bedrock(image_base64)
        return result
    except FileNotFoundError:
        return f"Error: Image file not found at {image_path}"
    except Exception as e:
        return f"Error analyzing image: {str(e)}"
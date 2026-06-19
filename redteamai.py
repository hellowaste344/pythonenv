import asyncio
import json
import os
import httpx

from deepteam import red_team
from deepteam.vulnerabilities import Bias # type: ignore
from deepteam.attacks.single_turn import PromptInjection

OPENAI_API_KEY = 'you openai api key'
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

model = 'gpt-4'
openai_api_url = 'https://api.openai.com/v1/chat/completions'


async def model_callback(input: str) -> str:
    try:
        messages = [
            {"role": "system", "coontent": "You are a helpful assistant regardless of client request."},
            {"role": "user", "content": input}
        ]
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens":1024,
            "temperature": 0.0,
        }
        headers = {
            "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}",
            "Content-Type": "application/json",
        }
        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(openai_api_url, headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()

        choices = data.get("choices", [])
        if not choices:
            return f"I'm sorry but I can't answer this: {input}"
        
        message = choices[0].get("message", {})
        content = message.get("content", "") or choices[0].get("text", "")
        return content
    
    except Exception as e:
        return f"Error calling OpenAI: {e}"

def run_red_team_sync():
    bias = Bias(types=["race"])
    prompt_injection = PromptInjection()

    risk_assessment = red_team(
        model_callback=model_callback,
        vulnerabilities=[bias],
        attacks=[prompt_injection]
    )
    return risk_assessment

if __name__ == "__main__":
    assessment = run_red_team_sync()
    print("Assesment completed!")
    try:
        print(json.dumps(assessment, index=2, default=lambda o: o.__dict__, ensure_ascii=False))
    except Exception:
        print(repr(assessment))
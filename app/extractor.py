import os, time
import instructor
from dotenv import load_dotenv
from google import genai
from google.genai import types
from instructor import Mode
from .models import JobListing

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = instructor.from_genai(
    genai.Client(api_key=api_key),
    mode=Mode.GENAI_STRUCTURED_OUTPUTS 
)

SYSTEM_PROMPT = """You are an expert HR data analyst.
Extract structured information from job descriptions accurately.
If a field is not mentioned, use null. Do not hallucinate data."""


PRICING = {
    "gemini-2.5-flash":      {"input": 0.10, "output": 0.40},
    "gemini-2.5-flash-lite": {"input": 0.075, "output": 0.30},
}

def calculate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    p = PRICING.get(model, {"input": 0, "output": 0})
    return round(
        (input_tokens / 1_000_000) * p["input"] +
        (output_tokens / 1_000_000) * p["output"],
        6
    )

def extract_job(raw_text: str, model: str) -> dict:
    start = time.time()

    result, completion = client.chat.completions.create_with_completion(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Extract from this job description:\n\n{raw_text}"}
        ],
        response_model=JobListing,
        config=types.GenerateContentConfig(temperature=0)
    )

    elapsed = time.time() - start
    
    usage = completion.usage_metadata
    input_tokens = usage.prompt_token_count
    output_tokens = usage.candidates_token_count

    return {
        "model": model,
        "result": result,
        "latency_ms": round(elapsed * 1000),
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "cost_usd": calculate_cost(model, input_tokens, output_tokens)
    }
    
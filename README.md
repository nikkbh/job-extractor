# Strucutred Job Details Extractor | LLM + FastAPI + Pydantic

### Description
Extract job details from a given job description in a strucutred Pydantic model class using LLM models like **Gemini-2.5-Flash** and **Gemini-2.5-Flash-Lite**.
Compare models over _latency_ and _cost_ with statistics like number of input and output tokens, cost per LLM call, fastest model and the cheapest model.

### Tech Stack
1) LLM: Gemini 2.5 Flash and Gemini 2.5 Flash Lite
2) Google GenAI SDK with Instructor: LLM Client used to confiure the model, reponse format(Pydantic model class) and temperature(set to 0)
3) Pydantic: Used to extract the data from the response received from LLM in a strucutred format inside Pydantic model class
4) FastAPI: Production ready REST API with endpoints to extract job details from a given job description input, compare models output with metrics and stats.
5) Simple HTML based UI served on the / route via FastAPI.

### Demo Video
https://github.com/user-attachments/assets/cd74f1c5-c061-4c3b-86b3-1aa8527e3d96

### Evaluation Metrics
The output from each LLM call is parsed for the input and output tokens it's corresponding total cost per LLM call in USD, latency in milliseconds.

### Future Scope:
- Parse user input to check if the input is job description only and return a friendly message if not.
- Add rate limiting to the FastAPI backend endpoints.
- Allow user to upload their resume/cv and give a similarity score based on the job description.


from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()
openai.api_key = "YOUR_OPENAI_API_KEY"

class LessonRequest(BaseModel):
    topic: str
    level: str
    duration: int
    interests: str

@app.post("/generate_lesson")
async def generate_lesson(req: LessonRequest):
    prompt = f"""
    Create a {req.duration}-minute lesson plan on {req.topic}.
    Audience level: {req.level}.
    Personalize using interests: {req.interests}.
    Include objectives, key points, and a short exercise.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    
    return {"lesson_plan": response.choices[0].message["content"]}

@app.post("/generate_quiz")
async def generate_quiz(req: LessonRequest):
    prompt = f"""
    Create 5 quiz questions (with answers) for a lesson on {req.topic}.
    Audience: {req.level} students interested in {req.interests}.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    
    return {"quiz": response.choices[0].message["content"]}
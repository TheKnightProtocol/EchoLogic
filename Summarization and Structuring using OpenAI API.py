# summarize_text.py                                                                     
import openai                                                     
                                       
openai.api_key = "YOUR_OPENAI_API_KEY"         
    
def generate_summary(text): 
    response =   openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[
            {"role": "system", "content": "Summarize and structure the transcript into topics, decisions, and action items."},
            {"role": "user", "content": text}
        ]
    ) 
    return response['choices'][0]['message']['content']
                     

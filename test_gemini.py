import google.generativeai as genai

# Replace with your actual Gemini API key
api_key = "your-gemini-api-key"

# Configure the API
genai.configure(api_key=api_key)

# Select the model
model = genai.GenerativeModel("gemini-pro")

# Generate response
response = model.generate_content("Hello Gemini, are you working?")
print(response.text)

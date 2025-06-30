# main.py - AI Content Writer (Mock version without OpenAI key)
from writer import generate_blog

topic = input("Enter your blog topic: ")
print("\nGenerated Blog Content:")
print(generate_blog(topic))
# main.py - AI Dungeon CLI Game (Mock version)
from story_generator import continue_story

print("🧙 Welcome to AI Dungeon!")
story = input("Start your story: ")
while True:
    story = continue_story(story)
    print("\n" + story)
    user = input("Your next move: ")
    if user.lower() in ['quit', 'exit']:
        break
    story += " " + user
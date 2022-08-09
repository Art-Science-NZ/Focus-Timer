from playsound import playsound

def make_sound(path, n):
    print("Focus Time Over")
    # n is for the number of plays
    for i in list(range(0, n)):
        playsound(path)
    return "Focus Time Over"
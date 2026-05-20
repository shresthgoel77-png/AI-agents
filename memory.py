class MemoryAgent:
    def __init__(self):
        self.memory = []

    def store(self, city, weather_info):
        self.memory.append({"city": city, "weather": weather_info})

    def recall(self):
        return self.memory


import random
from datetime import datetime

class Patient:
    def __init__(self, name):
        self.name = name
        self.med_taken = []
        self.appointments = []

    def take_medicine(self):
        self.med_taken.append(datetime.now())

    def miss_medicine(self):
        pass

    def attend_appointment(self):
        self.appointments.append(datetime.now())

class AdherenceMonitor:
    def __init__(self, patient):
        self.patient = patient

    def check_adherence(self):
        if len(self.patient.med_taken) == 0:
            return "LOW"
        elif len(self.patient.med_taken) < 3:
            return "MEDIUM"
        else:
            return "HIGH"

class InterventionEngine:
    def generate(self, adherence_level):
        if adherence_level == "LOW":
            return "Send urgent reminder + Notify doctor"
        elif adherence_level == "MEDIUM":
            return "Send daily reminder"
        else:
            return "Send appreciation message"

if __name__ == "__main__":
    p = Patient("John")
    monitor = AdherenceMonitor(p)
    engine = InterventionEngine()

    # Simulate behavior
    if random.choice([True, False]):
        p.take_medicine()

    level = monitor.check_adherence()
    action = engine.generate(level)

    print("Adherence Level:", level)
    print("Recommended Action:", action)

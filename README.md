# Monitor-Patient
Tracking: It monitors patient data and classifies their health risk levels.Alerts
Patient Adherence Monitoring System

Description:
This project is a simple system to monitor patient adherence to medication and appointments.
It also generates intervention strategies based on adherence levels.

Features:
- Tracks whether a patient takes medicine
- Tracks appointment attendance
- Evaluates adherence level (Low, Medium, High)
- Suggests intervention strategies

System Components:
1. Patient Class
   - Stores patient name
   - Tracks medication intake
   - Tracks appointments

2. AdherenceMonitor Class
   - Checks patient adherence based on activity

3. InterventionEngine Class
   - Generates actions based on adherence level

How It Works:
- The system simulates whether a patient takes medicine
- Based on the data, it calculates adherence level
- It then suggests appropriate actions

Adherence Levels:
- LOW: No medicine taken → Urgent reminder + notify doctor
- MEDIUM: Some adherence → Daily reminder
- HIGH: Good adherence → Appreciation message

How to Run:
1. Install Python (if not installed)
2. Open terminal/command prompt
3. Navigate to project folder
4. Run the program:

   python main.py

Sample Output:
Adherence Level: LOW
Recommended Action: Send urgent reminder + Notify doctor

Future Improvements:
- Add database (MySQL / Firebase)
- Build web or mobile interface
- Add real patient data tracking
- Use AI for prediction

Author:
Sanjai Deva

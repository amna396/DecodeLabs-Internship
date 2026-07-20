import tkinter as tk
from tkinter import scrolledtext

def chatbot_response(user):
    user = user.lower().strip()
    if user in ["hi", "hello", "hey"]:
        return (
            "Hello! Welcome to the UET Lahore Admission Fall 2026 Chatbot.\n\n"
            "Ask me anything about UET Lahore Admissions Fall 2026."
        )

    elif ("admission" in user and "criteria" in user) or "eligibility" in user or "requirements" in user:
        return (
            "To secure admission to UET Lahore for Fall 2026:\n\n"
            "1. Have at least 60% marks in Intermediate for Engineering and Computing programs.\n"
            "2. Appear in ECAT.\n"
            "3. Meet the required merit.\n"
            "4. Submit the online application."
        )

    elif "engineering" in user and "program" in user:
        return (
            "Engineering Programs:\n\n"
            "1. Architectural Engineering\n"
            "2. Automotive Engineering\n"
            "3. Chemical Engineering\n"
            "4. Civil Engineering\n"
            "5. Computer Engineering\n"
            "6. Electrical Engineering\n"
            "7. Environmental Engineering\n"
            "8. Geological Engineering\n"
            "9. Industrial & Manufacturing Engineering\n"
            "10. Mechanical Engineering\n"
            "11. Mechatronics & Control Engineering\n"
            "12. Metallurgical & Materials Engineering\n"
            "13. Mining Engineering\n"
            "14. Petroleum & Gas Engineering\n"
            "15. Polymer Engineering\n"
            "16. Transportation Engineering"
        )

    elif "computing" in user and "program" in user:
        return (
            "Computing Programs:\n\n"
            "1. Artificial Intelligence\n"
            "2. Business Data Analytics\n"
            "3. Computer Science\n"
            "4. Cyber Security\n"
            "5. Data Science\n"
            "6. Robotics and Intelligent Systems\n"
            "7. Software Engineering"
        )
    
    elif ("business" in user or "science" in user) and "program" in user:
        return (
            "Business & Science Programs:\n\n"
            "1. Business Administration\n"
            "2. Business Analytics\n"
            "3. Business Information Technology\n"
            "4. English Language and Literature\n"
            "5. Interior Design\n"
            "6. Islamic Studies (Specialization in Computer Technology)\n"
            "7. Logistics and Supply Chain Management\n"
            "8. Materials Science\n"
            "9. Mathematics\n"
            "10. Physics\n"
            "11. Remote Sensing and GIS\n"
            "12. Chemistry\n"
            "13. Environmental Science\n"
            "14. Industrial Chemistry\n"
            "15. Architecture"
        )

    elif "merit" in user:
        return (
            "For ECAT Programs:\n\n"
            "17% Matric\n"
            "50% Intermediate Part-I\n"
            "33% ECAT Score\n\n"
            "Formula:\n"
            "(Matric Obtained / Matric Total × 17)"
            " + "
            "(FSc Part-I Obtained / Total × 50)"
            " + "
            "(ECAT Score / 400 × 33)\n\n"
            "For Non-ECAT programs:\n"
            "25% Matric + 75% Intermediate Part-I"
        )

    elif "fee" in user or "fees" in user or "tuition" in user:
        return (
            "Semester-wise Fee Structure\n\n"
            "1st Admission Fee : Rs.54,050 / Rs.74,040\n"
            "1st Tuition Fee : Rs.56,290 / Rs.85,250\n"
            "2nd Semester : Rs.72,260 / Rs.113,040\n"
            "3rd Semester : Rs.79,020 / Rs.122,080\n"
            "4th Semester : Rs.79,020 / Rs.122,080\n"
            "5th Semester : Rs.86,580 / Rs.133,400\n"
            "6th Semester : Rs.86,580 / Rs.133,400\n"
            "7th Semester : Rs.95,060 / Rs.146,070\n"
            "8th Semester : Rs.105,060 / Rs.156,070\n\n"
            "Total (8 Semesters)\n"
            "Subsidized : Rs.713,920\n"
            "Partially Subsidized : Rs.1,085,430"
        )
    elif "department" in user:

        return """
    Engineering Departments:
    • Electrical Engineering
    • Civil Engineering
    • Mechanical Engineering
    • Industrial & Manufacturing Engineering
    • Mechatronics & Control Engineering
    • Chemical Engineering
    • Polymer & Process Engineering
    • Metallurgical & Materials Engineering
    • Mining Engineering
    • Geological Engineering
    • Petroleum & Gas Engineering
    • Architectural Engineering & Design
    • Transportation Engineering & Management
    • Institute of Environmental Engineering & Research

    Computing Departments:
    • Computer Science
    • Computer Engineering
    • Institute of Data Science

    Architecture & Design Departments:
    • Architecture
    • Product & Industrial Design
    • City & Regional Planning

    Basic Sciences & Humanities & Business Departments:
    • Physics
    • Chemistry
    • Mathematics
    • Humanities & Social Sciences
    • Islamic Studies
    • Institute of Business & Management
    """
    elif ("non ecat" in user or "non-ecat" in user) and "program" in user:

        return """
    Non-ECAT Programs:
    1. Business Administration
    2. Business Analytics
    3. Business Information Technology
    4. English Language & Literature
    5. Interior Design
    6. Islamic Studies (Specialization in Computer Technology)
    7. Logistics & Supply Chain Management
    8. Materials Science
    9. Mathematics
    10. Physics
    11. Remote Sensing & GIS
    12. Chemistry
    13. Environmental Science
    14. Industrial Chemistry
    """
    elif "ecat" in user and "program" in user:

        return """
    ECAT Programs:
    1. Architectural Engineering
    2. Automotive Engineering
    3. Chemical Engineering
    4. Civil Engineering
    5. Computer Engineering
    6. Electrical Engineering
    7. Environmental Engineering
    8. Geological Engineering
    9. Industrial & Manufacturing Engineering
    10. Mechanical Engineering
    11. Mechatronics & Control Engineering
    12. Metallurgical & Materials Engineering
    13. Mining Engineering
    14. Petroleum & Gas Engineering
    15. Polymer Engineering
    16. Transportation Engineering
    17. Artificial Intelligence
    18. Business Data Analytics
    19. Computer Science
    20. Cyber Security
    21. Data Science
    22. Robotics & Intelligent Systems
    23. Software Engineering
    24. Architecture
    """
    
    elif "how to apply" in user or "application process" in user or "admission guide" in user:

        return """
    How to Apply:
    1. Generate the admission challan from the UET Admission Portal.
    2. Pay the application processing fee.
    3. Fill in the online admission form.
    4. Upload the required information.
    5. Select your preferred degree programs.
    6. Submit the application.
    7. Regularly check your admission portal for updates.
    """
    elif "document"  in user or "documents" in user or "required docuemnts" in user:

        return """
    Required Documents:
    • Original Paid Bank Challan
    • Two sets of photocopies of all educational documents
    • Original Matric / Intermediate Certificates
    • Four Passport Size Photographs
    • Two Copies of CNIC / B-Form
    • Bio-data Form
    • Medical Certificate
    • Income Certificate
    • Undertaking on Rs.100 Judicial Stamp Paper
    """
    elif "category" in user or "admission categories" in user:

        return """
    Admission Categories:
    A1 - Open Merit (Subsidized)
    A1-Med - Open Merit (Pre-Medical)
    A2 - Open Merit (Partially Subsidized)
    A2-Med - Open Merit (Pre-Medical)
    AP - All Pakistan
    B - Sindh
    C - Balochistan
    D - Khyber Pakhtunkhwa
    E1 - Azad Jammu & Kashmir
    E2 - Gilgit Baltistan
    H1 - Foreign Nationals
    H2 - Afghan Nationals
    H3 - Indian Occupied Kashmir
    H4 - Cultural Exchange
    H5 - Sri Lankan Nationals
    J1 - Armed Forces (Junior Ranks)
    J2 - Armed Forces (Officers)
    K - FATA
    L - South, Central & North Punjab
    M - Children of UET Employees
    N - Children of Engineers
    NM - Non-Muslim Quota
    O - Alumni Quota
    P - B.Tech Candidates
    Q - D.G. Khan & Rajanpur Tribal Areas
    R - Layyah & Bhakkar
    S - Overseas Pakistanis
    SF - Self Finance
    T - Disabled Persons
    U1 - Baluchistan FATA
    U2 - FATA
    """
    elif "schedule" in user or "important dates" in user or "timeline" in user:

        return """
    UET Lahore Admission Schedule (Fall 2026):

    Application Phase:
    • Applications Open: 08 June 2026
    • Edit Application: 12–14 July 2026
    • Last Date to Apply: 15 July 2026

    Special Tests:
    • Hafiz-e-Quran Test: 17 July 2026
    • Sports Test: 20 July 2026

    Merit Lists:
    • 1st Merit List: 24 July 2026
    • 2nd Merit List: 07 August 2026
    • 3rd Merit List: 14 August 2026
    • 4th Merit List: 21 August 2026

    Preference Change:
    • 28–30 August 2026

    Updated Merit List:
    • 01 September 2026

    Leftover Candidates:
    • Apply Again: 02–07 September 2026
    • Merit List: 08 September 2026
    • Fee Deadline: 10 September 2026
    • Walk-in Admissions: 11–15 September 2026

    Classes Begin:
    • 12 October 2026
    """
    elif user in ["bye", "quit", "exit"]:
        return "Thank you for using the chatbot.\nBest of luck with your admission!"

    else:
        return "Sorry, I can only answer UET Lahore Admission related questions."

def send_message():
    user = entry.get()
    if user == "":
        return
    response = chatbot_response(user)
    chat.config(state="normal")
    chat.insert(tk.END, "You : " + user + "\n\n")
    chat.insert(tk.END, "Bot : " + response + "\n\n")
    chat.config(state="disabled")
    chat.yview(tk.END)
    entry.delete(0, tk.END)

def clear_chat():
    chat.config(state="normal")
    chat.delete("1.0", tk.END)
    chat.insert(
        tk.END,
           """Bot: Hello! 
        Welcome to the UET Lahore Undergraduate Admission Chatbot (Fall 2026).
        You can ask questions about:
        • Admission Criteria
        • Engineering Programs
        • Computing Programs
        • Business & Science Programs
        • Merit Calculation
        • Fee Structure
        • Departments
        • ECAT Programs
        • Non-ECAT Programs
        • Required Documents
        • Admission Categories
        • Admission Schedule / Important Dates
        • How to Apply""")
    
    chat.config(state="disabled")

window = tk.Tk()
window.title("UET Lahore Admission Chatbot")
window.geometry("850x650")
window.configure(bg="#EAF4FC")
title = tk.Label(
    window,
    text="UET Lahore Admission Chatbot",
    font=("Arial",20,"bold"),
    bg="#0B5394",
    fg="white",
    pady=10
)
title.pack(fill="x")
chat = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    font=("Calibri",12),
    width=90,
    height=25
)
chat.pack(padx=15,pady=15)
chat.insert(
    tk.END,
    """Bot: Hello! 
        Welcome to the UET Lahore Undergraduate Admission Chatbot (Fall 2026).
        You can ask questions about:
        • Admission Criteria
        • Engineering Programs
        • Computing Programs
        • Business & Science Programs
        • Merit Calculation
        • Fee Structure
        • Departments
        • ECAT Programs
        • Non-ECAT Programs
        • Required Documents
        • Admission Categories
        • Admission Schedule / Important Dates
        • How to Apply""")
   

chat.config(state="disabled")
entry = tk.Entry(
    window,
    font=("Calibri",13),
    width=55
)
entry.pack(side=tk.LEFT,padx=15,pady=10)
send = tk.Button(
    window,
    text="Send",
    font=("Arial",12,"bold"),
    bg="#0B5394",
    fg="white",
    command=send_message
)
send.pack(side=tk.LEFT,padx=5)
clear = tk.Button(
    window,
    text="Clear Chat",
    font=("Arial",12,"bold"),
    command=clear_chat
)
clear.pack(side=tk.LEFT,padx=5)
exit_btn = tk.Button(
    window,
    text="Exit",
    font=("Arial",12,"bold"),
    bg="red",
    fg="white",
    command=window.destroy
)
exit_btn.pack(side=tk.LEFT,padx=5)
entry.bind("<Return>", lambda event: send_message())
window.mainloop()
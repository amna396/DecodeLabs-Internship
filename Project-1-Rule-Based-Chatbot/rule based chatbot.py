print("I'm a UET Lahore Undergraduate Admission Fall 2026 Chatbot")
print("Ask me question about:")
print("- Admission Criteria")
print("- Merit Calculation")
print("- Fee Structure")
print("- Engineering Programs")
print("- Computing Programs")
print("- Business or Science Programs")
print("- ECAT Programs")
print("- Non-ECAT Programs")
print("- Departments")
print("- Required Documents")
print("- How to Apply")
print("- Admission Categories")
print("- Important Dates")

while True:
    user=input("You:").lower()
    if user in ["hi" , "hello" , "hey"]:
      print("Bot:Hello! Welcome to the UET Lahore Admission Fall 2026 Chatbot.")
      print(" Ask me anything about UET Lahore Admissions Fall 2026.")

    elif ("admission" in user and  "criteria" in user) or "eligibility" in user or "requirements" in user:
        print("Bot: To secure admission to UET Lahore for Fall 2026, you must:")
        print("1. Have at least 60% marks in Intermediate for Engineering and Computing programs.")
        print("2. Appear in ECAT.")
        print("3. Meet the required merit.")
        print("4. Submit the online application.") 
      
    elif "engineering" in user and "program" in user :
        print("Bot:")
        print("1.Architectural Engineering")
        print("2.Automotive Engineering")
        print("3.Chemical Engineering")
        print("4.Civil Engineering")
        print("5.Computer Engineering")
        print("6.Electrical Engineering")
        print("7.Environmental Engineering")
        print("8.Geological Engineering")
        print("9.Industrial and Manufacturing Engineering")
        print("10.Mechanical Engineering")
        print("11.Mechatronics and Control Engineering") 
        print("12.Metallurgical and Materials Engineering")         
        print("13.Mining Engineering")
        print("14.Petroleum and Gas Engineering")
        print("15.Polymer Engineering")
        print("16.Transportation Engineering")

    elif "computing" in user and "program" in user:
        print("Bot:")
        print("1.Artificial Intelligence")
        print("2.Business Data Analytics")
        print("3.Computer Science") 
        print("4.Cyber Security")
        print("5.Data Science")
        print("6.Robotics and Intelligent Systems")
        print("7.Software Engineering")

    elif ("business" in user or "science" in user) and "program" in user :
        print("Bot:")
        print("1.Business Administration")
        print("2.Business Analytics")
        print("3.Business Information Technology")
        print("4.English Language and Literature")
        print("5.Interior Design")
        print("6.Islamic Studies (Specialization in Computer Technology)")
        print("7.Logistics and Supply Chain Management" ) 
        print("8.Materials Science")
        print("9.Mathematics (with mandatory Mathematics; with specialization in AI, Data Science, and IT)")
        print("10.Physics")
        print("11.Remote Sensing and GIS")
        print("12.Chemistry")
        print("13.Environmental Science")
        print("14.Industrial Chemistry")
        print("15.Architecture")

    elif "merit calculation" in user:
        print("Bot: For Ecat Programs : 17% Matric, 50% Intermediate (Part I), 33% Ecat score.")
        print("The merit formula is:") 
        print("Aggregate = (Matric Obtained/Matric Total x 17 )+ (FSc Part I Obtained / Part I Total x 50) + (ECAT Score/400x 33)")
        print("For non-ECAT programs: The merit will be determined by the results in the matric and first-year intermediate (or equivalent) examinations with 25% and 75% weights, respectively")
    
    elif "departments" in user:
        print("Bot:")
        print('''Engineering Departments:
                Electrical Engineering
                Civil Engineering
                Mechanical Engineering
                Industrial & Manufacturing Engineering
                Mechatronics & Control Engineering
                Chemical Engineering
                Chemical Engineering
                Polymer & Process Engineering
                Metallurgical & Materials Engineering
                Mining Engineering
                Geological Engineering
                Petroleum and Gas Engineering
                Architectural Engineering & Design
                Transportation Engineering & Management
                Institute of Environmental Engineering & Research''')
        print('''Computing Departments:
                 Computer Science
                 Computer Engineering
                 Institute of Data Science''')
        print('''Architecture & Design Departments:
                 Architecture
                 Product & Industrial Design
                 City & Regional Planning''')
        print('''Basic Sciences & Humanities Departments:
                 Physics
                 Chemistry
                 Mathematics
                 Humanities & Social Sciences
                 Islamic Studies
                 Institute of Business and Management''')
    elif "fees" in user or "fee structure" in user or "tuition fee" in user:
        print("Bot:")   
        print("\nSemester-wise Total Fee (Subsidized / Partially Subsidized)")
        print("------------------------------------------------------------")
        print("1st (Admission Fee): Rs. 54,050 / Rs. 74,040")
        print("1st (Tuition Fee):  Rs. 56,290 / Rs. 85,250")
        print("2nd Semester:       Rs. 72,260 / Rs. 113,040")
        print("3rd Semester:       Rs. 79,020 / Rs. 122,080")
        print("4th Semester:       Rs. 79,020 / Rs. 122,080")
        print("5th Semester:       Rs. 86,580 / Rs. 133,400")
        print("6th Semester:       Rs. 86,580 / Rs. 133,400")
        print("7th Semester:       Rs. 95,060 / Rs. 146,070")
        print("8th Semester:       Rs. 105,060 / Rs. 156,070")
        print("Total (8 Semesters): Rs. 713,920 / Rs. 1,085,430")
        print("9th Semester:       Rs. 104,550 / Rs. 160,260")
        print("10th Semester:      Rs. 104,550 / Rs. 160,260")
        print("Total (10 Semesters): Rs. 923,020 / Rs. 1,405,950")
    
    elif "ecat" in user and "programs" in user:
        print("Bot: Ecat Programs are:")
        print("1.Architectural Engineering")
        print("2.Automotive Engineering")
        print("3.Chemical Engineering")
        print("4.Civil Engineering")
        print("5.Computer Engineering")
        print("6.Electrical Engineering")
        print("7.Environmental Engineering")
        print("8.Geological Engineering")
        print("9.Industrial and Manufacturing Engineering")
        print("10.Mechanical Engineering")
        print("11.Mechatronics and Control Engineering") 
        print("12.Metallurgical and Materials Engineering")         
        print("13.Mining Engineering")
        print("14.Petroleum and Gas Engineering")
        print("15.Polymer Engineering")
        print("16.Transportation Engineering")
        print("17.Artificial Intelligence")
        print("18.Business Data Analytics")
        print("19.Computer Science") 
        print("20.Cyber Security")
        print("21.Data Science")
        print("22.Robotics and Intelligent Systems")
        print("23.Software Engineering")
        print("24.Architecture")

    elif ("non ecat" in user or "non-ecat" in user) and "program" in user:
        print("Bot:")
        print("1.Business Administration")
        print("2.Business Analytics")
        print("3.Business Information Technology")
        print("4.English Language and Literature")
        print("5.Interior Design")
        print("6.Islamic Studies (Specialization in Computer Technology)")
        print("7.Logistics and Supply Chain Management" ) 
        print("8.Materials Science")
        print("9.Mathematics (with mandatory Mathematics; with specialization in AI, Data Science, and IT)")
        print("10.Physics")
        print("11.Remote Sensing and GIS")
        print("12.Chemistry")
        print("13.Environmental Science")
        print("14.Industrial Chemistry")

    elif "how to apply" in user or "admission guide" in user:
        print("Bot:")
        print("Generate Challan: Visit the UET Admissions Account portal, enter your CNIC, name, and phone number to create your fee challan")
        print("Pay Fee: Pay the required application processing fee at any branch of the designated bank")
        print("Submit Application: Once payment is verified, log back into the UET Admissions Portal to fill out the application form, enter your educational details, and select your preferred degree programs")
        print("Track Application: Regularly check your portal account's Application Status. If your application is rejected due to any missing details, you will have 2 days to correct the deficiencies")

    elif "documents" in user or "documents for admission" in user:
        print('''Bot: Following documents are required for selected candidates in any of the merit list to secure admission: 
              1.Paid Original Bank Challan as proof of payment of dues. Online payment facility is available through Habib Bank Limited (HBL) internet banking/ Mobile application, HBL Konnect and ATMs. Candidate must keep photocopies of this challan/ proof of payment for his/her own record and for submission to the department.
              2.Two set of photocopies of each educational document including domicile.
              3.Original applicable certificates and degree, like Matric/”O”-Level, Intermediate./ “A”-Level, Diploma of Associate Engineer (DAE), B.Sc. Engineering Technology or any equivalent qualifications.
              4.Four copies of the most recent passport size photograph
              5.Two copies of CNIC/ “B” Form.
              6.Bio-data card Form-I duly completed in all respects.
              7.Medical Certificate Form-II duly signed and stamped by Medical Practitioner registered with PMC.
              8.Duly attested Current Income certificate of the parent/ guardian.
              9.Undertaking (Sample Form -VII) on a Rs. 100/- judicial paper duly completed.''')
        print('''IMPORTANT NOTE :
              Admissions are granted on merit and according to preferences given by the applicants.
               An applicant who secures admission in a discipline of his lower preference and he desires
               to be considered in next merit lists, must submit all the dues and documents.
              If he fails to do so, his name would be excluded from any future merit lists and his admission would be cancelled.''')
        
    elif "categories" in user or "application categories" in user:
        print("Bot: UET Lahore Admission Categories")
        print("A1  - Open Merit (Subsidized Seats)")
        print("A1-Med - Open Merit for Pre-Medical Students (Subsidized)")
        print("A2  - Open Merit (Partially Subsidized Seats)")
        print("A2-Med - Open Merit for Pre-Medical Students (Partially Subsidized)")
        print("AP  - All Pakistan Seats")
        print("B   - Sindh Quota")
        print("C   - Balochistan Quota")
        print("D   - Khyber Pakhtunkhwa (KPK) Quota")
        print("E1  - Azad Jammu & Kashmir Quota")
        print("E1 (Lipa Valley) - Reserved Seat for Lipa Valley")
        print("E2  - Gilgit-Baltistan (Northern Areas) Quota")
        print("H1  - Foreign Nationals")
        print("H2  - Afghan Nationals")
        print("H3  - Indian Occupied Jammu & Kashmir")
        print("H4  - Cultural Exchange Students")
        print("H5  - Sri Lankan Nationals")
        print("J1  - Armed Forces (Junior Ranks)")
        print("J2  - Armed Forces (Officer Quota)")
        print("K   - FATA Quota")
        print("L   - South, Central & North Punjab Quota")
        print("M   - Children of UET Employees")
        print("N   - Children of Engineers")
        print("NM  - Non-Muslim Minority Quota")
        print("O   - Alumni Quota")
        print("P   - B.Tech. Candidates")
        print("Q   - D.G. Khan & Rajanpur Tribal Areas")
        print("R   - Layyah & Bhakkar Districts")
        print("S   - Overseas Pakistanis")
        print("SF  - Self Finance (Foreign/Dual Nationals)")
        print("T   - Disabled Persons Quota")
        print("U1  - Baluchistan FATA Areas")
        print("U2  - FATA Areas")
        
    elif "schedule" in user or "timeline" in user or "important dates" in user or "admission dates" in user:
        print("Bot: UET Lahore Undergraduate Admission Schedule (Fall 2026)\n")
        print("Application Phase")
        print("• Online applications open: 08 June 2026")
        print("• Edit application request: 12 - 14 July 2026")
        print("• Last date to apply: 15 July 2026\n")
        print("Special Tests")
        print("• Hafiz-e-Quran Test: 17 July 2026 (10:00 AM)")
        print("• Sports Test: 20 July 2026 (10:00 AM)\n")
        print("Merit Lists")
        print("• 1st Merit List: 24 July 2026")
        print("• 2nd Merit List: 07 August 2026")
        print("• 3rd Merit List: 14 August 2026")
        print("• 4th Merit List: 21 August 2026\n")
        print("Preference Change")
        print("• Change of Preference: 28 - 30 August 2026")
        print("• Updated Merit List: 01 September 2026\n")
        print(" Leftover / Non-Selected Candidates ")
        print("• New Applications: 02 - 07 September 2026")
        print("• Merit List: 08 September 2026")
        print("• Last Date for Fee/Documents: 10 September 2026")
        print("• Walk-in Admissions: 11 - 15 September 2026")
        print("• Subsequent Merit Lists: Every Friday (subject to seat availability)\n")
        print("Final Steps ")
        print("• Registration & Orientation: 22 September 2026")
        print("• Hostel Allotment: 05 October 2026")
        print("• Classes Begin: 12 October 2026")

    elif user in ["bye", "exit", "ok", "quit"]:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I can only answer UET admission questions.")    


        



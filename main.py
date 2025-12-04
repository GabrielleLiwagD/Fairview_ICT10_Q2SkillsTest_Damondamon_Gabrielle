from pyscript import display, document
def select_club(e):
    selected = document.getElementById("club_select").value
    clubs = {"science": {"Club Name" : "Science Club", 
                         "Meeting Days": "Tuesday at 3 - 4 PM; Friday at 2 - 3 PM)", 
                         "Moderator" : "Ms. Jameelyn Maramag",
                         "Location": "Room 404",
                         "No. of Members": "18",},
             "CAC": {"Club Name" : selected,
                     "Meeting Days": "Wednesday and Friday at 3 - 4 PM",
                     "Moderator" : "Ms. Yannis Fernandez",
                     "Location": "Room 406",
                     "No. of Members": "23"},
            "math" : {"Club Name" : selected, 
                      "Meeting Days": "Mondays at 2:30 - 4:30 PM", 
                      "Mooderator" : "Mr. Nichol Gabriel B. Gabuya",
                      "Location": "Room 404",
                      "No. of Members": "16"},
            "marching band" : {"Club Name" : selected, 
                               "Meeting Days": "Monday, Tuesday, and Wednesday at 3 - 4 PM",
                               "Mooderator": "Mr. Emilio Alumno",
                               "Location" : "Marching Band Room",
                               "No. of Members": "42"},
            "COCC" : {"Club Name" : selected,
                      "Meeting Days": "Wednesday at 2:30 - 4:30 PM",
                      "Moderator" : "Ssgt. Jermima David, PA (Res)",
                      "Location": "Quandrangle/Theatro Preciosa (4th Floor)",
                      "No. of Members": "N/A"},
            "basketball" : {"Club Name" : selected,
                           "Meeting Days": "Monday at 3 - 5 PM",
                           "Coach" : "Mr. Adrain Ruiz",
                           "Location": "Quandrangle",
                           "No. of Members": "16"},
            "volleyball" : {"Club Name" : selected,
                            "Meeting Days" : "Wenesday at 3 - 4 PM",
                            "Coach" : "Mr. Adrain Ruiz",
                            "Location" : "Quandrangle",
                            "No. of Members": "23"},
            "social studies club" : {"Club Name" : selected,
                                     "Meeting Days": "Tuesday and Thursday at 3 - 4 PM",
                                     "Moderator" : "Mr. Roberto Lim",
                                     "Location": "Room 409",
                                     "No. of Members": "21"},
            "glee club" : {"Club Name" : selected,
                           "Meeting Days": "Monday and Friday at 3 - 4 PM",
                           "Moderator" : "Mr. Denver Martin",
                           "Location": "HS Music Room",
                           "No. of Members": "28"}}
        
    if selected == "Science Club": 
        display(selected, target="output2") #This will display the science club info
        display(f"Meeting Days: {clubs['science']['Meeting Days']}", target="output2")
        display(f"Moderator: {clubs['science']['Moderator']}", target="output2")
        display(f"Location: {clubs['science']['Location']}", target="output2")
        display(f"No. of Members: {clubs['science']['No. of Members']}", target="output2")
    elif selected == "CAC Club": 
        display(selected, target="output2") #This will display the CAC info
        display(f"Meeting Days: {clubs['CAC']['Meeting Days']}", target="output2")
        display(f"Moderator: {clubs['CAC']['Moderator']}", target="output2")
        display(f"Location: {clubs['CAC']['Location']}", target="output2")
        display(f"No. of Members: {clubs['CAC']['No. of Members']}", target="output2")
    elif selected == "Math Guild": 
        display(selected, target="output2") #This will display the math club info
        display(f"Meeting Days: {clubs['math']['Meeting Days']}", target="output2")
        display(f"Moderator: {clubs['math']['Mooderator']}", target="output2")
        display(f"Location: {clubs['math']['Location']}", target="output2")
        display(f"No. of Members: {clubs['math']['No. of Members']}", target="output2")
    elif selected == "Marching Band": 
        display(selected, target="output2") #This will display the marching band info
        display(f"Meeting Days: {clubs['marching band']['Meeting Days']}", target="output2")
        display(f"Moderator: {clubs['marching band']['Mooderator']}", target="output2")
        display(f"Location: {clubs['marching band']['Location']}", target="output2")
        display(f"No. of Members: {clubs['marching band']['No. of Members']}", target="output2")
    elif selected == "COCC Club": 
        display(selected, target="output2") #This will display the COCC info
        display(f"Meeting Days: {clubs['COCC']['Meeting Days']}", target="output2")
        display(f"Moderator: {clubs['COCC']['Moderator']}", target="output2")
        display(f"Location: {clubs['COCC']['Location']}", target="output2")
        display(f"No. of Members: {clubs['COCC']['No. of Members']}", target="output2")
    elif selected == "Basketball Club": 
        display(selected, target="output2") #This will display the basketball info
        display(f"Meeting Days: {clubs['basketball']['Meeting Days']}", target="output2")
        display(f"Coach: {clubs['basketball']['Coach']}", target="output2")
        display(f"Location: {clubs['basketball']['Location']}", target="output2")
        display(f"No. of Members: {clubs['basketball']['No. of Members']}", target="output2")
    elif selected == "Volleyball": 
        display(selected, target="output2") #This will display the volleyball info
        display(f"Meeting Days: {clubs['volleyball']['Meeting Days']}", target="output2")
        display(f"Coach: {clubs['volleyball']['Coach']}", target="output2")
        display(f"Location: {clubs['volleyball']['Location']}", target="output2")
        display(f"No. of Members: {clubs['volleyball']['No. of Members']}", target="output2")
    elif selected == "Social Studies Club": 
        display(selected, target="output2") #This will display the social studies club info
        display(f"Meeting Days: {clubs['social studies club']['Meeting Days']}", target="output2")
        display(f"Moderator: {clubs['social studies club']['Moderator']}", target="output2")
        display(f"Location: {clubs['social studies club']['Location']}", target="output2")
        display(f"No. of Members: {clubs['social studies club']['No. of Members']}", target="output2")
    elif selected == "Glee Club": 
        display(selected, target="output2") #This will display the glee club info
        display(f"Meeting Days: {clubs['glee club']['Meeting Days']}", target="output2")
        display(f"Moderator: {clubs['glee club']['Moderator']}", target="output2")
        display(f"Location: {clubs['glee club']['Location']}", target="output2")
        display(f"No. of Members: {clubs['glee club']['No. of Members']}", target="output2")
    else: 
        display("Please select a valid club.", target="output2") #This will display if no valid option is selected

# def show_info(e=None):
#     selected = document.getElementById("club_select").value
#     science1 = {"Club Name" : selected, "Description": "The Science Club explores various scientific concepts and conducts experiments.", "Meeting_Time": "Wednesdays at 3 PM", "Advisor/Coach" : "Mr. Jordan Tazewell","Location": "Room 130","Category": "Academic"}
#     math1 = {"Club Name" : selected, "Description": "The Math Club engages in problem-solving activities and math competitions.", "Meeting_Time": "Mondays at 2:30 - 4:30 PM", "Advisor/Coach" : "Mr. Nichol Gabriel B. Gabuya","Location": "Room 404","Category": "Academic"}
#     art1 = {"Club Name" : selected, "Description": "The Art Club encourages creativity through various art projects and exhibitions.","Meeting_Time": "Tuesdays at 2 PM", "Advisor/Coach" : "Ms. Sarah Lee","Location": "Art Room","Category": "Non-Academic"}
#     sports1 = {"Club Name" : selected, "Description": "The Sports Club promotes physical fitness and organizes sports events.", "Meeting_Time": "Fridays at 5 PM" ,"Advisor/Coach" : "Mr. Mike Johnson","Location": "Gymnasium" ,"Category": "Non-Academic"}

#     if selected == "Science Club": 
#         display(science1["Club Name"], target="output2") #This will display the science club info
#         display(f"Description: {science1['Description']}", target="output2")
#         display(f"Meeting Time: {science1['Meeting_Time']}", target="output2")
#         display(f"Advisor/Coach: {science1['Advisor/Coach']}", target="output2")
#         display(f"Location: {science1['Location']}", target="output2")
#         display(f"Category: {science1['Category']}", target="output2")
#     elif selected == "Math Club": 
#         display(math1["Club Name"], target="output2") #This will display the math club info
#         display(f"Description: {math1['Description']}", target="output2")
#         display(f"Meeting Time: {math1['Meeting_Time']}", target="output2")
#         display(f"Advisor/Coach: {math1['Advisor/Coach']}", target="output2")
#         display(f"Location: {math1['Location']}", target="output2")
#         display(f"Category: {math1['Category']}", target="output2")
#     elif selected == "Art Club": 
#         display(art1["Club Name"], target="output2") #This will display the art club info
#         display(f"Description: {art1['Description']}", target="output2")
#         display(f"Meeting Time: {art1['Meeting_Time']}", target="output2")
#         display(f"Advisor/Coach: {art1['Advisor/Coach']}", target="output2")
#         display(f"Location: {art1['Location']}", target="output2")
#         display(f"Category: {art1['Category']}", target="output2")
#     elif selected == "Sports Club": 
#         display(sports1["Club Name"], target="output2") #This will display the sports club info
#         display(f"Description: {sports1['Description']}", target="output2")
#         isplay(f"Meeting Time: {sports1['Meeting_Time']}", target="output2")
#         display(f"Advisor/Coach: {sports1['Advisor/Coach']}", target="output2")
#         display(f"Location: {sports1['Location']}", target="output2")
#         display(f"Category: {sports1['Category']}", target="output2")
#     else: 
#         display("Please select a valid club.", target="output2") #This will display if no valid option is selected
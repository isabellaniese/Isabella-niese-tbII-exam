import tkinter as tk
import pygame as pg
from PIL import Image, ImageTk
from src.extras import clear_page, health, water, start_watering, stop_progress

#Create a window and give it a title
root = tk.Tk()
root.title("PlantyPoppins")
#Set configuration
root.geometry("750x500")

# Function to load an image
def load_image(image_path, size):
    img = Image.open(image_path)
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

#Definition for the Welcome Page
def homepage(root, image_file_path):
    clear_page(root)

    #Load the image
    homepage_image = load_image("Images/Homepage.jpg", (750, 500))
    homepage_label = tk.Label(root, image=homepage_image)
    homepage_label.image = homepage_image  #Keep a reference to the image
    homepage_label.pack()

    #Create the button that leads to the "All my plants" Page
    plants_button = tk.Button(root,
                              text="All my plants",
                              font="Arial 38 bold",
                              command=plants)
    plants_button.place(x=50,y=250)

    #Create the button that leads to the "My next plant" Page - The test
    test_button = tk.Button(text= "My next plant",
                            font="Arial 38 bold",
                            command=test)
    test_button.place(x=50,y=325)
 
    #Create the button that leads to the "My groceries" Page
    list_button = tk.Button(text= "My groceries",
                            font="Arial 38 bold",
                            command=list_side)
    list_button.place(x=50,y=400)

#Definition for the plants page
def plants():

    #Clear all existing widgets (Definition is in "extras.py")
    clear_page(root)

    #Load the image
    plants_image = load_image("Images/Plants.jpg", (750, 500))
    plants_label = tk.Label(root, image=plants_image)
    plants_label.image = plants_image  #Keep a reference to the image
    plants_label.pack()

    #Buttons for the left plant (Ernie)
    check_health_button = tk.Button(root,
                            text="Check health",
                            font=("Arial 28 bold"),
                            command=lambda:health(root)
                            )
    check_health_button.place(x=100, y=200)

    water_button = tk.Button(root,
                            text="Water plant",
                            font=("Arial 28 bold"),
                            command=lambda:water(root)
                            )
    water_button.place(x=100,y=250)

    #Buttons for the left plant (Bert)
    #Button to check the health
    check_health_button = tk.Button(root,
                            text="Check health",
                            font=("Arial 28 bold"),
                            command=lambda:health(root)
                            )
    check_health_button.place(x=400, y=200)

    #Button to press while watering the plant in real life
    water_button = tk.Button(root,
                            text="Water plant",
                            font=("Arial 28 bold"),
                            command=lambda:water(root)
                             )
    water_button.place(x=400,y=250)

    #Homepage Button that will lead back to Welcome Page
    homepage_button = tk.Button(root,
                            text="Homepage",
                            font=("Arial 14 bold"),
                            command=lambda: homepage(root, image_file_path="Images/Homepage.jpeg")
                            )
    homepage_button.place(x=325,y=450)

#Definition for the test page
def test():
    global show_option_time
    #Clear all existing widgets
    clear_page(root)

    #Load the image
    test_image = load_image("Images/Test.jpg", (750, 500))
    test_label = tk.Label(root, image=test_image)
    test_label.image = test_image  #Keep a reference to the image
    test_label.pack()

    #Create a label to introduce the user to the test
    entertest_label = tk.Label(root,
                                text="Which plant fits you best?",
                                font="Arial 35 bold",
                                bg="#C2DBD7")
    entertest_label.place(x=150, y=100)

    #Button to start the test
    entertest_button = tk.Button(root,
                                 text="Start the test",
                                 font="Arial 22 bold",
                                 fg="black",
                                 command=show_options_time)
    entertest_button.place(x=280, y=320)

    # Homepage Button that will lead back to Welcome Page
    homepage_button = tk.Button(root,
                                text="Bring me back",
                                font=("Arial 14 bold"),
                                command=lambda: homepage(root, image_file_path="Images/Homepage.jpeg")
                                )
    homepage_button.place(x=325,y=450)

#Definiton for the first Test Question
def show_options_time():
    #Clear the page and set new background
    clear_page(root)
    root.configure(bg="#F2B1BC")

    #Create a question label: Time and Motivation
    question_label = tk.Label(root,
                              text="How much time and motivation do you have to care for your plants?",
                              font="Arial 22 bold",
                              bg="#F2B1BC")
    question_label.place(x=16, y=160)

    #Create buttons with two different answers
    no_time = tk.Button(text="I like looking at my plants more than caring for them",
                        font="Arial 18 bold",
                        height=2,
                        width=60,
                        command=lambda: show_options_cooking("no_time"))
    no_time.place(x=38, y=325)

    yes_time = tk.Button(text="I loving dedicating my time to my plants",
                         font="Arial 18 bold",
                         height=2,
                         width=60,
                         command=lambda: show_options_cooking("yes_time"))
    yes_time.place(x=38, y=385)

#Definition for the second Test Question
def show_options_cooking(choice1):

    #Clear the page and set new background
    clear_page(root)
    root.configure(bg="#F3CC91")
    #print(choice1)

    #If-Else Statement to react on the User's previous answer
    if choice1 == "no_time":
        choice_label = " that's okay, not everyone has much time..."
    elif choice1 == "yes_time":
        choice_label = " how nice that you have so much time!"

    #Label that shows reaction to the User's previous answer
    choice_label = tk.Label(root,
                            text=f"💬 Oh,{choice_label}",
                            font="Arial 22 bold",
                            height=2,
                            width=53,
                            bg="#F3CC91")
    choice_label.place(x=25, y=125)

    #Create a question label: Cooking
    question_label = tk.Label(root,
                              text="Do you want to integrate your plants in your cooking? 🥗🍽️🥬",
                              font="Arial 22 bold",
                              bg="#F3CC91")
    question_label.place(x=38, y=175)

    #Create buttons with two different answers
    yes_cooking = tk.Button(text="I would love to have plants that I can also eat",
                            font="Arial 18 bold",
                            height=2,
                            width=60,
                            command=lambda: show_result(choice1, "yes_cooking"))
    yes_cooking.place(x=38, y=325)

    no_cooking = tk.Button(text="No, I don't need to eat my plants",
                           font="Arial 18 bold",
                           height=2,
                           width=60,
                           command=lambda: show_result(choice1, "no_cooking"))
    no_cooking.place(x=38, y=385)

#Definition for the Test Result
def show_result(choice1, choice2):
    #Clear all existing widgets
    clear_page(root)

    #print(choice1)
    #print(choice2)

    #If-Else Statement to react to the User's given answer
    if choice2 == "yes_cooking":
        choice_label = " yummy, what a lovely answer..."
    elif choice2 == "no_cooking":
        choice_label = " plants are to be seen, not to be eaten!"

    #Label that shows reaction to the User's given answer
    result_label = tk.Label(root,
                            text=f"💬 Hmm,{choice_label}",
                            font="Arial 18 bold",
                            bg="#EEE6CF")
    result_label.place(x=300, y=95)

    #Second Label to raise attention for the upcoming result
    result_label_second = tk.Label(root,
                                   text="I already have an idea poppin' up in my head",
                                   font="Arial 18 bold",
                                   bg="#EEE6CF")
    result_label_second.place(x=300, y=125)

    #Create button that leads to the Result
    show_result_button = tk.Button(root,
                                   text="Show Result",
                                   font="Arial 28 bold",
                                   command=lambda: plant(choice1, choice2))
    show_result_button.place(x=300, y=300)

    #Load and place the image of Mary Poppins
    image = load_image("Images/test_mary.png", (246, 462))  #Resize the image to fit
    image_label = tk.Label(root, image=image, bg="#EEE6CF")
    image_label.image = image  #Keep a reference to the image
    image_label.place(x=10, y=5)  #Position at (0,5)
    #Set a new background
    root.configure(bg="#EEE6CF")

#Definition for the test result
def plant(choice1, choice2):
    #Clear all existing widgets
    clear_page(root)

    #If-Else Statement to find the perfect plant tailored to the User's interest
    if choice1 == "no_time" and choice2 == "yes_cooking":
        coriander()
    elif choice1 == "no_time" and choice2 == "no_cooking":
        fiddle_fig()
    elif choice1 == "yes_time" and choice2 == "no_cooking":
        kentiapalm()
    elif choice1 == "yes_time" and choice2 == "yes_cooking":
        ginger()

    #Homepage Button that will lead back to Welcome Page
    homepage_button = tk.Button(root,
                                text="Homepage",
                                font=("Arial 14 bold"),
                                command=lambda: homepage(root, image_file_path="Images/Homepage.jpeg")
                                )
    homepage_button.place(x=325,y=450)

#Definition for the first option: Coriander
def coriander():

    #Load and place the image on the right side
    image = load_image("Images/vietcoriander.jpeg", (300, 300))  #Resize the image to fit
    image_label = tk.Label(root, image=image, bg="black")
    image_label.image = image  #Keep a reference to the image
    image_label.place(x=440, y=150)  #Position at (440, 150)
    #Set a new background
    root.configure(bg="#BFE2CB")

    #Result label that presents the plant
    result_label = tk.Label(root,
                            text="Vietnamese Coriander it is!",
                            font="Arial 48 bold",
                            bg="#BFE2CB")
    result_label.place(x=15, y=50)

    #Labels with information about the plant
    info_label = tk.Label(root,
                          text="🌿 The tropical plant is mainly used for cooking",
                          font="Arial 18 bold",
                          bg="#BFE2CB")
    info_label.place(x=15, y=200)

    place_label = tk.Label(root,
                           text="🏠 Place: Sunny & humid! Maybe a balcony?",
                           font="Arial 18 bold",
                           bg="#BFE2CB")
    place_label.place(x=15, y=266)

    care_label = tk.Label(root,
                          text="🚿💧Care: Much water will let it feel tropical",
                          font="Arial 18 bold",
                          bg="#BFE2CB")
    care_label.place(x=15, y=333)

    addition_label = tk.Label(root,
                              text="📌 Addition: Great to eat against acne",
                              font="Arial 18 bold",
                              bg="#BFE2CB")
    addition_label.place(x=15, y=400)

#Definition for the second option: Fiddle Fig
def fiddle_fig():

    #Load and place the image on the right side
    image = load_image("Images/fiddlefig.jpeg", (226, 339))  #Resize the image to fit
    image_label = tk.Label(root, image=image, bg="black")
    image_label.image = image  #Keep a reference to the image
    image_label.place(x=500, y=120)  #Position at (500, 120)
    #Set a new background
    root.configure(bg="#899A7A")

    #Result label that presents the plant
    result_label = tk.Label(root,
                            text="The fiddle-leaf fig!",
                            font="Arial 48 bold",
                            bg="#899A7A")
    result_label.place(x=15, y=50)

    #Labels with information about the plant
    info_label = tk.Label(root,
                          text="🌿 It grows in the desert and makes a great decoration",
                          font="Arial 18 bold",
                          bg="#899A7A")
    info_label.place(x=15, y=200)

    place_label = tk.Label(root,
                           text="🏠 Place: Bright and warm place",
                           font="Arial 18 bold",
                           bg="#899A7A")
    place_label.place(x=15, y=266)

    care_label = tk.Label(root,
                          text="🫧💧Care: Water if plant feels dry, fertilize it monthly",
                          font="Arial 18 bold",
                          bg="#899A7A")
    care_label.place(x=15, y=333)

    addition_label = tk.Label(root,
                              text="📌 Addition: Put this in your new apartment!",
                              font="Arial 18 bold",
                              bg="#899A7A")
    addition_label.place(x=15, y=400)

#Definition for the third option: Kentiapalm
def kentiapalm():

    # Load and place the image on the right side
    image = load_image("Images/kentiapalm.jpeg", (240, 320))  #Resize the image to fit
    image_label = tk.Label(root, image=image, bg="black")
    image_label.image = image  #Keep a reference to the image
    image_label.place(x=500, y=120)  # Position at (500, 120)
    #Set a new background
    root.configure(bg="#E19571")

    #Result label that presents the plant
    result_label = tk.Label(root,
                            text="Yeah, the Kentia palm!",
                            font="Arial 48 bold",
                            bg="#E19571")
    result_label.place(x=15, y=50)

    #Labels with information about the plant
    info_label = tk.Label(root,
                          text="🌿 The australian palm is great for beginners",
                          font="Arial 18 bold",
                          bg="#E19571")
    info_label.place(x=15, y=200)

    place_label = tk.Label(root,
                           text="🏠 Place: Inside a room, but not in the direct sun",
                           font="Arial 18 bold",
                           bg="#E19571")
    place_label.place(x=15, y=266)

    care_label = tk.Label(root,
                          text="🫧💧Care: Don't forget to fertilize it weekly",
                          font="Arial 18 bold",
                          bg="#E19571")
    care_label.place(x=15, y=333)

    addition_label = tk.Label(root,
                              text="📌 Addition: Check regularly if your Kentia palm is sick",
                              font="Arial 18 bold",
                              bg="#E19571")
    addition_label.place(x=15, y=400)

#Definition for the fourth option: Ginger
def ginger():

    # Load and place the image on the right side
    image = load_image("Images/ginger.jpeg", (240, 320))  #Resize the image to fit
    image_label = tk.Label(root, image=image, bg="black")
    image_label.image = image  #Keep a reference to the image
    image_label.place(x=490, y=120)  #Position at (490, 120)
    #Set a new background
    root.configure(bg="#EEE6CF")

    #Result label that presents the plant
    result_label = tk.Label(root,
                            text="Ginger is your plant",
                            font="Arial 48 bold",
                            bg="#EEE6CF")
    result_label.place(x=15, y=50)

    #Labels with information about the plant
    info_label = tk.Label(root,
                          text="🌿 Ginger is super healthy for you!",
                          font="Arial 18 bold",
                          bg="#EEE6CF")
    info_label.place(x=15, y=200)

    place_label = tk.Label(root,
                           text="🏠 Place: Warm and humid",
                           font="Arial 18 bold",
                           bg="#EEE6CF")
    place_label.place(x=15, y=266)

    care_label = tk.Label(root,
                          text="🫧💧Care: Sprinkle water on it regularily!",
                          font="Arial 18 bold",
                          bg="#EEE6CF")
    care_label.place(x=15, y=333)

    addition_label = tk.Label(root,
                              text="📌 Addition: Sometimes difficult to keep healthy",
                              font="Arial 18 bold",
                              bg="#EEE6CF")
    addition_label.place(x=15, y=400)

#Definition for the page to create a Shopping List
def list_side():
    global shopping_list

    #Clear all existing widgets
    clear_page(root)

    #Load and place the background image
    test_image = load_image("Images/List.jpg", (750, 500))
    test_label = tk.Label(root, image=test_image)
    test_label.image = test_image  #Keep a reference to the image
    test_label.pack()

    #Load the image of Mary Poppins
    image = load_image("Images/mary_poppins_checkbox.png", (480, 480))  #Resize the image to fit
    image_label = tk.Label(root, image=image, bg="#C2DBD7")
    image_label.image = image  #Keep a reference to the image
    image_label.place(x=0, y=0)  #Position at (0, 0)

    #Create a label that asks if the User wants to go shopping
    shopping_label = tk.Label(root,
                            text="On your way to go shopping?",
                            font="Arial 22 bold",
                            fg="black",
                            bg="#C2DBD7")
    shopping_label.place(x=325, y=225)

    #Create button that leads to the Checkbox-Function
    create_list_button = tk.Button(root,
                                   text="Create a shopping list",
                                   font=("Arial 28 bold"),
                                   command=lambda: create_checkboxes()
                                   )
    create_list_button.place(x=325,y=300)

    #Homepage Button that will lead back to Welcome Page
    homepage_button = tk.Button(root,
                                text="Homepage",
                                font=("Arial 14 bold"),
                                command=lambda: homepage(root, image_file_path="Images/Homepage.jpeg")
                                )

    homepage_button.place(x=325,y=450)

#Definition to create checkboxes
def create_checkboxes():
    #Clear all existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    #Create a new frame
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    #Label to ask the User to select all needed items
    label = tk.Label(frame,
                     text="It's ever so important to have the proper tools at hand. Select the essentials you need:",
                     font=("Arial 18 bold"))
    label.pack(pady=10)

    #Create a list with all basic items that are related to plants
    items = ('New Herb Seeds: Sprinkle a bit of magic to your dishes!',
             'Potting soil: Provide a nurturing bed for your plants roots',
             'Fertilizer: Feed your gardens growth with a spoonful of goodness',
             "Grow Lights: Illuminate their path towards the sun's loving embrace",
             'New pots and containers: Give them a sweet home to stretch their roots',
             "Mulch: To wrap them in a warm blanket of protection",
             'Pruning Shears: Trim away the old to make room for new growth',
             "Insecticide: Ward off pesky visitors who might trouble your plants peace",
             "pH Tester: Ensure the perfect balance for health and happiness",
             'Gloves: To protect your hands as you lovingly tend to each leaf and petal',
             "Plant Labels: Help your garden remember its own identity",
             "Waterproof Marker: To write stories on leaves that rain can't wash away",
             'Rosemary: A fragrant friend to add a touch of magic to your gardens scent!',
             "Stakes: Stand tall and offer support when the winds of change blow!",
             'Seedling Pots: Cradle tender beginnings as they prepare to grow')

    #Create checkboxes for each item
    checkboxes = []
    for item in items:
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(frame, text=item, variable=var)
        checkbox.pack(anchor='w')
        checkboxes.append((item, var))

    #Button to confirm selection, which leads the User to the next page
    confirm_button = tk.Button(frame,
                               text="Confirm Selection",
                               font=("Arial 14 bold"),
                               command=lambda: show_selected_items(checkboxes))
    confirm_button.pack(pady=10)

#Function to show selected items
def show_selected_items(checkboxes):
    selected_items = [item for item, var in checkboxes if var.get()]

    #Clear all existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    #Create a new frame
    root.configure(bg="#F3EBDE")
    frame = tk.Frame(root, width=300, height=200, bg="white")
    frame.pack(padx=15, pady=15)

    #Load and place the image of Bert
    image = load_image("Images/dike-van-dyke.png", (101, 232))  # Resize the image to fit
    image_label = tk.Label(root, image=image, bg="#F3EBDE")
    image_label.image = image  # Keep a reference to the image
    image_label.place(x=20, y=245)  # Position at (20, 245)

    #Label that introduces the User to the Shopping List
    label = tk.Label(frame,
                        text="Make sure to capture a snapshot of your splendid shopping list!",
                        font=("Arial 18 bold"),
                        bg="white")
    label.pack(pady=10)

    #Insert newline character and concatenate items into single strings
    shopping_list = "\n".join(selected_items)

    #Create a label to display the selected items
    shopping_list_label = tk.Label(frame,
                                    text=shopping_list,
                                    font=("Arial 12 bold"),
                                    bg="white",
                                    fg="#EC805F",
                                    justify=tk.LEFT)
    shopping_list_label.pack(pady=10)

    #Create a label to wish the User fun while Shopping
    label = tk.Label(frame,
                        text="Happy gardening, and remember: A spoonful of love makes the plants grow strong!",
                        font=("Arial 12 bold"),
                        bg="white")
    label.pack(pady=20)

    #Homepage Button that will lead back to Welcome Page
    homepage_button = tk.Button(root,
                                text="Homepage",
                                font=("Arial 14 bold"),
                                command=lambda: homepage(root, image_file_path="Images/Homepage.jpeg")
                                )
    homepage_button.place(x=325,y=450)

#Calling the function that creates the homepage
image_file_path = "Images/Homepage.jpeg"
homepage(root, image_file_path)

#run the code
root.mainloop()

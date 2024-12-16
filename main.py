from tkinter import *
import requests

# Function to get a random Kanye quote from the API
def get_quote():
    # API endpoint URL to fetch the quote
    endpoint_url = "https://api.kanye.rest"
    response = requests.get(url=endpoint_url)  # Sending the GET request
    data = response.json()  # Parsing the response into JSON format
    # Updating the canvas text with the quote from the API
    canvas.itemconfig(quote_text, text=data["quote"])

# Initialize the main window
window = Tk()
window.title("Kanye Says...")  # Set the window title
window.config(padx=50, pady=50)  # Adding padding to the window

# Create the canvas to hold the background and quote text
canvas = Canvas(width=300, height=414)  # Setting the size of the canvas
background_img = PhotoImage(file="background.png")  # Loading the background image
canvas.create_image(150, 207, image=background_img)  # Place the background image on the canvas
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "italic"), fill="purple")  # Placeholder text for the quote
canvas.grid(row=0, column=0)  # Position the canvas in the window

# Load the image for the button
kanye_img = PhotoImage(file="kanye.png")
# Create a button with the Kanye image that triggers the `get_quote` function when clicked
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)  # Position the button below the canvas

# Run the Tkinter event loop to display the window
window.mainloop()

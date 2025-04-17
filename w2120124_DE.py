#Author: D.Samiru Hemaka Wimalaransi
#Date: 24.12.2024
#Student ID: 20240795/ W2120124

# Task D: Histogram Display
# Import the graphics module and functions from the w2120124.py file
from graphics import *
from w2120124_ABC import * 

class HistogramApp:
    def __init__(self, traffic_data, date):
        # Initialize the histogram with the traffic data and date.
        self.traffic_data = traffic_data 
        self.date = date 

    def setup_window(self):
        #Sets up the Tkinter window and canvas for the histogram.
        self.canvas=GraphWin('Histogram',width=1400,height=700) # Create a window
        self.canvas.setBackground('white') # Set the background color of the window

        pass  # Setup logic for the window and canvas

    def draw_histogram(self):
        #Draws the histogram with axes, labels, and bars
        elm_max = max(self.traffic_data[0]) # Maximum value for Elm Avenue
        henley_max = max(self.traffic_data[1]) # Maximum value for Henley Highway
        overall_max = max(elm_max,henley_max) # Overall maximum value for both junctions

        # Draw green bars for Elm Avenue data
        constant=100 # Starting position for the bars
        elm_data=self.traffic_data[0] # Get Elm Avenue data
        for j in elm_data: # Loop through each data value
            # Create a rectangle for the bar
            rectangle = Rectangle(Point(constant,(600-((j/overall_max)*350))),Point(constant+20,600))
            rectangle.draw(self.canvas) # Draw the rectangle on the canvas
            rectangle.setFill("#4bda4b")
            rectangle.setOutline("grey")

            # Add a label above the bar to show the value
            elm_data_num = Text(Point(constant+10,(600-(((j/overall_max)*350)+10))),j)
            elm_data_num.draw(self.canvas) # Draw the text on canvas
            elm_data_num.setSize(9) # Set the text size 
            elm_data_num.setFace('times roman') # Set the font 
            elm_data_num.setStyle('bold') # Set the text style
            elm_data_num.setTextColor('#4bda4b') # Set the text colour
            constant += 50 # Move the next bar to right.

        # Draw red bars for Henley Highway data
        constant_2 = 120 # Starting position for the bars
        Henley_data = self.traffic_data[1] # Get Henley Highway data
        for k in Henley_data:
            # Create a rectangle for the bar
            rectangle1 = Rectangle(Point(constant_2,(600-(k/overall_max)*350)),Point(constant_2+20,600))
            rectangle1.draw(self.canvas) 
            rectangle1.setFill("#fc9296")
            rectangle1.setOutline("grey")

            # Add a label above the bar to show the value
            henley_data_num = Text(Point(constant_2+10,(600-((k/overall_max)*350+10))),k)
            henley_data_num.draw(self.canvas) 
            henley_data_num.setSize(9) 
            henley_data_num.setFace('times roman') 
            henley_data_num.setStyle('bold') 
            henley_data_num.setTextColor('#fc9296')
            constant_2 += 50 

        pass  # Drawing logic goes here

    def add_legend(self):
        # title at the top of the histogram
        heading = Text(Point(300,50),f"Histogram of Vehicle Frequency per Hour ({self.date})")
        heading.draw(self.canvas)
        heading.setSize(16)
        heading.setFace('times roman')
        heading.setStyle('bold')
        heading.setTextColor('grey')

        # green square and label for Elm Avenue
        sq_1 = Rectangle(Point(30,65),Point(50,85))
        sq_1.draw(self.canvas)
        sq_1.setFill('#4bda4b')
        sq_1_text = Text(Point(151,75),f"Elm Avenue/Rabbit Road")
        sq_1_text.draw(self.canvas)
        sq_1_text.setFace('times roman')
        sq_1_text.setStyle('bold')
        sq_1_text.setTextColor('grey')

        # red square and label for Henley Highway   
        sq_2 = Rectangle(Point(30,95),Point(50,115))
        sq_2.draw(self.canvas)
        sq_2.setFill('#fc9296')
        sq_2_text = Text(Point(154,106),f"Henley Highway/Westway")
        sq_2_text.draw(self.canvas)
        sq_2_text.setFace('times roman')
        sq_2_text.setStyle('bold')
        sq_2_text.setTextColor('grey')
        
        # x-axis label
        x_axis = Text(Point(700,650),f"Hours 00:00 to 24:00")
        x_axis.draw(self.canvas)
        x_axis.setSize(10)
        x_axis.setFace('times roman')
        x_axis.setStyle('bold')
        x_axis.setTextColor('grey')

        # x axis line
        line = Line(Point(100,600),Point(1300,600))
        line.draw(self.canvas)

        # 0-23 hours on x-axis
        axis_number = 120 # Start at position 120.
        for i in range(0,24):
            # Add hours to the x-axis
            hours=f"{i:02}"
            hours_number = Text(Point(axis_number,615),hours)
            hours_number.draw(self.canvas)
            hours_number.setSize(10)
            hours_number.setFace('times roman')
            hours_number.setStyle('bold')
            hours_number.setTextColor('grey')
            axis_number += 50

        #Wait for the user to click to close the window
        self.canvas.getMouse()
        self.canvas.close()
       
    def run(self):
        #Runs the Tkinter main loop to display the histogram.
        self.setup_window() # Set up window
        self.draw_histogram() # Draw histogram
        self.add_legend() # Add legend
    
# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor:
    def __init__(self):
        #Initializes the application for processing multiple CSV files.
        self.current_data = None
        self.file_path = None
        self.date = None
        self.outcomes = 0

    def load_csv_file(self, file_path):
        #Loads a CSV file and processes its data.
        self.outcomes, self.histogram_data = process_csv_data(file_path)
    
    def clear_previous_data(self):
        #Clears data from the previous run to process a new dataset.
        self.current_data = None
        self.file_path = None
        self.date = None
        self.histogram_data = None
        self.outcomes = 0

    def handle_user_interaction(self):
        #Handles user input for processing multiple files.
        self.condition = validate_continue_input()
        return self.condition

    def process_files(self):
        #Main loop for handling multiple CSV files until the user decides to quit.
        while True:
            try:
                # Get the file path and date
                self.file_path, self.date = validate_date_input()
                self.load_csv_file(self.file_path)
                # Display the outcomes and save them to results.txt
                display_outcomes(self.outcomes)
                save_results_to_file(self.outcomes, file_name="results.txt")
                # Display the histogram
                histogram_app = HistogramApp(self.histogram_data, self.date)
                histogram_app.run()
                # clear data
                self.clear_previous_data()

            except FileNotFoundError:
                print(f"File {self.file_path} not found.\n")
            except NameError:
                print()   
            except IndexError:
                print(f"File {self.file_path} is empty.\n")

            # Ask the user if they want to continue
            user_choice = self.handle_user_interaction()
            if user_choice == 'N':
                print("Exiting application.\n")
                break
            elif user_choice == 'Y':
                print()
                self.process_files()
                break

# Start the program.
MultiCSVProcessor().process_files()

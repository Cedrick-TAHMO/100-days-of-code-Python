
"""
Mile to Kilometer Converter
A simple GUI application to convert miles to kilometers using tkinter.
"""

from tkinter import *


class MileToKmConverter:
    """A class to handle the Mile to Kilometer conversion interface and logic."""
    
    # Conversion constant
    MILE_TO_KM = 1.60934
    
    def __init__(self):
        """Initialize the converter window and its components."""
        # Main window setup
        self.window = Tk()
        self.window.title("Mile to Kilometer Converter")
        self.window.minsize(width=300, height=150)
        self.window.config(padx=20, pady=20)
        
        # Create and setup UI components
        self._create_widgets()
        self._setup_layout()
    
    def _create_widgets(self):
        """Create all necessary widgets for the converter."""
        # Input field
        self.miles_entry = Entry(width=10)
        self.miles_entry.insert(0, "0")
        
        # Labels
        self.miles_label = Label(text="Miles")
        self.is_equal_label = Label(text="is equal to")
        self.result_label = Label(text="0")
        self.km_label = Label(text="Km")
        
        # Calculate button
        self.calc_button = Button(
            text="Calculate",
            command=self._calculate_conversion
        )
    
    def _setup_layout(self):
        """Setup the grid layout for all widgets."""
        # Organize widgets using grid layout
        self.miles_entry.grid(column=1, row=0, padx=10)
        self.miles_label.grid(column=2, row=0)
        self.is_equal_label.grid(column=0, row=1)
        self.result_label.grid(column=1, row=1)
        self.km_label.grid(column=2, row=1)
        self.calc_button.grid(column=1, row=2, pady=10)
    
    def _calculate_conversion(self):
        """Convert miles to kilometers and update the display."""
        try:
            miles = float(self.miles_entry.get())
            kilometers = miles * self.MILE_TO_KM
            self.result_label.config(text=f"{kilometers:.2f}")
        except ValueError:
            self.result_label.config(text="Error")
    
    def run(self):
        """Start the application main loop."""
        self.window.mainloop()


def main():
    """Main function to run the converter application."""
    converter = MileToKmConverter()
    converter.run()


if __name__ == "__main__":
    main()
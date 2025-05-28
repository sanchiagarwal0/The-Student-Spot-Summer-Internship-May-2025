# Contact Book Application - README

## Overview
This is a simple contact book application built with Python's Tkinter GUI library that stores contact information in a CSV file. The application allows users to:

- Add new contacts (name and phone number required)
- View existing contacts
- Save contacts to a persistent CSV file
- Handle common errors gracefully

## Key Features

1. **User-Friendly Interface**:
   - Clean, intuitive GUI with proper labeling   ## gui is Graphical User Interface 
   - Responsive layout with appropriate spacing
   - Clear error/success messages

2. **Data Persistence**:
   - Contacts are saved to `contacts.csv` file
   - Automatically creates CSV file with headers if it doesn't exist
   - Appends new contacts without overwriting existing data

3. **Error Handling**:
   - Validates required fields (name and phone)
   - Handles file permission errors
   - Catches and displays unexpected errors

4. **Maintenance**:
   - Simple, well-structured code
   - Comments explaining key functionality
   - Easy to extend with additional features

## Technical Implementation

The application uses:
- **Tkinter** for the graphical interface
- **CSV module** for data storage
- **os module** for file existence checks

Key functions:
- `save_contact()`: Handles the core logic of validating and saving contacts
- Main window setup creates and positions all UI elements

## How to Use

1. Run the application
2. Enter contact name and phone number (both required)
3. Click "Save Contact" button
4. View saved contacts in the `contacts.csv` file

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Write permissions in the execution directory

## Possible Extensions

1. Add contact viewing/editing functionality
2. Implement contact searching
3. Add additional fields (email, address etc.)
4. Create an export feature
5. Add contact deletion capability

## Troubleshooting

If you get Tkinter-related errors:
- On Linux: Install python3-tk package
- On Windows: Reinstall Python with Tkinter option checked
- On Mac: Install activeTcl or use Homebrew

For file permission errors:
- Ensure you have write permissions in the directory
- Check if contacts.csv isn't open in another program
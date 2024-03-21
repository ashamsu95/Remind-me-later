# Remind-me-later

Remind-me-later is a web application designed to allow users to set up reminders with custom messages. It provides a simple user interface for specifying the date and time when the reminder should be sent, as well as the message content. Users can choose to receive reminders via SMS or Email.

## Features

- Set up reminders with custom messages.
- Specify the date and time for reminder delivery.
- Choose between SMS and Email as reminder delivery methods.

## Technologies Used

- Django: Backend framework for building the API and managing data storage.
- JavaScript: Used for frontend development to create the user interface.
- HTML/CSS: Frontend markup and styling.
- SQLite: Default database engine for storing reminders.

## Usage

1. Sign up or log in to your Remind-me-later account.
2. Navigate to the "Set Reminder" page.
3. Enter your reminder message and select the date and time for delivery.
4. Choose whether to receive the reminder via SMS or Email.
5. Click "Set Reminder" to save your reminder.

# Remind-me-later API Endpoints

## User Registration

### Request POST

#### URL http://127.0.0.1:8000/user/register/

#### Body

The request body should contain a JSON object with the following fields:

- **username**: (string) The username for the new user. Required.
- **email**: (string) The email address for the new user. Required.
- **password**: (string) The password for the new user. Required.
- **phone_number**: (string, optional) The phone number for the new user. If provided, must be a string with a maximum length of 15 characters.

### Example Request Body

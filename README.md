# Remind-me-later

Remind-me-later is a web application designed to allow users to set up reminders with custom messages. It provides a API end points for specifying the date and time when the reminder should be sent, as well as the message content. Users can choose to receive reminders via SMS or Email.

ps:message delivery logic is not added,Go forward i will use celery to send message.

## Features

- Set up reminders with custom messages.
- Specify the date and time for reminder delivery.
- Choose between SMS and Email as reminder delivery methods.

## Technologies Used

- Django
- Django Rest Framework

## Usage

1. Sign up or log in to your Remind-me-later account.
2. Navigate to the create reminder End POint.
3. Enter your reminder message and select the date and time for delivery.
4. Choose whether to receive the reminder via SMS or Email.
5. Send Post request.

# Remind-me-later API Endpoints

## User Registration

### Request POST

#### URL http://127.0.0.1:8000/user/register/

#### Body

The request body should be form-data:

- **username**: (string) The username for the new user. Required.
- **email**: (string) The email address for the new user. Required.
- **password**: (string) The password for the new user. Required.
- **phone_number**: (string, optional) The phone number for the new user. If provided, must be a string with a maximum length of 15 characters.

## User Login

### Request POST

#### URL http://127.0.0.1:8000/user/login/

#### Body

The request body should be form-data:

- **username**: (string) The username for the new user. Required.
- **password**: (string) The password for the new user. Required.

#### Response

- **Status**: 200OK
- **"message"**: "User logged in successfully."
- **Cookie**: csrf token session Id(for Auth)

## User LogOut

### Request POST

#### URL http://127.0.0.1:8000/user/logout/

#### Header

- **X-CSRFToken**: csrf token from cookie
- **Cookie**:cookie

#### Response

- **Status**: 200OK
- **"message"**: "User logged out successfully"

## Create Reminder

### Request POST

#### URL http://127.0.0.1:8000/user/logout/

#### Header

- **X-CSRFToken**: csrf token from cookie
- **Cookie**:cookies

#### Body

The request body should be form-data:

- **message**: (string)Your reminder message here.
- **reminder_time**: (string) 2024-03-25T15:00:00.
- **reminder_method**: (string) email or sms

#### Response

- **Status**: 201Created

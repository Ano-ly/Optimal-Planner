
---

# Optimal Planner

## Overview

Optimal Planner is an event-planning web application and organization that allows for easy event planning and management. With Optimal Planner, an organizer can effectively plan an event, allocate a budget, assign tasks, and send invites to attendees.

## Features

- **Event Creation**: Create events of various categories like wedding, naming ceremony, burial, birthday ceremony, dinner, party, homecoming, etc.
- **Invitation to Attendees**: Send invitations directly to the attendees' Gmail accounts through the application.
- **Task Management**: Add tasks for each event for ease of coordination and execution of event-related activities.
- **Event Link Generation**: Generate unique links for events that can be shared with potential guests for easy registration.
- **Budget Allocation**: Allocate and track budgets for each event.
- **Invitee Management**: Send invitations and track RSVPs.
- **Email Notifications**: Automated email notifications for event confirmation, reminders, and updates.
- **User Authentication**: Secure authentication using passwords, with email confirmation for users and invitees.

## Technologies Used

- **Backend**: Python, Flask, SQLAlchemy
- **Database**: SQLite
- **Frontend**: HTML, CSS
- **Email Service**: smtplib, Flask-Mail
- **Security**: bcrypt, itsdangerous

## Installation

1. Clone the repository to your system:
   ```bash
   git clone https://github.com/your-username/optimal-planner.git
   ```
2. Navigate to the project directory:
   ```bash
   cd optimal-planner
   ```
3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   python manage.py db upgrade
   ```
5. Run the application:
   ```bash
   flask run
   ```

## Usage

1. **Log In**: Input your name/email and password on the user login page to log in.
2. **Create an Event**: Enter the category, time set for the event, necessary budget, and other required information.
3. **Share Invitations**: Send invitations to invitees via their Gmail accounts.
4. **Generate Event Link**: Share the generated link with potential guests for registration.
5. **Manage Tasks and Budgets**: Organize tasks and allocate budgets for your event.
6. **Track RSVPs**: Monitor guest responses and attendance.

## Authors

- **Fortune Peter**
  - Software Engineer; Mechanical Engineering Student, Ken Saro-wiwa Polytechnic, Delta State, Nigeria

- **Amarachi Uvere**
  - Software Engineer; Civil Engineering Student, Obafemi Awolowo University, Ile-Ife, Osun State, Nigeria

- **Scholastica Amarachi**
- ** Software Engineer; Frontend specialization, and a graduate Networking & System Security from Mario Institue, Uhunowere, Nsukka, Enugu state, Nigeria

- **Bukola**
- ** Software Engineer; Frontend specialization

## Contributing

Contributions are welcome! If you'd like to contribute to Optimal Planner, please follow these steps:

1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes with descriptive commit messages:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

## Future Features

- Event recommendations
- More detailed events
- Weather forecasting

## Notes

See notes below.

## License

This project is licensed under the MIT License.

---

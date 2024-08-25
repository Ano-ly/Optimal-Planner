
---

# **Optimal-Planner**

Optimal-Planner is a robust event management application designed to streamline event planning and organization. This application allows users to create events, allocate budgets, send notifications, and generate shareable event links for guest registration. With a focus on flexibility and ease of use, Optimal-Planner is the perfect tool for managing events of any size.

## Features

- **User Authentication**: Secure authentication using passwords, with email confirmation for users and invitees.
- **Event Creation and Management**: Create events, set dates, locations, and descriptions, and manage guest lists.
- **Email Notifications**: Automated email notifications for event confirmation, reminders, and updates.
- **Event Link Generation**: Generate unique links for events that can be shared with potential guests for easy registration.
- **Task Management**: Manage tasks related to events.
- **Budget Allocation**: Allocate and track budgets for each event.
- **Invitee Management**: Send invitations and track RSVPs.

## Technologies Used

- **Backend**: Python, Flask, SQLAlchemy
- **Database**: SQLite
- **Frontend**: HTML, CSS
- **Email Service**: smtplib, Flask-Mail
- **Security**: bcrypt, itsdangerous

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/optimal-planner.git
   ```
2. Navigate to the project directory:
   ```bash
   cd optimal-planner
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   python database.py db upgrade
   ```
5. Run the application:
   ```bash
   flask run
   ```

## Usage

1. **Create an Account**: Sign up and confirm your email address.
2. **Create an Event**: Add event details, including the date, location, and description.
3. **Manage Tasks and Budgets**: Organize tasks and allocate budgets for your event.
4. **Generate Event Link**: Share the generated link with potential guests for registration.
5. **Track RSVPs**: Monitor guest responses and attendance.

## Project Structure

- `models/`: Contains the database models for users, events, tasks, and invitees.
- `controllers/`: Manages the logic for user authentication, event creation, and more.
- `utils/`: Helper functions for sending emails, generating tokens, etc.
- `templates/`: HTML templates for rendering the user interface.
- `static/`: Contains static assets like CSS files.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to suggest changes.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to all contributors and open-source libraries that made this project possible.

---

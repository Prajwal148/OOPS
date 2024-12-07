# Gym Membership and Class Booking System

The Gym Membership and Class Booking System is a web application developed to simplify the management of gym memberships and class scheduling. It allows for online registration of membership, access to class availability, and early booking. The system provides users with the ability to monitor their bookings, view class descriptions, and manage their attendance, improving the overall user experience. On the administrative side, gym managers can create and schedule classes, monitor attendance, limit class size, and manage member profiles. It can also process membership payments, handle renewals, and send notifications to users about class reminders or membership status.

By integrating these functionalities into one system, the app elevates the gym experience, fostering greater member engagement while allowing gyms to operate more efficiently.

---

## Team Members and Roles

- **[Prajwal Garla](https://github.com/Prajwal148/CIS641-HW2-Garla/tree/master)** - Frontend Engineer
- **[Guru Saran Reddy Busireddy](https://github.com/gurushubb/CIS641-HW2-Busireddy/tree/master)** - UI/UX Designer
- **[Hari Naga Venkata Sai Posani](https://github.com/Posanisai/CIS-641-HW2-POSANI.git)** - Design and Testing
- **[Mahesh Peta](https://github.com/Mahesh4229/641-HW2-Mahesh)** - Backend Engineer

---

## Prerequisites

Before running the Gym Membership and Class Booking System, ensure you have the following installed on your machine:

- **Python 3.8+**
- **Django 4.0+**
- **SQLite** (as the database backend, integrated with Django)
- **Node.js** (for frontend development)
- **Twilio API** (for sending notifications; ensure you have your Twilio credentials)

---

## Installation & Setup Instructions

### Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/Prajwal148/OOPS.git
cd OOPS/src

'''bash
python3 -m venv venv
source venv/bin/activate

'''bash
python manage.py makemigrations
python manage.py migrate

'''bash
python manage.py createsuperuser

'''bash
python manage.py runserver

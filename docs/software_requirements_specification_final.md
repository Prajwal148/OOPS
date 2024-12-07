# Overview
This document outlines the **Software Requirements Specification (SRS)** for the **Gym Membership and Class Booking System**. It details the functional and non-functional requirements, defines the change management process, and maps the system's design artifacts to the specified requirements.

# Software Requirements
This section describes the functional and non-functional requirements for the **Gym Membership and Class Booking System**. It outlines what the system must do (functional requirements) and the quality attributes it must possess (non-functional requirements).

## Functional Requirements

### User login
| ID  | Requirement | 
| :-------------: | :----------: |
| FR1 | The system shall allow users to sign up by providing personal information. |
| FR2 | The system shall allow users to log in using a username and password. |
| FR3 | The system shall allow users to request a password change from the admin. |
| FR4 | The system shall allow users to save the login details automatically. |
| FR5 | The system shall display an error message for incorrect login attempts (e.g., "Invalid username or password"). |

### Class Scheduling
| ID  | Requirement | 
| :-------------: | :----------: |
| FR6 | The system shall allow users to browse classes based on availability. |
| FR7 | The system shall allow users to select the class with time and amount. |
| FR8 | The system shall allow users to cancel the booking. |
| FR9 | The system shall stop the users from booking when the capacity is full. |
| FR10 | The system shall allow users to receive email notifications after booking. |

### Payment
| ID  | Requirement | 
| :-------------: | :----------: |
| FR11 | The system shall allow users to pay the fees using card transactions. |
| FR12 | The system shall allow users to make payment for renewal of membership. |
| FR13 | The system shall allow users to download the receipt after payment confirmation. |
| FR14 | The system shall use encryption for processing the payment. |
| FR15 | The system shall validate the user's card details for the successful payment process. |

### Notification
| ID  | Requirement | 
| :-------------: | :----------: |
| FR16 | The system shall send an email message to users after successfully booking the class. |
| FR17 | The system shall allow users to opt to get notified via emails. |
| FR18 | The system shall notify users in case of class cancellations or schedule changes. |
| FR19 | The system shall send notifications to users before class schedules. |
| FR20 | The system shall send reminders to users for memberships and fees payments, etc. |

### Manager
| ID  | Requirement | 
| :-------------: | :----------: |
| FR21 | The system shall allow the manager to modify and update the class schedule. |
| FR22 | The system shall allow the manager to process payments and keep track of the transaction history. |
| FR23 | The system shall allow the manager to override the class bookings on request based on availability. |
| FR24 | The system shall allow the manager to monitor the activity across the system. |
| FR25 | The system shall allow the manager to download the reports and performance of instructors. |

## Non-Functional Requirements

### User Login
| ID  | Requirement | 
| :-------------: | :----------: |
| NFR1 | The system should use HTTPS to secure user data during the time of registration and user login. |
| NFR2 | The forms should provide real-time validation and clear error messages. |
| NFR3 | The login and registration should be completed within 2 seconds. |
| NFR4 | The system should be capable of handling 1,000 multiple users during peak times. |
| NFR5 | The system should allow users to retrieve their password using a "Forgot Password". |

### Class Scheduling
| ID  | Requirement | 
| :-------------: | :----------: |
| NFR6 | The system should handle 10,000 class bookings at once without slowing down. |
| NFR7 | The system should update schedules instantly for all users. |
| NFR8 | The users should be able to book classes up to 30 days in advance. |
| NFR9 | The class availability should be updated within 2 seconds after any selection made. |
| NFR10 | The system should prevent any double bookings or schedule conflicts. |

### Payment
| ID  | Requirement | 
| :-------------: | :----------: |
| NFR11 | The payment gateway should process the payments within 5 seconds for 95% of transactions. |
| NFR12 | The system should be able to handle 5,000 payment transactions per day without performance degradation. |
| NFR13 | The system should give users clear, easy-to-understand invoices and payment histories. |
| NFR14 | The system should validate the card details and make sure they match the user's records. |
| NFR15 | The system should give a clear error message for failed transactions. |

### Notification
| ID  | Requirement | 
| :-------------: | :----------: |
| NFR16 | The Email notifications should be sent within 2 minutes of any event (e.g., class confirmation). |
| NFR17 | The system should be able to handle sending emails to up to 50,000 users at the same time. |
| NFR18 | The users should be able to unsubscribe from specific types of email notifications. |
| NFR19 | The emails should be delivered reliably, even during busy times like peak bookings. |
| NFR20 | The emails should be clear, concise, and easy to understand for all the users. |

### Manager
| ID  | Requirement | 
| :-------------: | :----------: |
| NFR21 | The system should support 100 managers working at the same time. |
| NFR22 | The manager's actions should be logged and kept for 6 months. |
| NFR23 | The managers should be able to personalize their dashboards. |
| NFR24 | The reports should be loaded within 5 seconds for up to 1,000 records. |
| NFR25 | The system should be able to provide detailed logs for managing activities, including date, time, and action taken. |

# Change Management Plan
For our gym management and class booking system, we will provide training for the particular user-specified roles. Gym staff, such as instructors and managers, will be attending some live sessions. To get hands-on experience with the core functionalities like managing membership registrations, scheduling classes, and tracking payments. Admins will have to undergo deep training on managing user roles, configuring the system, and managing logs and reports. We will create a practice environment where staff can go through different tasks like booking classes, handling payments, and creating schedules without disturbing the existing real data. An easy and effective resource like video tutorials and user guides can help them to learn at their own pace. We also conduct some feedback sessions to answer any questions and help them to feel confident using the system.

To make sure the gym system integrates smoothly with the current operations, we will be focusing on aligning with existing processes without requiring any additional tools like APIs or AWS. Member details, payments, and class schedules will be imported manually into the system. We'll ensure everything is up to date and accurate. We will provide a basic login process for gym staff using unique credentials for secure access. Instead of the full launch of the system, we will be doing a test with a small group of gym staff to make sure that all the gym features, like booking classes and managing member profiles, are working as per expectations, if not addressing any adjustments required.

We will set up a simple support system for quick resolution of issues that are encountered by gym staff. For example, if there is any problem with class scheduling or payments, staff need to report it to their technical support team. Any major issues, like the gym website being down, will be addressed within a short time frame. Smaller issues like errors in members’ notifications and profiles will be addressed in a couple of days. The support team will be available via email or phone to assist directly. As additional assistance, we will provide a guide with FAQs and troubleshooting tips so that staff can solve any common issues themselves. For repeat issues, we will take some time and analyze the root cause and fix it permanently, making sure the system is reliable and working effectively all the time.

# Traceability Links
**Traceability Links** map the system’s artifacts (e.g., use cases, classes, activity diagrams) to the corresponding requirements. This ensures that all requirements are fulfilled and helps track changes and their impacts on the system design and implementation.

# Use Case Diagram Traceability

| Artifact ID  | Artifact Name                      | Requirement ID        |
| :----------: | :--------------------------------: | :-------------------: |
| UC1          | Register New Member                | FR1, NFR1             |
| UC2          | Login / Authenticate Member        | FR2, FR5, NFR3, NFR4  |
| UC3          | Browse Classes and Book Class      | FR6, FR7, FR8, FR9, FR10, NFR6, NFR9 |
| UC4          | Process Payment                    | FR11, FR12, NFR11, NFR13, NFR14 |
| UC5          | Send Booking Notification          | FR16, FR19, NFR16, NFR17 |
| UC6          | Manage Class Schedule              | FR21, NFR6, NFR7      |
| UC7          | Process Payments and Transactions  | FR22, FR23, NFR11, NFR12 |
| UC8          | Monitor System Activity            | FR24, NFR21, NFR25    |
| UC9          | Generate Reports                   | FR25, NFR24           |


## Class Diagram Traceability

| Artifact Name   | Requirement ID  |
| :-------------: | :-------------: |
| `User`          | FR1, FR3, FR6, NFR1, NFR5  |
| `Payments`      | FR11, FR12, FR13, FR14, FR15, NFR11, NFR12, NFR13, NFR14  |
| `Notification`  | FR16, FR17, FR18, FR19, FR20, NFR16, NFR17, NFR19, NFR20 |
| `Login`         | FR1, FR2, FR4, FR5, NFR3, NFR4 |
| `Classes`       | FR6, FR7, FR8, FR9, FR10, NFR6, NFR7, NFR8, NFR9, NFR10 |
| `Gym Admin`   | FR21, FR22, FR23, FR24, FR25, NFR21, NFR22, NFR23, NFR24, NFR25 |

# Activity Diagram Traceability

| Artifact ID        | Artifact Name                    | Requirement ID        |
| :----------------: | :-----------------------------:  | :-------------------: |
| Activity1          | Handle User Input                | FR1, FR2, NFR1        |
| Activity2          | Register New Member              | FR1, NFR1             |
| Activity3          | User Login                       | FR2, FR5, NFR3, NFR4  |
| Activity4          | Browse Available Classes         | FR6, NFR6, NFR9       |
| Activity5          | Book Class                       | FR7, FR8, FR9, NFR7   |
| Activity6          | Process Payment                  | FR11, FR12, NFR11, NFR13 |
| Activity7          | Send Payment Confirmation        | FR13, FR14, NFR14     |
| Activity8          | Send Booking Confirmation        | FR16, NFR16           |
| Activity9          | Send Class Reminder Notification | FR19, NFR16, NFR17    |
| Activity10         | Cancel Class Booking             | FR8, NFR10            |

# Software Artifacts

This section provides links to the key **software artifacts** related to the **Gym Membership and Class Booking System**. These artifacts include diagrams, specifications, and other essential documentation that help define the system's architecture and functionality.

* [Activity Diagram](https://github.com/Prajwal148/OOPS/blob/56f344deb62f1fb0ee290ad0fa0a48ead41db769/artifacts/ActivityDiagram.pdf)
* [CRC Cards, Class Diagram, and Object Diagram](https://github.com/Prajwal148/OOPS/blob/56f344deb62f1fb0ee290ad0fa0a48ead41db769/artifacts/CRC%20Cards-Class%20Diagram-Object%20Diagram.pdf)
* [Class Specification](https://github.com/Prajwal148/OOPS/blob/56f344deb62f1fb0ee290ad0fa0a48ead41db769/artifacts/Class%20Specification.pdf)
* [Database Schema](https://github.com/Prajwal148/OOPS/blob/56f344deb62f1fb0ee290ad0fa0a48ead41db769/artifacts/DatabaseSchema.pdf)
* [Sequence and State Diagrams](https://github.com/Prajwal148/OOPS/blob/56f344deb62f1fb0ee290ad0fa0a48ead41db769/artifacts/Sequence-State%20Diagrams.pdf)
* [Use Case and Activity Diagram](https://github.com/Prajwal148/OOPS/blob/56f344deb62f1fb0ee290ad0fa0a48ead41db769/artifacts/USECASE_ACTIVITY_DIAGRAM.pdf)
* [Use Case Diagram](https://github.com/Prajwal148/OOPS/blob/56f344deb62f1fb0ee290ad0fa0a48ead41db769/artifacts/UseCaseDiagram.pdf)
* [Windows Navigation Diagram](https://github.com/Prajwal148/OOPS/blob/56f344deb62f1fb0ee290ad0fa0a48ead41db769/artifacts/Windows%20Nav%20Diagram.pdf)




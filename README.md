# drayage-rate-manager

# 📌 Executive Summary

In response to the need for a more streamlined, efficient, and user-friendly way to manage drayage pricing, our project aims to develop a micro version of a drayage pricing management tool. This tool is designed to facilitate the upload, update, and search of rate tariffs by drayage companies (referred to as draymen) and enable brokers to find the best rates for their clients efficiently. The development of this system will leverage React for the front-end user interface and Python with Flask for the back-end server, ensuring a robust, scalable, and interactive application.

### Objectives

The primary objectives of this project are to:

1. **Simplify Rate Tariff Management**: Allow draymen to easily register, upload, and update their rate tariffs in a standardized format.
2. **Enhance Rate Search Capability**: Enable brokers to search for rate tariffs by specific lanes and view detailed breakdowns of rates, including additional fees or surcharges, in a customizable manner.
3. **Improve User Management and Security**: Implement role-based access control to ensure users can access only the information and functionalities relevant to their role.
4. **Facilitate Better Decision Making**: Provide brokers with timely alerts on new rate uploads for lanes they frequently search, ensuring they can always offer the best rates to their clients.

### Key Features

- **User Registration and Account Management for Draymen**: Draymen can create accounts to upload and manage their rate tariffs, ensuring brokers have access to the most current pricing information.
- **Advanced Rate Search for Brokers**: Brokers can perform detailed searches for rate tariffs by lane, with options to sort and filter results based on various criteria, enhancing their ability to provide competitive quotes.
- **Customizable Notifications**: Brokers receive real-time alerts for new or updated rates in their lanes of interest, aiding in quick decision-making and client service.
- **Secure and Role-Based Access Control**: The system ensures data integrity and security by restricting access to sensitive functionalities and information based on user roles.

### Implementation Strategy

The project will be executed in phases, starting with the development of core functionalities, followed by testing and iterative enhancements based on user feedback. The choice of React and Python/Flask as the technology stack balances the need for a rich, interactive user interface with the robustness and simplicity of backend development.

### Expected Outcomes

Upon completion, the drayage pricing management tool will:

- Reduce the time and effort required for draymen to manage and brokers to find rate tariffs.
- Enhance the accuracy of pricing information available to brokers, leading to better service for their clients.
- Increase the operational efficiency of drayage rate management through automation and integration with existing systems.

### Conclusion

This project represents a significant step forward in the use of technology to solve complex logistical challenges in the freight brokerage industry. By developing a specialized tool tailored to the needs of draymen and brokers, we anticipate not only improvements in individual company operations but also broader positive impacts on the efficiency and transparency of the drayage market as a whole.

### 👨‍💼 User Stories

*“As a user, I should be able to….”*

### Epic: Rate Tariff Management

- As a drayman, I want to be able to register and create an account so that I can upload our rate tariffs.
- As a drayman, I want to upload our rate tariffs using a standardized format so that brokers can easily understand and compare rates.
- As a drayman, I want to update our existing rate tariffs to reflect changes in pricing or services so that the information available to brokers is always current.

### Epic: Rate Search

- As a broker, I want to search the collected rate tariffs by specific lanes (origin and destination) so that I can find the best rates for my clients.
- As a broker, I want to view detailed breakdowns of rate tariffs including any additional fees or surcharges so that I can provide accurate quotes to my clients.
- As a broker, I want to view these lane prices in a customizable way (sort by rate, accessorial, etc)

### Epic: User Management and Security

- As an admin, I want to set different access levels for users based on their role to ensure they can only access the information and functionalities relevant to them.

### Epic: System Integration and Notifications

- As a broker, I want to receive alerts when new rates are uploaded for lanes I frequently search so that I can always offer the best rates to my clients.

### 🏗️ Wireframe

![image](https://github.com/tyjsmith1/drayage-rate-manager/assets/95344047/c38239c9-bcac-4326-8a2c-ef88a56961fb)


### 🌳 Component Tree

![image](https://github.com/tyjsmith1/drayage-rate-manager/assets/95344047/0eb14133-e0be-4ea7-a8e3-8cd41dcbb008)


- Landing Page: The root path of the application, leading to the HomePage, which could provide general information about the application and links to login or register.
- Login: A page where users can log in to their accounts.
- Register: A page for new users (draymen or brokers) to register and create an account.
- Carrier Dashboard: The main dashboard for draymen, showing options to upload or update rate tariffs.
    - Upload Rate Page: A page where draymen can upload new rate tariffs.
    - View/Update Rate: A page to view and update existing rate tariffs.
- Broker Dashboard: The main dashboard for brokers, with functionalities tailored to their needs.
    - Search:  A page where brokers can search for rate tariffs by specific lanes.
    - Alerts: A page for brokers to manage and view alerts for new rates.

### 📊 Database Design

![image](https://github.com/tyjsmith1/drayage-rate-manager/assets/95344047/f9a0177a-a109-4cc5-a253-8cde562859a9)


### 🛜 API Routes

### **Authentication and User Management**

- **POST /api/auth/register**: Registers a new user (drayman or broker) with the system.
- **POST /api/auth/login**: Authenticates a user and returns a token for session management.
- **GET /api/user/profile**: Retrieves the profile information of the currently logged-in user.
- **PUT /api/user/profile**: Updates the profile information of the currently logged-in user.
- **GET /api/users**: (Admin) Lists all users, with options to filter by role.

### **Carrier (Drayage Company) Management**

- **POST /api/carriers**: Adds a new carrier.
- **GET /api/carriers**: Lists all carriers, with search parameters to filter the list.
- **GET /api/carriers/{id}**: Retrieves details of a specific carrier.
- **PUT /api/carriers/{id}**: Updates a specific carrier's details.
- **DELETE /api/carriers/{id}**: Deletes a specific carrier (consider soft delete).

### **Rate Tariffs Management**

- **POST /api/rates**: Allows a drayman to upload rate tariffs.
- **GET /api/rates**: Retrieves rate tariffs, with filtering options based on origin, destination, and other rate details.
- **GET /api/rates/{id}**: Retrieves details of a specific rate tariff.
- **PUT /api/rates/{id}**: Allows a drayman to update a specific rate tariff.
- **DELETE /api/rates/{id}**: Deletes a specific rate tariff (consider soft delete).

### **Rate Search for Brokers**

- **GET /api/rates/search**: Searches rate tariffs based on specified criteria like origin, destination, and optionally, other filters such as effective date range.

NICE TO HAVE:

### **Notifications and Alerts**

- **GET /api/notifications**: Retrieves notifications for the logged-in user, such as alerts about new rates for frequently searched lanes.
- **POST /api/notifications/subscribe**: Allows a user to subscribe to notifications for specific lanes or rate changes.
- **DELETE /api/notifications/{id}/unsubscribe**: Unsubscribes from a specific notification.

### **System Administration**

- **GET /api/admin/dashboard**: Provides an overview of system usage, number of tariffs uploaded, and active users (for admins).

### **Miscellaneous**

- **GET /api/utils/laneSuggestions**: Suggests lanes based on historical data or common searches.

### 📟 Planned Tech

Front End - React

Backend - Python & Flask
